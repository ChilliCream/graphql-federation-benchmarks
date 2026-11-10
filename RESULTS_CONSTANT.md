## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 5,133 | 5,156 | 5,118 | 0.3% | 379 MB | 75.6 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 5,071 | 5,078 | 5,043 | 0.3% | 363 MB | 73.3 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,893 | 4,907 | 4,877 | 0.3% | 376 MB | 78.8 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,772 | 4,789 | 4,765 | 0.2% | 145 MB | 31.2 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,757 | 4,785 | 4,733 | 0.4% | 374 MB | 80.6 KB |  |
| fusion-aot-11 | 16.7.3 | 4,753 | 4,772 | 4,726 | 0.4% | 122 MB | 26.4 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,550 | 4,569 | 4,546 | 0.2% | 129 MB | 29.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,464 | 4,484 | 4,447 | 0.3% | 128 MB | 29.4 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,325 | 4,505 | 4,099 | 3.8% | 2,306 MB | 546.0 KB |  |
| hive-router | v0.3.10 | 3,057 | 3,082 | 3,043 | 0.5% | 90 MB | 30.1 KB |  |
| grafbase | 0.53.5 | 1,869 | 1,886 | 1,855 | 0.6% | 105 MB | 57.6 KB |  |
| cosmo | 0.365.2 | 1,490 | 1,493 | 1,489 | 0.1% | 164 MB | 112.9 KB |  |
| caliban | 3.2.0 | 1,383 | 1,385 | 1,381 | 0.1% | 4,707 MB | 3,485.2 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 550 | 550 | 547 | 0.2% | 2,754 MB | 5,128.2 KB |  |
| apollo-router | v2.19.0 | 528 | 529 | 527 | 0.1% | 176 MB | 340.6 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 396 | 396 | 396 | 0.0% | 201 MB | 519.3 KB |  |
| apollo-gateway | 2.14.4 | 270 | 271 | 269 | 0.3% | 2,152 MB | 8,161.9 KB |  |
| hive-gateway | 2.15.6 | 270 | 271 | 270 | 0.2% | 3,478 MB | 13,188.8 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1849572     ✗ 0     
     data_received..................: 54 GB   449 MB/s
     data_sent......................: 741 MB  6.2 MB/s
     http_req_blocked...............: avg=5.94µs  min=781ns    med=1.91µs  max=195.89ms p(90)=3.06µs  p(95)=3.69µs   p(99.9)=26.76µs
     http_req_connecting............: avg=3.59µs  min=0s       med=0s      max=195.87ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.52ms  min=782.75µs med=8.68ms  max=173.35ms p(90)=14.75ms p(95)=17.54ms  p(99.9)=29.59ms
       { expected_response:true }...: avg=9.52ms  min=782.75µs med=8.68ms  max=173.35ms p(90)=14.75ms p(95)=17.54ms  p(99.9)=29.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 616624
     http_req_receiving.............: avg=92.53µs min=24.41µs  med=45.48µs max=40.08ms  p(90)=88.23µs p(95)=188.54µs p(99.9)=6.21ms 
     http_req_sending...............: avg=41.99µs min=4.34µs   med=8µs     max=88.23ms  p(90)=14.36µs p(95)=99.85µs  p(99.9)=4.64ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.38ms  min=745.1µs  med=8.57ms  max=173.11ms p(90)=14.53ms p(95)=17.29ms  p(99.9)=29.23ms
     http_reqs......................: 616624  5133.934358/s
     iteration_duration.............: avg=9.72ms  min=1.2ms    med=8.87ms  max=304.62ms p(90)=14.96ms p(95)=17.75ms  p(99.9)=29.84ms
     iterations.....................: 616524  5133.101771/s
     success_rate...................: 100.00% ✓ 616524      ✗ 0     
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

     checks.........................: 100.00% ✓ 1827135     ✗ 0     
     data_received..................: 53 GB   444 MB/s
     data_sent......................: 732 MB  6.1 MB/s
     http_req_blocked...............: avg=2.45µs  min=801ns    med=1.84µs  max=10.95ms  p(90)=2.95µs  p(95)=3.55µs   p(99.9)=26.49µs
     http_req_connecting............: avg=147ns   min=0s       med=0s      max=4.11ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.64ms  min=822.49µs med=8.84ms  max=274.44ms p(90)=14.8ms  p(95)=17.51ms  p(99.9)=29.29ms
       { expected_response:true }...: avg=9.64ms  min=822.49µs med=8.84ms  max=274.44ms p(90)=14.8ms  p(95)=17.51ms  p(99.9)=29.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 609145
     http_req_receiving.............: avg=88.37µs min=23.55µs  med=44.66µs max=114.01ms p(90)=88.36µs p(95)=186.77µs p(99.9)=5.6ms  
     http_req_sending...............: avg=40.62µs min=4.33µs   med=7.89µs  max=203.4ms  p(90)=14.17µs p(95)=98.22µs  p(99.9)=4.46ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.51ms  min=759.14µs med=8.73ms  max=256.52ms p(90)=14.6ms  p(95)=17.25ms  p(99.9)=28.93ms
     http_reqs......................: 609145  5071.498331/s
     iteration_duration.............: avg=9.84ms  min=1.37ms   med=9.02ms  max=298.32ms p(90)=15ms    p(95)=17.72ms  p(99.9)=29.55ms
     iterations.....................: 609045  5070.665771/s
     success_rate...................: 100.00% ✓ 609045      ✗ 0     
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

     checks.........................: 100.00% ✓ 1763394     ✗ 0     
     data_received..................: 51 GB   428 MB/s
     data_sent......................: 707 MB  5.9 MB/s
     http_req_blocked...............: avg=2.63µs  min=812ns    med=2.01µs max=23.04ms  p(90)=3.29µs  p(95)=4.06µs   p(99.9)=27.71µs
     http_req_connecting............: avg=210ns   min=0s       med=0s     max=22.79ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.99ms  min=983.83µs med=9.16ms max=207.62ms p(90)=15.31ms p(95)=18.11ms  p(99.9)=30.52ms
       { expected_response:true }...: avg=9.99ms  min=983.83µs med=9.16ms max=207.62ms p(90)=15.31ms p(95)=18.11ms  p(99.9)=30.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 587898
     http_req_receiving.............: avg=98.67µs min=24.91µs  med=47.5µs max=49.87ms  p(90)=95.37µs p(95)=194.66µs p(99.9)=6.45ms 
     http_req_sending...............: avg=44.57µs min=4.56µs   med=8.31µs max=106.84ms p(90)=16.04µs p(95)=103.64µs p(99.9)=5.05ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.85ms  min=894.33µs med=9.04ms max=207.55ms p(90)=15.09ms p(95)=17.83ms  p(99.9)=30.02ms
     http_reqs......................: 587898  4893.825445/s
     iteration_duration.............: avg=10.19ms min=1.36ms   med=9.35ms max=319.11ms p(90)=15.53ms p(95)=18.33ms  p(99.9)=30.78ms
     iterations.....................: 587798  4892.993017/s
     success_rate...................: 100.00% ✓ 587798      ✗ 0     
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

     checks.........................: 100.00% ✓ 1719603     ✗ 0     
     data_received..................: 50 GB   418 MB/s
     data_sent......................: 689 MB  5.7 MB/s
     http_req_blocked...............: avg=2.94µs  min=912ns    med=2.29µs  max=5.55ms   p(90)=3.63µs  p(95)=4.3µs    p(99.9)=32.37µs
     http_req_connecting............: avg=222ns   min=0s       med=0s      max=4.68ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.26ms min=907.66µs med=9.48ms  max=273.2ms  p(90)=15.53ms p(95)=18.39ms  p(99.9)=30.22ms
       { expected_response:true }...: avg=10.26ms min=907.66µs med=9.48ms  max=273.2ms  p(90)=15.53ms p(95)=18.39ms  p(99.9)=30.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 573301
     http_req_receiving.............: avg=97.83µs min=24.01µs  med=46.11µs max=56.79ms  p(90)=94.59µs p(95)=214.19µs p(99.9)=6.47ms 
     http_req_sending...............: avg=42.48µs min=4.46µs   med=8.43µs  max=151.43ms p(90)=15.49µs p(95)=109.67µs p(99.9)=4.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.12ms min=860.56µs med=9.37ms  max=253.67ms p(90)=15.31ms p(95)=18.12ms  p(99.9)=29.76ms
     http_reqs......................: 573301  4772.670167/s
     iteration_duration.............: avg=10.45ms min=1.37ms   med=9.67ms  max=289.84ms p(90)=15.74ms p(95)=18.61ms  p(99.9)=30.53ms
     iterations.....................: 573201  4771.837677/s
     success_rate...................: 100.00% ✓ 573201      ✗ 0     
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

     checks.........................: 100.00% ✓ 1714275     ✗ 0     
     data_received..................: 50 GB   416 MB/s
     data_sent......................: 687 MB  5.7 MB/s
     http_req_blocked...............: avg=4.86µs   min=922ns    med=2.46µs  max=139.42ms p(90)=3.74µs  p(95)=4.42µs   p(99.9)=31.81µs
     http_req_connecting............: avg=1.91µs   min=0s       med=0s      max=139.38ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.28ms  min=1.02ms   med=9.44ms  max=246.56ms p(90)=15.76ms p(95)=18.73ms  p(99.9)=31.99ms
       { expected_response:true }...: avg=10.28ms  min=1.02ms   med=9.44ms  max=246.56ms p(90)=15.76ms p(95)=18.73ms  p(99.9)=31.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 571525
     http_req_receiving.............: avg=103.91µs min=24.86µs  med=49.13µs max=33.07ms  p(90)=97.41µs p(95)=208.88µs p(99.9)=7.18ms 
     http_req_sending...............: avg=46.47µs  min=4.49µs   med=8.95µs  max=193.19ms p(90)=16.23µs p(95)=107.05µs p(99.9)=5.2ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.13ms  min=947.66µs med=9.31ms  max=201.23ms p(90)=15.52ms p(95)=18.44ms  p(99.9)=31.42ms
     http_reqs......................: 571525  4757.486749/s
     iteration_duration.............: avg=10.48ms  min=1.39ms   med=9.64ms  max=301.65ms p(90)=15.97ms p(95)=18.95ms  p(99.9)=32.36ms
     iterations.....................: 571425  4756.654329/s
     success_rate...................: 100.00% ✓ 571425      ✗ 0     
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

     checks.........................: 100.00% ✓ 1712733     ✗ 0     
     data_received..................: 50 GB   416 MB/s
     data_sent......................: 686 MB  5.7 MB/s
     http_req_blocked...............: avg=2.96µs  min=892ns    med=2.36µs  max=5.41ms   p(90)=3.67µs  p(95)=4.3µs    p(99.9)=32.68µs
     http_req_connecting............: avg=168ns   min=0s       med=0s      max=4.03ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.3ms  min=938.09µs med=9.57ms  max=279.71ms p(90)=15.45ms p(95)=18.21ms  p(99.9)=29.89ms
       { expected_response:true }...: avg=10.3ms  min=938.09µs med=9.57ms  max=279.71ms p(90)=15.45ms p(95)=18.21ms  p(99.9)=29.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 571011
     http_req_receiving.............: avg=94.61µs min=25.18µs  med=47.01µs max=18.78ms  p(90)=93.2µs  p(95)=211.59µs p(99.9)=5.98ms 
     http_req_sending...............: avg=41.41µs min=4.39µs   med=8.56µs  max=101.19ms p(90)=15.13µs p(95)=108.43µs p(99.9)=4.22ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.16ms min=852.71µs med=9.46ms  max=279.38ms p(90)=15.25ms p(95)=17.96ms  p(99.9)=29.4ms 
     http_reqs......................: 571011  4753.585923/s
     iteration_duration.............: avg=10.5ms  min=1.24ms   med=9.75ms  max=293.54ms p(90)=15.66ms p(95)=18.43ms  p(99.9)=30.19ms
     iterations.....................: 570911  4752.753437/s
     success_rate...................: 100.00% ✓ 570911      ✗ 0     
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

     checks.........................: 100.00% ✓ 1639806     ✗ 0     
     data_received..................: 48 GB   398 MB/s
     data_sent......................: 657 MB  5.5 MB/s
     http_req_blocked...............: avg=3.47µs   min=911ns   med=2.42µs  max=9ms      p(90)=3.87µs   p(95)=4.66µs   p(99.9)=33.18µs
     http_req_connecting............: avg=525ns    min=0s      med=0s      max=8.94ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.75ms  min=1.08ms  med=10.03ms max=276.93ms p(90)=16.07ms  p(95)=18.83ms  p(99.9)=31.26ms
       { expected_response:true }...: avg=10.75ms  min=1.08ms  med=10.03ms max=276.93ms p(90)=16.07ms  p(95)=18.83ms  p(99.9)=31.26ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 546702
     http_req_receiving.............: avg=103.59µs min=25.54µs med=48.86µs max=150.47ms p(90)=103.19µs p(95)=219.77µs p(99.9)=6.74ms 
     http_req_sending...............: avg=43.57µs  min=4.35µs  med=8.73µs  max=159.57ms p(90)=17.29µs  p(95)=111.65µs p(99.9)=4.49ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.61ms  min=992.5µs med=9.91ms  max=276.22ms p(90)=15.84ms  p(95)=18.56ms  p(99.9)=30.81ms
     http_reqs......................: 546702  4550.750925/s
     iteration_duration.............: avg=10.96ms  min=1.58ms  med=10.23ms max=303.77ms p(90)=16.28ms  p(95)=19.05ms  p(99.9)=31.6ms 
     iterations.....................: 546602  4549.918524/s
     success_rate...................: 100.00% ✓ 546602      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1608975     ✗ 0     
     data_received..................: 47 GB   391 MB/s
     data_sent......................: 645 MB  5.4 MB/s
     http_req_blocked...............: avg=2.94µs   min=922ns  med=2.33µs  max=8.18ms   p(90)=3.64µs   p(95)=4.33µs   p(99.9)=35.02µs
     http_req_connecting............: avg=157ns    min=0s     med=0s      max=3.34ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.97ms  min=1.05ms med=10.33ms max=218.31ms p(90)=16.09ms  p(95)=18.67ms  p(99.9)=31.24ms
       { expected_response:true }...: avg=10.97ms  min=1.05ms med=10.33ms max=218.31ms p(90)=16.09ms  p(95)=18.67ms  p(99.9)=31.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 536425
     http_req_receiving.............: avg=102.07µs min=26.2µs med=48.48µs max=193.79ms p(90)=100.84µs p(95)=218.4µs  p(99.9)=6.45ms 
     http_req_sending...............: avg=42.96µs  min=4.52µs med=8.64µs  max=76.55ms  p(90)=16.5µs   p(95)=110.65µs p(99.9)=4.44ms 
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.82ms  min=1.01ms med=10.21ms max=217.85ms p(90)=15.87ms  p(95)=18.41ms  p(99.9)=30.68ms
     http_reqs......................: 536425  4464.774225/s
     iteration_duration.............: avg=11.17ms  min=1.21ms med=10.53ms max=314.91ms p(90)=16.3ms   p(95)=18.89ms  p(99.9)=31.59ms
     iterations.....................: 536325  4463.941905/s
     success_rate...................: 100.00% ✓ 536325      ✗ 0     
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

     checks.........................: 100.00% ✓ 1558146     ✗ 0     
     data_received..................: 45 GB   378 MB/s
     data_sent......................: 624 MB  5.2 MB/s
     http_req_blocked...............: avg=3.56µs  min=992ns    med=2.63µs  max=12.8ms   p(90)=4.01µs  p(95)=4.68µs   p(99.9)=33.78µs
     http_req_connecting............: avg=480ns   min=0s       med=0s      max=12.72ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.34ms min=783.64µs med=11.04ms max=275.74ms p(90)=17.42ms p(95)=19.91ms  p(99.9)=31.62ms
       { expected_response:true }...: avg=11.34ms min=783.64µs med=11.04ms max=275.74ms p(90)=17.42ms p(95)=19.91ms  p(99.9)=31.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 519482
     http_req_receiving.............: avg=94.48µs min=25.92µs  med=50.27µs max=186.06ms p(90)=98.45µs p(95)=221.58µs p(99.9)=5.04ms 
     http_req_sending...............: avg=43.13µs min=4.83µs   med=9.68µs  max=77.65ms  p(90)=16.57µs p(95)=117.75µs p(99.9)=3.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.2ms  min=714.43µs med=10.92ms max=264.17ms p(90)=17.24ms p(95)=19.69ms  p(99.9)=31.28ms
     http_reqs......................: 519482  4325.038416/s
     iteration_duration.............: avg=11.54ms min=1.25ms   med=11.23ms max=290.17ms p(90)=17.62ms p(95)=20.13ms  p(99.9)=31.89ms
     iterations.....................: 519382  4324.205849/s
     success_rate...................: 100.00% ✓ 519382      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1101957     ✗ 0     
     data_received..................: 32 GB   267 MB/s
     data_sent......................: 442 MB  3.7 MB/s
     http_req_blocked...............: avg=2.81µs  min=852ns   med=2.26µs  max=3.76ms   p(90)=3.77µs  p(95)=4.55µs   p(99.9)=34.37µs
     http_req_connecting............: avg=187ns   min=0s      med=0s      max=3.73ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.12ms min=1.31ms  med=16.13ms max=280.36ms p(90)=21.55ms p(95)=23.02ms  p(99.9)=30.74ms
       { expected_response:true }...: avg=16.12ms min=1.31ms  med=16.13ms max=280.36ms p(90)=21.55ms p(95)=23.02ms  p(99.9)=30.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 367419
     http_req_receiving.............: avg=73.72µs min=24.85µs med=50.77µs max=41.2ms   p(90)=93.97µs p(95)=176.07µs p(99.9)=1.34ms 
     http_req_sending...............: avg=35.76µs min=4.52µs  med=9.81µs  max=265.81ms p(90)=18.21µs p(95)=108.36µs p(99.9)=1.41ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.01ms min=1.23ms  med=16.03ms max=279.94ms p(90)=21.44ms p(95)=22.9ms   p(99.9)=30.49ms
     http_reqs......................: 367419  3057.238074/s
     iteration_duration.............: avg=16.32ms min=2.6ms   med=16.32ms max=334.85ms p(90)=21.74ms p(95)=23.21ms  p(99.9)=31.03ms
     iterations.....................: 367319  3056.405989/s
     success_rate...................: 100.00% ✓ 367319      ✗ 0     
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

     checks.........................: 100.00% ✓ 674079      ✗ 0     
     data_received..................: 20 GB   164 MB/s
     data_sent......................: 270 MB  2.2 MB/s
     http_req_blocked...............: avg=3.16µs  min=821ns   med=2.24µs  max=4.11ms   p(90)=4.26µs   p(95)=5.29µs   p(99.9)=34.11µs
     http_req_connecting............: avg=416ns   min=0s      med=0s      max=4.06ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.46ms min=1.84ms  med=25.89ms max=306.16ms p(90)=34.32ms  p(95)=37.01ms  p(99.9)=51.01ms
       { expected_response:true }...: avg=26.46ms min=1.84ms  med=25.89ms max=306.16ms p(90)=34.32ms  p(95)=37.01ms  p(99.9)=51.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 224793
     http_req_receiving.............: avg=82.73µs min=26.84µs med=57.27µs max=71.87ms  p(90)=116.94µs p(95)=178.12µs p(99.9)=1.33ms 
     http_req_sending...............: avg=33.29µs min=4.63µs  med=9.7µs   max=212.24ms p(90)=21.82µs  p(95)=96.39µs  p(99.9)=1.5ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.34ms min=1.78ms  med=25.79ms max=277.9ms  p(90)=34.2ms   p(95)=36.9ms   p(99.9)=50.8ms 
     http_reqs......................: 224793  1869.14699/s
     iteration_duration.............: avg=26.69ms min=5.6ms   med=26.11ms max=313.02ms p(90)=34.53ms  p(95)=37.23ms  p(99.9)=51.27ms
     iterations.....................: 224693  1868.315493/s
     success_rate...................: 100.00% ✓ 224693      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 537504      ✗ 0     
     data_received..................: 16 GB   130 MB/s
     data_sent......................: 215 MB  1.8 MB/s
     http_req_blocked...............: avg=3.55µs  min=1.08µs  med=2.74µs  max=4.09ms   p(90)=4.29µs  p(95)=4.98µs   p(99.9)=35.02µs 
     http_req_connecting............: avg=507ns   min=0s      med=0s      max=4.06ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.25ms min=2.08ms  med=32.36ms max=304.05ms p(90)=48.02ms p(95)=52.99ms  p(99.9)=76.01ms 
       { expected_response:true }...: avg=33.25ms min=2.08ms  med=32.36ms max=304.05ms p(90)=48.02ms p(95)=52.99ms  p(99.9)=76.01ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 179268
     http_req_receiving.............: avg=73.55µs min=27.31µs med=62.84µs max=50.37ms  p(90)=99.14µs p(95)=114.62µs p(99.9)=721.74µs
     http_req_sending...............: avg=24.38µs min=4.86µs  med=11.32µs max=178.46ms p(90)=17.68µs p(95)=21.51µs  p(99.9)=778.26µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.15ms min=2.01ms  med=32.27ms max=303.56ms p(90)=47.91ms p(95)=52.89ms  p(99.9)=75.88ms 
     http_reqs......................: 179268  1490.426943/s
     iteration_duration.............: avg=33.48ms min=4.23ms  med=32.57ms max=312.9ms  p(90)=48.22ms p(95)=53.19ms  p(99.9)=76.45ms 
     iterations.....................: 179168  1489.595547/s
     success_rate...................: 100.00% ✓ 179168      ✗ 0     
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

     checks.........................: 100.00% ✓ 498882      ✗ 0     
     data_received..................: 15 GB   121 MB/s
     data_sent......................: 200 MB  1.7 MB/s
     http_req_blocked...............: avg=2.9µs   min=881ns   med=2.05µs  max=4.07ms   p(90)=3.31µs  p(95)=3.89µs  p(99.9)=29.43µs 
     http_req_connecting............: avg=580ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=35.85ms min=2.21ms  med=34.83ms max=307.02ms p(90)=51.21ms p(95)=56.67ms p(99.9)=88.02ms 
       { expected_response:true }...: avg=35.85ms min=2.21ms  med=34.83ms max=307.02ms p(90)=51.21ms p(95)=56.67ms p(99.9)=88.02ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 166394
     http_req_receiving.............: avg=65.85µs min=25.57µs med=54.63µs max=168.51ms p(90)=83.63µs p(95)=97.14µs p(99.9)=693.49µs
     http_req_sending...............: avg=17.75µs min=4.66µs  med=9.71µs  max=130.68ms p(90)=14.07µs p(95)=16.84µs p(99.9)=654.92µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=35.77ms min=2.15ms  med=34.74ms max=306.43ms p(90)=51.13ms p(95)=56.59ms p(99.9)=87.04ms 
     http_reqs......................: 166394  1383.322547/s
     iteration_duration.............: avg=36.07ms min=5.69ms  med=35.02ms max=316.23ms p(90)=51.4ms  p(95)=56.86ms p(99.9)=88.5ms  
     iterations.....................: 166294  1382.491193/s
     success_rate...................: 100.00% ✓ 166294      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 198642     ✗ 0    
     data_received..................: 5.8 GB  48 MB/s
     data_sent......................: 80 MB   661 kB/s
     http_req_blocked...............: avg=5.04µs  min=1µs     med=2.45µs  max=7.47ms   p(90)=3.91µs   p(95)=4.48µs   p(99.9)=46.32µs 
     http_req_connecting............: avg=2.25µs  min=0s      med=0s      max=7.28ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=90.28ms min=3.78ms  med=88.91ms max=306.03ms p(90)=120.97ms p(95)=133.47ms p(99.9)=229.38ms
       { expected_response:true }...: avg=90.28ms min=3.78ms  med=88.91ms max=306.03ms p(90)=120.97ms p(95)=133.47ms p(99.9)=229.38ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 66314
     http_req_receiving.............: avg=75.14µs min=28.68µs med=67.75µs max=45.34ms  p(90)=101.67µs p(95)=114.06µs p(99.9)=545.38µs
     http_req_sending...............: avg=17.88µs min=4.85µs  med=12.32µs max=71.01ms  p(90)=18.46µs  p(95)=20.35µs  p(99.9)=586.52µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=90.18ms min=3.71ms  med=88.82ms max=304.38ms p(90)=120.88ms p(95)=133.37ms p(99.9)=229.31ms
     http_reqs......................: 66314   550.193965/s
     iteration_duration.............: avg=90.64ms min=20.38ms med=89.21ms max=322.23ms p(90)=121.22ms p(95)=133.73ms p(99.9)=231.71ms
     iterations.....................: 66214   549.364285/s
     success_rate...................: 100.00% ✓ 66214      ✗ 0    
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

     checks.........................: 100.00% ✓ 190866     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   635 kB/s
     http_req_blocked...............: avg=4.29µs  min=1.08µs  med=2.9µs   max=3.28ms   p(90)=4.34µs   p(95)=4.86µs   p(99.9)=56.52µs 
     http_req_connecting............: avg=1.19µs  min=0s      med=0s      max=3.25ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.94ms min=4.41ms  med=91.96ms max=316.32ms p(90)=126.91ms p(95)=137.3ms  p(99.9)=177.18ms
       { expected_response:true }...: avg=93.94ms min=4.41ms  med=91.96ms max=316.32ms p(90)=126.91ms p(95)=137.3ms  p(99.9)=177.18ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63722
     http_req_receiving.............: avg=78.13µs min=27.14µs med=71.93µs max=83.24ms  p(90)=102.6µs  p(95)=114.55µs p(99.9)=514.16µs
     http_req_sending...............: avg=23.21µs min=5.05µs  med=14.37µs max=134.67ms p(90)=19.55µs  p(95)=21.41µs  p(99.9)=578.77µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.83ms min=4.33ms  med=91.86ms max=315.85ms p(90)=126.8ms  p(95)=137.18ms p(99.9)=176.6ms 
     http_reqs......................: 63722   528.511716/s
     iteration_duration.............: avg=94.32ms min=10.27ms med=92.23ms max=323.8ms  p(90)=127.17ms p(95)=137.57ms p(99.9)=178ms   
     iterations.....................: 63622   527.682314/s
     success_rate...................: 100.00% ✓ 63622      ✗ 0    
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

     checks.........................: 100.00% ✓ 143379     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   476 kB/s
     http_req_blocked...............: avg=6.25µs   min=1.08µs  med=2.83µs   max=6.06ms   p(90)=4.11µs   p(95)=4.6µs    p(99.9)=371.86µs
     http_req_connecting............: avg=3.03µs   min=0s      med=0s       max=6.02ms   p(90)=0s       p(95)=0s       p(99.9)=229.06µs
     http_req_duration..............: avg=125.08ms min=5.41ms  med=122.71ms max=329.8ms  p(90)=163.91ms p(95)=176.67ms p(99.9)=226.58ms
       { expected_response:true }...: avg=125.08ms min=5.41ms  med=122.71ms max=329.8ms  p(90)=163.91ms p(95)=176.67ms p(99.9)=226.58ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47893
     http_req_receiving.............: avg=78.9µs   min=27.84µs med=73.94µs  max=57.09ms  p(90)=103.07µs p(95)=114.72µs p(99.9)=535.35µs
     http_req_sending...............: avg=19.44µs  min=4.88µs  med=15.02µs  max=26.17ms  p(90)=19.6µs   p(95)=21.27µs  p(99.9)=589.63µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=124.98ms min=5.31ms  med=122.62ms max=327.87ms p(90)=163.8ms  p(95)=176.56ms p(99.9)=226.49ms
     http_reqs......................: 47893   396.784609/s
     iteration_duration.............: avg=125.58ms min=25.63ms med=123.03ms max=353.44ms p(90)=164.19ms p(95)=176.95ms p(99.9)=230.8ms 
     iterations.....................: 47793   395.956127/s
     success_rate...................: 100.00% ✓ 47793      ✗ 0    
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

     checks.........................: 100.00% ✓ 97965      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   325 kB/s
     http_req_blocked...............: avg=6.38µs   min=1.13µs  med=3.26µs   max=3.45ms   p(90)=4.56µs   p(95)=5.09µs   p(99.9)=1.5ms   
     http_req_connecting............: avg=2.91µs   min=0s      med=0s       max=3.42ms   p(90)=0s       p(95)=0s       p(99.9)=1.48ms  
     http_req_duration..............: avg=182.99ms min=7.66ms  med=176.12ms max=366.4ms  p(90)=208.22ms p(95)=212.94ms p(99.9)=288.95ms
       { expected_response:true }...: avg=182.99ms min=7.66ms  med=176.12ms max=366.4ms  p(90)=208.22ms p(95)=212.94ms p(99.9)=288.95ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32755
     http_req_receiving.............: avg=85.66µs  min=32µs    med=82.75µs  max=14.97ms  p(90)=111.09µs p(95)=121.53µs p(99.9)=348.82µs
     http_req_sending...............: avg=27.01µs  min=5.38µs  med=16.18µs  max=130.78ms p(90)=20.63µs  p(95)=22.38µs  p(99.9)=478.73µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.88ms min=7.57ms  med=176.02ms max=365.92ms p(90)=208.11ms p(95)=212.84ms p(99.9)=288.68ms
     http_reqs......................: 32755   270.803342/s
     iteration_duration.............: avg=183.81ms min=34.43ms med=176.39ms max=372.16ms p(90)=208.49ms p(95)=213.26ms p(99.9)=290.12ms
     iterations.....................: 32655   269.976588/s
     success_rate...................: 100.00% ✓ 32655      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 97689      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   325 kB/s
     http_req_blocked...............: avg=6.23µs   min=1.07µs  med=3.02µs   max=4.3ms    p(90)=4.32µs   p(95)=4.86µs   p(99.9)=1.35ms  
     http_req_connecting............: avg=3.03µs   min=0s      med=0s       max=4.26ms   p(90)=0s       p(95)=0s       p(99.9)=1.33ms  
     http_req_duration..............: avg=183.58ms min=5.78ms  med=166.19ms max=829.32ms p(90)=209.99ms p(95)=241.12ms p(99.9)=722.6ms 
       { expected_response:true }...: avg=183.58ms min=5.78ms  med=166.19ms max=829.32ms p(90)=209.99ms p(95)=241.12ms p(99.9)=722.6ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 32663
     http_req_receiving.............: avg=87.63µs  min=31.34µs med=83.96µs  max=15.91ms  p(90)=112.97µs p(95)=124.21µs p(99.9)=712.27µs
     http_req_sending...............: avg=20.15µs  min=5.43µs  med=16.26µs  max=16.87ms  p(90)=20.31µs  p(95)=21.91µs  p(99.9)=477.34µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.47ms min=5.64ms  med=166.08ms max=829.25ms p(90)=209.9ms  p(95)=241.03ms p(99.9)=722.51ms
     http_reqs......................: 32663   270.317177/s
     iteration_duration.............: avg=184.37ms min=75.32ms med=166.51ms max=829.5ms  p(90)=210.33ms p(95)=241.51ms p(99.9)=722.84ms
     iterations.....................: 32563   269.489583/s
     success_rate...................: 100.00% ✓ 32563      ✗ 0    
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

