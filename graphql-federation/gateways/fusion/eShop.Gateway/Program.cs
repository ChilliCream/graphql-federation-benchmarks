using HotChocolate.Fusion.Configuration;
using eShop.Gateway.BenchmarkDiagnostics;

var builder = WebApplication.CreateBuilder(args);

builder.Logging.ClearProviders();

// Run Kestrel's request processing inline on the socket thread instead of the thread pool.
builder.WebHost.UseSockets(o => o.UnsafePreferInlineScheduling = true);

if (Environment.GetEnvironmentVariable("BENCH_DIAGNOSTIC_RUN") == "1")
{
    builder.Services.AddHostedService<FusionPoolDiagnostics>();
}

builder.Services
    .AddHeaderPropagation(
        options =>
        {
            options.Headers.Add("Authorization");
        });

builder.Services
    .AddHttpClient("fusion")
    // Drop the default LoggingHttpMessageHandler and LoggingScopeHttpMessageHandler. Even with
    // logging disabled they add two async state machines and a scope per subgraph call.
    .RemoveAllLoggers()
    .ConfigurePrimaryHttpMessageHandler(
        () => new SocketsHttpHandler
        {
            MaxConnectionsPerServer = 256,
            PooledConnectionIdleTimeout = TimeSpan.FromMinutes(16)
        })
    .SetHandlerLifetime(Timeout.InfiniteTimeSpan)
    .AddHeaderPropagation();

#if FUSION_16_7_OR_GREATER
builder
    .AddGraphQLGateway(disableDefaultSecurity: true)
    .AddFileSystemConfiguration("./gateway.far")
    .ModifyRequestOptions(o => o.IncludeExceptionDetails = true);
#else
builder
    .AddGraphQLGateway()
    .AddFileSystemConfiguration("./gateway.far")
    .ModifyRequestOptions(o => o.IncludeExceptionDetails = true);
#endif

var app = builder.Build();

app.UseHeaderPropagation();
app.MapGraphQLHttp();

app.Run();
