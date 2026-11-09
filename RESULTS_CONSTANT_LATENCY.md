## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 3,430 | 3,438 | 3,404 | 0.5% | 383 MB | 114.2 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,404 | 3,408 | 3,374 | 0.4% | 395 MB | 118.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,401 | 3,415 | 3,396 | 0.2% | 130 MB | 39.1 KB |  |
| fusion-aot-11 | 16.7.3 | 3,339 | 3,363 | 3,325 | 0.4% | 145 MB | 44.5 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,305 | 3,336 | 3,262 | 1.0% | 2,313 MB | 716.6 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,784 | 2,794 | 2,747 | 0.7% | 409 MB | 150.4 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,782 | 2,789 | 2,778 | 0.2% | 398 MB | 146.4 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,745 | 2,749 | 2,722 | 0.4% | 142 MB | 52.9 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,739 | 2,746 | 2,737 | 0.1% | 137 MB | 51.1 KB |  |
| hive-router | v0.3.10 | 2,038 | 2,050 | 2,033 | 0.3% | 92 MB | 46.2 KB |  |
| grafbase | 0.53.5 | 1,442 | 1,457 | 1,435 | 0.6% | 100 MB | 71.0 KB |  |
| cosmo | 0.365.2 | 1,352 | 1,354 | 1,351 | 0.1% | 149 MB | 113.0 KB |  |
| caliban | 3.2.0 | 1,333 | 1,360 | 1,329 | 1.2% | 4,242 MB | 3,258.8 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 538 | 539 | 537 | 0.1% | 2,752 MB | 5,238.6 KB |  |
| apollo-router | v2.19.0 | 481 | 484 | 481 | 0.3% | 178 MB | 379.7 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 417 | 417 | 417 | 0.0% | 205 MB | 503.2 KB |  |
| hive-gateway | 2.15.6 | 264 | 264 | 262 | 0.3% | 3,472 MB | 13,465.4 KB |  |
| apollo-gateway | 2.14.4 | 263 | 264 | 262 | 0.4% | 2,176 MB | 8,471.8 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1244601     ✗ 0     
     data_received..................: 36 GB   300 MB/s
     data_sent......................: 499 MB  4.1 MB/s
     http_req_blocked...............: avg=2.44µs  min=781ns   med=1.84µs  max=9.33ms   p(90)=2.98µs  p(95)=3.69µs   p(99.9)=23.99µs
     http_req_connecting............: avg=219ns   min=0s      med=0s      max=4.12ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.25ms min=8.1ms   med=13.83ms max=272.04ms p(90)=17.73ms p(95)=19.08ms  p(99.9)=27.01ms
       { expected_response:true }...: avg=14.25ms min=8.1ms   med=13.83ms max=272.04ms p(90)=17.73ms p(95)=19.08ms  p(99.9)=27.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 414967
     http_req_receiving.............: avg=68.65µs min=25.24µs med=43.17µs max=109.23ms p(90)=89.6µs  p(95)=166.67µs p(99.9)=2.05ms 
     http_req_sending...............: avg=30.16µs min=4.45µs  med=7.78µs  max=123.39ms p(90)=15.87µs p(95)=90.19µs  p(99.9)=1.76ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.15ms min=8.05ms  med=13.73ms max=271.96ms p(90)=17.63ms p(95)=18.97ms  p(99.9)=26.76ms
     http_reqs......................: 414967  3430.80375/s
     iteration_duration.............: avg=14.45ms min=8.23ms  med=14.02ms max=298.87ms p(90)=17.93ms p(95)=19.27ms  p(99.9)=27.24ms
     iterations.....................: 414867  3429.976984/s
     success_rate...................: 100.00% ✓ 414867      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1235052     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 495 MB  4.1 MB/s
     http_req_blocked...............: avg=2.69µs  min=811ns   med=1.82µs  max=8.8ms    p(90)=3.06µs  p(95)=3.83µs   p(99.9)=24.42µs
     http_req_connecting............: avg=482ns   min=0s      med=0s      max=7.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.36ms min=8.15ms  med=13.95ms max=268.08ms p(90)=17.86ms p(95)=19.21ms  p(99.9)=27.14ms
       { expected_response:true }...: avg=14.36ms min=8.15ms  med=13.95ms max=268.08ms p(90)=17.86ms p(95)=19.21ms  p(99.9)=27.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 411784
     http_req_receiving.............: avg=69.06µs min=24.11µs med=42.57µs max=133.44ms p(90)=91.15µs p(95)=165.31µs p(99.9)=2.03ms 
     http_req_sending...............: avg=31.38µs min=4.34µs  med=7.78µs  max=167.25ms p(90)=16.09µs p(95)=89.58µs  p(99.9)=2.01ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.26ms min=8.01ms  med=13.85ms max=267.6ms  p(90)=17.75ms p(95)=19.09ms  p(99.9)=26.92ms
     http_reqs......................: 411784  3404.397106/s
     iteration_duration.............: avg=14.56ms min=8.4ms   med=14.14ms max=287.14ms p(90)=18.05ms p(95)=19.4ms   p(99.9)=27.36ms
     iterations.....................: 411684  3403.570363/s
     success_rate...................: 100.00% ✓ 411684      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1233906     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 494 MB  4.1 MB/s
     http_req_blocked...............: avg=2.44µs  min=821ns   med=1.8µs   max=4.24ms   p(90)=2.95µs  p(95)=3.67µs   p(99.9)=23.33µs
     http_req_connecting............: avg=299ns   min=0s      med=0s      max=4.19ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.38ms min=8.31ms  med=13.97ms max=280.06ms p(90)=17.74ms p(95)=19.07ms  p(99.9)=27.14ms
       { expected_response:true }...: avg=14.38ms min=8.31ms  med=13.97ms max=280.06ms p(90)=17.74ms p(95)=19.07ms  p(99.9)=27.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 411402
     http_req_receiving.............: avg=64.62µs min=22.91µs med=41.35µs max=118.25ms p(90)=87.41µs p(95)=154.93µs p(99.9)=1.61ms 
     http_req_sending...............: avg=29.95µs min=4.15µs  med=7.71µs  max=156.96ms p(90)=15.39µs p(95)=87µs     p(99.9)=1.58ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.29ms min=8.23ms  med=13.88ms max=279.69ms p(90)=17.64ms p(95)=18.96ms  p(99.9)=26.94ms
     http_reqs......................: 411402  3401.233274/s
     iteration_duration.............: avg=14.57ms min=8.52ms  med=14.16ms max=291.51ms p(90)=17.93ms p(95)=19.26ms  p(99.9)=27.37ms
     iterations.....................: 411302  3400.406532/s
     success_rate...................: 100.00% ✓ 411302      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1211727     ✗ 0     
     data_received..................: 35 GB   292 MB/s
     data_sent......................: 486 MB  4.0 MB/s
     http_req_blocked...............: avg=2.4µs   min=831ns   med=1.87µs  max=3.64ms   p(90)=2.98µs  p(95)=3.66µs   p(99.9)=22.69µs
     http_req_connecting............: avg=218ns   min=0s      med=0s      max=3.59ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.65ms min=8.4ms   med=14.21ms max=266.03ms p(90)=18.12ms p(95)=19.52ms  p(99.9)=27.63ms
       { expected_response:true }...: avg=14.65ms min=8.4ms   med=14.21ms max=266.03ms p(90)=18.12ms p(95)=19.52ms  p(99.9)=27.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 404009
     http_req_receiving.............: avg=67.52µs min=24.61µs med=43.52µs max=147.71ms p(90)=89.33µs p(95)=167.16µs p(99.9)=1.67ms 
     http_req_sending...............: avg=30.12µs min=4.5µs   med=7.96µs  max=102.5ms  p(90)=15.53µs p(95)=89.94µs  p(99.9)=1.59ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.55ms min=8.35ms  med=14.12ms max=265.43ms p(90)=18.02ms p(95)=19.41ms  p(99.9)=27.4ms 
     http_reqs......................: 404009  3339.924173/s
     iteration_duration.............: avg=14.84ms min=8.56ms  med=14.4ms  max=295.62ms p(90)=18.31ms p(95)=19.71ms  p(99.9)=27.84ms
     iterations.....................: 403909  3339.097477/s
     success_rate...................: 100.00% ✓ 403909      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-10-25-0247)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1199328     ✗ 0     
     data_received..................: 35 GB   289 MB/s
     data_sent......................: 481 MB  4.0 MB/s
     http_req_blocked...............: avg=2.51µs  min=812ns   med=1.91µs  max=3.96ms   p(90)=3.3µs   p(95)=4.16µs   p(99.9)=25.17µs
     http_req_connecting............: avg=225ns   min=0s      med=0s      max=3.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.8ms  min=8.64ms  med=14.46ms max=316.54ms p(90)=17.87ms p(95)=19.11ms  p(99.9)=26.45ms
       { expected_response:true }...: avg=14.8ms  min=8.64ms  med=14.46ms max=316.54ms p(90)=17.87ms p(95)=19.11ms  p(99.9)=26.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 399876
     http_req_receiving.............: avg=67.78µs min=22.98µs med=42.96µs max=270.8ms  p(90)=91.63µs p(95)=166.92µs p(99.9)=1.62ms 
     http_req_sending...............: avg=32.17µs min=4.37µs  med=8.21µs  max=211.34ms p(90)=17.11µs p(95)=93.81µs  p(99.9)=1.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.7ms  min=8.58ms  med=14.36ms max=290.6ms  p(90)=17.76ms p(95)=18.99ms  p(99.9)=26.22ms
     http_reqs......................: 399876  3305.711459/s
     iteration_duration.............: avg=14.99ms min=8.85ms  med=14.65ms max=323.34ms p(90)=18.05ms p(95)=19.3ms   p(99.9)=26.64ms
     iterations.....................: 399776  3304.884775/s
     success_rate...................: 100.00% ✓ 399776      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1013886     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 406 MB  3.3 MB/s
     http_req_blocked...............: avg=2.56µs  min=781ns   med=2.01µs  max=2.5ms    p(90)=3.54µs  p(95)=4.32µs   p(99.9)=27.61µs
     http_req_connecting............: avg=174ns   min=0s      med=0s      max=2.47ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.53ms min=11.72ms med=17.1ms  max=288.38ms p(90)=20.6ms  p(95)=21.84ms  p(99.9)=29.05ms
       { expected_response:true }...: avg=17.53ms min=11.72ms med=17.1ms  max=288.38ms p(90)=20.6ms  p(95)=21.84ms  p(99.9)=29.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 338062
     http_req_receiving.............: avg=70.12µs min=24.08µs med=46.07µs max=133.15ms p(90)=96.85µs p(95)=154.06µs p(99.9)=1.5ms  
     http_req_sending...............: avg=29.97µs min=4.13µs  med=8.21µs  max=206.65ms p(90)=17.4µs  p(95)=86.05µs  p(99.9)=1.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.43ms min=11.56ms med=17.01ms max=287.53ms p(90)=20.49ms p(95)=21.73ms  p(99.9)=28.79ms
     http_reqs......................: 338062  2784.527045/s
     iteration_duration.............: avg=17.74ms min=11.9ms  med=17.3ms  max=299.35ms p(90)=20.79ms p(95)=22.04ms  p(99.9)=29.26ms
     iterations.....................: 337962  2783.703372/s
     success_rate...................: 100.00% ✓ 337962      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1012983     ✗ 0     
     data_received..................: 30 GB   243 MB/s
     data_sent......................: 406 MB  3.3 MB/s
     http_req_blocked...............: avg=2.56µs  min=811ns   med=1.87µs  max=3.82ms   p(90)=3.24µs  p(95)=4.04µs   p(99.9)=25.76µs
     http_req_connecting............: avg=305ns   min=0s      med=0s      max=3.77ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.55ms min=11.56ms med=17.12ms max=276.93ms p(90)=20.64ms p(95)=21.87ms  p(99.9)=29.18ms
       { expected_response:true }...: avg=17.55ms min=11.56ms med=17.12ms max=276.93ms p(90)=20.64ms p(95)=21.87ms  p(99.9)=29.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 337761
     http_req_receiving.............: avg=66µs    min=24.01µs med=43.09µs max=76.9ms   p(90)=91.17µs p(95)=149.46µs p(99.9)=1.54ms 
     http_req_sending...............: avg=28.63µs min=4.16µs  med=7.81µs  max=219.13ms p(90)=16.37µs p(95)=82.23µs  p(99.9)=1.51ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.46ms min=11.52ms med=17.04ms max=276.47ms p(90)=20.53ms p(95)=21.76ms  p(99.9)=28.9ms 
     http_reqs......................: 337761  2782.182975/s
     iteration_duration.............: avg=17.76ms min=11.74ms med=17.32ms max=305.6ms  p(90)=20.83ms p(95)=22.06ms  p(99.9)=29.39ms
     iterations.....................: 337661  2781.359261/s
     success_rate...................: 100.00% ✓ 337661      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 999756      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 401 MB  3.3 MB/s
     http_req_blocked...............: avg=2.61µs  min=782ns   med=1.86µs  max=6.16ms   p(90)=3.2µs   p(95)=3.98µs   p(99.9)=27.16µs
     http_req_connecting............: avg=349ns   min=0s      med=0s      max=5.8ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.79ms min=11.8ms  med=17.38ms max=277.05ms p(90)=20.83ms p(95)=22.07ms  p(99.9)=29.2ms 
       { expected_response:true }...: avg=17.79ms min=11.8ms  med=17.38ms max=277.05ms p(90)=20.83ms p(95)=22.07ms  p(99.9)=29.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 333352
     http_req_receiving.............: avg=66.53µs min=24.75µs med=44.61µs max=68.92ms  p(90)=92.31µs p(95)=146.55µs p(99.9)=1.35ms 
     http_req_sending...............: avg=27.51µs min=4.27µs  med=8.03µs  max=73.07ms  p(90)=16.97µs p(95)=82.9µs   p(99.9)=1.49ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.7ms  min=11.76ms med=17.29ms max=276.58ms p(90)=20.73ms p(95)=21.96ms  p(99.9)=28.92ms
     http_reqs......................: 333352  2745.714716/s
     iteration_duration.............: avg=17.99ms min=11.92ms med=17.58ms max=299.48ms p(90)=21.03ms p(95)=22.27ms  p(99.9)=29.45ms
     iterations.....................: 333252  2744.891047/s
     success_rate...................: 100.00% ✓ 333252      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 997377      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=3.38µs  min=872ns   med=2.27µs  max=8.78ms   p(90)=3.67µs  p(95)=4.41µs  p(99.9)=33.15µs
     http_req_connecting............: avg=710ns   min=0s      med=0s      max=8.47ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.83ms min=11.78ms med=17.38ms max=276.88ms p(90)=20.95ms p(95)=22.27ms p(99.9)=29.72ms
       { expected_response:true }...: avg=17.83ms min=11.78ms med=17.38ms max=276.88ms p(90)=20.95ms p(95)=22.27ms p(99.9)=29.72ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 332559
     http_req_receiving.............: avg=68.71µs min=23.85µs med=45.71µs max=88.37ms  p(90)=92.99µs p(95)=150.7µs p(99.9)=1.35ms 
     http_req_sending...............: avg=29.42µs min=4.45µs  med=8.58µs  max=133.41ms p(90)=16.95µs p(95)=86.61µs p(99.9)=1.42ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.73ms min=11.72ms med=17.29ms max=275.53ms p(90)=20.84ms p(95)=22.15ms p(99.9)=29.43ms
     http_reqs......................: 332559  2739.394482/s
     iteration_duration.............: avg=18.03ms min=11.92ms med=17.59ms max=307.01ms p(90)=21.15ms p(95)=22.47ms p(99.9)=30ms   
     iterations.....................: 332459  2738.57075/s
     success_rate...................: 100.00% ✓ 332459      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 744972      ✗ 0     
     data_received..................: 22 GB   178 MB/s
     data_sent......................: 299 MB  2.4 MB/s
     http_req_blocked...............: avg=3.39µs  min=971ns   med=2.64µs  max=4.02ms   p(90)=4.24µs  p(95)=4.98µs   p(99.9)=36.3µs  
     http_req_connecting............: avg=404ns   min=0s      med=0s      max=3.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.92ms min=17.39ms med=23.57ms max=301.42ms p(90)=27.06ms p(95)=28.2ms   p(99.9)=34.18ms 
       { expected_response:true }...: avg=23.92ms min=17.39ms med=23.57ms max=301.42ms p(90)=27.06ms p(95)=28.2ms   p(99.9)=34.18ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 248424
     http_req_receiving.............: avg=67.99µs min=24.42µs med=50.97µs max=107.99ms p(90)=93.75µs p(95)=120.31µs p(99.9)=976.88µs
     http_req_sending...............: avg=28.41µs min=4.59µs  med=10.48µs max=184.04ms p(90)=18.39µs p(95)=26.78µs  p(99.9)=1ms     
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.83ms min=17.29ms med=23.48ms max=300.87ms p(90)=26.96ms p(95)=28.1ms   p(99.9)=34.02ms 
     http_reqs......................: 248424  2038.591824/s
     iteration_duration.............: avg=24.15ms min=17.56ms med=23.78ms max=318.23ms p(90)=27.27ms p(95)=28.42ms  p(99.9)=34.45ms 
     iterations.....................: 248324  2037.771214/s
     success_rate...................: 100.00% ✓ 248324      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: grafbase (HotChocolate subgraphs) (0.53.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 527223      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=3µs     min=782ns   med=2.14µs  max=2.77ms   p(90)=4.47µs   p(95)=5.43µs   p(99.9)=37.69µs
     http_req_connecting............: avg=321ns   min=0s      med=0s      max=2.75ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.88ms min=17.66ms med=33.58ms max=292.79ms p(90)=39.54ms  p(95)=41.22ms  p(99.9)=49.44ms
       { expected_response:true }...: avg=33.88ms min=17.66ms med=33.58ms max=292.79ms p(90)=39.54ms  p(95)=41.22ms  p(99.9)=49.44ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 175841
     http_req_receiving.............: avg=78.64µs min=26.43µs med=54.17µs max=107.49ms p(90)=116.29µs p(95)=154.93µs p(99.9)=1.46ms 
     http_req_sending...............: avg=26.62µs min=4.39µs  med=9.01µs  max=212.67ms p(90)=21.21µs  p(95)=30.01µs  p(99.9)=1.12ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.77ms min=17.58ms med=33.49ms max=292.65ms p(90)=39.44ms  p(95)=41.11ms  p(99.9)=49.2ms 
     http_reqs......................: 175841  1442.154116/s
     iteration_duration.............: avg=34.13ms min=20.21ms med=33.82ms max=319.8ms  p(90)=39.75ms  p(95)=41.43ms  p(99.9)=49.8ms 
     iterations.....................: 175741  1441.33397/s
     success_rate...................: 100.00% ✓ 175741      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.365.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 494550      ✗ 0     
     data_received..................: 14 GB   118 MB/s
     data_sent......................: 198 MB  1.6 MB/s
     http_req_blocked...............: avg=3.08µs  min=982ns   med=2.1µs   max=3.99ms   p(90)=3.5µs   p(95)=4.15µs   p(99.9)=29.06µs 
     http_req_connecting............: avg=678ns   min=0s      med=0s      max=3.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=36.18ms min=17.99ms med=35.63ms max=300.75ms p(90)=43.37ms p(95)=45.83ms  p(99.9)=58.51ms 
       { expected_response:true }...: avg=36.18ms min=17.99ms med=35.63ms max=300.75ms p(90)=43.37ms p(95)=45.83ms  p(99.9)=58.51ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 164950
     http_req_receiving.............: avg=68.79µs min=24.65µs med=58.15µs max=64.97ms  p(90)=95.04µs p(95)=112.17µs p(99.9)=637.52µs
     http_req_sending...............: avg=20.75µs min=4.55µs  med=9.82µs  max=184.24ms p(90)=15.75µs p(95)=19.35µs  p(99.9)=713.11µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=36.09ms min=17.87ms med=35.55ms max=300.51ms p(90)=43.28ms p(95)=45.74ms  p(99.9)=58.39ms 
     http_reqs......................: 164950  1352.456447/s
     iteration_duration.............: avg=36.39ms min=20.91ms med=35.83ms max=309.97ms p(90)=43.57ms p(95)=46.02ms  p(99.9)=58.71ms 
     iterations.....................: 164850  1351.636528/s
     success_rate...................: 100.00% ✓ 164850      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 487923      ✗ 0     
     data_received..................: 14 GB   117 MB/s
     data_sent......................: 196 MB  1.6 MB/s
     http_req_blocked...............: avg=3.03µs  min=982ns   med=2.17µs  max=3.48ms   p(90)=3.55µs  p(95)=4.2µs    p(99.9)=35.15µs 
     http_req_connecting............: avg=570ns   min=0s      med=0s      max=3.45ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=36.67ms min=18.75ms med=36.11ms max=303.67ms p(90)=43.68ms p(95)=46.22ms  p(99.9)=61.89ms 
       { expected_response:true }...: avg=36.67ms min=18.75ms med=36.11ms max=303.67ms p(90)=43.68ms p(95)=46.22ms  p(99.9)=61.89ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 162741
     http_req_receiving.............: avg=71.13µs min=26.23µs med=55.83µs max=147.74ms p(90)=89.23µs p(95)=103.68µs p(99.9)=738.39µs
     http_req_sending...............: avg=20.82µs min=4.79µs  med=10.62µs max=125.75ms p(90)=16.5µs  p(95)=19.79µs  p(99.9)=693.5µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=36.57ms min=18.55ms med=36.02ms max=302.22ms p(90)=43.6ms  p(95)=46.13ms  p(99.9)=61.28ms 
     http_reqs......................: 162741  1333.483909/s
     iteration_duration.............: avg=36.88ms min=21.93ms med=36.31ms max=314.35ms p(90)=43.88ms p(95)=46.43ms  p(99.9)=62.6ms  
     iterations.....................: 162641  1332.664519/s
     success_rate...................: 100.00% ✓ 162641      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 197229     ✗ 0    
     data_received..................: 5.8 GB  47 MB/s
     data_sent......................: 79 MB   647 kB/s
     http_req_blocked...............: avg=6.08µs  min=1.03µs  med=2.85µs  max=7.38ms   p(90)=4.36µs   p(95)=4.98µs   p(99.9)=44.47µs 
     http_req_connecting............: avg=2.86µs  min=0s      med=0s      max=7.29ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=90.93ms min=21.04ms med=88.05ms max=324.78ms p(90)=111.97ms p(95)=122.16ms p(99.9)=222.47ms
       { expected_response:true }...: avg=90.93ms min=21.04ms med=88.05ms max=324.78ms p(90)=111.97ms p(95)=122.16ms p(99.9)=222.47ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65843
     http_req_receiving.............: avg=81.16µs min=28.88µs med=72.13µs max=103.13ms p(90)=106.91µs p(95)=119.46µs p(99.9)=561µs   
     http_req_sending...............: avg=24.65µs min=5.08µs  med=13.62µs max=127.41ms p(90)=19.57µs  p(95)=21.66µs  p(99.9)=669.09µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=90.83ms min=20.94ms med=87.94ms max=323.4ms  p(90)=111.86ms p(95)=122.03ms p(99.9)=222.09ms
     http_reqs......................: 65843   538.551151/s
     iteration_duration.............: avg=91.28ms min=30.88ms med=88.29ms max=332.76ms p(90)=112.21ms p(95)=122.43ms p(99.9)=224.06ms
     iterations.....................: 65743   537.733219/s
     success_rate...................: 100.00% ✓ 65743      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 176157     ✗ 0    
     data_received..................: 5.1 GB  42 MB/s
     data_sent......................: 71 MB   578 kB/s
     http_req_blocked...............: avg=8.19µs   min=1.28µs  med=3.17µs   max=8.74ms   p(90)=4.62µs   p(95)=5.21µs   p(99.9)=50.47µs 
     http_req_connecting............: avg=4.65µs   min=0s      med=0s       max=8.7ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.81ms min=19.44ms med=99.84ms  max=311.72ms p(90)=129.11ms p(95)=138.39ms p(99.9)=179.23ms
       { expected_response:true }...: avg=101.81ms min=19.44ms med=99.84ms  max=311.72ms p(90)=129.11ms p(95)=138.39ms p(99.9)=179.23ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58819
     http_req_receiving.............: avg=86.29µs  min=30.74µs med=72.28µs  max=150.61ms p(90)=105.33µs p(95)=117.7µs  p(99.9)=484.82µs
     http_req_sending...............: avg=23.19µs  min=5.5µs   med=14.76µs  max=75.66ms  p(90)=20.4µs   p(95)=22.47µs  p(99.9)=665.5µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.7ms  min=19.32ms med=99.75ms  max=310.46ms p(90)=129.01ms p(95)=138.27ms p(99.9)=178.45ms
     http_reqs......................: 58819   481.243196/s
     iteration_duration.............: avg=102.2ms  min=27.33ms med=100.11ms max=345.59ms p(90)=129.36ms p(95)=138.66ms p(99.9)=181.16ms
     iterations.....................: 58719   480.42502/s
     success_rate...................: 100.00% ✓ 58719      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-v3 (HotChocolate subgraphs) (v3.0.0-preview.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 153018     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 61 MB   502 kB/s
     http_req_blocked...............: avg=5.6µs    min=1.16µs  med=3.42µs   max=4.15ms   p(90)=4.89µs   p(95)=5.49µs   p(99.9)=154.89µs
     http_req_connecting............: avg=1.92µs   min=0s      med=0s       max=4.11ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=117.22ms min=20.95ms med=115.66ms max=350.08ms p(90)=144.85ms p(95)=154.26ms p(99.9)=197.44ms
       { expected_response:true }...: avg=117.22ms min=20.95ms med=115.66ms max=350.08ms p(90)=144.85ms p(95)=154.26ms p(99.9)=197.44ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51106
     http_req_receiving.............: avg=86.51µs  min=31µs    med=81.57µs  max=53.22ms  p(90)=112.03µs p(95)=123.66µs p(99.9)=499.07µs
     http_req_sending...............: avg=24.52µs  min=5.44µs  med=16.26µs  max=100.65ms p(90)=21.35µs  p(95)=23.33µs  p(99.9)=573.36µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=117.11ms min=20.82ms med=115.55ms max=349.53ms p(90)=144.74ms p(95)=154.14ms p(99.9)=197.33ms
     http_reqs......................: 51106   417.762075/s
     iteration_duration.............: avg=117.67ms min=34.44ms med=115.96ms max=357.09ms p(90)=145.12ms p(95)=154.53ms p(99.9)=199.43ms
     iterations.....................: 51006   416.944633/s
     success_rate...................: 100.00% ✓ 51006      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 96726      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=7.02µs   min=1.39µs  med=3.7µs    max=4.16ms   p(90)=5.24µs   p(95)=5.86µs   p(99.9)=1.37ms  
     http_req_connecting............: avg=3.05µs   min=0s      med=0s       max=4.12ms   p(90)=0s       p(95)=0s       p(99.9)=1.35ms  
     http_req_duration..............: avg=185.4ms  min=17.91ms med=170.19ms max=741.8ms  p(90)=221.87ms p(95)=243.93ms p(99.9)=671.96ms
       { expected_response:true }...: avg=185.4ms  min=17.91ms med=170.19ms max=741.8ms  p(90)=221.87ms p(95)=243.93ms p(99.9)=671.96ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32342
     http_req_receiving.............: avg=98.16µs  min=30.85µs med=88.57µs  max=69.56ms  p(90)=118.9µs  p(95)=130.95µs p(99.9)=731.49µs
     http_req_sending...............: avg=31.82µs  min=6.33µs  med=17.44µs  max=109.61ms p(90)=22.2µs   p(95)=24.16µs  p(99.9)=513.06µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.27ms min=17.75ms med=170.07ms max=741.64ms p(90)=221.75ms p(95)=243.78ms p(99.9)=671.84ms
     http_reqs......................: 32342   264.665172/s
     iteration_duration.............: avg=186.21ms min=42.56ms med=170.61ms max=742.15ms p(90)=222.26ms p(95)=244.84ms p(99.9)=672.34ms
     iterations.....................: 32242   263.846839/s
     success_rate...................: 100.00% ✓ 32242      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-gateway (HotChocolate subgraphs) (2.14.4)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 96582      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   316 kB/s
     http_req_blocked...............: avg=7.08µs   min=1.49µs  med=3.4µs    max=4.21ms   p(90)=4.8µs    p(95)=5.4µs    p(99.9)=1.64ms  
     http_req_connecting............: avg=3.32µs   min=0s      med=0s       max=4.18ms   p(90)=0s       p(95)=0s       p(99.9)=1.54ms  
     http_req_duration..............: avg=185.66ms min=22.24ms med=189.82ms max=389.29ms p(90)=199.74ms p(95)=204.78ms p(99.9)=272.74ms
       { expected_response:true }...: avg=185.66ms min=22.24ms med=189.82ms max=389.29ms p(90)=199.74ms p(95)=204.78ms p(99.9)=272.74ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32294
     http_req_receiving.............: avg=95.94µs  min=36.42µs med=88.13µs  max=80.19ms  p(90)=118.77µs p(95)=131.27µs p(99.9)=498.33µs
     http_req_sending...............: avg=30.22µs  min=6.01µs  med=17.2µs   max=80.74ms  p(90)=21.73µs  p(95)=23.52µs  p(99.9)=632.21µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.53ms min=22.09ms med=189.7ms  max=388.71ms p(90)=199.63ms p(95)=204.67ms p(99.9)=272.59ms
     http_reqs......................: 32294   263.450775/s
     iteration_duration.............: avg=186.46ms min=62.9ms  med=190.1ms  max=415.25ms p(90)=200.02ms p(95)=205.07ms p(99.9)=274.34ms
     iterations.....................: 32194   262.634987/s
     success_rate...................: 100.00% ✓ 32194      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

