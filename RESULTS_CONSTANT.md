## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 5,115 | 5,117 | 5,103 | 0.1% | 372 MB | 74.5 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.7 | 5,032 | 5,048 | 5,002 | 0.3% | 382 MB | 77.7 KB |  |
| fusion-aot-11 | 16.7.3 | 4,865 | 4,874 | 4,857 | 0.1% | 128 MB | 27.0 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,807 | 4,810 | 4,783 | 0.2% | 403 MB | 85.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.7 | 4,770 | 4,792 | 4,751 | 0.4% | 371 MB | 79.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.7 | 4,652 | 4,658 | 4,642 | 0.1% | 126 MB | 27.8 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.7 | 4,650 | 4,660 | 4,624 | 0.3% | 129 MB | 28.5 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,560 | 4,571 | 4,520 | 0.4% | 130 MB | 29.3 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,267 | 4,387 | 4,261 | 1.3% | 2,314 MB | 555.4 KB |  |
| hive-router | v0.3.6 | 2,872 | 2,894 | 2,862 | 0.4% | 90 MB | 32.1 KB |  |
| grafbase | 0.53.5 | 1,839 | 1,840 | 1,836 | 0.1% | 109 MB | 60.7 KB |  |
| caliban | 3.2.0 | 1,532 | 1,534 | 1,525 | 0.2% | 5,405 MB | 3,612.8 KB |  |
| cosmo | 0.363.0 | 1,495 | 1,498 | 1,494 | 0.1% | 163 MB | 111.3 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 543 | 545 | 543 | 0.2% | 2,756 MB | 5,197.1 KB |  |
| apollo-router | v2.19.0 | 531 | 532 | 524 | 0.6% | 173 MB | 333.6 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 432 | 432 | 431 | 0.1% | 205 MB | 486.4 KB |  |
| hive-gateway | 2.15.3 | 272 | 273 | 271 | 0.3% | 3,623 MB | 13,638.9 KB |  |
| apollo-gateway | 2.14.4 | 269 | 270 | 269 | 0.2% | 2,193 MB | 8,348.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1842975     ✗ 0     
     data_received..................: 54 GB   448 MB/s
     data_sent......................: 739 MB  6.1 MB/s
     http_req_blocked...............: avg=2.8µs   min=821ns    med=2.23µs  max=12.88ms  p(90)=3.49µs  p(95)=4.13µs   p(99.9)=31.39µs
     http_req_connecting............: avg=139ns   min=0s       med=0s      max=3.37ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.55ms  min=819.69µs med=8.63ms  max=285.93ms p(90)=15ms    p(95)=17.99ms  p(99.9)=30.68ms
       { expected_response:true }...: avg=9.55ms  min=819.69µs med=8.63ms  max=285.93ms p(90)=15ms    p(95)=17.99ms  p(99.9)=30.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 614425
     http_req_receiving.............: avg=95.1µs  min=23.95µs  med=45.99µs max=122.07ms p(90)=90.63µs p(95)=196.15µs p(99.9)=6.18ms 
     http_req_sending...............: avg=43.41µs min=4.3µs    med=8.42µs  max=131.83ms p(90)=15.1µs  p(95)=103.62µs p(99.9)=4.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.41ms  min=733.57µs med=8.52ms  max=285.38ms p(90)=14.77ms p(95)=17.71ms  p(99.9)=30.19ms
     http_reqs......................: 614425  5115.368545/s
     iteration_duration.............: avg=9.75ms  min=1ms      med=8.82ms  max=296.74ms p(90)=15.21ms p(95)=18.21ms  p(99.9)=30.96ms
     iterations.....................: 614325  5114.536/s
     success_rate...................: 100.00% ✓ 614325      ✗ 0     
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

     checks.........................: 100.00% ✓ 1813194     ✗ 0     
     data_received..................: 53 GB   440 MB/s
     data_sent......................: 727 MB  6.0 MB/s
     http_req_blocked...............: avg=2.93µs  min=852ns    med=2.29µs max=5.35ms   p(90)=3.54µs  p(95)=4.18µs   p(99.9)=31.71µs
     http_req_connecting............: avg=147ns   min=0s       med=0s     max=3.69ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.71ms  min=790.59µs med=8.8ms  max=275.55ms p(90)=15.15ms p(95)=18.21ms  p(99.9)=31.06ms
       { expected_response:true }...: avg=9.71ms  min=790.59µs med=8.8ms  max=275.55ms p(90)=15.15ms p(95)=18.21ms  p(99.9)=31.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 604498
     http_req_receiving.............: avg=96µs    min=24.6µs   med=46.4µs max=148.54ms p(90)=92.15µs p(95)=200.81µs p(99.9)=6.3ms  
     http_req_sending...............: avg=44.45µs min=4.1µs    med=8.39µs max=148.23ms p(90)=15.3µs  p(95)=106.46µs p(99.9)=5ms    
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.57ms  min=731.59µs med=8.69ms max=275.14ms p(90)=14.92ms p(95)=17.93ms  p(99.9)=30.46ms
     http_reqs......................: 604498  5032.901981/s
     iteration_duration.............: avg=9.91ms  min=1.23ms   med=9ms    max=284.27ms p(90)=15.37ms p(95)=18.43ms  p(99.9)=31.37ms
     iterations.....................: 604398  5032.069406/s
     success_rate...................: 100.00% ✓ 604398      ✗ 0     
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

     checks.........................: 100.00% ✓ 1752936     ✗ 0     
     data_received..................: 51 GB   426 MB/s
     data_sent......................: 702 MB  5.8 MB/s
     http_req_blocked...............: avg=2.71µs  min=821ns    med=1.88µs  max=8.96ms   p(90)=2.98µs  p(95)=3.55µs  p(99.9)=27.53µs
     http_req_connecting............: avg=406ns   min=0s       med=0s      max=8.92ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=10.06ms min=941.9µs  med=9.39ms  max=208.91ms p(90)=14.96ms p(95)=17.44ms p(99.9)=28.78ms
       { expected_response:true }...: avg=10.06ms min=941.9µs  med=9.39ms  max=208.91ms p(90)=14.96ms p(95)=17.44ms p(99.9)=28.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 584412
     http_req_receiving.............: avg=87.34µs min=24.7µs   med=45.11µs max=39.61ms  p(90)=88.66µs p(95)=194.8µs p(99.9)=5.24ms 
     http_req_sending...............: avg=38.79µs min=4.48µs   med=8.02µs  max=180.95ms p(90)=14.05µs p(95)=99.84µs p(99.9)=3.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=9.93ms  min=879.93µs med=9.28ms  max=200.57ms p(90)=14.78ms p(95)=17.21ms p(99.9)=28.46ms
     http_reqs......................: 584412  4865.17015/s
     iteration_duration.............: avg=10.25ms min=1.31ms   med=9.57ms  max=364.05ms p(90)=15.16ms p(95)=17.66ms p(99.9)=29.06ms
     iterations.....................: 584312  4864.337661/s
     success_rate...................: 100.00% ✓ 584312      ✗ 0     
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

     checks.........................: 100.00% ✓ 1732377     ✗ 0     
     data_received..................: 51 GB   421 MB/s
     data_sent......................: 694 MB  5.8 MB/s
     http_req_blocked...............: avg=2.56µs  min=751ns    med=1.96µs max=6.64ms   p(90)=3.19µs  p(95)=3.88µs   p(99.9)=26.74µs
     http_req_connecting............: avg=148ns   min=0s       med=0s     max=3.42ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.18ms min=1.04ms   med=9.43ms max=273.99ms p(90)=15.37ms p(95)=17.99ms  p(99.9)=30.25ms
       { expected_response:true }...: avg=10.18ms min=1.04ms   med=9.43ms max=273.99ms p(90)=15.37ms p(95)=17.99ms  p(99.9)=30.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 577559
     http_req_receiving.............: avg=97.16µs min=24.31µs  med=47.1µs max=19.61ms  p(90)=95.24µs p(95)=195.34µs p(99.9)=6.66ms 
     http_req_sending...............: avg=42.42µs min=4.41µs   med=8.22µs max=140.82ms p(90)=15.64µs p(95)=100.28µs p(99.9)=4.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.04ms min=965.43µs med=9.32ms max=273.43ms p(90)=15.16ms p(95)=17.74ms  p(99.9)=29.78ms
     http_reqs......................: 577559  4807.617358/s
     iteration_duration.............: avg=10.38ms min=1.47ms   med=9.63ms max=283.78ms p(90)=15.57ms p(95)=18.21ms  p(99.9)=30.58ms
     iterations.....................: 577459  4806.784955/s
     success_rate...................: 100.00% ✓ 577459      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1718931     ✗ 0     
     data_received..................: 50 GB   417 MB/s
     data_sent......................: 689 MB  5.7 MB/s
     http_req_blocked...............: avg=3.11µs   min=822ns    med=2.42µs  max=7.19ms   p(90)=3.84µs   p(95)=4.68µs   p(99.9)=33.95µs
     http_req_connecting............: avg=170ns    min=0s       med=0s      max=4.04ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.24ms  min=1ms      med=9.37ms  max=267.35ms p(90)=15.81ms  p(95)=18.77ms  p(99.9)=31.92ms
       { expected_response:true }...: avg=10.24ms  min=1ms      med=9.37ms  max=267.35ms p(90)=15.81ms  p(95)=18.77ms  p(99.9)=31.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 573077
     http_req_receiving.............: avg=103.43µs min=24.38µs  med=49.37µs max=155.61ms p(90)=100.94µs p(95)=208µs    p(99.9)=6.82ms 
     http_req_sending...............: avg=46.43µs  min=4.32µs   med=8.79µs  max=183.27ms p(90)=17.01µs  p(95)=108.38µs p(99.9)=5.15ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.09ms  min=930.41µs med=9.25ms  max=267.25ms p(90)=15.58ms  p(95)=18.49ms  p(99.9)=31.33ms
     http_reqs......................: 573077  4770.5545/s
     iteration_duration.............: avg=10.45ms  min=1.4ms    med=9.57ms  max=289.48ms p(90)=16.02ms  p(95)=19ms     p(99.9)=32.23ms
     iterations.....................: 572977  4769.722054/s
     success_rate...................: 100.00% ✓ 572977      ✗ 0     
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

     checks.........................: 100.00% ✓ 1676280     ✗ 0     
     data_received..................: 49 GB   407 MB/s
     data_sent......................: 672 MB  5.6 MB/s
     http_req_blocked...............: avg=3.26µs  min=871ns    med=2.29µs  max=25.6ms   p(90)=3.58µs  p(95)=4.23µs   p(99.9)=31.98µs
     http_req_connecting............: avg=533ns   min=0s       med=0s      max=16.37ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.53ms min=928.07µs med=9.84ms  max=287.49ms p(90)=15.67ms p(95)=18.3ms   p(99.9)=29.93ms
       { expected_response:true }...: avg=10.53ms min=928.07µs med=9.84ms  max=287.49ms p(90)=15.67ms p(95)=18.3ms   p(99.9)=29.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 558860
     http_req_receiving.............: avg=96.69µs min=24.09µs  med=48.21µs max=42.21ms  p(90)=95.92µs p(95)=217.6µs  p(99.9)=5.64ms 
     http_req_sending...............: avg=40.92µs min=4.39µs   med=8.54µs  max=176.18ms p(90)=15.06µs p(95)=107.15µs p(99.9)=3.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.39ms min=855.3µs  med=9.73ms  max=284.54ms p(90)=15.46ms p(95)=18.05ms  p(99.9)=29.58ms
     http_reqs......................: 558860  4652.497037/s
     iteration_duration.............: avg=10.72ms min=1.42ms   med=10.03ms max=323.73ms p(90)=15.87ms p(95)=18.52ms  p(99.9)=30.21ms
     iterations.....................: 558760  4651.664539/s
     success_rate...................: 100.00% ✓ 558760      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1675710     ✗ 0     
     data_received..................: 49 GB   407 MB/s
     data_sent......................: 671 MB  5.6 MB/s
     http_req_blocked...............: avg=2.61µs  min=811ns    med=1.93µs  max=6.46ms   p(90)=3.17µs  p(95)=3.87µs   p(99.9)=28.29µs
     http_req_connecting............: avg=194ns   min=0s       med=0s      max=4.38ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.53ms min=1.04ms   med=9.88ms  max=273.91ms p(90)=15.48ms p(95)=18.02ms  p(99.9)=30.03ms
       { expected_response:true }...: avg=10.53ms min=1.04ms   med=9.88ms  max=273.91ms p(90)=15.48ms p(95)=18.02ms  p(99.9)=30.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 558670
     http_req_receiving.............: avg=94.92µs min=25.11µs  med=46.03µs max=172.72ms p(90)=94.4µs  p(95)=201.76µs p(99.9)=5.99ms 
     http_req_sending...............: avg=41.1µs  min=4.45µs   med=8.24µs  max=166.94ms p(90)=15.85µs p(95)=103.31µs p(99.9)=4.06ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.39ms min=989.39µs med=9.77ms  max=266.14ms p(90)=15.28ms p(95)=17.78ms  p(99.9)=29.58ms
     http_reqs......................: 558670  4650.57515/s
     iteration_duration.............: avg=10.73ms min=1.53ms   med=10.07ms max=290.58ms p(90)=15.68ms p(95)=18.24ms  p(99.9)=30.32ms
     iterations.....................: 558570  4649.742713/s
     success_rate...................: 100.00% ✓ 558570      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1643493     ✗ 0     
     data_received..................: 48 GB   399 MB/s
     data_sent......................: 659 MB  5.5 MB/s
     http_req_blocked...............: avg=4.74µs  min=801ns    med=1.95µs  max=115.15ms p(90)=3.18µs  p(95)=3.87µs   p(99.9)=27.36µs
     http_req_connecting............: avg=2.37µs  min=0s       med=0s      max=115.02ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.74ms min=1.06ms   med=10.13ms max=269.05ms p(90)=15.67ms p(95)=18.06ms  p(99.9)=29.72ms
       { expected_response:true }...: avg=10.74ms min=1.06ms   med=10.13ms max=269.05ms p(90)=15.67ms p(95)=18.06ms  p(99.9)=29.72ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 547931
     http_req_receiving.............: avg=95.58µs min=24.3µs   med=46.35µs max=106.04ms p(90)=95.15µs p(95)=204.91µs p(99.9)=6.26ms 
     http_req_sending...............: avg=44.78µs min=4.37µs   med=8.14µs  max=120.11ms p(90)=15.64µs p(95)=103.45µs p(99.9)=4.23ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.6ms  min=991.34µs med=10.02ms max=149.03ms p(90)=15.48ms p(95)=17.82ms  p(99.9)=29.23ms
     http_reqs......................: 547931  4560.688/s
     iteration_duration.............: avg=10.94ms min=1.77ms   med=10.32ms max=289.6ms  p(90)=15.88ms p(95)=18.27ms  p(99.9)=30ms   
     iterations.....................: 547831  4559.855653/s
     success_rate...................: 100.00% ✓ 547831      ✗ 0     
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

     checks.........................: 100.00% ✓ 1537275     ✗ 0     
     data_received..................: 45 GB   373 MB/s
     data_sent......................: 616 MB  5.1 MB/s
     http_req_blocked...............: avg=2.67µs  min=812ns    med=2.1µs   max=4.86ms   p(90)=3.35µs  p(95)=3.99µs   p(99.9)=29.62µs
     http_req_connecting............: avg=185ns   min=0s       med=0s      max=3.86ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.5ms  min=779.83µs med=11.29ms max=287.45ms p(90)=17.01ms p(95)=19.15ms  p(99.9)=29.76ms
       { expected_response:true }...: avg=11.5ms  min=779.83µs med=11.29ms max=287.45ms p(90)=17.01ms p(95)=19.15ms  p(99.9)=29.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 512525
     http_req_receiving.............: avg=84.92µs min=23.97µs  med=47.78µs max=186.09ms p(90)=93.91µs p(95)=207.15µs p(99.9)=4.01ms 
     http_req_sending...............: avg=40.95µs min=4.42µs   med=9.02µs  max=203.39ms p(90)=15.79µs p(95)=111.91µs p(99.9)=3.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.37ms min=709.64µs med=11.17ms max=267.71ms p(90)=16.85ms p(95)=18.96ms  p(99.9)=29.41ms
     http_reqs......................: 512525  4267.031599/s
     iteration_duration.............: avg=11.69ms min=1.31ms   med=11.47ms max=298.48ms p(90)=17.21ms p(95)=19.36ms  p(99.9)=30ms   
     iterations.....................: 512425  4266.199048/s
     success_rate...................: 100.00% ✓ 512425      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1035216     ✗ 0     
     data_received..................: 30 GB   251 MB/s
     data_sent......................: 415 MB  3.5 MB/s
     http_req_blocked...............: avg=3.32µs  min=1.02µs  med=2.73µs  max=3.69ms   p(90)=4.16µs  p(95)=4.85µs   p(99.9)=37.84µs
     http_req_connecting............: avg=283ns   min=0s      med=0s      max=3.66ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.17ms min=1.41ms  med=17.2ms  max=288.95ms p(90)=23.1ms  p(95)=24.68ms  p(99.9)=32.38ms
       { expected_response:true }...: avg=17.17ms min=1.41ms  med=17.2ms  max=288.95ms p(90)=23.1ms  p(95)=24.68ms  p(99.9)=32.38ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 345172
     http_req_receiving.............: avg=77.39µs min=25.38µs med=54.73µs max=121.27ms p(90)=96.06µs p(95)=178.16µs p(99.9)=1.32ms 
     http_req_sending...............: avg=35.84µs min=4.82µs  med=10.68µs max=145.61ms p(90)=17.72µs p(95)=111.95µs p(99.9)=1.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.06ms min=1.37ms  med=17.09ms max=270.87ms p(90)=22.99ms p(95)=24.56ms  p(99.9)=32.25ms
     http_reqs......................: 345172  2872.035661/s
     iteration_duration.............: avg=17.37ms min=3.59ms  med=17.4ms  max=302.45ms p(90)=23.3ms  p(95)=24.89ms  p(99.9)=32.65ms
     iterations.....................: 345072  2871.203601/s
     success_rate...................: 100.00% ✓ 345072      ✗ 0     
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

     checks.........................: 100.00% ✓ 663381      ✗ 0     
     data_received..................: 19 GB   161 MB/s
     data_sent......................: 266 MB  2.2 MB/s
     http_req_blocked...............: avg=3.69µs  min=851ns   med=2.78µs  max=4.83ms   p(90)=4.87µs   p(95)=5.9µs    p(99.9)=43.93µs
     http_req_connecting............: avg=430ns   min=0s      med=0s      max=4.1ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.88ms min=1.88ms  med=26.31ms max=325.17ms p(90)=34.93ms  p(95)=37.69ms  p(99.9)=51.67ms
       { expected_response:true }...: avg=26.88ms min=1.88ms  med=26.31ms max=325.17ms p(90)=34.93ms  p(95)=37.69ms  p(99.9)=51.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 221227
     http_req_receiving.............: avg=87.76µs min=27.61µs med=60.45µs max=33.23ms  p(90)=121.95µs p(95)=195.78µs p(99.9)=1.64ms 
     http_req_sending...............: avg=32.75µs min=4.49µs  med=10.77µs max=29.01ms  p(90)=22.36µs  p(95)=106.35µs p(99.9)=1.37ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.76ms min=1.79ms  med=26.2ms  max=295.58ms p(90)=34.8ms   p(95)=37.56ms  p(99.9)=51.49ms
     http_reqs......................: 221227  1839.526845/s
     iteration_duration.............: avg=27.12ms min=4.22ms  med=26.53ms max=338.07ms p(90)=35.16ms  p(95)=37.91ms  p(99.9)=51.98ms
     iterations.....................: 221127  1838.695334/s
     success_rate...................: 100.00% ✓ 221127      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 552507      ✗ 0     
     data_received..................: 16 GB   134 MB/s
     data_sent......................: 221 MB  1.8 MB/s
     http_req_blocked...............: avg=3.44µs  min=992ns   med=2.56µs  max=3.99ms   p(90)=4.39µs   p(95)=5.16µs   p(99.9)=37.16µs 
     http_req_connecting............: avg=530ns   min=0s      med=0s      max=3.95ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.33ms min=2.02ms  med=31.46ms max=320.27ms p(90)=45.65ms  p(95)=50.29ms  p(99.9)=75.51ms 
       { expected_response:true }...: avg=32.33ms min=2.02ms  med=31.46ms max=320.27ms p(90)=45.65ms  p(95)=50.29ms  p(99.9)=75.51ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 184269
     http_req_receiving.............: avg=75.94µs min=27.03µs med=62.77µs max=226.24ms p(90)=101.55µs p(95)=118.78µs p(99.9)=894.62µs
     http_req_sending...............: avg=23.29µs min=4.83µs  med=11.84µs max=158.42ms p(90)=19.4µs   p(95)=23.24µs  p(99.9)=778.84µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.23ms min=1.97ms  med=31.37ms max=315.59ms p(90)=45.55ms  p(95)=50.19ms  p(99.9)=75.22ms 
     http_reqs......................: 184269  1532.085788/s
     iteration_duration.............: avg=32.57ms min=5.84ms  med=31.68ms max=331.72ms p(90)=45.87ms  p(95)=50.51ms  p(99.9)=75.93ms 
     iterations.....................: 184169  1531.254348/s
     success_rate...................: 100.00% ✓ 184169      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 539196      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 216 MB  1.8 MB/s
     http_req_blocked...............: avg=3.12µs  min=1.05µs  med=2.56µs  max=2.75ms   p(90)=4.08µs  p(95)=4.79µs   p(99.9)=35.92µs 
     http_req_connecting............: avg=239ns   min=0s      med=0s      max=2.44ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.15ms min=2.07ms  med=32.27ms max=288.07ms p(90)=47.8ms  p(95)=52.65ms  p(99.9)=76.64ms 
       { expected_response:true }...: avg=33.15ms min=2.07ms  med=32.27ms max=288.07ms p(90)=47.8ms  p(95)=52.65ms  p(99.9)=76.64ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 179832
     http_req_receiving.............: avg=74.48µs min=24.72µs med=61.35µs max=221.37ms p(90)=98.28µs p(95)=114.61µs p(99.9)=730.06µs
     http_req_sending...............: avg=23.18µs min=4.77µs  med=11.31µs max=118.09ms p(90)=17.68µs p(95)=21.74µs  p(99.9)=790.96µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.05ms min=2.01ms  med=32.17ms max=269.45ms p(90)=47.7ms  p(95)=52.55ms  p(99.9)=76.37ms 
     http_reqs......................: 179832  1495.164024/s
     iteration_duration.............: avg=33.37ms min=4.02ms  med=32.47ms max=309.23ms p(90)=48ms    p(95)=52.85ms  p(99.9)=77.1ms  
     iterations.....................: 179732  1494.332601/s
     success_rate...................: 100.00% ✓ 179732      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 196329     ✗ 0    
     data_received..................: 5.7 GB  48 MB/s
     data_sent......................: 79 MB   653 kB/s
     http_req_blocked...............: avg=7µs     min=992ns   med=2.66µs  max=8.85ms   p(90)=4.11µs   p(95)=4.69µs   p(99.9)=47.71µs 
     http_req_connecting............: avg=3.97µs  min=0s      med=0s      max=8.78ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.32ms min=3.88ms  med=88.64ms max=329.45ms p(90)=109.56ms p(95)=119.37ms p(99.9)=216.98ms
       { expected_response:true }...: avg=91.32ms min=3.88ms  med=88.64ms max=329.45ms p(90)=109.56ms p(95)=119.37ms p(99.9)=216.98ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65543
     http_req_receiving.............: avg=76.22µs min=26.56µs med=68.65µs max=48.87ms  p(90)=103.33µs p(95)=116.07µs p(99.9)=518.75µs
     http_req_sending...............: avg=18.94µs min=4.74µs  med=13.78µs max=55.97ms  p(90)=19.41µs  p(95)=21.28µs  p(99.9)=672.68µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.22ms min=3.81ms  med=88.54ms max=328.47ms p(90)=109.46ms p(95)=119.24ms p(99.9)=216.81ms
     http_reqs......................: 65543   543.901202/s
     iteration_duration.............: avg=91.69ms min=28.53ms med=88.87ms max=358.01ms p(90)=109.81ms p(95)=119.65ms p(99.9)=217.57ms
     iterations.....................: 65443   543.071363/s
     success_rate...................: 100.00% ✓ 65443      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 192021     ✗ 0    
     data_received..................: 5.6 GB  47 MB/s
     data_sent......................: 77 MB   639 kB/s
     http_req_blocked...............: avg=5.1µs   min=1.13µs  med=3.32µs  max=4.01ms   p(90)=4.76µs   p(95)=5.38µs   p(99.9)=55.99µs 
     http_req_connecting............: avg=1.53µs  min=0s      med=0s      max=3.97ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.35ms min=4.39ms  med=91.26ms max=295.85ms p(90)=126.12ms p(95)=136.09ms p(99.9)=178.38ms
       { expected_response:true }...: avg=93.35ms min=4.39ms  med=91.26ms max=295.85ms p(90)=126.12ms p(95)=136.09ms p(99.9)=178.38ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64107
     http_req_receiving.............: avg=81.04µs min=30.21µs med=75.42µs max=84.55ms  p(90)=106.66µs p(95)=119.17µs p(99.9)=508.48µs
     http_req_sending...............: avg=26.21µs min=5.27µs  med=16.24µs max=131.65ms p(90)=21.55µs  p(95)=23.5µs   p(99.9)=560.6µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.24ms min=4.27ms  med=91.16ms max=295.26ms p(90)=126.01ms p(95)=135.99ms p(99.9)=178.26ms
     http_reqs......................: 64107   531.717169/s
     iteration_duration.............: avg=93.74ms min=21.13ms med=91.55ms max=313.93ms p(90)=126.38ms p(95)=136.37ms p(99.9)=180.2ms 
     iterations.....................: 64007   530.887747/s
     success_rate...................: 100.00% ✓ 64007      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 156324     ✗ 0    
     data_received..................: 4.6 GB  38 MB/s
     data_sent......................: 63 MB   520 kB/s
     http_req_blocked...............: avg=4.88µs   min=1.04µs  med=2.96µs   max=3.93ms   p(90)=4.29µs   p(95)=4.81µs   p(99.9)=102.23µs
     http_req_connecting............: avg=1.76µs   min=0s      med=0s       max=3.89ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=114.72ms min=5.34ms  med=112.34ms max=340.41ms p(90)=150.1ms  p(95)=161.88ms p(99.9)=207.76ms
       { expected_response:true }...: avg=114.72ms min=5.34ms  med=112.34ms max=340.41ms p(90)=150.1ms  p(95)=161.88ms p(99.9)=207.76ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 52208
     http_req_receiving.............: avg=76.52µs  min=27.18µs med=73.45µs  max=10.07ms  p(90)=103.46µs p(95)=115.64µs p(99.9)=447.09µs
     http_req_sending...............: avg=18.57µs  min=4.98µs  med=14.84µs  max=35.02ms  p(90)=19.62µs  p(95)=21.34µs  p(99.9)=513.06µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=114.62ms min=5.24ms  med=112.26ms max=330.65ms p(90)=150.02ms p(95)=161.8ms  p(99.9)=207.68ms
     http_reqs......................: 52208   432.640645/s
     iteration_duration.............: avg=115.17ms min=30.05ms med=112.63ms max=349.52ms p(90)=150.37ms p(95)=162.17ms p(99.9)=208.8ms 
     iterations.....................: 52108   431.811958/s
     success_rate...................: 100.00% ✓ 52108      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 98361      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   327 kB/s
     http_req_blocked...............: avg=8.64µs   min=1.18µs  med=3.51µs   max=6.67ms   p(90)=4.98µs   p(95)=5.68µs   p(99.9)=1.62ms  
     http_req_connecting............: avg=4.74µs   min=0s      med=0s       max=6.65ms   p(90)=0s       p(95)=0s       p(99.9)=1.51ms  
     http_req_duration..............: avg=182.28ms min=5.84ms  med=166.68ms max=768.09ms p(90)=216.26ms p(95)=244.5ms  p(99.9)=699.56ms
       { expected_response:true }...: avg=182.28ms min=5.84ms  med=166.68ms max=768.09ms p(90)=216.26ms p(95)=244.5ms  p(99.9)=699.56ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32887
     http_req_receiving.............: avg=93.58µs  min=39.41µs med=89.66µs  max=9.95ms   p(90)=118.8µs  p(95)=130.26µs p(99.9)=737.19µs
     http_req_sending...............: avg=23.4µs   min=6.55µs  med=17.83µs  max=21.51ms  p(90)=22.26µs  p(95)=24.08µs  p(99.9)=1.46ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.17ms min=5.76ms  med=166.57ms max=768ms    p(90)=216.12ms p(95)=244.42ms p(99.9)=699.06ms
     http_reqs......................: 32887   272.193617/s
     iteration_duration.............: avg=183.08ms min=24.02ms med=167.06ms max=768.29ms p(90)=216.57ms p(95)=245.06ms p(99.9)=700ms   
     iterations.....................: 32787   271.365954/s
     success_rate...................: 100.00% ✓ 32787      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 97608      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   324 kB/s
     http_req_blocked...............: avg=6.36µs   min=1.29µs  med=3.25µs   max=4.26ms   p(90)=4.5µs    p(95)=5.04µs   p(99.9)=1.28ms  
     http_req_connecting............: avg=2.91µs   min=0s      med=0s       max=4.22ms   p(90)=0s       p(95)=0s       p(99.9)=1.26ms  
     http_req_duration..............: avg=183.68ms min=7.49ms  med=184.35ms max=353.58ms p(90)=194.27ms p(95)=199.45ms p(99.9)=268.82ms
       { expected_response:true }...: avg=183.68ms min=7.49ms  med=184.35ms max=353.58ms p(90)=194.27ms p(95)=199.45ms p(99.9)=268.82ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32636
     http_req_receiving.............: avg=85.47µs  min=35.06µs med=80.99µs  max=30.68ms  p(90)=109.93µs p(95)=120.23µs p(99.9)=528.47µs
     http_req_sending...............: avg=28.03µs  min=5.63µs  med=16.04µs  max=105.53ms p(90)=20.21µs  p(95)=21.93µs  p(99.9)=616.29µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.57ms min=7.4ms   med=184.24ms max=353.5ms  p(90)=194.16ms p(95)=199.35ms p(99.9)=268.64ms
     http_reqs......................: 32636   269.790908/s
     iteration_duration.............: avg=184.5ms  min=46.02ms med=184.67ms max=387.96ms p(90)=194.54ms p(95)=199.7ms  p(99.9)=270.67ms
     iterations.....................: 32536   268.964241/s
     success_rate...................: 100.00% ✓ 32536      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

