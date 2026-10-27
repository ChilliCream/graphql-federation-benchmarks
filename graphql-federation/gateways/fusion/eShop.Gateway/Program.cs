using HotChocolate.Fusion.Configuration;
using eShop.Gateway.BenchmarkDiagnostics;

var builder = WebApplication.CreateBuilder(args);

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
            MaxConnectionsPerServer = 256
        })
    .AddHeaderPropagation();

#if FUSION_16_7_OR_GREATER
builder
    .AddGraphQLGateway(disableDefaultSecurity: true)
    .AddFileSystemConfiguration("./gateway.far");
#else
builder
    .AddGraphQLGateway()
    .AddFileSystemConfiguration("./gateway.far");
#endif

var app = builder.Build();

app.UseHeaderPropagation();
app.MapGraphQLHttp();

app.Run();
