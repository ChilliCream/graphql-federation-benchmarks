## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 3,405 | 3,429 | 3,379 | 0.6% | 366 MB | 110.2 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,388 | 3,415 | 3,376 | 0.4% | 386 MB | 116.6 KB |  |
| fusion-aot-11 | 16.7.3 | 3,370 | 3,399 | 3,364 | 0.5% | 127 MB | 38.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,353 | 3,373 | 3,337 | 0.4% | 152 MB | 46.6 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,283 | 3,313 | 3,242 | 0.8% | 2,294 MB | 715.5 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,790 | 2,800 | 2,780 | 0.3% | 392 MB | 143.8 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,771 | 2,779 | 2,769 | 0.1% | 405 MB | 149.7 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,757 | 2,759 | 2,750 | 0.1% | 155 MB | 57.5 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,749 | 2,753 | 2,739 | 0.2% | 133 MB | 49.4 KB |  |
| hive-router | v0.3.10 | 2,061 | 2,067 | 2,041 | 0.6% | 93 MB | 46.0 KB |  |
| caliban | 3.2.0 | 1,498 | 1,502 | 1,496 | 0.2% | 5,498 MB | 3,758.5 KB |  |
| grafbase | 0.53.5 | 1,443 | 1,446 | 1,435 | 0.4% | 100 MB | 70.8 KB |  |
| cosmo | 0.365.2 | 1,409 | 1,410 | 1,406 | 0.1% | 151 MB | 110.0 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 531 | 533 | 526 | 0.5% | 2,743 MB | 5,290.5 KB |  |
| apollo-router | v2.19.0 | 490 | 496 | 487 | 0.8% | 181 MB | 377.5 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 402 | 404 | 397 | 0.7% | 197 MB | 500.7 KB |  |
| apollo-gateway | 2.14.4 | 267 | 268 | 266 | 0.3% | 2,164 MB | 8,300.4 KB |  |
| hive-gateway | 2.15.6 | 261 | 262 | 260 | 0.3% | 3,491 MB | 13,696.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1235550     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 495 MB  4.1 MB/s
     http_req_blocked...............: avg=2.85µs  min=902ns   med=2.27µs  max=7.38ms   p(90)=3.65µs  p(95)=4.4µs    p(99.9)=30.49µs
     http_req_connecting............: avg=189ns   min=0s      med=0s      max=4.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.36ms min=8.21ms  med=13.9ms  max=271.23ms p(90)=17.93ms p(95)=19.36ms  p(99.9)=28.01ms
       { expected_response:true }...: avg=14.36ms min=8.21ms  med=13.9ms  max=271.23ms p(90)=17.93ms p(95)=19.36ms  p(99.9)=28.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 411950
     http_req_receiving.............: avg=72.25µs min=24.04µs med=44.61µs max=197.57ms p(90)=93.42µs p(95)=181.65µs p(99.9)=2.01ms 
     http_req_sending...............: avg=33.37µs min=4.29µs  med=8.4µs   max=154.56ms p(90)=16.87µs p(95)=97.99µs  p(99.9)=2.11ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.25ms min=8.17ms  med=13.8ms  max=270.95ms p(90)=17.81ms p(95)=19.23ms  p(99.9)=27.82ms
     http_reqs......................: 411950  3405.71011/s
     iteration_duration.............: avg=14.55ms min=8.33ms  med=14.09ms max=294.08ms p(90)=18.12ms p(95)=19.56ms  p(99.9)=28.24ms
     iterations.....................: 411850  3404.883381/s
     success_rate...................: 100.00% ✓ 411850      ✗ 0     
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

     checks.........................: 100.00% ✓ 1229310     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 493 MB  4.1 MB/s
     http_req_blocked...............: avg=2.79µs  min=871ns  med=2.24µs  max=3.83ms   p(90)=3.54µs  p(95)=4.27µs   p(99.9)=27.45µs
     http_req_connecting............: avg=193ns   min=0s     med=0s      max=3.78ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.43ms min=8.36ms med=13.97ms max=306.13ms p(90)=18.06ms p(95)=19.47ms  p(99.9)=28.21ms
       { expected_response:true }...: avg=14.43ms min=8.36ms med=13.97ms max=306.13ms p(90)=18.06ms p(95)=19.47ms  p(99.9)=28.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 409870
     http_req_receiving.............: avg=72.34µs min=24.1µs med=45.8µs  max=11.7ms   p(90)=93.85µs p(95)=179.89µs p(99.9)=2.11ms 
     http_req_sending...............: avg=34.24µs min=4.38µs med=8.41µs  max=161.57ms p(90)=16.93µs p(95)=96.56µs  p(99.9)=2.17ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.32ms min=8.22ms med=13.87ms max=305.83ms p(90)=17.94ms p(95)=19.34ms  p(99.9)=27.95ms
     http_reqs......................: 409870  3388.680836/s
     iteration_duration.............: avg=14.63ms min=8.51ms med=14.17ms max=335.8ms  p(90)=18.25ms p(95)=19.67ms  p(99.9)=28.45ms
     iterations.....................: 409770  3387.854066/s
     success_rate...................: 100.00% ✓ 409770      ✗ 0     
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

     checks.........................: 100.00% ✓ 1222647     ✗ 0     
     data_received..................: 36 GB   295 MB/s
     data_sent......................: 490 MB  4.0 MB/s
     http_req_blocked...............: avg=2.68µs  min=812ns   med=2.14µs  max=3.5ms    p(90)=3.46µs  p(95)=4.18µs  p(99.9)=28.39µs
     http_req_connecting............: avg=211ns   min=0s      med=0s      max=3.47ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.51ms min=8.3ms   med=14.05ms max=292.89ms p(90)=18.02ms p(95)=19.44ms p(99.9)=27.65ms
       { expected_response:true }...: avg=14.51ms min=8.3ms   med=14.05ms max=292.89ms p(90)=18.02ms p(95)=19.44ms p(99.9)=27.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 407649
     http_req_receiving.............: avg=70.97µs min=23.79µs med=44.48µs max=189.64ms p(90)=92.19µs p(95)=177.2µs p(99.9)=1.96ms 
     http_req_sending...............: avg=32.59µs min=4.49µs  med=8.42µs  max=154.7ms  p(90)=16.37µs p(95)=96.27µs p(99.9)=1.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.41ms min=8.25ms  med=13.95ms max=278.71ms p(90)=17.91ms p(95)=19.32ms p(99.9)=27.47ms
     http_reqs......................: 407649  3370.054474/s
     iteration_duration.............: avg=14.71ms min=8.49ms  med=14.25ms max=301.85ms p(90)=18.21ms p(95)=19.63ms p(99.9)=27.87ms
     iterations.....................: 407549  3369.227769/s
     success_rate...................: 100.00% ✓ 407549      ✗ 0     
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

     checks.........................: 100.00% ✓ 1216443     ✗ 0     
     data_received..................: 36 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=2.39µs  min=771ns   med=1.84µs  max=3.46ms   p(90)=2.97µs  p(95)=3.65µs   p(99.9)=24.79µs
     http_req_connecting............: avg=209ns   min=0s      med=0s      max=3.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.59ms min=8.31ms  med=14.18ms max=282.41ms p(90)=17.98ms p(95)=19.35ms  p(99.9)=27.1ms 
       { expected_response:true }...: avg=14.59ms min=8.31ms  med=14.18ms max=282.41ms p(90)=17.98ms p(95)=19.35ms  p(99.9)=27.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 405581
     http_req_receiving.............: avg=66.93µs min=23.55µs med=42.4µs  max=99.74ms  p(90)=88.16µs p(95)=162.06µs p(99.9)=1.68ms 
     http_req_sending...............: avg=29.87µs min=4.18µs  med=7.69µs  max=211.87ms p(90)=15.6µs  p(95)=88.68µs  p(99.9)=1.64ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.5ms  min=8.24ms  med=14.08ms max=253.42ms p(90)=17.89ms p(95)=19.25ms  p(99.9)=26.92ms
     http_reqs......................: 405581  3353.006345/s
     iteration_duration.............: avg=14.78ms min=8.43ms  med=14.37ms max=297.15ms p(90)=18.17ms p(95)=19.53ms  p(99.9)=27.31ms
     iterations.....................: 405481  3352.179629/s
     success_rate...................: 100.00% ✓ 405481      ✗ 0     
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

     checks.........................: 100.00% ✓ 1191057     ✗ 0     
     data_received..................: 35 GB   287 MB/s
     data_sent......................: 477 MB  3.9 MB/s
     http_req_blocked...............: avg=3.06µs  min=891ns   med=2.44µs  max=4.22ms   p(90)=3.95µs  p(95)=4.77µs   p(99.9)=29.82µs
     http_req_connecting............: avg=257ns   min=0s      med=0s      max=4.18ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.9ms  min=8.46ms  med=14.52ms max=289.21ms p(90)=18.06ms p(95)=19.34ms  p(99.9)=27.13ms
       { expected_response:true }...: avg=14.9ms  min=8.46ms  med=14.52ms max=289.21ms p(90)=18.06ms p(95)=19.34ms  p(99.9)=27.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 397119
     http_req_receiving.............: avg=73.82µs min=24.11µs med=47.59µs max=18.98ms  p(90)=98.42µs p(95)=187.74µs p(99.9)=1.79ms 
     http_req_sending...............: avg=34.91µs min=4.48µs  med=9.09µs  max=166.21ms p(90)=18.41µs p(95)=104.54µs p(99.9)=1.85ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.79ms min=8.4ms   med=14.42ms max=289.02ms p(90)=17.95ms p(95)=19.21ms  p(99.9)=26.94ms
     http_reqs......................: 397119  3283.028645/s
     iteration_duration.............: avg=15.1ms  min=8.63ms  med=14.72ms max=306ms    p(90)=18.26ms p(95)=19.53ms  p(99.9)=27.35ms
     iterations.....................: 397019  3282.201933/s
     success_rate...................: 100.00% ✓ 397019      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1016160     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 407 MB  3.4 MB/s
     http_req_blocked...............: avg=2.44µs  min=771ns   med=1.78µs  max=3.84ms   p(90)=3.08µs  p(95)=3.85µs   p(99.9)=25.38µs
     http_req_connecting............: avg=266ns   min=0s      med=0s      max=3.76ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.5ms  min=11.67ms med=17.06ms max=281.49ms p(90)=20.57ms p(95)=21.84ms  p(99.9)=28.76ms
       { expected_response:true }...: avg=17.5ms  min=11.67ms med=17.06ms max=281.49ms p(90)=20.57ms p(95)=21.84ms  p(99.9)=28.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 338820
     http_req_receiving.............: avg=69.28µs min=23.52µs med=42.27µs max=194.42ms p(90)=89.02µs p(95)=137.25µs p(99.9)=1.39ms 
     http_req_sending...............: avg=27.47µs min=4.14µs  med=7.61µs  max=151.37ms p(90)=16.43µs p(95)=76.04µs  p(99.9)=1.47ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.4ms  min=11.62ms med=16.98ms max=281.26ms p(90)=20.47ms p(95)=21.73ms  p(99.9)=28.57ms
     http_reqs......................: 338820  2790.960747/s
     iteration_duration.............: avg=17.7ms  min=11.79ms med=17.26ms max=300.57ms p(90)=20.77ms p(95)=22.03ms  p(99.9)=29ms   
     iterations.....................: 338720  2790.137017/s
     success_rate...................: 100.00% ✓ 338720      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 1009065     ✗ 0     
     data_received..................: 29 GB   243 MB/s
     data_sent......................: 404 MB  3.3 MB/s
     http_req_blocked...............: avg=3.19µs  min=901ns   med=2.27µs  max=6.29ms   p(90)=3.81µs  p(95)=4.65µs   p(99.9)=31.61µs
     http_req_connecting............: avg=520ns   min=0s      med=0s      max=6.26ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.62ms min=11.77ms med=17.16ms max=278.5ms  p(90)=20.82ms p(95)=22.15ms  p(99.9)=29.81ms
       { expected_response:true }...: avg=17.62ms min=11.77ms med=17.16ms max=278.5ms  p(90)=20.82ms p(95)=22.15ms  p(99.9)=29.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 336455
     http_req_receiving.............: avg=69.57µs min=23.74µs med=45.36µs max=15.45ms  p(90)=97.15µs p(95)=161.58µs p(99.9)=1.65ms 
     http_req_sending...............: avg=29.38µs min=4.18µs  med=8.53µs  max=27.27ms  p(90)=18.05µs p(95)=89.27µs  p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.52ms min=11.71ms med=17.07ms max=278.38ms p(90)=20.7ms  p(95)=22.03ms  p(99.9)=29.6ms 
     http_reqs......................: 336455  2771.430775/s
     iteration_duration.............: avg=17.82ms min=11.93ms med=17.36ms max=310.33ms p(90)=21.02ms p(95)=22.34ms  p(99.9)=30.04ms
     iterations.....................: 336355  2770.60706/s
     success_rate...................: 100.00% ✓ 336355      ✗ 0     
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

     checks.........................: 100.00% ✓ 1003851     ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 402 MB  3.3 MB/s
     http_req_blocked...............: avg=2.55µs  min=812ns   med=1.93µs  max=3.49ms   p(90)=3.3µs   p(95)=4.06µs   p(99.9)=25.81µs
     http_req_connecting............: avg=256ns   min=0s      med=0s      max=3.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.72ms min=11.87ms med=17.3ms  max=296.37ms p(90)=20.67ms p(95)=21.89ms  p(99.9)=28.79ms
       { expected_response:true }...: avg=17.72ms min=11.87ms med=17.3ms  max=296.37ms p(90)=20.67ms p(95)=21.89ms  p(99.9)=28.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 334717
     http_req_receiving.............: avg=66µs    min=23.48µs med=43.96µs max=188.91ms p(90)=91.12µs p(95)=141.18µs p(99.9)=1.29ms 
     http_req_sending...............: avg=26.6µs  min=4.14µs  med=8µs     max=44.11ms  p(90)=16.2µs  p(95)=80.77µs  p(99.9)=1.28ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.62ms min=11.8ms  med=17.22ms max=278.63ms p(90)=20.57ms p(95)=21.78ms  p(99.9)=28.55ms
     http_reqs......................: 334717  2757.003999/s
     iteration_duration.............: avg=17.92ms min=11.99ms med=17.5ms  max=305.1ms  p(90)=20.87ms p(95)=22.08ms  p(99.9)=29.03ms
     iterations.....................: 334617  2756.180317/s
     success_rate...................: 100.00% ✓ 334617      ✗ 0     
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

     checks.........................: 100.00% ✓ 1000887    ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 401 MB  3.3 MB/s
     http_req_blocked...............: avg=2.99µs  min=892ns   med=2.29µs  max=4.3ms    p(90)=3.77µs  p(95)=4.57µs   p(99.9)=32.55µs
     http_req_connecting............: avg=333ns   min=0s      med=0s      max=4.25ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.76ms min=11.89ms med=17.33ms max=288.68ms p(90)=20.82ms p(95)=22.12ms  p(99.9)=29.27ms
       { expected_response:true }...: avg=17.76ms min=11.89ms med=17.33ms max=288.68ms p(90)=20.82ms p(95)=22.12ms  p(99.9)=29.27ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 333729
     http_req_receiving.............: avg=68.01µs min=23.88µs med=45.14µs max=23.37ms  p(90)=93.05µs p(95)=155.97µs p(99.9)=1.43ms 
     http_req_sending...............: avg=29.6µs  min=4.31µs  med=8.63µs  max=154.18ms p(90)=17.39µs p(95)=88.82µs  p(99.9)=1.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.67ms min=11.79ms med=17.24ms max=288.52ms p(90)=20.71ms p(95)=21.99ms  p(99.9)=29.03ms
     http_reqs......................: 333729  2749.06046/s
     iteration_duration.............: avg=17.97ms min=12.12ms med=17.53ms max=304.67ms p(90)=21.02ms p(95)=22.31ms  p(99.9)=29.48ms
     iterations.....................: 333629  2748.23672/s
     success_rate...................: 100.00% ✓ 333629     ✗ 0     
     vus............................: 50      min=0        max=50  
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 753339      ✗ 0     
     data_received..................: 22 GB   180 MB/s
     data_sent......................: 302 MB  2.5 MB/s
     http_req_blocked...............: avg=2.79µs  min=882ns   med=2.07µs  max=4.29ms   p(90)=3.62µs  p(95)=4.32µs   p(99.9)=25.12µs 
     http_req_connecting............: avg=382ns   min=0s      med=0s      max=4.24ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.67ms min=16.82ms med=23.32ms max=296.15ms p(90)=26.67ms p(95)=27.75ms  p(99.9)=33.07ms 
       { expected_response:true }...: avg=23.67ms min=16.82ms med=23.32ms max=296.15ms p(90)=26.67ms p(95)=27.75ms  p(99.9)=33.07ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 251213
     http_req_receiving.............: avg=62.98µs min=23.94µs med=47.67µs max=72.33ms  p(90)=88.98µs p(95)=111.07µs p(99.9)=866.64µs
     http_req_sending...............: avg=23.45µs min=4.44µs  med=9.24µs  max=88.83ms  p(90)=17.45µs p(95)=23.46µs  p(99.9)=909.67µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.58ms min=16.76ms med=23.24ms max=276.6ms  p(90)=26.58ms p(95)=27.66ms  p(99.9)=32.93ms 
     http_reqs......................: 251213  2061.424409/s
     iteration_duration.............: avg=23.88ms min=17.01ms med=23.52ms max=308.28ms p(90)=26.87ms p(95)=27.95ms  p(99.9)=33.31ms 
     iterations.....................: 251113  2060.603821/s
     success_rate...................: 100.00% ✓ 251113      ✗ 0     
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

     checks.........................: 100.00% ✓ 547845      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 220 MB  1.8 MB/s
     http_req_blocked...............: avg=3.75µs  min=891ns   med=2.53µs  max=6.55ms   p(90)=4.53µs   p(95)=5.35µs  p(99.9)=34.82µs 
     http_req_connecting............: avg=786ns   min=0s      med=0s      max=6.2ms    p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=32.61ms min=17.85ms med=32.14ms max=286.2ms  p(90)=37.9ms   p(95)=39.93ms p(99.9)=51.08ms 
       { expected_response:true }...: avg=32.61ms min=17.85ms med=32.14ms max=286.2ms  p(90)=37.9ms   p(95)=39.93ms p(99.9)=51.08ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 182715
     http_req_receiving.............: avg=77.97µs min=27.49µs med=62.41µs max=198.94ms p(90)=105.66µs p(95)=125.5µs p(99.9)=1.03ms  
     http_req_sending...............: avg=22.62µs min=4.55µs  med=11.71µs max=83.45ms  p(90)=20.13µs  p(95)=24.11µs p(99.9)=814.99µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=32.51ms min=17.78ms med=32.05ms max=285.57ms p(90)=37.8ms   p(95)=39.84ms p(99.9)=50.99ms 
     http_reqs......................: 182715  1498.164117/s
     iteration_duration.............: avg=32.84ms min=20.59ms med=32.36ms max=297.09ms p(90)=38.12ms  p(95)=40.15ms p(99.9)=51.33ms 
     iterations.....................: 182615  1497.344171/s
     success_rate...................: 100.00% ✓ 182615      ✗ 0     
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

     checks.........................: 100.00% ✓ 527784      ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 212 MB  1.7 MB/s
     http_req_blocked...............: avg=3.07µs  min=842ns   med=2.11µs  max=3.38ms   p(90)=4.37µs   p(95)=5.33µs   p(99.9)=32.76µs
     http_req_connecting............: avg=444ns   min=0s      med=0s      max=3.31ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.85ms min=17.5ms  med=33.51ms max=292.4ms  p(90)=39.51ms  p(95)=41.25ms  p(99.9)=50.41ms
       { expected_response:true }...: avg=33.85ms min=17.5ms  med=33.51ms max=292.4ms  p(90)=39.51ms  p(95)=41.25ms  p(99.9)=50.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 176028
     http_req_receiving.............: avg=78.06µs min=24.96µs med=53.35µs max=200.22ms p(90)=113.62µs p(95)=154.63µs p(99.9)=1.47ms 
     http_req_sending...............: avg=26.65µs min=4.27µs  med=9.06µs  max=69.34ms  p(90)=21.29µs  p(95)=33.16µs  p(99.9)=1.21ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.74ms min=17.39ms med=33.41ms max=291.69ms p(90)=39.41ms  p(95)=41.14ms  p(99.9)=50.08ms
     http_reqs......................: 176028  1443.684112/s
     iteration_duration.............: avg=34.09ms min=20.04ms med=33.74ms max=307.12ms p(90)=39.73ms  p(95)=41.46ms  p(99.9)=50.65ms
     iterations.....................: 175928  1442.863968/s
     success_rate...................: 100.00% ✓ 175928      ✗ 0     
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

     checks.........................: 100.00% ✓ 515517      ✗ 0     
     data_received..................: 15 GB   123 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.51µs  min=1.05µs  med=2.69µs  max=3.57ms   p(90)=4.29µs   p(95)=5.02µs  p(99.9)=32.45µs 
     http_req_connecting............: avg=518ns   min=0s      med=0s      max=3.54ms   p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=34.68ms min=18.24ms med=34.11ms max=311.37ms p(90)=41.41ms  p(95)=43.83ms p(99.9)=55.95ms 
       { expected_response:true }...: avg=34.68ms min=18.24ms med=34.11ms max=311.37ms p(90)=41.41ms  p(95)=43.83ms p(99.9)=55.95ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 171939
     http_req_receiving.............: avg=76.69µs min=26.11µs med=62.22µs max=172.87ms p(90)=100.82µs p(95)=118.4µs p(99.9)=748.4µs 
     http_req_sending...............: avg=22.81µs min=5.07µs  med=11.35µs max=57.9ms   p(90)=17.96µs  p(95)=22.21µs p(99.9)=784.76µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=34.58ms min=18.08ms med=34.01ms max=310.73ms p(90)=41.31ms  p(95)=43.72ms p(99.9)=55.77ms 
     http_reqs......................: 171939  1409.792471/s
     iteration_duration.............: avg=34.91ms min=20.81ms med=34.31ms max=320.95ms p(90)=41.61ms  p(95)=44.03ms p(99.9)=56.26ms 
     iterations.....................: 171839  1408.972533/s
     success_rate...................: 100.00% ✓ 171839      ✗ 0     
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

     checks.........................: 100.00% ✓ 194433     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   638 kB/s
     http_req_blocked...............: avg=4.98µs  min=1.16µs  med=3.21µs  max=3.75ms   p(90)=4.75µs   p(95)=5.43µs   p(99.9)=52.16µs 
     http_req_connecting............: avg=1.52µs  min=0s      med=0s      max=3.71ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.22ms min=20.76ms med=90.16ms max=338.99ms p(90)=111.37ms p(95)=120.92ms p(99.9)=215.21ms
       { expected_response:true }...: avg=92.22ms min=20.76ms med=90.16ms max=338.99ms p(90)=111.37ms p(95)=120.92ms p(99.9)=215.21ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64911
     http_req_receiving.............: avg=83.06µs min=29.13µs med=73.76µs max=198.46ms p(90)=106.34µs p(95)=118.43µs p(99.9)=594.79µs
     http_req_sending...............: avg=23.74µs min=5.31µs  med=14.39µs max=103.9ms  p(90)=20.34µs  p(95)=22.47µs  p(99.9)=566.64µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.12ms min=20.5ms  med=90.06ms max=338.57ms p(90)=111.27ms p(95)=120.8ms  p(99.9)=215.09ms
     http_reqs......................: 64911   531.041602/s
     iteration_duration.............: avg=92.58ms min=32.17ms med=90.41ms max=348.02ms p(90)=111.63ms p(95)=121.21ms p(99.9)=216.88ms
     iterations.....................: 64811   530.223495/s
     success_rate...................: 100.00% ✓ 64811      ✗ 0    
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

     checks.........................: 100.00% ✓ 179700     ✗ 0    
     data_received..................: 5.2 GB  43 MB/s
     data_sent......................: 72 MB   590 kB/s
     http_req_blocked...............: avg=4.51µs   min=1.05µs  med=2.73µs  max=4.13ms   p(90)=4.17µs   p(95)=4.71µs   p(99.9)=50.35µs 
     http_req_connecting............: avg=1.55µs   min=0s      med=0s      max=4.09ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=99.81ms  min=20.11ms med=97.85ms max=325.74ms p(90)=126.54ms p(95)=135.87ms p(99.9)=175.69ms
       { expected_response:true }...: avg=99.81ms  min=20.11ms med=97.85ms max=325.74ms p(90)=126.54ms p(95)=135.87ms p(99.9)=175.69ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 60000
     http_req_receiving.............: avg=78.27µs  min=27.4µs  med=70.1µs  max=163.47ms p(90)=101.82µs p(95)=113.47µs p(99.9)=485.2µs 
     http_req_sending...............: avg=22.16µs  min=4.87µs  med=13.08µs max=104.59ms p(90)=18.57µs  p(95)=20.46µs  p(99.9)=534.13µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=99.71ms  min=19.99ms med=97.76ms max=325.34ms p(90)=126.43ms p(95)=135.75ms p(99.9)=175.3ms 
     http_reqs......................: 60000   490.924968/s
     iteration_duration.............: avg=100.18ms min=35.44ms med=98.12ms max=340.32ms p(90)=126.82ms p(95)=136.11ms p(99.9)=176.96ms
     iterations.....................: 59900   490.106759/s
     success_rate...................: 100.00% ✓ 59900      ✗ 0    
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

     checks.........................: 100.00% ✓ 147264     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   483 kB/s
     http_req_blocked...............: avg=5.02µs   min=982ns   med=2.92µs   max=3.51ms   p(90)=4.29µs   p(95)=4.8µs    p(99.9)=375.28µs
     http_req_connecting............: avg=1.95µs   min=0s      med=0s       max=3.47ms   p(90)=0s       p(95)=0s       p(99.9)=338.89µs
     http_req_duration..............: avg=121.81ms min=20.88ms med=119.92ms max=339.19ms p(90)=151.3ms  p(95)=161.13ms p(99.9)=206.35ms
       { expected_response:true }...: avg=121.81ms min=20.88ms med=119.92ms max=339.19ms p(90)=151.3ms  p(95)=161.13ms p(99.9)=206.35ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49188
     http_req_receiving.............: avg=79.82µs  min=28.06µs med=75.14µs  max=27.25ms  p(90)=105.88µs p(95)=117.69µs p(99.9)=500.69µs
     http_req_sending...............: avg=20.54µs  min=5.09µs  med=14.63µs  max=43.3ms   p(90)=19.7µs   p(95)=21.46µs  p(99.9)=482.96µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=121.71ms min=20.63ms med=119.83ms max=339ms    p(90)=151.2ms  p(95)=161.04ms p(99.9)=206.18ms
     http_reqs......................: 49188   402.087714/s
     iteration_duration.............: avg=122.26ms min=38.29ms med=120.2ms  max=349.43ms p(90)=151.57ms p(95)=161.41ms p(99.9)=208.71ms
     iterations.....................: 49088   401.270263/s
     success_rate...................: 100.00% ✓ 49088      ✗ 0    
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

     checks.........................: 100.00% ✓ 97929      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   321 kB/s
     http_req_blocked...............: avg=6.88µs   min=1.31µs  med=3.46µs   max=3.95ms   p(90)=4.91µs   p(95)=5.49µs   p(99.9)=1.61ms  
     http_req_connecting............: avg=3.13µs   min=0s      med=0s       max=3.91ms   p(90)=0s       p(95)=0s       p(99.9)=1.59ms  
     http_req_duration..............: avg=183.14ms min=22.41ms med=183.75ms max=413.88ms p(90)=196.25ms p(95)=201.22ms p(99.9)=274.97ms
       { expected_response:true }...: avg=183.14ms min=22.41ms med=183.75ms max=413.88ms p(90)=196.25ms p(95)=201.22ms p(99.9)=274.97ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32743
     http_req_receiving.............: avg=91.92µs  min=36.02µs med=85.62µs  max=88.41ms  p(90)=115.86µs p(95)=126.57µs p(99.9)=446.51µs
     http_req_sending...............: avg=29.47µs  min=6.08µs  med=16.73µs  max=174.55ms p(90)=21.3µs   p(95)=23.15µs  p(99.9)=414.41µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.02ms min=22.33ms med=183.65ms max=381.21ms p(90)=196.14ms p(95)=201.09ms p(99.9)=274.59ms
     http_reqs......................: 32743   267.107438/s
     iteration_duration.............: avg=183.91ms min=54.65ms med=184.14ms max=414.3ms  p(90)=196.52ms p(95)=201.52ms p(99.9)=276.26ms
     iterations.....................: 32643   266.291669/s
     success_rate...................: 100.00% ✓ 32643      ✗ 0    
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

     checks.........................: 100.00% ✓ 95472      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   314 kB/s
     http_req_blocked...............: avg=4.78µs   min=1.15µs  med=3.15µs   max=2.08ms   p(90)=4.54µs   p(95)=5.15µs   p(99.9)=616.47µs
     http_req_connecting............: avg=1.38µs   min=0s      med=0s       max=2.04ms   p(90)=0s       p(95)=0s       p(99.9)=588.36µs
     http_req_duration..............: avg=187.84ms min=17.52ms med=175.13ms max=781.71ms p(90)=218.28ms p(95)=240.94ms p(99.9)=718.49ms
       { expected_response:true }...: avg=187.84ms min=17.52ms med=175.13ms max=781.71ms p(90)=218.28ms p(95)=240.94ms p(99.9)=718.49ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31924
     http_req_receiving.............: avg=95.38µs  min=31.62µs med=87.58µs  max=111.58ms p(90)=117.93µs p(95)=129.99µs p(99.9)=960.39µs
     http_req_sending...............: avg=23.71µs  min=5.23µs  med=16.74µs  max=35.68ms  p(90)=21.15µs  p(95)=22.88µs  p(99.9)=504.84µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=187.72ms min=17.37ms med=175ms    max=781.56ms p(90)=218.16ms p(95)=240.83ms p(99.9)=718.39ms
     http_reqs......................: 31924   261.591599/s
     iteration_duration.............: avg=188.64ms min=62.07ms med=175.5ms  max=781.98ms p(90)=218.64ms p(95)=241.44ms p(99.9)=718.77ms
     iterations.....................: 31824   260.772179/s
     success_rate...................: 100.00% ✓ 31824      ✗ 0    
     vus............................: 21      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

