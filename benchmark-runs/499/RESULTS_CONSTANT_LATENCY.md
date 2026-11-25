## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.7 | 3,624 | 3,629 | 3,611 | 0.2% | 362 MB | 102.3 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.21 | 3,623 | 3,632 | 3,597 | 0.4% | 109 MB | 30.7 KB |  |
| fusion-aot-11 | 16.7.7 | 3,612 | 3,621 | 3,590 | 0.4% | 113 MB | 32.1 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.21 | 3,592 | 3,600 | 3,585 | 0.2% | 351 MB | 100.0 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.21 | 3,582 | 3,588 | 3,561 | 0.3% | 353 MB | 100.8 KB |  |
| fusion-fed-net-11 | 16.7.7 | 3,569 | 3,577 | 3,553 | 0.3% | 364 MB | 104.5 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 3,555 | 3,559 | 3,541 | 0.2% | 110 MB | 31.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.21 | 3,551 | 3,554 | 3,538 | 0.2% | 104 MB | 30.0 KB |  |
| feddi-gateway | 2026-11-22-1912 | 3,514 | 3,528 | 3,499 | 0.3% | 2,313 MB | 674.0 KB |  |
| hive-router | v0.3.17 | 3,386 | 3,398 | 3,368 | 0.3% | 92 MB | 27.7 KB |  |
| hive-router-nightly | v0.3.19-nightly.be76f6cb | 3,348 | 3,365 | 3,328 | 0.5% | 89 MB | 27.2 KB |  |
| grafbase | 0.53.5 | 1,456 | 1,468 | 1,451 | 0.4% | 101 MB | 71.1 KB |  |
| caliban | 3.2.1 | 1,405 | 1,408 | 1,399 | 0.2% | 5,694 MB | 4,150.0 KB |  |
| cosmo | 0.373.0 | 1,371 | 1,372 | 1,368 | 0.1% | 152 MB | 113.3 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 586 | 586 | 586 | 0.0% | 2,602 MB | 4,547.7 KB |  |
| apollo-router | v2.19.1 | 492 | 498 | 487 | 0.8% | 181 MB | 376.9 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.0e21b2b0 | 472 | 472 | 471 | 0.1% | 200 MB | 433.5 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 389 | 407 | 389 | 2.0% | 206 MB | 542.6 KB |  |
| hive-gateway | 2.15.10 | 291 | 292 | 289 | 0.4% | 3,216 MB | 11,315.8 KB |  |
| apollo-gateway | 2.14.4 | 270 | 270 | 269 | 0.2% | 2,166 MB | 8,214.8 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1314720     ✗ 0     
     data_received..................: 38 GB   317 MB/s
     data_sent......................: 527 MB  4.4 MB/s
     http_req_blocked...............: avg=2.4µs   min=802ns   med=1.81µs  max=4.05ms   p(90)=3µs     p(95)=3.74µs   p(99.9)=24.81µs
     http_req_connecting............: avg=224ns   min=0s      med=0s      max=3.99ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.49ms min=8.08ms  med=13.08ms max=266.48ms p(90)=16.57ms p(95)=17.8ms   p(99.9)=24.96ms
       { expected_response:true }...: avg=13.49ms min=8.08ms  med=13.08ms max=266.48ms p(90)=16.57ms p(95)=17.8ms   p(99.9)=24.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 438340
     http_req_receiving.............: avg=69.57µs min=24.42µs med=43.74µs max=189.72ms p(90)=91.21µs p(95)=172.27µs p(99.9)=1.78ms 
     http_req_sending...............: avg=30.63µs min=3.99µs  med=7.77µs  max=90.29ms  p(90)=16.09µs p(95)=92.83µs  p(99.9)=1.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.38ms min=8.02ms  med=12.98ms max=266.34ms p(90)=16.46ms p(95)=17.67ms  p(99.9)=24.63ms
     http_reqs......................: 438340  3624.026156/s
     iteration_duration.............: avg=13.68ms min=8.22ms  med=13.27ms max=289.4ms  p(90)=16.76ms p(95)=17.98ms  p(99.9)=25.21ms
     iterations.....................: 438240  3623.199394/s
     success_rate...................: 100.00% ✓ 438240      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1314522     ✗ 0     
     data_received..................: 38 GB   317 MB/s
     data_sent......................: 527 MB  4.4 MB/s
     http_req_blocked...............: avg=2.34µs  min=811ns   med=1.81µs  max=8.84ms   p(90)=2.97µs  p(95)=3.67µs   p(99.9)=24.26µs
     http_req_connecting............: avg=162ns   min=0s      med=0s      max=3.35ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.49ms min=8.16ms  med=13.08ms max=243.31ms p(90)=16.54ms p(95)=17.79ms  p(99.9)=24.97ms
       { expected_response:true }...: avg=13.49ms min=8.16ms  med=13.08ms max=243.31ms p(90)=16.54ms p(95)=17.79ms  p(99.9)=24.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 438274
     http_req_receiving.............: avg=68.43µs min=24.64µs med=43.61µs max=106.11ms p(90)=91.19µs p(95)=171.39µs p(99.9)=1.74ms 
     http_req_sending...............: avg=31.39µs min=4.18µs  med=7.77µs  max=136.89ms p(90)=15.9µs  p(95)=93.12µs  p(99.9)=1.79ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.39ms min=8.11ms  med=12.98ms max=243.07ms p(90)=16.43ms p(95)=17.67ms  p(99.9)=24.75ms
     http_reqs......................: 438274  3623.606427/s
     iteration_duration.............: avg=13.68ms min=8.33ms  med=13.27ms max=287.02ms p(90)=16.72ms p(95)=17.97ms  p(99.9)=25.2ms 
     iterations.....................: 438174  3622.779636/s
     success_rate...................: 100.00% ✓ 438174      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1310694     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 525 MB  4.3 MB/s
     http_req_blocked...............: avg=2.41µs  min=772ns   med=1.9µs   max=3.41ms   p(90)=3.02µs  p(95)=3.68µs   p(99.9)=24.44µs
     http_req_connecting............: avg=194ns   min=0s      med=0s      max=3.37ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.53ms min=8.16ms  med=13.12ms max=272.88ms p(90)=16.52ms p(95)=17.75ms  p(99.9)=25.06ms
       { expected_response:true }...: avg=13.53ms min=8.16ms  med=13.12ms max=272.88ms p(90)=16.52ms p(95)=17.75ms  p(99.9)=25.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 436998
     http_req_receiving.............: avg=69.4µs  min=24.63µs med=45µs    max=100.89ms p(90)=91.11µs p(95)=172.48µs p(99.9)=1.67ms 
     http_req_sending...............: avg=32.52µs min=4.17µs  med=8.07µs  max=197.61ms p(90)=15.8µs  p(95)=93.65µs  p(99.9)=1.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.43ms min=8.11ms  med=13.02ms max=272.33ms p(90)=16.41ms p(95)=17.63ms  p(99.9)=24.84ms
     http_reqs......................: 436998  3612.722569/s
     iteration_duration.............: avg=13.72ms min=8.29ms  med=13.31ms max=292.22ms p(90)=16.71ms p(95)=17.94ms  p(99.9)=25.29ms
     iterations.....................: 436898  3611.895855/s
     success_rate...................: 100.00% ✓ 436898      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1303044     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 522 MB  4.3 MB/s
     http_req_blocked...............: avg=3.16µs  min=862ns   med=2.2µs   max=9.14ms   p(90)=3.52µs  p(95)=4.24µs   p(99.9)=32.04µs
     http_req_connecting............: avg=580ns   min=0s      med=0s      max=9.09ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.6ms  min=8ms     med=13.16ms max=262.53ms p(90)=16.85ms p(95)=18.18ms  p(99.9)=26.36ms
       { expected_response:true }...: avg=13.6ms  min=8ms     med=13.16ms max=262.53ms p(90)=16.85ms p(95)=18.18ms  p(99.9)=26.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 434448
     http_req_receiving.............: avg=71.84µs min=23.47µs med=44.15µs max=135.5ms  p(90)=93.81µs p(95)=183.64µs p(99.9)=2.08ms 
     http_req_sending...............: avg=33.68µs min=4.29µs  med=8.27µs  max=169.2ms  p(90)=16.83µs p(95)=98.94µs  p(99.9)=2.1ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.5ms  min=7.94ms  med=13.06ms max=259.86ms p(90)=16.73ms p(95)=18.04ms  p(99.9)=26.06ms
     http_reqs......................: 434448  3592.16941/s
     iteration_duration.............: avg=13.8ms  min=8.2ms   med=13.35ms max=277.99ms p(90)=17.04ms p(95)=18.38ms  p(99.9)=26.58ms
     iterations.....................: 434348  3591.342575/s
     success_rate...................: 100.00% ✓ 434348      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1299456     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 521 MB  4.3 MB/s
     http_req_blocked...............: avg=2.88µs  min=842ns   med=2.29µs  max=3.92ms   p(90)=3.66µs  p(95)=4.44µs   p(99.9)=33.46µs
     http_req_connecting............: avg=226ns   min=0s      med=0s      max=3.86ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.64ms min=8.06ms  med=13.19ms max=284ms    p(90)=16.88ms p(95)=18.19ms  p(99.9)=26.17ms
       { expected_response:true }...: avg=13.64ms min=8.06ms  med=13.19ms max=284ms    p(90)=16.88ms p(95)=18.19ms  p(99.9)=26.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433252
     http_req_receiving.............: avg=73.63µs min=23.99µs med=45.28µs max=161.25ms p(90)=96.9µs  p(95)=187.65µs p(99.9)=2.13ms 
     http_req_sending...............: avg=33.86µs min=4.25µs  med=8.58µs  max=161.2ms  p(90)=17.49µs p(95)=100.66µs p(99.9)=1.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.53ms min=7.99ms  med=13.09ms max=283.57ms p(90)=16.76ms p(95)=18.05ms  p(99.9)=25.84ms
     http_reqs......................: 433252  3582.175177/s
     iteration_duration.............: avg=13.84ms min=8.29ms  med=13.39ms max=298.45ms p(90)=17.08ms p(95)=18.39ms  p(99.9)=26.43ms
     iterations.....................: 433152  3581.348366/s
     success_rate...................: 100.00% ✓ 433152      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1294845     ✗ 0     
     data_received..................: 38 GB   312 MB/s
     data_sent......................: 519 MB  4.3 MB/s
     http_req_blocked...............: avg=2.94µs  min=872ns   med=2.3µs   max=4.67ms   p(90)=3.75µs   p(95)=4.58µs   p(99.9)=32.78µs
     http_req_connecting............: avg=228ns   min=0s      med=0s      max=4.05ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.68ms min=8.06ms  med=13.24ms max=290.9ms  p(90)=16.9ms   p(95)=18.23ms  p(99.9)=26.41ms
       { expected_response:true }...: avg=13.68ms min=8.06ms  med=13.24ms max=290.9ms  p(90)=16.9ms   p(95)=18.23ms  p(99.9)=26.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 431715
     http_req_receiving.............: avg=75.67µs min=25.05µs med=47.18µs max=105.99ms p(90)=101.88µs p(95)=189.55µs p(99.9)=2.11ms 
     http_req_sending...............: avg=35.25µs min=4.39µs  med=8.55µs  max=213.14ms p(90)=18.71µs  p(95)=103.1µs  p(99.9)=2.05ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.57ms min=8.02ms  med=13.14ms max=274.2ms  p(90)=16.78ms  p(95)=18.09ms  p(99.9)=26.07ms
     http_reqs......................: 431715  3569.102352/s
     iteration_duration.............: avg=13.89ms min=8.23ms  med=13.44ms max=308.61ms p(90)=17.09ms  p(95)=18.43ms  p(99.9)=26.65ms
     iterations.....................: 431615  3568.275626/s
     success_rate...................: 100.00% ✓ 431615      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1289691     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.49µs  min=771ns   med=1.92µs  max=3.86ms   p(90)=3.18µs  p(95)=3.94µs   p(99.9)=23.8µs 
     http_req_connecting............: avg=227ns   min=0s      med=0s      max=3.81ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.75ms min=8.22ms  med=13.33ms max=273.06ms p(90)=16.89ms p(95)=18.14ms  p(99.9)=25.35ms
       { expected_response:true }...: avg=13.75ms min=8.22ms  med=13.33ms max=273.06ms p(90)=16.89ms p(95)=18.14ms  p(99.9)=25.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429997
     http_req_receiving.............: avg=69.15µs min=24.42µs med=43.26µs max=115.5ms  p(90)=92.57µs p(95)=174.69µs p(99.9)=1.72ms 
     http_req_sending...............: avg=31.74µs min=4.31µs  med=8.13µs  max=116.18ms p(90)=16.42µs p(95)=95.3µs   p(99.9)=1.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.65ms min=8.15ms  med=13.24ms max=272.71ms p(90)=16.77ms p(95)=18.02ms  p(99.9)=25.09ms
     http_reqs......................: 429997  3555.010399/s
     iteration_duration.............: avg=13.94ms min=8.41ms  med=13.53ms max=282.11ms p(90)=17.08ms p(95)=18.33ms  p(99.9)=25.6ms 
     iterations.....................: 429897  3554.183646/s
     success_rate...................: 100.00% ✓ 429897      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1288281     ✗ 0     
     data_received..................: 38 GB   311 MB/s
     data_sent......................: 516 MB  4.3 MB/s
     http_req_blocked...............: avg=2.85µs  min=911ns   med=2.25µs  max=4.22ms   p(90)=3.64µs  p(95)=4.44µs   p(99.9)=32.42µs
     http_req_connecting............: avg=227ns   min=0s      med=0s      max=4.18ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.76ms min=8.13ms  med=13.32ms max=279.77ms p(90)=16.98ms p(95)=18.3ms   p(99.9)=26.14ms
       { expected_response:true }...: avg=13.76ms min=8.13ms  med=13.32ms max=279.77ms p(90)=16.98ms p(95)=18.3ms   p(99.9)=26.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429527
     http_req_receiving.............: avg=74.42µs min=24.63µs med=46.57µs max=121.53ms p(90)=99.8µs  p(95)=187.42µs p(99.9)=1.88ms 
     http_req_sending...............: avg=33.69µs min=4.39µs  med=8.67µs  max=95.7ms   p(90)=17.88µs p(95)=101.01µs p(99.9)=1.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.65ms min=8.07ms  med=13.22ms max=279.43ms p(90)=16.85ms p(95)=18.17ms  p(99.9)=25.82ms
     http_reqs......................: 429527  3551.225098/s
     iteration_duration.............: avg=13.96ms min=8.31ms  med=13.52ms max=302.94ms p(90)=17.17ms p(95)=18.5ms   p(99.9)=26.38ms
     iterations.....................: 429427  3550.398322/s
     success_rate...................: 100.00% ✓ 429427      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-22-1912)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1274910     ✗ 0     
     data_received..................: 37 GB   307 MB/s
     data_sent......................: 511 MB  4.2 MB/s
     http_req_blocked...............: avg=3.08µs  min=852ns  med=2.43µs  max=5.59ms   p(90)=3.94µs  p(95)=4.79µs   p(99.9)=31.77µs
     http_req_connecting............: avg=231ns   min=0s     med=0s      max=4.17ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.9ms  min=8.16ms med=13.42ms max=286.58ms p(90)=17.22ms p(95)=18.61ms  p(99.9)=26.96ms
       { expected_response:true }...: avg=13.9ms  min=8.16ms med=13.42ms max=286.58ms p(90)=17.22ms p(95)=18.61ms  p(99.9)=26.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 425070
     http_req_receiving.............: avg=75.49µs min=23.5µs med=45.73µs max=158.83ms p(90)=99.94µs p(95)=192.42µs p(99.9)=2.13ms 
     http_req_sending...............: avg=35.52µs min=4.56µs med=9.17µs  max=178.79ms p(90)=18.87µs p(95)=103.88µs p(99.9)=2.1ms  
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.79ms min=8.09ms med=13.32ms max=286.42ms p(90)=17.09ms p(95)=18.46ms  p(99.9)=26.71ms
     http_reqs......................: 425070  3514.034609/s
     iteration_duration.............: avg=14.1ms  min=8.29ms med=13.63ms max=298.66ms p(90)=17.43ms p(95)=18.81ms  p(99.9)=27.18ms
     iterations.....................: 424970  3513.207914/s
     success_rate...................: 100.00% ✓ 424970      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1228617     ✗ 0     
     data_received..................: 36 GB   296 MB/s
     data_sent......................: 492 MB  4.1 MB/s
     http_req_blocked...............: avg=2.69µs  min=831ns   med=1.94µs  max=7.41ms   p(90)=3.35µs  p(95)=4.24µs   p(99.9)=24.66µs
     http_req_connecting............: avg=341ns   min=0s      med=0s      max=7.31ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.44ms min=8.6ms   med=14.08ms max=265.12ms p(90)=17.52ms p(95)=18.78ms  p(99.9)=26.58ms
       { expected_response:true }...: avg=14.44ms min=8.6ms   med=14.08ms max=265.12ms p(90)=17.52ms p(95)=18.78ms  p(99.9)=26.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 409639
     http_req_receiving.............: avg=70.22µs min=24.61µs med=45.03µs max=61.93ms  p(90)=98.13µs p(95)=175.67µs p(99.9)=1.62ms 
     http_req_sending...............: avg=30.92µs min=4.46µs  med=8.25µs  max=86.75ms  p(90)=18.07µs p(95)=95.42µs  p(99.9)=1.58ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.34ms min=8.49ms  med=13.99ms max=264.07ms p(90)=17.41ms p(95)=18.65ms  p(99.9)=26.31ms
     http_reqs......................: 409639  3386.3104/s
     iteration_duration.............: avg=14.64ms min=8.74ms  med=14.28ms max=276.41ms p(90)=17.71ms p(95)=18.97ms  p(99.9)=26.78ms
     iterations.....................: 409539  3385.483742/s
     success_rate...................: 100.00% ✓ 409539      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.be76f6cb)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1215033     ✗ 0     
     data_received..................: 35 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=3.11µs  min=942ns   med=2.46µs  max=4.04ms   p(90)=4.12µs   p(95)=5.03µs   p(99.9)=36.33µs
     http_req_connecting............: avg=217ns   min=0s      med=0s      max=3.54ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.59ms min=8.6ms   med=14.2ms  max=279.12ms p(90)=17.83ms  p(95)=19.15ms  p(99.9)=26.99ms
       { expected_response:true }...: avg=14.59ms min=8.6ms   med=14.2ms  max=279.12ms p(90)=17.83ms  p(95)=19.15ms  p(99.9)=26.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405111
     http_req_receiving.............: avg=76.3µs  min=23.63µs med=47.27µs max=98.71ms  p(90)=105.76µs p(95)=195.99µs p(99.9)=2.01ms 
     http_req_sending...............: avg=36.92µs min=4.62µs  med=9.42µs  max=198.5ms  p(90)=20.22µs  p(95)=105.85µs p(99.9)=2.03ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.48ms min=8.54ms  med=14.1ms  max=259.91ms p(90)=17.71ms  p(95)=19.01ms  p(99.9)=26.67ms
     http_reqs......................: 405111  3348.653893/s
     iteration_duration.............: avg=14.8ms  min=8.79ms  med=14.4ms  max=290.33ms p(90)=18.03ms  p(95)=19.35ms  p(99.9)=27.22ms
     iterations.....................: 405011  3347.827292/s
     success_rate...................: 100.00% ✓ 405011      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 532518      ✗ 0     
     data_received..................: 16 GB   128 MB/s
     data_sent......................: 213 MB  1.8 MB/s
     http_req_blocked...............: avg=4.29µs   min=802ns   med=2.13µs  max=8.9ms    p(90)=4.44µs   p(95)=5.35µs   p(99.9)=34.16µs
     http_req_connecting............: avg=1.55µs   min=0s      med=0s      max=8.85ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.54ms  min=17.23ms med=33.3ms  max=317.25ms p(90)=39.16ms  p(95)=40.8ms   p(99.9)=48.55ms
       { expected_response:true }...: avg=33.54ms  min=17.23ms med=33.3ms  max=317.25ms p(90)=39.16ms  p(95)=40.8ms   p(99.9)=48.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 177606
     http_req_receiving.............: avg=107.61µs min=23.87µs med=51.77µs max=258.16ms p(90)=114.17µs p(95)=153.62µs p(99.9)=1.65ms 
     http_req_sending...............: avg=26.55µs  min=4.02µs  med=8.82µs  max=87.35ms  p(90)=21.87µs  p(95)=32.47µs  p(99.9)=1.27ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.41ms  min=17.15ms med=33.19ms max=108.47ms p(90)=39.06ms  p(95)=40.7ms   p(99.9)=48.28ms
     http_reqs......................: 177606  1456.589929/s
     iteration_duration.............: avg=33.79ms  min=19.93ms med=33.53ms max=330.54ms p(90)=39.38ms  p(95)=41.02ms  p(99.9)=48.8ms 
     iterations.....................: 177506  1455.769805/s
     success_rate...................: 100.00% ✓ 177506      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 514059      ✗ 0     
     data_received..................: 15 GB   123 MB/s
     data_sent......................: 206 MB  1.7 MB/s
     http_req_blocked...............: avg=3.34µs  min=1.04µs  med=2.81µs  max=2.62ms   p(90)=4.41µs  p(95)=5.13µs   p(99.9)=30.83µs 
     http_req_connecting............: avg=239ns   min=0s      med=0s      max=2.59ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.78ms min=18.87ms med=34.26ms max=289.14ms p(90)=41.02ms p(95)=43.3ms   p(99.9)=56.6ms  
       { expected_response:true }...: avg=34.78ms min=18.87ms med=34.26ms max=289.14ms p(90)=41.02ms p(95)=43.3ms   p(99.9)=56.6ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 171453
     http_req_receiving.............: avg=73.92µs min=26.71µs med=59.72µs max=204.4ms  p(90)=96.36µs p(95)=113.24µs p(99.9)=883.32µs
     http_req_sending...............: avg=22.09µs min=4.91µs  med=11.78µs max=102.14ms p(90)=17.68µs p(95)=21.53µs  p(99.9)=759.79µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.68ms min=18.77ms med=34.17ms max=280.63ms p(90)=40.93ms p(95)=43.2ms   p(99.9)=56.44ms 
     http_reqs......................: 171453  1405.783209/s
     iteration_duration.............: avg=35ms    min=21.71ms med=34.47ms max=309.04ms p(90)=41.23ms p(95)=43.52ms  p(99.9)=57.1ms  
     iterations.....................: 171353  1404.963286/s
     success_rate...................: 100.00% ✓ 171353      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.373.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 501588      ✗ 0     
     data_received..................: 15 GB   120 MB/s
     data_sent......................: 201 MB  1.6 MB/s
     http_req_blocked...............: avg=3.44µs  min=1.07µs  med=2.57µs  max=3.48ms   p(90)=4.15µs   p(95)=4.86µs   p(99.9)=34.48µs 
     http_req_connecting............: avg=565ns   min=0s      med=0s      max=3.44ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.65ms min=18.15ms med=35.1ms  max=297.28ms p(90)=42.64ms  p(95)=45.07ms  p(99.9)=57.33ms 
       { expected_response:true }...: avg=35.65ms min=18.15ms med=35.1ms  max=297.28ms p(90)=42.64ms  p(95)=45.07ms  p(99.9)=57.33ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 167296
     http_req_receiving.............: avg=74.6µs  min=26.86µs med=62.14µs max=121.21ms p(90)=102.63µs p(95)=121.34µs p(99.9)=717.93µs
     http_req_sending...............: avg=22.65µs min=4.85µs  med=11.12µs max=144.01ms p(90)=17.57µs  p(95)=21.45µs  p(99.9)=748.54µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.56ms min=18.01ms med=35.01ms max=296.76ms p(90)=42.55ms  p(95)=44.98ms  p(99.9)=57.22ms 
     http_reqs......................: 167296  1371.731059/s
     iteration_duration.............: avg=35.87ms min=20.59ms med=35.31ms max=306.91ms p(90)=42.84ms  p(95)=45.27ms  p(99.9)=57.57ms 
     iterations.....................: 167196  1370.911116/s
     success_rate...................: 100.00% ✓ 167196      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 214536     ✗ 0    
     data_received..................: 6.3 GB  51 MB/s
     data_sent......................: 86 MB   704 kB/s
     http_req_blocked...............: avg=4.5µs   min=1.13µs  med=2.98µs  max=7.04ms   p(90)=4.44µs   p(95)=5.08µs   p(99.9)=45.03µs 
     http_req_connecting............: avg=1.08µs  min=0s      med=0s      max=5.23ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=83.58ms min=20.07ms med=81.51ms max=313.61ms p(90)=99.22ms  p(95)=107.25ms p(99.9)=207.66ms
       { expected_response:true }...: avg=83.58ms min=20.07ms med=81.51ms max=313.61ms p(90)=99.22ms  p(95)=107.25ms p(99.9)=207.66ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 71612
     http_req_receiving.............: avg=80.02µs min=29.86µs med=69.7µs  max=160.57ms p(90)=101.73µs p(95)=113.68µs p(99.9)=648.04µs
     http_req_sending...............: avg=19.55µs min=5.06µs  med=13.76µs max=65.24ms  p(90)=19.12µs  p(95)=21.25µs  p(99.9)=596.81µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=83.48ms min=19.93ms med=81.42ms max=307.03ms p(90)=99.12ms  p(95)=107.14ms p(99.9)=207.09ms
     http_reqs......................: 71612   586.046968/s
     iteration_duration.............: avg=83.91ms min=32.59ms med=81.75ms max=334.54ms p(90)=99.45ms  p(95)=107.53ms p(99.9)=209.75ms
     iterations.....................: 71512   585.228604/s
     success_rate...................: 100.00% ✓ 71512      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 180228     ✗ 0    
     data_received..................: 5.3 GB  43 MB/s
     data_sent......................: 72 MB   591 kB/s
     http_req_blocked...............: avg=6.74µs  min=1.03µs  med=2.68µs  max=8.9ms    p(90)=4.16µs   p(95)=4.71µs   p(99.9)=54.22µs 
     http_req_connecting............: avg=3.79µs  min=0s      med=0s      max=8.87ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=99.52ms min=20.33ms med=97.62ms max=318.63ms p(90)=126.17ms p(95)=135.23ms p(99.9)=177.09ms
       { expected_response:true }...: avg=99.52ms min=20.33ms med=97.62ms max=318.63ms p(90)=126.17ms p(95)=135.23ms p(99.9)=177.09ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 60176
     http_req_receiving.............: avg=76.96µs min=28.27µs med=70.87µs max=47.31ms  p(90)=102.47µs p(95)=114.47µs p(99.9)=514.93µs
     http_req_sending...............: avg=20.55µs min=4.74µs  med=13µs    max=137.78ms p(90)=18.64µs  p(95)=20.6µs   p(99.9)=522.68µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=99.42ms min=20.24ms med=97.52ms max=318.46ms p(90)=126.06ms p(95)=135.13ms p(99.9)=176.89ms
     http_reqs......................: 60176   492.376394/s
     iteration_duration.............: avg=99.89ms min=32.85ms med=97.89ms max=325.51ms p(90)=126.44ms p(95)=135.47ms p(99.9)=178.55ms
     iterations.....................: 60076   491.558167/s
     success_rate...................: 100.00% ✓ 60076      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.0e21b2b0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 173106     ✗ 0    
     data_received..................: 5.1 GB  41 MB/s
     data_sent......................: 69 MB   568 kB/s
     http_req_blocked...............: avg=6.69µs   min=1.24µs  med=3.18µs   max=9.22ms   p(90)=4.61µs   p(95)=5.21µs   p(99.9)=58.12µs 
     http_req_connecting............: avg=2.94µs   min=0s      med=0s       max=6.93ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=103.6ms  min=20.22ms med=102.01ms max=310.46ms p(90)=129.78ms p(95)=139.04ms p(99.9)=182.18ms
       { expected_response:true }...: avg=103.6ms  min=20.22ms med=102.01ms max=310.46ms p(90)=129.78ms p(95)=139.04ms p(99.9)=182.18ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 57802
     http_req_receiving.............: avg=83.18µs  min=31.35µs med=73.01µs  max=111.79ms p(90)=105.75µs p(95)=117.47µs p(99.9)=510.32µs
     http_req_sending...............: avg=30.09µs  min=5.57µs  med=14.89µs  max=140.13ms p(90)=20.36µs  p(95)=22.38µs  p(99.9)=647.38µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=103.49ms min=20.1ms  med=101.91ms max=286.87ms p(90)=129.65ms p(95)=138.92ms p(99.9)=180.94ms
     http_reqs......................: 57802   472.834355/s
     iteration_duration.............: avg=104ms    min=33.23ms med=102.29ms max=326.14ms p(90)=130.04ms p(95)=139.32ms p(99.9)=184.2ms 
     iterations.....................: 57702   472.01633/s
     success_rate...................: 100.00% ✓ 57702      ✗ 0    
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

     checks.........................: 100.00% ✓ 142482     ✗ 0    
     data_received..................: 4.2 GB  34 MB/s
     data_sent......................: 57 MB   467 kB/s
     http_req_blocked...............: avg=7.99µs   min=1.08µs  med=2.82µs   max=8.33ms   p(90)=4.2µs    p(95)=4.75µs   p(99.9)=517.26µs
     http_req_connecting............: avg=4.88µs   min=0s      med=0s       max=8.29ms   p(90)=0s       p(95)=0s       p(99.9)=431.34µs
     http_req_duration..............: avg=125.87ms min=20.86ms med=124.02ms max=354.03ms p(90)=156.15ms p(95)=166.82ms p(99.9)=218.37ms
       { expected_response:true }...: avg=125.87ms min=20.86ms med=124.02ms max=354.03ms p(90)=156.15ms p(95)=166.82ms p(99.9)=218.37ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47594
     http_req_receiving.............: avg=82.6µs   min=29.19µs med=73.56µs  max=85.03ms  p(90)=104.87µs p(95)=117.17µs p(99.9)=508.42µs
     http_req_sending...............: avg=22.35µs  min=5.17µs  med=14.55µs  max=73.58ms  p(90)=19.54µs  p(95)=21.3µs   p(99.9)=901.67µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=125.77ms min=20.74ms med=123.93ms max=352.7ms  p(90)=156.04ms p(95)=166.7ms  p(99.9)=217.78ms
     http_reqs......................: 47594   389.080244/s
     iteration_duration.............: avg=126.35ms min=30.06ms med=124.3ms  max=369.83ms p(90)=156.46ms p(95)=167.1ms  p(99.9)=223ms   
     iterations.....................: 47494   388.262745/s
     success_rate...................: 100.00% ✓ 47494      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 106623     ✗ 0    
     data_received..................: 3.1 GB  26 MB/s
     data_sent......................: 43 MB   350 kB/s
     http_req_blocked...............: avg=5.33µs   min=1.28µs  med=3.65µs   max=2.9ms    p(90)=5.2µs    p(95)=5.84µs   p(99.9)=441.71µs
     http_req_connecting............: avg=1.42µs   min=0s      med=0s       max=2.86ms   p(90)=0s       p(95)=0s       p(99.9)=418.83µs
     http_req_duration..............: avg=168.26ms min=17.37ms med=158.79ms max=768.57ms p(90)=212.54ms p(95)=232.21ms p(99.9)=716.46ms
       { expected_response:true }...: avg=168.26ms min=17.37ms med=158.79ms max=768.57ms p(90)=212.54ms p(95)=232.21ms p(99.9)=716.46ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 35641
     http_req_receiving.............: avg=92.49µs  min=35.8µs  med=85.98µs  max=49.08ms  p(90)=115.89µs p(95)=127.53µs p(99.9)=576.63µs
     http_req_sending...............: avg=21.25µs  min=6.08µs  med=17.62µs  max=19.68ms  p(90)=22.36µs  p(95)=24.23µs  p(99.9)=425.13µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=168.14ms min=17.22ms med=158.69ms max=768.44ms p(90)=212.43ms p(95)=232.11ms p(99.9)=716.35ms
     http_reqs......................: 35641   291.819218/s
     iteration_duration.............: avg=168.96ms min=51.56ms med=159.21ms max=768.84ms p(90)=212.86ms p(95)=232.78ms p(99.9)=716.72ms
     iterations.....................: 35541   291.000444/s
     success_rate...................: 100.00% ✓ 35541      ✗ 0    
     vus............................: 20      min=0        max=50 
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

     checks.........................: 100.00% ✓ 99153      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   325 kB/s
     http_req_blocked...............: avg=6.38µs   min=1.42µs  med=3.6µs    max=4.47ms   p(90)=5.11µs   p(95)=5.73µs   p(99.9)=895.82µs
     http_req_connecting............: avg=2.42µs   min=0s      med=0s       max=4.2ms    p(90)=0s       p(95)=0s       p(99.9)=865.02µs
     http_req_duration..............: avg=180.87ms min=22.58ms med=180.95ms max=342.8ms  p(90)=192.28ms p(95)=196.91ms p(99.9)=262.29ms
       { expected_response:true }...: avg=180.87ms min=22.58ms med=180.95ms max=342.8ms  p(90)=192.28ms p(95)=196.91ms p(99.9)=262.29ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33151
     http_req_receiving.............: avg=92.06µs  min=35.38µs med=86.61µs  max=27.84ms  p(90)=116.88µs p(95)=128.46µs p(99.9)=686.06µs
     http_req_sending...............: avg=27.78µs  min=6.25µs  med=17.82µs  max=54.03ms  p(90)=22.49µs  p(95)=24.42µs  p(99.9)=697.12µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.75ms min=22.41ms med=180.84ms max=342.06ms p(90)=192.15ms p(95)=196.78ms p(99.9)=262.08ms
     http_reqs......................: 33151   270.407856/s
     iteration_duration.............: avg=181.63ms min=82.01ms med=181.3ms  max=358.58ms p(90)=192.55ms p(95)=197.2ms  p(99.9)=263.34ms
     iterations.....................: 33051   269.592171/s
     success_rate...................: 100.00% ✓ 33051      ✗ 0    
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

