## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,395 | 3,409 | 3,387 | 0.3% | 387 MB | 116.6 KB |  |
| fusion-net-11 | 16.7.3 | 3,376 | 3,386 | 3,367 | 0.2% | 393 MB | 119.2 KB |  |
| fusion-aot-11 | 16.7.3 | 3,364 | 3,394 | 3,352 | 0.5% | 130 MB | 39.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,353 | 3,370 | 3,336 | 0.4% | 128 MB | 39.0 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,280 | 3,290 | 3,256 | 0.5% | 2,301 MB | 718.3 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,788 | 2,793 | 2,771 | 0.3% | 390 MB | 143.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,778 | 2,787 | 2,751 | 0.5% | 387 MB | 142.7 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,765 | 2,776 | 2,756 | 0.3% | 142 MB | 52.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,760 | 2,766 | 2,751 | 0.2% | 141 MB | 52.5 KB |  |
| hive-router | v0.3.10 | 2,045 | 2,060 | 2,041 | 0.4% | 93 MB | 46.8 KB |  |
| grafbase | 0.53.5 | 1,440 | 1,451 | 1,429 | 0.6% | 101 MB | 71.8 KB |  |
| cosmo | 0.365.2 | 1,414 | 1,415 | 1,413 | 0.1% | 150 MB | 108.4 KB |  |
| caliban | 3.2.0 | 1,394 | 1,398 | 1,385 | 0.4% | 5,333 MB | 3,917.5 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 535 | 536 | 534 | 0.2% | 2,750 MB | 5,264.5 KB |  |
| apollo-router | v2.19.0 | 484 | 485 | 484 | 0.1% | 177 MB | 373.9 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 420 | 420 | 420 | 0.0% | 209 MB | 509.6 KB |  |
| apollo-gateway | 2.14.4 | 265 | 266 | 264 | 0.3% | 2,164 MB | 8,362.6 KB |  |
| hive-gateway | 2.15.6 | 260 | 261 | 258 | 0.4% | 3,490 MB | 13,744.1 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1231974     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 494 MB  4.1 MB/s
     http_req_blocked...............: avg=2.85µs  min=902ns   med=2.28µs  max=5.13ms   p(90)=3.66µs  p(95)=4.42µs   p(99.9)=30.5µs 
     http_req_connecting............: avg=185ns   min=0s      med=0s      max=5.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.39ms min=8.09ms  med=13.94ms max=279.54ms p(90)=17.96ms p(95)=19.38ms  p(99.9)=28.51ms
       { expected_response:true }...: avg=14.39ms min=8.09ms  med=13.94ms max=279.54ms p(90)=17.96ms p(95)=19.38ms  p(99.9)=28.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 410758
     http_req_receiving.............: avg=73.87µs min=24.62µs med=46.3µs  max=13.24ms  p(90)=96.36µs p(95)=181.26µs p(99.9)=2.19ms 
     http_req_sending...............: avg=34.07µs min=4.31µs  med=8.62µs  max=87.77ms  p(90)=17.65µs p(95)=98.47µs  p(99.9)=2.14ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.28ms min=8.04ms  med=13.84ms max=278.21ms p(90)=17.85ms p(95)=19.26ms  p(99.9)=28.25ms
     http_reqs......................: 410758  3395.949605/s
     iteration_duration.............: avg=14.6ms  min=8.22ms  med=14.14ms max=305.63ms p(90)=18.16ms p(95)=19.58ms  p(99.9)=28.72ms
     iterations.....................: 410658  3395.122853/s
     success_rate...................: 100.00% ✓ 410658      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1224867     ✗ 0     
     data_received..................: 36 GB   295 MB/s
     data_sent......................: 491 MB  4.1 MB/s
     http_req_blocked...............: avg=2.42µs  min=822ns   med=1.83µs  max=4.97ms   p(90)=2.98µs  p(95)=3.66µs   p(99.9)=24.05µs
     http_req_connecting............: avg=248ns   min=0s      med=0s      max=4.27ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.49ms min=8.3ms   med=14.09ms max=294.8ms  p(90)=17.94ms p(95)=19.29ms  p(99.9)=27.26ms
       { expected_response:true }...: avg=14.49ms min=8.3ms   med=14.09ms max=294.8ms  p(90)=17.94ms p(95)=19.29ms  p(99.9)=27.26ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 408389
     http_req_receiving.............: avg=72.98µs min=23.97µs med=42.73µs max=117.69ms p(90)=89.63µs p(95)=168.19µs p(99.9)=1.98ms 
     http_req_sending...............: avg=31.61µs min=4.33µs  med=7.78µs  max=158.15ms p(90)=15.92µs p(95)=90.17µs  p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.38ms min=8.24ms  med=13.99ms max=176.63ms p(90)=17.84ms p(95)=19.18ms  p(99.9)=27.03ms
     http_reqs......................: 408389  3376.498022/s
     iteration_duration.............: avg=14.68ms min=8.45ms  med=14.28ms max=303.62ms p(90)=18.13ms p(95)=19.48ms  p(99.9)=27.52ms
     iterations.....................: 408289  3375.671237/s
     success_rate...................: 100.00% ✓ 408289      ✗ 0     
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

     checks.........................: 100.00% ✓ 1220691     ✗ 0     
     data_received..................: 36 GB   294 MB/s
     data_sent......................: 489 MB  4.0 MB/s
     http_req_blocked...............: avg=2.87µs  min=912ns   med=2.22µs  max=9.37ms   p(90)=3.6µs   p(95)=4.35µs   p(99.9)=31.31µs
     http_req_connecting............: avg=252ns   min=0s      med=0s      max=4.12ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.53ms min=8.28ms  med=14.09ms max=287.2ms  p(90)=17.99ms p(95)=19.39ms  p(99.9)=27.78ms
       { expected_response:true }...: avg=14.53ms min=8.28ms  med=14.09ms max=287.2ms  p(90)=17.99ms p(95)=19.39ms  p(99.9)=27.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 406997
     http_req_receiving.............: avg=72.93µs min=24.39µs med=45.05µs max=137.98ms p(90)=95.06µs p(95)=185.97µs p(99.9)=1.94ms 
     http_req_sending...............: avg=33.37µs min=4.31µs  med=8.28µs  max=194.82ms p(90)=16.9µs  p(95)=99.85µs  p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.43ms min=8.22ms  med=13.99ms max=263ms    p(90)=17.88ms p(95)=19.26ms  p(99.9)=27.48ms
     http_reqs......................: 406997  3364.612247/s
     iteration_duration.............: avg=14.73ms min=8.48ms  med=14.29ms max=297.22ms p(90)=18.19ms p(95)=19.58ms  p(99.9)=28.01ms
     iterations.....................: 406897  3363.785555/s
     success_rate...................: 100.00% ✓ 406897      ✗ 0     
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

     checks.........................: 100.00% ✓ 1216710     ✗ 0     
     data_received..................: 36 GB   294 MB/s
     data_sent......................: 488 MB  4.0 MB/s
     http_req_blocked...............: avg=2.56µs  min=821ns   med=1.84µs  max=61.84ms  p(90)=3.05µs  p(95)=3.8µs    p(99.9)=25.48µs
     http_req_connecting............: avg=379ns   min=0s      med=0s      max=61.78ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.59ms min=8.26ms  med=14.17ms max=281.7ms  p(90)=17.98ms p(95)=19.33ms  p(99.9)=27.27ms
       { expected_response:true }...: avg=14.59ms min=8.26ms  med=14.17ms max=281.7ms  p(90)=17.98ms p(95)=19.33ms  p(99.9)=27.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405670
     http_req_receiving.............: avg=66.62µs min=23.34µs med=42.58µs max=107.03ms p(90)=89.14µs p(95)=168.35µs p(99.9)=1.66ms 
     http_req_sending...............: avg=29.39µs min=4.01µs  med=7.71µs  max=93.6ms   p(90)=15.79µs p(95)=92.17µs  p(99.9)=1.56ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.49ms min=8.21ms  med=14.08ms max=281.06ms p(90)=17.88ms p(95)=19.22ms  p(99.9)=27.07ms
     http_reqs......................: 405670  3353.748058/s
     iteration_duration.............: avg=14.78ms min=8.43ms  med=14.36ms max=290.54ms p(90)=18.17ms p(95)=19.51ms  p(99.9)=27.57ms
     iterations.....................: 405570  3352.92134/s
     success_rate...................: 100.00% ✓ 405570      ✗ 0     
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

     checks.........................: 100.00% ✓ 1190082     ✗ 0     
     data_received..................: 35 GB   287 MB/s
     data_sent......................: 477 MB  3.9 MB/s
     http_req_blocked...............: avg=3.13µs  min=882ns   med=2.5µs   max=5.39ms   p(90)=4.1µs   p(95)=4.94µs   p(99.9)=34.08µs
     http_req_connecting............: avg=229ns   min=0s      med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.9ms  min=8.51ms  med=14.52ms max=300.16ms p(90)=18.11ms p(95)=19.41ms  p(99.9)=27.23ms
       { expected_response:true }...: avg=14.9ms  min=8.51ms  med=14.52ms max=300.16ms p(90)=18.11ms p(95)=19.41ms  p(99.9)=27.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 396794
     http_req_receiving.............: avg=75.63µs min=24.24µs med=47.79µs max=172.33ms p(90)=99.16µs p(95)=190.76µs p(99.9)=1.87ms 
     http_req_sending...............: avg=35.07µs min=4.53µs  med=9.3µs   max=115.81ms p(90)=19.02µs p(95)=107.49µs p(99.9)=1.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.79ms min=8.46ms  med=14.42ms max=299.56ms p(90)=17.99ms p(95)=19.28ms  p(99.9)=26.98ms
     http_reqs......................: 396794  3280.084325/s
     iteration_duration.............: avg=15.11ms min=8.63ms  med=14.72ms max=311.43ms p(90)=18.31ms p(95)=19.62ms  p(99.9)=27.46ms
     iterations.....................: 396694  3279.257678/s
     success_rate...................: 100.00% ✓ 396694      ✗ 0     
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

     checks.........................: 100.00% ✓ 1015302     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 407 MB  3.4 MB/s
     http_req_blocked...............: avg=2.5µs   min=772ns   med=1.87µs  max=3.48ms   p(90)=3.24µs  p(95)=4.14µs   p(99.9)=24.83µs
     http_req_connecting............: avg=249ns   min=0s      med=0s      max=3.44ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.51ms min=11.59ms med=17.08ms max=282.94ms p(90)=20.6ms  p(95)=21.82ms  p(99.9)=28.66ms
       { expected_response:true }...: avg=17.51ms min=11.59ms med=17.08ms max=282.94ms p(90)=20.6ms  p(95)=21.82ms  p(99.9)=28.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 338534
     http_req_receiving.............: avg=65.32µs min=23.54µs med=42.88µs max=154.22ms p(90)=90.21µs p(95)=143.25µs p(99.9)=1.47ms 
     http_req_sending...............: avg=27.08µs min=4.39µs  med=7.85µs  max=58.97ms  p(90)=15.86µs p(95)=81.46µs  p(99.9)=1.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.42ms min=11.53ms med=17ms    max=282.39ms p(90)=20.49ms p(95)=21.71ms  p(99.9)=28.48ms
     http_reqs......................: 338534  2788.746632/s
     iteration_duration.............: avg=17.72ms min=11.77ms med=17.28ms max=291.88ms p(90)=20.79ms p(95)=22.02ms  p(99.9)=28.88ms
     iterations.....................: 338434  2787.92286/s
     success_rate...................: 100.00% ✓ 338434      ✗ 0     
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

     checks.........................: 100.00% ✓ 1011603     ✗ 0     
     data_received..................: 30 GB   243 MB/s
     data_sent......................: 405 MB  3.3 MB/s
     http_req_blocked...............: avg=2.56µs  min=821ns   med=1.87µs  max=4.27ms   p(90)=3.29µs  p(95)=4.13µs   p(99.9)=26.01µs
     http_req_connecting............: avg=296ns   min=0s      med=0s      max=4.23ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.58ms min=11.73ms med=17.15ms max=289.48ms p(90)=20.68ms p(95)=21.93ms  p(99.9)=29.2ms 
       { expected_response:true }...: avg=17.58ms min=11.73ms med=17.15ms max=289.48ms p(90)=20.68ms p(95)=21.93ms  p(99.9)=29.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 337301
     http_req_receiving.............: avg=84.08µs min=24.22µs med=45.05µs max=257.36ms p(90)=92.88µs p(95)=141.21µs p(99.9)=1.47ms 
     http_req_sending...............: avg=26.34µs min=4.32µs  med=7.85µs  max=32.52ms  p(90)=15.73µs p(95)=76.48µs  p(99.9)=1.47ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.47ms min=11.67ms med=17.06ms max=100.85ms p(90)=20.58ms p(95)=21.82ms  p(99.9)=28.98ms
     http_reqs......................: 337301  2778.559047/s
     iteration_duration.............: avg=17.78ms min=11.89ms med=17.35ms max=313.52ms p(90)=20.88ms p(95)=22.12ms  p(99.9)=29.43ms
     iterations.....................: 337201  2777.735284/s
     success_rate...................: 100.00% ✓ 337201      ✗ 0     
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

     checks.........................: 100.00% ✓ 1007163     ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 404 MB  3.3 MB/s
     http_req_blocked...............: avg=2.87µs  min=911ns   med=2.23µs  max=3.83ms   p(90)=3.58µs  p(95)=4.32µs   p(99.9)=29.46µs
     http_req_connecting............: avg=302ns   min=0s      med=0s      max=3.79ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.65ms min=11.96ms med=17.24ms max=285.61ms p(90)=20.62ms p(95)=21.88ms  p(99.9)=28.96ms
       { expected_response:true }...: avg=17.65ms min=11.96ms med=17.24ms max=285.61ms p(90)=20.62ms p(95)=21.88ms  p(99.9)=28.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 335821
     http_req_receiving.............: avg=69.82µs min=23.46µs med=45.89µs max=234.05ms p(90)=92.97µs p(95)=156.03µs p(99.9)=1.34ms 
     http_req_sending...............: avg=29.09µs min=4.3µs   med=8.58µs  max=104.8ms  p(90)=17.32µs p(95)=89.43µs  p(99.9)=1.27ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.55ms min=11.9ms  med=17.15ms max=285.28ms p(90)=20.52ms p(95)=21.77ms  p(99.9)=28.7ms 
     http_reqs......................: 335821  2765.916979/s
     iteration_duration.............: avg=17.86ms min=12.14ms med=17.44ms max=296.64ms p(90)=20.82ms p(95)=22.08ms  p(99.9)=29.2ms 
     iterations.....................: 335721  2765.093351/s
     success_rate...................: 100.00% ✓ 335721      ✗ 0     
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

     checks.........................: 100.00% ✓ 1005165     ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 403 MB  3.3 MB/s
     http_req_blocked...............: avg=2.92µs  min=892ns   med=2.28µs  max=3.88ms   p(90)=3.69µs  p(95)=4.47µs   p(99.9)=29.66µs
     http_req_connecting............: avg=279ns   min=0s      med=0s      max=3.83ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.69ms min=11.74ms med=17.3ms  max=313.52ms p(90)=20.58ms p(95)=21.81ms  p(99.9)=29.21ms
       { expected_response:true }...: avg=17.69ms min=11.74ms med=17.3ms  max=313.52ms p(90)=20.58ms p(95)=21.81ms  p(99.9)=29.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 335155
     http_req_receiving.............: avg=87.29µs min=23.64µs med=46.22µs max=277.08ms p(90)=93.92µs p(95)=155.25µs p(99.9)=1.55ms 
     http_req_sending...............: avg=28.58µs min=4.42µs  med=8.7µs   max=26.06ms  p(90)=17.21µs p(95)=89.01µs  p(99.9)=1.46ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.57ms min=11.67ms med=17.21ms max=79.93ms  p(90)=20.48ms p(95)=21.69ms  p(99.9)=28.94ms
     http_reqs......................: 335155  2760.513641/s
     iteration_duration.............: avg=17.89ms min=11.9ms  med=17.5ms  max=331.76ms p(90)=20.78ms p(95)=22.01ms  p(99.9)=29.43ms
     iterations.....................: 335055  2759.689989/s
     success_rate...................: 100.00% ✓ 335055      ✗ 0     
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

     checks.........................: 100.00% ✓ 747582      ✗ 0     
     data_received..................: 22 GB   179 MB/s
     data_sent......................: 300 MB  2.5 MB/s
     http_req_blocked...............: avg=2.84µs  min=821ns   med=2.1µs   max=4.34ms   p(90)=3.72µs  p(95)=4.42µs  p(99.9)=29.96µs 
     http_req_connecting............: avg=383ns   min=0s      med=0s      max=4.27ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=23.85ms min=17.03ms med=23.51ms max=298.61ms p(90)=26.94ms p(95)=28.02ms p(99.9)=33.6ms  
       { expected_response:true }...: avg=23.85ms min=17.03ms med=23.51ms max=298.61ms p(90)=26.94ms p(95)=28.02ms p(99.9)=33.6ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 249294
     http_req_receiving.............: avg=64.97µs min=25.26µs med=49.69µs max=42.05ms  p(90)=91.77µs p(95)=116.1µs p(99.9)=897.29µs
     http_req_sending...............: avg=25.06µs min=4.37µs  med=9µs     max=180.93ms p(90)=17.2µs  p(95)=23.97µs p(99.9)=925.65µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=23.76ms min=16.94ms med=23.42ms max=298.05ms p(90)=26.85ms p(95)=27.93ms p(99.9)=33.47ms 
     http_reqs......................: 249294  2045.619899/s
     iteration_duration.............: avg=24.07ms min=17.24ms med=23.71ms max=307.38ms p(90)=27.15ms p(95)=28.22ms p(99.9)=33.81ms 
     iterations.....................: 249194  2044.799334/s
     success_rate...................: 100.00% ✓ 249194      ✗ 0     
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

     checks.........................: 100.00% ✓ 526518      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=3.34µs  min=842ns   med=2.24µs  max=4.18ms   p(90)=4.63µs   p(95)=5.59µs   p(99.9)=34.39µs
     http_req_connecting............: avg=553ns   min=0s      med=0s      max=4.14ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.93ms min=17.56ms med=33.66ms max=304.2ms  p(90)=39.65ms  p(95)=41.41ms  p(99.9)=49.85ms
       { expected_response:true }...: avg=33.93ms min=17.56ms med=33.66ms max=304.2ms  p(90)=39.65ms  p(95)=41.41ms  p(99.9)=49.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 175606
     http_req_receiving.............: avg=78.41µs min=25.25µs med=54.53µs max=62.68ms  p(90)=118.14µs p(95)=158.63µs p(99.9)=1.28ms 
     http_req_sending...............: avg=30.51µs min=4.62µs  med=9.3µs   max=134.91ms p(90)=21.85µs  p(95)=35.01µs  p(99.9)=1.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.82ms min=17.44ms med=33.56ms max=303.61ms p(90)=39.55ms  p(95)=41.29ms  p(99.9)=49.5ms 
     http_reqs......................: 175606  1440.111926/s
     iteration_duration.............: avg=34.17ms min=20.5ms  med=33.9ms  max=310.88ms p(90)=39.86ms  p(95)=41.62ms  p(99.9)=50.14ms
     iterations.....................: 175506  1439.291844/s
     success_rate...................: 100.00% ✓ 175506      ✗ 0     
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

     checks.........................: 100.00% ✓ 517338      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.38µs  min=912ns   med=2.18µs  max=7.12ms   p(90)=3.78µs  p(95)=4.5µs    p(99.9)=30.79µs 
     http_req_connecting............: avg=790ns   min=0s      med=0s      max=7.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.57ms min=18.02ms med=33.99ms max=296.71ms p(90)=41.3ms  p(95)=43.68ms  p(99.9)=55.73ms 
       { expected_response:true }...: avg=34.57ms min=18.02ms med=33.99ms max=296.71ms p(90)=41.3ms  p(95)=43.68ms  p(99.9)=55.73ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 172546
     http_req_receiving.............: avg=73.88µs min=25.28µs med=59.86µs max=236.06ms p(90)=99.16µs p(95)=116.66µs p(99.9)=779.78µs
     http_req_sending...............: avg=22.79µs min=4.56µs  med=10.26µs max=178.47ms p(90)=17.28µs p(95)=21.03µs  p(99.9)=777.34µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.47ms min=17.9ms  med=33.9ms  max=285.62ms p(90)=41.2ms  p(95)=43.58ms  p(99.9)=55.51ms 
     http_reqs......................: 172546  1414.822756/s
     iteration_duration.............: avg=34.78ms min=20.52ms med=34.19ms max=310.22ms p(90)=41.49ms p(95)=43.87ms  p(99.9)=56ms    
     iterations.....................: 172446  1414.002788/s
     success_rate...................: 100.00% ✓ 172446      ✗ 0     
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

     checks.........................: 100.00% ✓ 510033      ✗ 0     
     data_received..................: 15 GB   122 MB/s
     data_sent......................: 204 MB  1.7 MB/s
     http_req_blocked...............: avg=3.22µs  min=841ns   med=2.33µs  max=3.58ms   p(90)=4.06µs  p(95)=4.82µs   p(99.9)=32.12µs 
     http_req_connecting............: avg=560ns   min=0s      med=0s      max=3.55ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.06ms min=18.28ms med=34.5ms  max=287.69ms p(90)=41.46ms p(95)=43.76ms  p(99.9)=60.97ms 
       { expected_response:true }...: avg=35.06ms min=18.28ms med=34.5ms  max=287.69ms p(90)=41.46ms p(95)=43.76ms  p(99.9)=60.97ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 170111
     http_req_receiving.............: avg=99.14µs min=27.51µs med=61.27µs max=244.88ms p(90)=99.37µs p(95)=117.11µs p(99.9)=841.56µs
     http_req_sending...............: avg=20.76µs min=4.72µs  med=10.85µs max=114.33ms p(90)=17.83µs p(95)=21.6µs   p(99.9)=737.25µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.94ms min=18.14ms med=34.41ms max=229.83ms p(90)=41.37ms p(95)=43.65ms  p(99.9)=59.1ms  
     http_reqs......................: 170111  1394.694544/s
     iteration_duration.............: avg=35.28ms min=20.78ms med=34.71ms max=314.87ms p(90)=41.65ms p(95)=43.97ms  p(99.9)=61.44ms 
     iterations.....................: 170011  1393.874671/s
     success_rate...................: 100.00% ✓ 170011      ✗ 0     
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

     checks.........................: 100.00% ✓ 196152     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 79 MB   643 kB/s
     http_req_blocked...............: avg=5.11µs  min=1.19µs  med=3.37µs  max=3.53ms   p(90)=4.95µs   p(95)=5.64µs   p(99.9)=47.46µs 
     http_req_connecting............: avg=1.49µs  min=0s      med=0s      max=3.49ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.41ms min=20.75ms med=89.9ms  max=323.87ms p(90)=107.39ms p(95)=115.91ms p(99.9)=210.97ms
       { expected_response:true }...: avg=91.41ms min=20.75ms med=89.9ms  max=323.87ms p(90)=107.39ms p(95)=115.91ms p(99.9)=210.97ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65484
     http_req_receiving.............: avg=82.33µs min=31.41µs med=75.86µs max=6.05ms   p(90)=110.58µs p(95)=122.95µs p(99.9)=545.2µs 
     http_req_sending...............: avg=29.62µs min=5.05µs  med=15.2µs  max=136.53ms p(90)=21.08µs  p(95)=23.28µs  p(99.9)=598.5µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.3ms  min=20.61ms med=89.78ms max=323.58ms p(90)=107.27ms p(95)=115.8ms  p(99.9)=210.63ms
     http_reqs......................: 65484   535.695378/s
     iteration_duration.............: avg=91.77ms min=35.95ms med=90.16ms max=333.06ms p(90)=107.64ms p(95)=116.23ms p(99.9)=212.51ms
     iterations.....................: 65384   534.877322/s
     success_rate...................: 100.00% ✓ 65384      ✗ 0    
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

     checks.........................: 100.00% ✓ 177432     ✗ 0    
     data_received..................: 5.2 GB  42 MB/s
     data_sent......................: 71 MB   582 kB/s
     http_req_blocked...............: avg=4.46µs   min=1.1µs   med=2.67µs  max=3.96ms   p(90)=4.14µs   p(95)=4.71µs   p(99.9)=73.42µs 
     http_req_connecting............: avg=1.55µs   min=0s      med=0s      max=3.93ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=101.09ms min=19.73ms med=99.14ms max=325.51ms p(90)=128.29ms p(95)=137.54ms p(99.9)=178.4ms 
       { expected_response:true }...: avg=101.09ms min=19.73ms med=99.14ms max=325.51ms p(90)=128.29ms p(95)=137.54ms p(99.9)=178.4ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 59244
     http_req_receiving.............: avg=75.71µs  min=27.41µs med=70.45µs max=22.76ms  p(90)=102.1µs  p(95)=113.75µs p(99.9)=504.56µs
     http_req_sending...............: avg=22.23µs  min=5.08µs  med=13.25µs max=88ms     p(90)=18.89µs  p(95)=20.85µs  p(99.9)=437.96µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.99ms min=19.66ms med=99.04ms max=325.19ms p(90)=128.2ms  p(95)=137.44ms p(99.9)=178.34ms
     http_reqs......................: 59244   484.760642/s
     iteration_duration.............: avg=101.47ms min=30.63ms med=99.41ms max=338.44ms p(90)=128.55ms p(95)=137.8ms  p(99.9)=181.47ms
     iterations.....................: 59144   483.942398/s
     success_rate...................: 100.00% ✓ 59144      ✗ 0    
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

     checks.........................: 100.00% ✓ 153930     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 62 MB   505 kB/s
     http_req_blocked...............: avg=5.1µs    min=1.09µs  med=2.99µs   max=3.99ms   p(90)=4.43µs   p(95)=5µs      p(99.9)=108.29µs
     http_req_connecting............: avg=1.91µs   min=0s      med=0s       max=3.95ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=116.52ms min=21.2ms  med=114.98ms max=341.8ms  p(90)=143.81ms p(95)=153.55ms p(99.9)=196.75ms
       { expected_response:true }...: avg=116.52ms min=21.2ms  med=114.98ms max=341.8ms  p(90)=143.81ms p(95)=153.55ms p(99.9)=196.75ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51410
     http_req_receiving.............: avg=82.9µs   min=27.64µs med=77.65µs  max=107.62ms p(90)=109.2µs  p(95)=120.73µs p(99.9)=490.94µs
     http_req_sending...............: avg=19.43µs  min=5.08µs  med=14.87µs  max=63ms     p(90)=19.87µs  p(95)=21.82µs  p(99.9)=502.92µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.42ms min=21.07ms med=114.89ms max=341.24ms p(90)=143.72ms p(95)=153.46ms p(99.9)=196.35ms
     http_reqs......................: 51410   420.287404/s
     iteration_duration.............: avg=116.96ms min=35.65ms med=115.27ms max=358.97ms p(90)=144.1ms  p(95)=153.81ms p(99.9)=199.49ms
     iterations.....................: 51310   419.469884/s
     success_rate...................: 100.00% ✓ 51310      ✗ 0    
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

     checks.........................: 100.00% ✓ 97452      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   319 kB/s
     http_req_blocked...............: avg=6.26µs   min=1.14µs  med=3.04µs   max=3.52ms   p(90)=4.35µs   p(95)=4.88µs   p(99.9)=1.61ms  
     http_req_connecting............: avg=2.97µs   min=0s      med=0s       max=3.48ms   p(90)=0s       p(95)=0s       p(99.9)=1.51ms  
     http_req_duration..............: avg=184.02ms min=22.8ms  med=176.98ms max=372.48ms p(90)=209.74ms p(95)=215.94ms p(99.9)=280.38ms
       { expected_response:true }...: avg=184.02ms min=22.8ms  med=176.98ms max=372.48ms p(90)=209.74ms p(95)=215.94ms p(99.9)=280.38ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32584
     http_req_receiving.............: avg=97µs     min=33.79µs med=84.04µs  max=171.17ms p(90)=113.99µs p(95)=125.14µs p(99.9)=475.17µs
     http_req_sending...............: avg=23.65µs  min=5.36µs  med=15.94µs  max=63.85ms  p(90)=20.07µs  p(95)=21.79µs  p(99.9)=498.83µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.9ms  min=22.71ms med=176.87ms max=371.27ms p(90)=209.62ms p(95)=215.82ms p(99.9)=280.07ms
     http_reqs......................: 32584   265.837643/s
     iteration_duration.............: avg=184.8ms  min=49.76ms med=177.24ms max=386.45ms p(90)=210.01ms p(95)=216.24ms p(99.9)=282.23ms
     iterations.....................: 32484   265.021789/s
     success_rate...................: 100.00% ✓ 32484      ✗ 0    
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

     checks.........................: 100.00% ✓ 95217      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   313 kB/s
     http_req_blocked...............: avg=6µs      min=1.09µs  med=3.08µs   max=3.63ms   p(90)=4.42µs   p(95)=4.98µs   p(99.9)=1.39ms  
     http_req_connecting............: avg=2.76µs   min=0s      med=0s       max=3.58ms   p(90)=0s       p(95)=0s       p(99.9)=1.37ms  
     http_req_duration..............: avg=188.34ms min=18.14ms med=175.56ms max=774.16ms p(90)=218.74ms p(95)=240.11ms p(99.9)=707.8ms 
       { expected_response:true }...: avg=188.34ms min=18.14ms med=175.56ms max=774.16ms p(90)=218.74ms p(95)=240.11ms p(99.9)=707.8ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 31839
     http_req_receiving.............: avg=93.03µs  min=31.65µs med=84.51µs  max=66.76ms  p(90)=113.55µs p(95)=124.93µs p(99.9)=709.3µs 
     http_req_sending...............: avg=23.9µs   min=5.22µs  med=16.1µs   max=52.7ms   p(90)=20.26µs  p(95)=22.09µs  p(99.9)=507.4µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=188.22ms min=18.07ms med=175.46ms max=774.04ms p(90)=218.64ms p(95)=239.97ms p(99.9)=707.69ms
     http_reqs......................: 31839   260.510152/s
     iteration_duration.............: avg=189.13ms min=61.43ms med=175.95ms max=774.4ms  p(90)=219.08ms p(95)=240.7ms  p(99.9)=708.11ms
     iterations.....................: 31739   259.691941/s
     success_rate...................: 100.00% ✓ 31739      ✗ 0    
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

