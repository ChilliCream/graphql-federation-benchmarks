## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 5,046 | 5,070 | 5,009 | 0.4% | 387 MB | 78.6 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 5,017 | 5,038 | 4,981 | 0.4% | 363 MB | 74.1 KB |  |
| fusion-aot-11 | 16.7.3 | 4,854 | 4,871 | 4,848 | 0.2% | 144 MB | 30.4 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,830 | 4,855 | 4,775 | 0.6% | 383 MB | 81.2 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,819 | 4,856 | 4,783 | 0.6% | 376 MB | 79.8 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,727 | 4,763 | 4,719 | 0.5% | 134 MB | 29.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,474 | 4,487 | 4,433 | 0.5% | 127 MB | 29.2 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,464 | 4,470 | 4,451 | 0.2% | 129 MB | 29.7 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,351 | 4,381 | 4,260 | 1.2% | 2,300 MB | 541.3 KB |  |
| hive-router | v0.3.10 | 3,064 | 3,095 | 3,041 | 0.7% | 90 MB | 30.0 KB |  |
| grafbase | 0.53.5 | 1,878 | 1,893 | 1,875 | 0.4% | 112 MB | 61.2 KB |  |
| cosmo | 0.365.2 | 1,485 | 1,486 | 1,483 | 0.1% | 164 MB | 112.8 KB |  |
| caliban | 3.2.0 | 1,448 | 1,457 | 1,443 | 0.4% | 3,930 MB | 2,779.1 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 537 | 539 | 537 | 0.2% | 2,754 MB | 5,252.2 KB |  |
| apollo-router | v2.19.0 | 484 | 490 | 484 | 0.5% | 172 MB | 363.5 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 400 | 411 | 400 | 1.2% | 201 MB | 514.0 KB |  |
| hive-gateway | 2.15.6 | 269 | 269 | 268 | 0.2% | 3,570 MB | 13,589.8 KB |  |
| apollo-gateway | 2.14.4 | 268 | 269 | 268 | 0.2% | 2,178 MB | 8,321.8 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1818204     ✗ 0     
     data_received..................: 53 GB   442 MB/s
     data_sent......................: 729 MB  6.1 MB/s
     http_req_blocked...............: avg=2.94µs  min=911ns    med=2.31µs  max=6.44ms   p(90)=3.63µs  p(95)=4.34µs   p(99.9)=32.04µs
     http_req_connecting............: avg=185ns   min=0s       med=0s      max=4.3ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.69ms  min=840.73µs med=8.78ms  max=266.56ms p(90)=15.14ms p(95)=18.16ms  p(99.9)=30.61ms
       { expected_response:true }...: avg=9.69ms  min=840.73µs med=8.78ms  max=266.56ms p(90)=15.14ms p(95)=18.16ms  p(99.9)=30.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 606168
     http_req_receiving.............: avg=96.74µs min=24.72µs  med=46.97µs max=160.86ms p(90)=93.04µs p(95)=199.3µs  p(99.9)=6.26ms 
     http_req_sending...............: avg=44.54µs min=4.41µs   med=8.51µs  max=195.36ms p(90)=15.45µs p(95)=105.53µs p(99.9)=4.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.54ms  min=757.63µs med=8.67ms  max=263.4ms  p(90)=14.91ms p(95)=17.87ms  p(99.9)=30.15ms
     http_reqs......................: 606168  5046.930475/s
     iteration_duration.............: avg=9.89ms  min=1.18ms   med=8.97ms  max=293.82ms p(90)=15.35ms p(95)=18.39ms  p(99.9)=30.94ms
     iterations.....................: 606068  5046.097879/s
     success_rate...................: 100.00% ✓ 606068      ✗ 0     
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

     checks.........................: 100.00% ✓ 1807905     ✗ 0     
     data_received..................: 53 GB   439 MB/s
     data_sent......................: 724 MB  6.0 MB/s
     http_req_blocked...............: avg=2.41µs  min=791ns    med=1.85µs  max=8.82ms   p(90)=2.92µs  p(95)=3.47µs   p(99.9)=26.42µs
     http_req_connecting............: avg=139ns   min=0s       med=0s      max=3.27ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.75ms  min=833.27µs med=8.97ms  max=281.56ms p(90)=14.9ms  p(95)=17.5ms   p(99.9)=29.59ms
       { expected_response:true }...: avg=9.75ms  min=833.27µs med=8.97ms  max=281.56ms p(90)=14.9ms  p(95)=17.5ms   p(99.9)=29.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 602735
     http_req_receiving.............: avg=91.16µs min=24.36µs  med=45.16µs max=252.66ms p(90)=87.6µs  p(95)=190.54µs p(99.9)=5.67ms 
     http_req_sending...............: avg=40.36µs min=4.3µs    med=7.94µs  max=183.92ms p(90)=13.98µs p(95)=98.71µs  p(99.9)=4.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.62ms  min=764.99µs med=8.86ms  max=276.56ms p(90)=14.7ms  p(95)=17.27ms  p(99.9)=29.06ms
     http_reqs......................: 602735  5017.992862/s
     iteration_duration.............: avg=9.94ms  min=1.26ms   med=9.15ms  max=315.81ms p(90)=15.1ms  p(95)=17.71ms  p(99.9)=29.87ms
     iterations.....................: 602635  5017.160325/s
     success_rate...................: 100.00% ✓ 602635      ✗ 0     
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

     checks.........................: 100.00% ✓ 1748970     ✗ 0     
     data_received..................: 51 GB   425 MB/s
     data_sent......................: 701 MB  5.8 MB/s
     http_req_blocked...............: avg=2.49µs  min=791ns    med=1.88µs  max=6.73ms   p(90)=3µs     p(95)=3.59µs   p(99.9)=25.82µs
     http_req_connecting............: avg=170ns   min=0s       med=0s      max=3.58ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.09ms min=925.13µs med=9.41ms  max=280.05ms p(90)=14.96ms p(95)=17.5ms   p(99.9)=28.72ms
       { expected_response:true }...: avg=10.09ms min=925.13µs med=9.41ms  max=280.05ms p(90)=14.96ms p(95)=17.5ms   p(99.9)=28.72ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 583090
     http_req_receiving.............: avg=90.65µs min=24.15µs  med=44.34µs max=155.09ms p(90)=89.95µs p(95)=200.29µs p(99.9)=5.72ms 
     http_req_sending...............: avg=39.44µs min=4.35µs   med=8µs     max=167.09ms p(90)=14.3µs  p(95)=102.59µs p(99.9)=4.12ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.96ms  min=848.91µs med=9.31ms  max=279.88ms p(90)=14.75ms p(95)=17.25ms  p(99.9)=28.32ms
     http_reqs......................: 583090  4854.226234/s
     iteration_duration.............: avg=10.28ms min=1.18ms   med=9.6ms   max=290.75ms p(90)=15.15ms p(95)=17.72ms  p(99.9)=28.96ms
     iterations.....................: 582990  4853.393734/s
     success_rate...................: 100.00% ✓ 582990      ✗ 0     
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

     checks.........................: 100.00% ✓ 1740717     ✗ 0     
     data_received..................: 51 GB   423 MB/s
     data_sent......................: 698 MB  5.8 MB/s
     http_req_blocked...............: avg=2.62µs   min=772ns    med=1.98µs  max=6.43ms   p(90)=3.21µs  p(95)=3.98µs   p(99.9)=28.84µs
     http_req_connecting............: avg=166ns    min=0s       med=0s      max=3.6ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.12ms  min=999.48µs med=9.33ms  max=287.95ms p(90)=15.39ms p(95)=18.12ms  p(99.9)=30.85ms
       { expected_response:true }...: avg=10.12ms  min=999.48µs med=9.33ms  max=287.95ms p(90)=15.39ms p(95)=18.12ms  p(99.9)=30.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 580339
     http_req_receiving.............: avg=100.41µs min=25.91µs  med=48.25µs max=88.45ms  p(90)=95.75µs p(95)=196.52µs p(99.9)=6.72ms 
     http_req_sending...............: avg=43.1µs   min=4.38µs   med=8.28µs  max=206.18ms p(90)=15.2µs  p(95)=100.38µs p(99.9)=4.84ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.98ms   min=911.25µs med=9.22ms  max=287.75ms p(90)=15.16ms p(95)=17.87ms  p(99.9)=30.2ms 
     http_reqs......................: 580339  4830.642875/s
     iteration_duration.............: avg=10.33ms  min=1.32ms   med=9.53ms  max=312.72ms p(90)=15.6ms  p(95)=18.34ms  p(99.9)=31.21ms
     iterations.....................: 580239  4829.810492/s
     success_rate...................: 100.00% ✓ 580239      ✗ 0     
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

     checks.........................: 100.00% ✓ 1736421     ✗ 0     
     data_received..................: 51 GB   422 MB/s
     data_sent......................: 696 MB  5.8 MB/s
     http_req_blocked...............: avg=2.53µs  min=791ns    med=1.89µs  max=6.03ms   p(90)=3.09µs  p(95)=3.82µs   p(99.9)=27.62µs
     http_req_connecting............: avg=153ns   min=0s       med=0s      max=3.89ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.15ms min=955.14µs med=9.4ms   max=281.13ms p(90)=15.34ms p(95)=17.93ms  p(99.9)=30.2ms 
       { expected_response:true }...: avg=10.15ms min=955.14µs med=9.4ms   max=281.13ms p(90)=15.34ms p(95)=17.93ms  p(99.9)=30.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 578907
     http_req_receiving.............: avg=96.01µs min=25.38µs  med=47.22µs max=253.46ms p(90)=93.55µs p(95)=194.95µs p(99.9)=5.86ms 
     http_req_sending...............: avg=41.81µs min=3.95µs   med=7.95µs  max=88.27ms  p(90)=14.77µs p(95)=100.77µs p(99.9)=4.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.01ms min=878.36µs med=9.29ms  max=253.32ms p(90)=15.14ms p(95)=17.69ms  p(99.9)=29.78ms
     http_reqs......................: 578907  4819.085072/s
     iteration_duration.............: avg=10.35ms min=1.32ms   med=9.6ms   max=290.99ms p(90)=15.54ms p(95)=18.15ms  p(99.9)=30.6ms 
     iterations.....................: 578807  4818.252626/s
     success_rate...................: 100.00% ✓ 578807      ✗ 0     
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

     checks.........................: 100.00% ✓ 1703415     ✗ 0     
     data_received..................: 50 GB   414 MB/s
     data_sent......................: 683 MB  5.7 MB/s
     http_req_blocked...............: avg=4.99µs  min=922ns    med=2.37µs  max=191.3ms  p(90)=3.62µs  p(95)=4.25µs   p(99.9)=30.7µs 
     http_req_connecting............: avg=1.71µs  min=0s       med=0s      max=119.45ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.35ms min=910.92µs med=9.62ms  max=227.61ms p(90)=15.54ms p(95)=18.3ms   p(99.9)=30.44ms
       { expected_response:true }...: avg=10.35ms min=910.92µs med=9.62ms  max=227.61ms p(90)=15.54ms p(95)=18.3ms   p(99.9)=30.44ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 567905
     http_req_receiving.............: avg=95.32µs min=25.22µs  med=47.23µs max=52.02ms  p(90)=93.22µs p(95)=211.43µs p(99.9)=5.71ms 
     http_req_sending...............: avg=41.88µs min=4.65µs   med=8.81µs  max=81.66ms  p(90)=15.31µs p(95)=107.99µs p(99.9)=4.29ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.22ms min=849.13µs med=9.5ms   max=226.79ms p(90)=15.33ms p(95)=18.06ms  p(99.9)=30.03ms
     http_reqs......................: 567905  4727.954288/s
     iteration_duration.............: avg=10.55ms min=1.21ms   med=9.8ms   max=293.63ms p(90)=15.75ms p(95)=18.51ms  p(99.9)=30.7ms 
     iterations.....................: 567805  4727.121763/s
     success_rate...................: 100.00% ✓ 567805      ✗ 0     
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

     checks.........................: 100.00% ✓ 1612326     ✗ 0     
     data_received..................: 47 GB   392 MB/s
     data_sent......................: 646 MB  5.4 MB/s
     http_req_blocked...............: avg=2.58µs  min=801ns   med=1.97µs  max=6.43ms   p(90)=3.24µs  p(95)=3.94µs   p(99.9)=26.64µs
     http_req_connecting............: avg=166ns   min=0s      med=0s      max=3.5ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.95ms min=1.09ms  med=10.4ms  max=272.63ms p(90)=15.77ms p(95)=18.14ms  p(99.9)=30.37ms
       { expected_response:true }...: avg=10.95ms min=1.09ms  med=10.4ms  max=272.63ms p(90)=15.77ms p(95)=18.14ms  p(99.9)=30.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 537542
     http_req_receiving.............: avg=96.57µs min=25.06µs med=46.75µs max=108.83ms p(90)=97.37µs p(95)=208.83µs p(99.9)=6.15ms 
     http_req_sending...............: avg=39.29µs min=4.29µs  med=8.21µs  max=16.39ms  p(90)=15.61µs p(95)=103.81µs p(99.9)=3.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.81ms min=1.04ms  med=10.28ms max=272.09ms p(90)=15.58ms p(95)=17.9ms   p(99.9)=29.77ms
     http_reqs......................: 537542  4474.205372/s
     iteration_duration.............: avg=11.15ms min=1.6ms   med=10.59ms max=283.9ms  p(90)=15.97ms p(95)=18.35ms  p(99.9)=30.64ms
     iterations.....................: 537442  4473.373027/s
     success_rate...................: 100.00% ✓ 537442      ✗ 0     
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

     checks.........................: 100.00% ✓ 1608633     ✗ 0     
     data_received..................: 47 GB   391 MB/s
     data_sent......................: 645 MB  5.4 MB/s
     http_req_blocked...............: avg=2.51µs  min=792ns    med=1.92µs  max=4.89ms   p(90)=3.18µs  p(95)=3.88µs   p(99.9)=26.04µs
     http_req_connecting............: avg=181ns   min=0s       med=0s      max=3.76ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.98ms min=1.01ms   med=10.44ms max=277.54ms p(90)=15.77ms p(95)=18.08ms  p(99.9)=29.5ms 
       { expected_response:true }...: avg=10.98ms min=1.01ms   med=10.44ms max=277.54ms p(90)=15.77ms p(95)=18.08ms  p(99.9)=29.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 536311
     http_req_receiving.............: avg=95.68µs min=26.02µs  med=47.76µs max=175.96ms p(90)=98.81µs p(95)=209.55µs p(99.9)=5.56ms 
     http_req_sending...............: avg=39.13µs min=4.02µs   med=8.15µs  max=56.22ms  p(90)=15.66µs p(95)=104µs    p(99.9)=3.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.84ms min=968.32µs med=10.32ms max=277.23ms p(90)=15.58ms p(95)=17.84ms  p(99.9)=29.07ms
     http_reqs......................: 536311  4464.076743/s
     iteration_duration.............: avg=11.18ms min=1.65ms   med=10.63ms max=292.44ms p(90)=15.97ms p(95)=18.28ms  p(99.9)=29.72ms
     iterations.....................: 536211  4463.244376/s
     success_rate...................: 100.00% ✓ 536211      ✗ 0     
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

     checks.........................: 100.00% ✓ 1567587     ✗ 0     
     data_received..................: 46 GB   380 MB/s
     data_sent......................: 628 MB  5.2 MB/s
     http_req_blocked...............: avg=3.12µs  min=892ns    med=2.51µs  max=5.69ms   p(90)=3.96µs  p(95)=4.64µs   p(99.9)=35.79µs
     http_req_connecting............: avg=208ns   min=0s       med=0s      max=4.21ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.27ms min=749.98µs med=10.77ms max=268.65ms p(90)=16.8ms  p(95)=19.48ms  p(99.9)=31.2ms 
       { expected_response:true }...: avg=11.27ms min=749.98µs med=10.77ms max=268.65ms p(90)=16.8ms  p(95)=19.48ms  p(99.9)=31.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 522629
     http_req_receiving.............: avg=94.35µs min=24.65µs  med=49.66µs max=69.2ms   p(90)=99.17µs p(95)=224.3µs  p(99.9)=5.43ms 
     http_req_sending...............: avg=43.9µs  min=4.83µs   med=9.71µs  max=221.15ms p(90)=17.18µs p(95)=121.79µs p(99.9)=3.91ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.13ms min=671.54µs med=10.65ms max=268.29ms p(90)=16.61ms p(95)=19.23ms  p(99.9)=30.71ms
     http_reqs......................: 522629  4351.178527/s
     iteration_duration.............: avg=11.47ms min=1.2ms    med=10.96ms max=295.79ms p(90)=17.01ms p(95)=19.71ms  p(99.9)=31.44ms
     iterations.....................: 522529  4350.345971/s
     success_rate...................: 100.00% ✓ 522529      ✗ 0     
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

     checks.........................: 100.00% ✓ 1104420     ✗ 0     
     data_received..................: 32 GB   268 MB/s
     data_sent......................: 443 MB  3.7 MB/s
     http_req_blocked...............: avg=8.3µs   min=1.03µs  med=2.84µs  max=260.95ms p(90)=4.46µs   p(95)=5.26µs   p(99.9)=39.66µs
     http_req_connecting............: avg=5.06µs  min=0s      med=0s      max=260.17ms p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.07ms min=1.24ms  med=16.01ms max=260.3ms  p(90)=21.58ms  p(95)=23.17ms  p(99.9)=31.82ms
       { expected_response:true }...: avg=16.07ms min=1.24ms  med=16.01ms max=260.3ms  p(90)=21.58ms  p(95)=23.17ms  p(99.9)=31.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 368240
     http_req_receiving.............: avg=90.46µs min=26.43µs med=55.36µs max=212.83ms p(90)=105.92µs p(95)=226.42µs p(99.9)=2.02ms 
     http_req_sending...............: avg=41.52µs min=4.72µs  med=11.47µs max=90.85ms  p(90)=20.93µs  p(95)=127.47µs p(99.9)=1.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=15.93ms min=1.19ms  med=15.89ms max=173.28ms p(90)=21.46ms  p(95)=23.03ms  p(99.9)=31.5ms 
     http_reqs......................: 368240  3064.473779/s
     iteration_duration.............: avg=16.28ms min=3.49ms  med=16.22ms max=280.58ms p(90)=21.79ms  p(95)=23.38ms  p(99.9)=32.09ms
     iterations.....................: 368140  3063.641584/s
     success_rate...................: 100.00% ✓ 368140      ✗ 0     
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

     checks.........................: 100.00% ✓ 677595      ✗ 0     
     data_received..................: 20 GB   165 MB/s
     data_sent......................: 272 MB  2.3 MB/s
     http_req_blocked...............: avg=3.17µs  min=882ns   med=2.26µs  max=4.04ms   p(90)=4.24µs   p(95)=5.28µs   p(99.9)=38.42µs
     http_req_connecting............: avg=414ns   min=0s      med=0s      max=4ms      p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.32ms min=1.9ms   med=25.86ms max=303.23ms p(90)=34.13ms  p(95)=36.82ms  p(99.9)=50.26ms
       { expected_response:true }...: avg=26.32ms min=1.9ms   med=25.86ms max=303.23ms p(90)=34.13ms  p(95)=36.82ms  p(99.9)=50.26ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 225965
     http_req_receiving.............: avg=85.55µs min=28.55µs med=55.78µs max=90.31ms  p(90)=120.36µs p(95)=200.83µs p(99.9)=1.79ms 
     http_req_sending...............: avg=35.82µs min=4.65µs  med=9.57µs  max=203.96ms p(90)=22.47µs  p(95)=105.54µs p(99.9)=1.65ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.19ms min=1.84ms  med=25.75ms max=302.88ms p(90)=34ms     p(95)=36.69ms  p(99.9)=50ms   
     http_reqs......................: 225965  1878.99549/s
     iteration_duration.............: avg=26.55ms min=6.03ms  med=26.08ms max=313.99ms p(90)=34.35ms  p(95)=37.03ms  p(99.9)=50.56ms
     iterations.....................: 225865  1878.163947/s
     success_rate...................: 100.00% ✓ 225865      ✗ 0     
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

     checks.........................: 100.00% ✓ 535623      ✗ 0     
     data_received..................: 16 GB   130 MB/s
     data_sent......................: 215 MB  1.8 MB/s
     http_req_blocked...............: avg=3.53µs  min=1.06µs  med=2.69µs  max=5.12ms   p(90)=4.26µs   p(95)=4.96µs   p(99.9)=37.26µs 
     http_req_connecting............: avg=522ns   min=0s      med=0s      max=5.06ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.37ms min=2.08ms  med=32.45ms max=279.67ms p(90)=48.34ms  p(95)=53.27ms  p(99.9)=76.5ms  
       { expected_response:true }...: avg=33.37ms min=2.08ms  med=32.45ms max=279.67ms p(90)=48.34ms  p(95)=53.27ms  p(99.9)=76.5ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 178641
     http_req_receiving.............: avg=75.94µs min=27.14µs med=64.14µs max=165.01ms p(90)=101.15µs p(95)=117.42µs p(99.9)=722.74µs
     http_req_sending...............: avg=25.04µs min=4.97µs  med=11.4µs  max=168.61ms p(90)=17.62µs  p(95)=21.7µs   p(99.9)=823.43µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.27ms min=2.02ms  med=32.35ms max=278.39ms p(90)=48.24ms  p(95)=53.16ms  p(99.9)=76.2ms  
     http_reqs......................: 178641  1485.198012/s
     iteration_duration.............: avg=33.6ms  min=3.46ms  med=32.66ms max=294.16ms p(90)=48.54ms  p(95)=53.47ms  p(99.9)=76.88ms 
     iterations.....................: 178541  1484.366625/s
     success_rate...................: 100.00% ✓ 178541      ✗ 0     
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

     checks.........................: 100.00% ✓ 522318      ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.27µs  min=901ns   med=2.46µs  max=4.98ms   p(90)=4.04µs  p(95)=4.73µs   p(99.9)=32.71µs 
     http_req_connecting............: avg=471ns   min=0s      med=0s      max=4.53ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.22ms min=2.09ms  med=33.23ms max=275.07ms p(90)=48.79ms p(95)=53.88ms  p(99.9)=82.39ms 
       { expected_response:true }...: avg=34.22ms min=2.09ms  med=33.23ms max=275.07ms p(90)=48.79ms p(95)=53.88ms  p(99.9)=82.39ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 174206
     http_req_receiving.............: avg=69.43µs min=26.51µs med=57.88µs max=121.48ms p(90)=93.95µs p(95)=109.76µs p(99.9)=810.39µs
     http_req_sending...............: avg=20.92µs min=4.47µs  med=11.33µs max=112.82ms p(90)=18.24µs p(95)=21.8µs   p(99.9)=726.34µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.13ms min=1.99ms  med=33.14ms max=273.8ms  p(90)=48.7ms  p(95)=53.8ms   p(99.9)=82.19ms 
     http_reqs......................: 174206  1448.015702/s
     iteration_duration.............: avg=34.45ms min=6.24ms  med=33.43ms max=285.52ms p(90)=49ms    p(95)=54.09ms  p(99.9)=83.39ms 
     iterations.....................: 174106  1447.184493/s
     success_rate...................: 100.00% ✓ 174106      ✗ 0     
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

     checks.........................: 100.00% ✓ 194055     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   645 kB/s
     http_req_blocked...............: avg=4.95µs  min=1.21µs  med=3.07µs  max=4.28ms   p(90)=4.52µs   p(95)=5.15µs   p(99.9)=49.51µs 
     http_req_connecting............: avg=1.62µs  min=0s      med=0s      max=4.23ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.41ms min=3.89ms  med=89.98ms max=325.29ms p(90)=113.35ms p(95)=125.51ms p(99.9)=219.45ms
       { expected_response:true }...: avg=92.41ms min=3.89ms  med=89.98ms max=325.29ms p(90)=113.35ms p(95)=125.51ms p(99.9)=219.45ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64785
     http_req_receiving.............: avg=77.29µs min=29.59µs med=69.48µs max=26.68ms  p(90)=102.33µs p(95)=113.95µs p(99.9)=563.06µs
     http_req_sending...............: avg=24.97µs min=5.49µs  med=13.8µs  max=134.78ms p(90)=19.36µs  p(95)=21.34µs  p(99.9)=584.76µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.3ms  min=3.82ms  med=89.88ms max=325.05ms p(90)=113.24ms p(95)=125.37ms p(99.9)=219.14ms
     http_reqs......................: 64785   537.326806/s
     iteration_duration.............: avg=92.77ms min=23.63ms med=90.22ms max=334.78ms p(90)=113.61ms p(95)=125.83ms p(99.9)=221.15ms
     iterations.....................: 64685   536.497406/s
     success_rate...................: 100.00% ✓ 64685      ✗ 0    
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

     checks.........................: 100.00% ✓ 174819     ✗ 0    
     data_received..................: 5.1 GB  42 MB/s
     data_sent......................: 70 MB   581 kB/s
     http_req_blocked...............: avg=4.49µs   min=1.07µs  med=2.65µs   max=4.04ms   p(90)=4.04µs   p(95)=4.57µs   p(99.9)=46.54µs 
     http_req_connecting............: avg=1.63µs   min=0s      med=0s       max=3.99ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=102.57ms min=4.51ms  med=100.55ms max=301.66ms p(90)=138.58ms p(95)=149.58ms p(99.9)=193.89ms
       { expected_response:true }...: avg=102.57ms min=4.51ms  med=100.55ms max=301.66ms p(90)=138.58ms p(95)=149.58ms p(99.9)=193.89ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 58373
     http_req_receiving.............: avg=75.49µs  min=30.14µs med=69.52µs  max=65.46ms  p(90)=99.54µs  p(95)=111.79µs p(99.9)=429.81µs
     http_req_sending...............: avg=18.05µs  min=5.02µs  med=13.29µs  max=74.97ms  p(90)=18.84µs  p(95)=20.58µs  p(99.9)=518.39µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=102.47ms min=4.41ms  med=100.46ms max=294.31ms p(90)=138.49ms p(95)=149.49ms p(99.9)=193.55ms
     http_reqs......................: 58373   484.054416/s
     iteration_duration.............: avg=102.98ms min=14.12ms med=100.81ms max=315.97ms p(90)=138.85ms p(95)=149.85ms p(99.9)=197.89ms
     iterations.....................: 58273   483.225172/s
     success_rate...................: 100.00% ✓ 58273      ✗ 0    
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

     checks.........................: 100.00% ✓ 144762     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   481 kB/s
     http_req_blocked...............: avg=4.86µs   min=1.03µs  med=2.55µs   max=3.86ms   p(90)=3.91µs   p(95)=4.42µs   p(99.9)=563.98µs
     http_req_connecting............: avg=2.07µs   min=0s      med=0s       max=3.82ms   p(90)=0s       p(95)=0s       p(99.9)=506.45µs
     http_req_duration..............: avg=123.9ms  min=5.35ms  med=121.52ms max=330.46ms p(90)=162.6ms  p(95)=175.13ms p(99.9)=224.32ms
       { expected_response:true }...: avg=123.9ms  min=5.35ms  med=121.52ms max=330.46ms p(90)=162.6ms  p(95)=175.13ms p(99.9)=224.32ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48354
     http_req_receiving.............: avg=75.82µs  min=28.43µs med=68.97µs  max=78.26ms  p(90)=99.38µs  p(95)=112.62µs p(99.9)=505.76µs
     http_req_sending...............: avg=23.24µs  min=4.95µs  med=13.19µs  max=97.63ms  p(90)=18.28µs  p(95)=19.91µs  p(99.9)=430.27µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.8ms  min=5.29ms  med=121.43ms max=329.9ms  p(90)=162.48ms p(95)=175.03ms p(99.9)=223.61ms
     http_reqs......................: 48354   400.6428/s
     iteration_duration.............: avg=124.38ms min=22.15ms med=121.83ms max=338.58ms p(90)=162.88ms p(95)=175.41ms p(99.9)=227.12ms
     iterations.....................: 48254   399.814239/s
     success_rate...................: 100.00% ✓ 48254      ✗ 0    
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

     checks.........................: 100.00% ✓ 97362      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   324 kB/s
     http_req_blocked...............: avg=6.6µs    min=1.4µs   med=3.46µs   max=4.24ms   p(90)=4.84µs   p(95)=5.46µs   p(99.9)=1.28ms  
     http_req_connecting............: avg=2.87µs   min=0s      med=0s       max=4.2ms    p(90)=0s       p(95)=0s       p(99.9)=1.23ms  
     http_req_duration..............: avg=184.17ms min=5.64ms  med=168.56ms max=776.75ms p(90)=216.52ms p(95)=245.94ms p(99.9)=677.96ms
       { expected_response:true }...: avg=184.17ms min=5.64ms  med=168.56ms max=776.75ms p(90)=216.52ms p(95)=245.94ms p(99.9)=677.96ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32554
     http_req_receiving.............: avg=92.26µs  min=34.97µs med=86.72µs  max=24.81ms  p(90)=116.8µs  p(95)=128.8µs  p(99.9)=997.95µs
     http_req_sending...............: avg=31.86µs  min=6.05µs  med=17.05µs  max=89.93ms  p(90)=21.75µs  p(95)=23.65µs  p(99.9)=606.66µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.05ms min=5.49ms  med=168.45ms max=776.65ms p(90)=216.42ms p(95)=245.8ms  p(99.9)=677.86ms
     http_reqs......................: 32554   269.493647/s
     iteration_duration.............: avg=184.99ms min=54.53ms med=168.94ms max=776.99ms p(90)=216.9ms  p(95)=246.55ms p(99.9)=678.28ms
     iterations.....................: 32454   268.665811/s
     success_rate...................: 100.00% ✓ 32454      ✗ 0    
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

     checks.........................: 100.00% ✓ 97215      ✗ 0    
     data_received..................: 2.8 GB  24 MB/s
     data_sent......................: 39 MB   323 kB/s
     http_req_blocked...............: avg=6.51µs   min=1.22µs  med=3.39µs   max=4.22ms   p(90)=4.72µs   p(95)=5.27µs   p(99.9)=1.23ms  
     http_req_connecting............: avg=2.87µs   min=0s      med=0s       max=4.18ms   p(90)=0s       p(95)=0s       p(99.9)=1.2ms   
     http_req_duration..............: avg=184.44ms min=7.57ms  med=184.08ms max=457.2ms  p(90)=210.52ms p(95)=217.59ms p(99.9)=296.42ms
       { expected_response:true }...: avg=184.44ms min=7.57ms  med=184.08ms max=457.2ms  p(90)=210.52ms p(95)=217.59ms p(99.9)=296.42ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32505
     http_req_receiving.............: avg=90.11µs  min=34.12µs med=82.64µs  max=113.99ms p(90)=112.24µs p(95)=122.58µs p(99.9)=467.85µs
     http_req_sending...............: avg=39.67µs  min=5.7µs   med=16.44µs  max=111.62ms p(90)=20.79µs  p(95)=22.54µs  p(99.9)=526.79µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.31ms min=7.43ms  med=183.96ms max=456.97ms p(90)=210.41ms p(95)=217.47ms p(99.9)=296.32ms
     http_reqs......................: 32505   268.683578/s
     iteration_duration.............: avg=185.28ms min=21.24ms med=184.47ms max=465.63ms p(90)=210.8ms  p(95)=217.87ms p(99.9)=304.42ms
     iterations.....................: 32405   267.856987/s
     success_rate...................: 100.00% ✓ 32405      ✗ 0    
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

