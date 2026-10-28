## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.2 | 3,417 | 3,430 | 3,407 | 0.3% | 388 MB | 116.3 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.7 | 3,414 | 3,423 | 3,396 | 0.3% | 389 MB | 116.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 3,401 | 3,408 | 3,389 | 0.2% | 130 MB | 39.2 KB |  |
| fusion-aot-11 | 16.7.2 | 3,370 | 3,372 | 3,354 | 0.2% | 123 MB | 37.4 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,276 | 3,292 | 3,231 | 0.9% | 2,306 MB | 720.7 KB |  |
| fusion-fed-net-11 | 16.7.2 | 2,791 | 2,799 | 2,786 | 0.2% | 405 MB | 148.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 2,785 | 2,791 | 2,779 | 0.2% | 385 MB | 141.5 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 2,744 | 2,747 | 2,731 | 0.2% | 136 MB | 50.6 KB |  |
| fusion-fed-aot-11 | 16.7.2 | 2,743 | 2,753 | 2,719 | 0.5% | 136 MB | 50.8 KB |  |
| hive-router | v0.3.6 | 2,037 | 2,052 | 2,024 | 0.5% | 90 MB | 45.3 KB |  |
| grafbase | 0.53.5 | 1,450 | 1,460 | 1,442 | 0.6% | 100 MB | 70.3 KB |  |
| cosmo | 0.363.0 | 1,436 | 1,438 | 1,435 | 0.1% | 149 MB | 106.1 KB |  |
| caliban | 3.2.0 | 1,347 | 1,364 | 1,346 | 0.6% | 5,000 MB | 3,800.7 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 528 | 529 | 527 | 0.1% | 2,739 MB | 5,311.9 KB |  |
| apollo-router | v2.19.0 | 508 | 516 | 508 | 0.7% | 182 MB | 367.9 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 418 | 418 | 418 | 0.0% | 203 MB | 497.7 KB |  |
| apollo-gateway | 2.14.4 | 266 | 267 | 265 | 0.3% | 2,138 MB | 8,229.3 KB |  |
| hive-gateway | 2.15.3 | 265 | 266 | 263 | 0.4% | 3,651 MB | 14,108.7 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1239828     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 497 MB  4.1 MB/s
     http_req_blocked...............: avg=2.39µs  min=751ns  med=1.78µs  max=3.75ms   p(90)=3.04µs  p(95)=3.84µs   p(99.9)=23.88µs
     http_req_connecting............: avg=223ns   min=0s     med=0s      max=3.72ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.31ms min=8.1ms  med=13.9ms  max=283.65ms p(90)=17.73ms p(95)=19.05ms  p(99.9)=26.86ms
       { expected_response:true }...: avg=14.31ms min=8.1ms  med=13.9ms  max=283.65ms p(90)=17.73ms p(95)=19.05ms  p(99.9)=26.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 413376
     http_req_receiving.............: avg=68.22µs min=23.3µs med=41.91µs max=153.16ms p(90)=91.72µs p(95)=165.37µs p(99.9)=1.99ms 
     http_req_sending...............: avg=31.14µs min=4.07µs med=7.55µs  max=260.15ms p(90)=16.22µs p(95)=90.08µs  p(99.9)=2.04ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.21ms min=8.03ms med=13.8ms  max=283.2ms  p(90)=17.63ms p(95)=18.94ms  p(99.9)=26.57ms
     http_reqs......................: 413376  3417.648726/s
     iteration_duration.............: avg=14.5ms  min=8.27ms med=14.09ms max=297.6ms  p(90)=17.92ms p(95)=19.24ms  p(99.9)=27.08ms
     iterations.....................: 413276  3416.821961/s
     success_rate...................: 100.00% ✓ 413276      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1238517     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 496 MB  4.1 MB/s
     http_req_blocked...............: avg=2.42µs  min=802ns   med=1.86µs  max=3.5ms    p(90)=2.99µs  p(95)=3.7µs   p(99.9)=24.28µs
     http_req_connecting............: avg=208ns   min=0s      med=0s      max=3.47ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.32ms min=8.27ms  med=13.9ms  max=276.11ms p(90)=17.82ms p(95)=19.18ms p(99.9)=26.87ms
       { expected_response:true }...: avg=14.32ms min=8.27ms  med=13.9ms  max=276.11ms p(90)=17.82ms p(95)=19.18ms p(99.9)=26.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 412939
     http_req_receiving.............: avg=69.09µs min=24.09µs med=43.01µs max=105.38ms p(90)=90.58µs p(95)=173.4µs p(99.9)=2ms    
     http_req_sending...............: avg=31.24µs min=4.27µs  med=7.88µs  max=157.59ms p(90)=16.38µs p(95)=90.73µs p(99.9)=1.87ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.22ms min=8.22ms  med=13.8ms  max=253.94ms p(90)=17.72ms p(95)=19.06ms p(99.9)=26.65ms
     http_reqs......................: 412939  3414.081669/s
     iteration_duration.............: avg=14.52ms min=8.41ms  med=14.09ms max=291.41ms p(90)=18.01ms p(95)=19.36ms p(99.9)=27.11ms
     iterations.....................: 412839  3413.254893/s
     success_rate...................: 100.00% ✓ 412839      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1233993     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 494 MB  4.1 MB/s
     http_req_blocked...............: avg=2.36µs  min=812ns   med=1.86µs  max=2.54ms   p(90)=3.17µs  p(95)=3.97µs   p(99.9)=24.09µs
     http_req_connecting............: avg=137ns   min=0s      med=0s      max=2.51ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.38ms min=8ms     med=13.96ms max=273.09ms p(90)=17.72ms p(95)=19.07ms  p(99.9)=26.64ms
       { expected_response:true }...: avg=14.38ms min=8ms     med=13.96ms max=273.09ms p(90)=17.72ms p(95)=19.07ms  p(99.9)=26.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 411431
     http_req_receiving.............: avg=67.46µs min=22.58µs med=42.64µs max=63.75ms  p(90)=91.75µs p(95)=167.77µs p(99.9)=1.75ms 
     http_req_sending...............: avg=31.07µs min=4.2µs   med=7.84µs  max=172.35ms p(90)=16.85µs p(95)=91.55µs  p(99.9)=1.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.28ms min=7.95ms  med=13.87ms max=272.29ms p(90)=17.62ms p(95)=18.96ms  p(99.9)=26.4ms 
     http_reqs......................: 411431  3401.274631/s
     iteration_duration.............: avg=14.57ms min=8.19ms  med=14.15ms max=282.37ms p(90)=17.91ms p(95)=19.26ms  p(99.9)=26.87ms
     iterations.....................: 411331  3400.447937/s
     success_rate...................: 100.00% ✓ 411331      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1222743     ✗ 0     
     data_received..................: 36 GB   295 MB/s
     data_sent......................: 490 MB  4.1 MB/s
     http_req_blocked...............: avg=2.35µs  min=811ns   med=1.81µs  max=3.59ms   p(90)=2.89µs  p(95)=3.51µs  p(99.9)=23.04µs
     http_req_connecting............: avg=223ns   min=0s      med=0s      max=3.56ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.51ms min=8.4ms   med=14.08ms max=273.45ms p(90)=17.97ms p(95)=19.36ms p(99.9)=27.52ms
       { expected_response:true }...: avg=14.51ms min=8.4ms   med=14.08ms max=273.45ms p(90)=17.97ms p(95)=19.36ms p(99.9)=27.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 407681
     http_req_receiving.............: avg=67.9µs  min=24.83µs med=43.65µs max=170.66ms p(90)=89.5µs  p(95)=167.1µs p(99.9)=1.71ms 
     http_req_sending...............: avg=30.01µs min=4.12µs  med=7.86µs  max=183.58ms p(90)=15.35µs p(95)=91.21µs p(99.9)=1.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.41ms min=8.31ms  med=13.98ms max=268.5ms  p(90)=17.87ms p(95)=19.24ms p(99.9)=27.29ms
     http_reqs......................: 407681  3370.447822/s
     iteration_duration.............: avg=14.71ms min=8.53ms  med=14.27ms max=285.79ms p(90)=18.16ms p(95)=19.55ms p(99.9)=27.75ms
     iterations.....................: 407581  3369.621085/s
     success_rate...................: 100.00% ✓ 407581      ✗ 0     
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

     checks.........................: 100.00% ✓ 1188807     ✗ 0     
     data_received..................: 35 GB   286 MB/s
     data_sent......................: 476 MB  3.9 MB/s
     http_req_blocked...............: avg=3.06µs  min=952ns   med=2.43µs  max=9.88ms   p(90)=3.99µs  p(95)=4.82µs   p(99.9)=34.93µs
     http_req_connecting............: avg=212ns   min=0s      med=0s      max=4.52ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.92ms min=8.56ms  med=14.56ms max=271.17ms p(90)=18.04ms p(95)=19.34ms  p(99.9)=27.47ms
       { expected_response:true }...: avg=14.92ms min=8.56ms  med=14.56ms max=271.17ms p(90)=18.04ms p(95)=19.34ms  p(99.9)=27.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 396369
     http_req_receiving.............: avg=73.91µs min=23.21µs med=46.89µs max=167.77ms p(90)=97.82µs p(95)=190.19µs p(99.9)=1.75ms 
     http_req_sending...............: avg=34.24µs min=4.37µs  med=9.21µs  max=100.06ms p(90)=18.95µs p(95)=106.48µs p(99.9)=1.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.82ms min=8.5ms   med=14.46ms max=269.66ms p(90)=17.92ms p(95)=19.21ms  p(99.9)=27.2ms 
     http_reqs......................: 396369  3276.56264/s
     iteration_duration.............: avg=15.13ms min=8.76ms  med=14.76ms max=301.7ms  p(90)=18.24ms p(95)=19.54ms  p(99.9)=27.68ms
     iterations.....................: 396269  3275.735996/s
     success_rate...................: 100.00% ✓ 396269      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1016499     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 407 MB  3.4 MB/s
     http_req_blocked...............: avg=2.5µs   min=812ns   med=1.87µs  max=11.95ms  p(90)=3.37µs  p(95)=4.23µs   p(99.9)=24.95µs
     http_req_connecting............: avg=206ns   min=0s      med=0s      max=2.96ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.49ms min=11.74ms med=17.06ms max=288.61ms p(90)=20.53ms p(95)=21.75ms  p(99.9)=28.77ms
       { expected_response:true }...: avg=17.49ms min=11.74ms med=17.06ms max=288.61ms p(90)=20.53ms p(95)=21.75ms  p(99.9)=28.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 338933
     http_req_receiving.............: avg=67.93µs min=24.15µs med=44.62µs max=200.32ms p(90)=93.3µs  p(95)=144.24µs p(99.9)=1.5ms  
     http_req_sending...............: avg=28.37µs min=4.16µs  med=7.88µs  max=119.72ms p(90)=17.1µs  p(95)=81.94µs  p(99.9)=1.57ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.39ms min=11.69ms med=16.97ms max=288.27ms p(90)=20.42ms p(95)=21.65ms  p(99.9)=28.46ms
     http_reqs......................: 338933  2791.943839/s
     iteration_duration.............: avg=17.69ms min=11.91ms med=17.26ms max=300.18ms p(90)=20.72ms p(95)=21.95ms  p(99.9)=29ms   
     iterations.....................: 338833  2791.120094/s
     success_rate...................: 100.00% ✓ 338833      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1014195     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 406 MB  3.3 MB/s
     http_req_blocked...............: avg=2.42µs  min=781ns   med=1.8µs   max=3.45ms   p(90)=3.09µs  p(95)=3.86µs   p(99.9)=26.12µs
     http_req_connecting............: avg=255ns   min=0s      med=0s      max=3.42ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.53ms min=11.57ms med=17.1ms  max=272.27ms p(90)=20.62ms p(95)=21.84ms  p(99.9)=28.3ms 
       { expected_response:true }...: avg=17.53ms min=11.57ms med=17.1ms  max=272.27ms p(90)=20.62ms p(95)=21.84ms  p(99.9)=28.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 338165
     http_req_receiving.............: avg=65.79µs min=24.22µs med=44.02µs max=233.53ms p(90)=90.67µs p(95)=141.77µs p(99.9)=1.35ms 
     http_req_sending...............: avg=27.76µs min=4.16µs  med=7.69µs  max=220.62ms p(90)=16.43µs p(95)=77.93µs  p(99.9)=1.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.44ms min=11.53ms med=17.02ms max=258.95ms p(90)=20.52ms p(95)=21.73ms  p(99.9)=28.03ms
     http_reqs......................: 338165  2785.743854/s
     iteration_duration.............: avg=17.74ms min=11.76ms med=17.3ms  max=293.84ms p(90)=20.81ms p(95)=22.03ms  p(99.9)=28.53ms
     iterations.....................: 338065  2784.920071/s
     success_rate...................: 100.00% ✓ 338065      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 999504     ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 401 MB  3.3 MB/s
     http_req_blocked...............: avg=3.4µs   min=882ns   med=2.23µs  max=8.43ms   p(90)=3.74µs  p(95)=4.54µs   p(99.9)=33.24µs
     http_req_connecting............: avg=738ns   min=0s      med=0s      max=8.38ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.79ms min=11.88ms med=17.35ms max=286.32ms p(90)=20.85ms p(95)=22.11ms  p(99.9)=29.25ms
       { expected_response:true }...: avg=17.79ms min=11.88ms med=17.35ms max=286.32ms p(90)=20.85ms p(95)=22.11ms  p(99.9)=29.25ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 333268
     http_req_receiving.............: avg=70.46µs min=25.13µs med=47.04µs max=80.35ms  p(90)=96.82µs p(95)=158.35µs p(99.9)=1.44ms 
     http_req_sending...............: avg=30.07µs min=4.25µs  med=8.48µs  max=138.13ms p(90)=17.73µs p(95)=89.98µs  p(99.9)=1.5ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.68ms min=11.78ms med=17.26ms max=265.33ms p(90)=20.74ms p(95)=22ms     p(99.9)=28.98ms
     http_reqs......................: 333268  2744.85984/s
     iteration_duration.............: avg=17.99ms min=12.07ms med=17.55ms max=296.08ms p(90)=21.05ms p(95)=22.31ms  p(99.9)=29.49ms
     iterations.....................: 333168  2744.03622/s
     success_rate...................: 100.00% ✓ 333168     ✗ 0     
     vus............................: 50      min=0        max=50  
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 998967      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=3.45µs  min=891ns   med=2.33µs  max=9.35ms   p(90)=3.85µs  p(95)=4.66µs   p(99.9)=33.61µs
     http_req_connecting............: avg=670ns   min=0s      med=0s      max=9.27ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.8ms  min=11.65ms med=17.37ms max=289.96ms p(90)=20.86ms p(95)=22.14ms  p(99.9)=29.29ms
       { expected_response:true }...: avg=17.8ms  min=11.65ms med=17.37ms max=289.96ms p(90)=20.86ms p(95)=22.14ms  p(99.9)=29.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 333089
     http_req_receiving.............: avg=69.55µs min=23.78µs med=45.88µs max=149.86ms p(90)=95.03µs p(95)=158.82µs p(99.9)=1.47ms 
     http_req_sending...............: avg=30.83µs min=4.4µs   med=8.8µs   max=154.79ms p(90)=17.85µs p(95)=90.9µs   p(99.9)=1.5ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.7ms  min=11.6ms  med=17.28ms max=289.11ms p(90)=20.75ms p(95)=22.02ms  p(99.9)=29.02ms
     http_reqs......................: 333089  2743.282453/s
     iteration_duration.............: avg=18ms    min=11.85ms med=17.57ms max=305.07ms p(90)=21.07ms p(95)=22.34ms  p(99.9)=29.49ms
     iterations.....................: 332989  2742.458864/s
     success_rate...................: 100.00% ✓ 332989      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 744534      ✗ 0     
     data_received..................: 22 GB   178 MB/s
     data_sent......................: 298 MB  2.4 MB/s
     http_req_blocked...............: avg=3.34µs  min=932ns   med=2.58µs  max=4.52ms   p(90)=4.08µs  p(95)=4.78µs   p(99.9)=37.72µs 
     http_req_connecting............: avg=442ns   min=0s      med=0s      max=4.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.95ms min=17.06ms med=23.62ms max=307.06ms p(90)=26.9ms  p(95)=27.97ms  p(99.9)=33.36ms 
       { expected_response:true }...: avg=23.95ms min=17.06ms med=23.62ms max=307.06ms p(90)=26.9ms  p(95)=27.97ms  p(99.9)=33.36ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 248278
     http_req_receiving.............: avg=68.02µs min=24.61µs med=52.59µs max=163.82ms p(90)=91.87µs p(95)=113.62µs p(99.9)=890.33µs
     http_req_sending...............: avg=26.64µs min=4.59µs  med=10.33µs max=163.92ms p(90)=17.56µs p(95)=23.78µs  p(99.9)=939.69µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.85ms min=17.01ms med=23.53ms max=306.78ms p(90)=26.8ms  p(95)=27.88ms  p(99.9)=33.21ms 
     http_reqs......................: 248278  2037.101385/s
     iteration_duration.............: avg=24.16ms min=17.24ms med=23.82ms max=319.19ms p(90)=27.1ms  p(95)=28.18ms  p(99.9)=33.6ms  
     iterations.....................: 248178  2036.280892/s
     success_rate...................: 100.00% ✓ 248178      ✗ 0     
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

     checks.........................: 100.00% ✓ 530232      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=3.76µs  min=1.04µs  med=2.99µs  max=3.07ms   p(90)=5.24µs   p(95)=6.22µs   p(99.9)=48.12µs
     http_req_connecting............: avg=253ns   min=0s      med=0s      max=2.3ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.67ms min=17.71ms med=33.32ms max=305.71ms p(90)=39.28ms  p(95)=41.07ms  p(99.9)=50.01ms
       { expected_response:true }...: avg=33.67ms min=17.71ms med=33.32ms max=305.71ms p(90)=39.28ms  p(95)=41.07ms  p(99.9)=50.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 176844
     http_req_receiving.............: avg=88µs    min=26.8µs  med=62.53µs max=162.78ms p(90)=124.92µs p(95)=170.25µs p(99.9)=1.43ms 
     http_req_sending...............: avg=32.62µs min=4.73µs  med=11.57µs max=154.47ms p(90)=23.96µs  p(95)=50.19µs  p(99.9)=1.46ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.55ms min=17.57ms med=33.2ms  max=300.4ms  p(90)=39.17ms  p(95)=40.95ms  p(99.9)=49.78ms
     http_reqs......................: 176844  1450.324537/s
     iteration_duration.............: avg=33.93ms min=20.03ms med=33.57ms max=313.61ms p(90)=39.51ms  p(95)=41.3ms   p(99.9)=50.27ms
     iterations.....................: 176744  1449.504422/s
     success_rate...................: 100.00% ✓ 176744      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.363.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 525174      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=3.04µs  min=952ns   med=2.16µs  max=4.13ms   p(90)=3.73µs  p(95)=4.44µs   p(99.9)=29.19µs 
     http_req_connecting............: avg=540ns   min=0s      med=0s      max=4.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.05ms min=18.79ms med=33.48ms max=308.72ms p(90)=40.59ms p(95)=42.89ms  p(99.9)=55.1ms  
       { expected_response:true }...: avg=34.05ms min=18.79ms med=33.48ms max=308.72ms p(90)=40.59ms p(95)=42.89ms  p(99.9)=55.1ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 175158
     http_req_receiving.............: avg=69.33µs min=25.08µs med=57.53µs max=64.26ms  p(90)=96.55µs p(95)=113.92µs p(99.9)=707.54µs
     http_req_sending...............: avg=22.44µs min=4.4µs   med=9.92µs  max=157.53ms p(90)=17.11µs p(95)=21.11µs  p(99.9)=749.6µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.96ms min=18.72ms med=33.39ms max=308.47ms p(90)=40.5ms  p(95)=42.79ms  p(99.9)=54.99ms 
     http_reqs......................: 175158  1436.219849/s
     iteration_duration.............: avg=34.26ms min=20.53ms med=33.68ms max=316.17ms p(90)=40.78ms p(95)=43.07ms  p(99.9)=55.33ms 
     iterations.....................: 175058  1435.399892/s
     success_rate...................: 100.00% ✓ 175058      ✗ 0     
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

     checks.........................: 100.00% ✓ 492825      ✗ 0     
     data_received..................: 14 GB   118 MB/s
     data_sent......................: 198 MB  1.6 MB/s
     http_req_blocked...............: avg=3.01µs  min=912ns   med=2.16µs  max=3.51ms   p(90)=3.71µs  p(95)=4.4µs    p(99.9)=29.81µs 
     http_req_connecting............: avg=526ns   min=0s      med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=36.3ms  min=17.96ms med=35.75ms max=318.13ms p(90)=43.14ms p(95)=45.56ms  p(99.9)=60.47ms 
       { expected_response:true }...: avg=36.3ms  min=17.96ms med=35.75ms max=318.13ms p(90)=43.14ms p(95)=45.56ms  p(99.9)=60.47ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 164375
     http_req_receiving.............: avg=66.72µs min=24.94µs med=54.47µs max=234.89ms p(90)=88.39µs p(95)=103.19µs p(99.9)=745.01µs
     http_req_sending...............: avg=18.04µs min=4.39µs  med=10.31µs max=53.78ms  p(90)=16.49µs p(95)=19.92µs  p(99.9)=686.88µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=36.22ms min=17.85ms med=35.67ms max=317.9ms  p(90)=43.05ms p(95)=45.47ms  p(99.9)=60.3ms  
     http_reqs......................: 164375  1347.554568/s
     iteration_duration.............: avg=36.51ms min=21.37ms med=35.95ms max=330.29ms p(90)=43.34ms p(95)=45.76ms  p(99.9)=60.75ms 
     iterations.....................: 164275  1346.734763/s
     success_rate...................: 100.00% ✓ 164275      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 193548     ✗ 0    
     data_received..................: 5.7 GB  46 MB/s
     data_sent......................: 78 MB   635 kB/s
     http_req_blocked...............: avg=6.15µs  min=1.17µs  med=3.15µs  max=7.66ms   p(90)=4.62µs   p(95)=5.27µs   p(99.9)=48.97µs 
     http_req_connecting............: avg=2.68µs  min=0s      med=0s      max=7.43ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.63ms min=20.51ms med=91.15ms max=339.58ms p(90)=109.23ms p(95)=118.42ms p(99.9)=210.84ms
       { expected_response:true }...: avg=92.63ms min=20.51ms med=91.15ms max=339.58ms p(90)=109.23ms p(95)=118.42ms p(99.9)=210.84ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64616
     http_req_receiving.............: avg=89.4µs  min=30.39µs med=75.88µs max=159.9ms  p(90)=109.55µs p(95)=121.87µs p(99.9)=635.22µs
     http_req_sending...............: avg=22.07µs min=5.16µs  med=15.35µs max=45.69ms  p(90)=21.4µs   p(95)=23.54µs  p(99.9)=666.5µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.52ms min=20.39ms med=91.05ms max=325.93ms p(90)=109.13ms p(95)=118.29ms p(99.9)=210.24ms
     http_reqs......................: 64616   528.635019/s
     iteration_duration.............: avg=93.01ms min=34.64ms med=91.41ms max=358.81ms p(90)=109.49ms p(95)=118.75ms p(99.9)=211.96ms
     iterations.....................: 64516   527.816902/s
     success_rate...................: 100.00% ✓ 64516      ✗ 0    
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

     checks.........................: 100.00% ✓ 186069     ✗ 0    
     data_received..................: 5.4 GB  45 MB/s
     data_sent......................: 75 MB   611 kB/s
     http_req_blocked...............: avg=4.4µs   min=1.06µs  med=2.62µs  max=3.8ms    p(90)=4.07µs   p(95)=4.66µs   p(99.9)=44.51µs 
     http_req_connecting............: avg=1.49µs  min=0s      med=0s      max=3.76ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=96.39ms min=19.81ms med=94.54ms max=323.88ms p(90)=121.92ms p(95)=130.44ms p(99.9)=167.87ms
       { expected_response:true }...: avg=96.39ms min=19.81ms med=94.54ms max=323.88ms p(90)=121.92ms p(95)=130.44ms p(99.9)=167.87ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 62123
     http_req_receiving.............: avg=81.01µs min=29.4µs  med=71.21µs max=144.75ms p(90)=103.41µs p(95)=115.11µs p(99.9)=542.27µs
     http_req_sending...............: avg=24.82µs min=4.88µs  med=13.58µs max=156.93ms p(90)=19.39µs  p(95)=21.35µs  p(99.9)=450.32µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.28ms min=19.7ms  med=94.43ms max=315.48ms p(90)=121.82ms p(95)=130.34ms p(99.9)=167.23ms
     http_reqs......................: 62123   508.374451/s
     iteration_duration.............: avg=96.75ms min=35.21ms med=94.79ms max=331.75ms p(90)=122.17ms p(95)=130.69ms p(99.9)=168.89ms
     iterations.....................: 62023   507.556115/s
     success_rate...................: 100.00% ✓ 62023      ✗ 0    
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

     checks.........................: 100.00% ✓ 153441     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 62 MB   503 kB/s
     http_req_blocked...............: avg=4.98µs   min=1.07µs  med=3.01µs   max=3.43ms   p(90)=4.46µs   p(95)=5.02µs   p(99.9)=117.22µs
     http_req_connecting............: avg=1.73µs   min=0s      med=0s       max=3.41ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=116.89ms min=20.24ms med=115.2ms  max=340.11ms p(90)=144.16ms p(95)=154.11ms p(99.9)=196ms   
       { expected_response:true }...: avg=116.89ms min=20.24ms med=115.2ms  max=340.11ms p(90)=144.16ms p(95)=154.11ms p(99.9)=196ms   
     http_req_failed................: 0.00%   ✓ 0          ✗ 51247
     http_req_receiving.............: avg=83.77µs  min=28.29µs med=75.27µs  max=130.44ms p(90)=106.71µs p(95)=119.03µs p(99.9)=492.14µs
     http_req_sending...............: avg=26.4µs   min=5.2µs   med=14.66µs  max=157.99ms p(90)=19.9µs   p(95)=21.78µs  p(99.9)=552.37µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.78ms min=20.1ms  med=115.11ms max=339.6ms  p(90)=144.06ms p(95)=153.99ms p(99.9)=194.9ms 
     http_reqs......................: 51247   418.930187/s
     iteration_duration.............: avg=117.34ms min=30.55ms med=115.48ms max=369.05ms p(90)=144.45ms p(95)=154.4ms  p(99.9)=200.11ms
     iterations.....................: 51147   418.112715/s
     success_rate...................: 100.00% ✓ 51147      ✗ 0    
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

     checks.........................: 100.00% ✓ 97614      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   320 kB/s
     http_req_blocked...............: avg=5.61µs   min=1.2µs   med=3.4µs    max=3ms      p(90)=4.83µs   p(95)=5.48µs   p(99.9)=859.76µs
     http_req_connecting............: avg=1.87µs   min=0s      med=0s       max=2.97ms   p(90)=0s       p(95)=0s       p(99.9)=820.04µs
     http_req_duration..............: avg=183.71ms min=23.08ms med=185.7ms  max=351.49ms p(90)=212.23ms p(95)=218.08ms p(99.9)=288.35ms
       { expected_response:true }...: avg=183.71ms min=23.08ms med=185.7ms  max=351.49ms p(90)=212.23ms p(95)=218.08ms p(99.9)=288.35ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32638
     http_req_receiving.............: avg=94.99µs  min=37.08µs med=86.71µs  max=61.65ms  p(90)=116.66µs p(95)=128.68µs p(99.9)=644.65µs
     http_req_sending...............: avg=28.09µs  min=5.55µs  med=17.02µs  max=94.71ms  p(90)=21.62µs  p(95)=23.45µs  p(99.9)=463.32µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.58ms min=22.96ms med=185.59ms max=350.81ms p(90)=212.12ms p(95)=217.96ms p(99.9)=288ms   
     http_reqs......................: 32638   266.261395/s
     iteration_duration.............: avg=184.49ms min=42.82ms med=185.99ms max=369.48ms p(90)=212.53ms p(95)=218.38ms p(99.9)=290.53ms
     iterations.....................: 32538   265.445593/s
     success_rate...................: 100.00% ✓ 32538      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 96870      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=11.02µs  min=1.53µs  med=3.62µs   max=9.45ms   p(90)=5.1µs    p(95)=5.75µs   p(99.9)=3.54ms  
     http_req_connecting............: avg=6.88µs   min=0s      med=0s       max=9.28ms   p(90)=0s       p(95)=0s       p(99.9)=3.39ms  
     http_req_duration..............: avg=185.11ms min=17.35ms med=170.03ms max=820.35ms p(90)=219.89ms p(95)=242.32ms p(99.9)=717.31ms
       { expected_response:true }...: avg=185.11ms min=17.35ms med=170.03ms max=820.35ms p(90)=219.89ms p(95)=242.32ms p(99.9)=717.31ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32390
     http_req_receiving.............: avg=93.69µs  min=38.3µs  med=88.98µs  max=9.07ms   p(90)=119.46µs p(95)=131.43µs p(99.9)=815.7µs 
     http_req_sending...............: avg=24.65µs  min=6.71µs  med=18.27µs  max=47.15ms  p(90)=23.09µs  p(95)=25.07µs  p(99.9)=700.97µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.99ms min=17.21ms med=169.91ms max=820.26ms p(90)=219.77ms p(95)=242.21ms p(99.9)=717.18ms
     http_reqs......................: 32390   265.122344/s
     iteration_duration.............: avg=185.91ms min=59.61ms med=170.39ms max=820.6ms  p(90)=220.25ms p(95)=242.86ms p(99.9)=717.67ms
     iterations.....................: 32290   264.303812/s
     success_rate...................: 100.00% ✓ 32290      ✗ 0    
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

