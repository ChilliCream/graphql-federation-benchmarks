## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.10 | 5,152 | 5,170 | 5,118 | 0.4% | 384 MB | 76.2 KB |  |
| fusion-net-11 | 16.7.5 | 5,075 | 5,094 | 5,055 | 0.3% | 376 MB | 75.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.10 | 4,937 | 4,939 | 4,915 | 0.2% | 386 MB | 80.1 KB |  |
| fusion-aot-11 | 16.7.5 | 4,844 | 4,863 | 4,832 | 0.3% | 138 MB | 29.2 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.10 | 4,788 | 4,792 | 4,757 | 0.3% | 129 MB | 27.6 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,764 | 4,779 | 4,741 | 0.3% | 369 MB | 79.4 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.10 | 4,638 | 4,640 | 4,624 | 0.1% | 139 MB | 30.6 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,592 | 4,597 | 4,576 | 0.2% | 149 MB | 33.3 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,387 | 4,438 | 4,263 | 1.5% | 2,304 MB | 537.9 KB |  |
| hive-router | v0.3.10 | 3,082 | 3,087 | 3,079 | 0.1% | 95 MB | 31.6 KB |  |
| grafbase | 0.53.5 | 1,864 | 1,873 | 1,858 | 0.3% | 112 MB | 61.5 KB |  |
| caliban | 3.2.0 | 1,521 | 1,521 | 1,520 | 0.0% | 5,152 MB | 3,468.8 KB |  |
| cosmo | 0.365.2 | 1,477 | 1,478 | 1,476 | 0.1% | 165 MB | 114.6 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 549 | 550 | 549 | 0.1% | 2,756 MB | 5,140.7 KB |  |
| apollo-router | v2.19.0 | 528 | 529 | 527 | 0.2% | 173 MB | 335.2 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 430 | 430 | 429 | 0.1% | 198 MB | 471.0 KB |  |
| apollo-gateway | 2.14.4 | 274 | 274 | 273 | 0.2% | 2,168 MB | 8,100.8 KB |  |
| hive-gateway | 2.15.6 | 261 | 262 | 260 | 0.3% | 3,487 MB | 13,682.5 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1856217     ✗ 0     
     data_received..................: 54 GB   451 MB/s
     data_sent......................: 744 MB  6.2 MB/s
     http_req_blocked...............: avg=3.39µs  min=822ns    med=2.03µs max=50.91ms  p(90)=3.25µs  p(95)=3.89µs   p(99.9)=28.5µs 
     http_req_connecting............: avg=944ns   min=0s       med=0s     max=50.88ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.48ms  min=841.06µs med=8.63ms max=272.27ms p(90)=14.63ms p(95)=17.75ms  p(99.9)=29.78ms
       { expected_response:true }...: avg=9.48ms  min=841.06µs med=8.63ms max=272.27ms p(90)=14.63ms p(95)=17.75ms  p(99.9)=29.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 618839
     http_req_receiving.............: avg=95.04µs min=25.73µs  med=46.5µs max=156.27ms p(90)=87.91µs p(95)=195.66µs p(99.9)=6.19ms 
     http_req_sending...............: avg=43.33µs min=4.43µs   med=8.27µs max=157.27ms p(90)=14.18µs p(95)=101.52µs p(99.9)=5.04ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.35ms  min=784.95µs med=8.52ms max=252.95ms p(90)=14.4ms  p(95)=17.46ms  p(99.9)=29.31ms
     http_reqs......................: 618839  5152.064243/s
     iteration_duration.............: avg=9.68ms  min=1.13ms   med=8.81ms max=290.63ms p(90)=14.84ms p(95)=17.97ms  p(99.9)=30.07ms
     iterations.....................: 618739  5151.231706/s
     success_rate...................: 100.00% ✓ 618739      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1828674     ✗ 0     
     data_received..................: 53 GB   444 MB/s
     data_sent......................: 733 MB  6.1 MB/s
     http_req_blocked...............: avg=2.46µs  min=801ns    med=1.88µs  max=5.35ms   p(90)=2.99µs  p(95)=3.61µs   p(99.9)=27.27µs
     http_req_connecting............: avg=155ns   min=0s       med=0s      max=4.27ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.64ms  min=834.7µs  med=8.83ms  max=288.34ms p(90)=14.79ms p(95)=17.47ms  p(99.9)=29.47ms
       { expected_response:true }...: avg=9.64ms  min=834.7µs  med=8.83ms  max=288.34ms p(90)=14.79ms p(95)=17.47ms  p(99.9)=29.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 609658
     http_req_receiving.............: avg=89.34µs min=24.42µs  med=45.19µs max=260.99ms p(90)=87.3µs  p(95)=183.78µs p(99.9)=5.6ms  
     http_req_sending...............: avg=39.78µs min=4.24µs   med=7.94µs  max=122.31ms p(90)=14µs    p(95)=97.31µs  p(99.9)=4.43ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.51ms  min=768.14µs med=8.72ms  max=279.62ms p(90)=14.6ms  p(95)=17.23ms  p(99.9)=29.08ms
     http_reqs......................: 609658  5075.822697/s
     iteration_duration.............: avg=9.83ms  min=1.24ms   med=9.02ms  max=309.46ms p(90)=15ms    p(95)=17.68ms  p(99.9)=29.71ms
     iterations.....................: 609558  5074.990128/s
     success_rate...................: 100.00% ✓ 609558      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1778940     ✗ 0     
     data_received..................: 52 GB   432 MB/s
     data_sent......................: 713 MB  5.9 MB/s
     http_req_blocked...............: avg=2.47µs  min=781ns    med=1.9µs   max=6.14ms   p(90)=3.05µs  p(95)=3.7µs   p(99.9)=25.89µs
     http_req_connecting............: avg=165ns   min=0s       med=0s      max=4.06ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=9.9ms   min=1ms      med=9.16ms  max=285.74ms p(90)=14.91ms p(95)=17.64ms p(99.9)=29.76ms
       { expected_response:true }...: avg=9.9ms   min=1ms      med=9.16ms  max=285.74ms p(90)=14.91ms p(95)=17.64ms p(99.9)=29.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 593080
     http_req_receiving.............: avg=94.78µs min=25.38µs  med=47.45µs max=156.92ms p(90)=92.19µs p(95)=192.9µs p(99.9)=6.17ms 
     http_req_sending...............: avg=41.88µs min=4.2µs    med=8.03µs  max=202.5ms  p(90)=14.86µs p(95)=99.79µs p(99.9)=4.63ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=9.77ms  min=927.96µs med=9.05ms  max=285.22ms p(90)=14.7ms  p(95)=17.38ms p(99.9)=29.32ms
     http_reqs......................: 593080  4937.061734/s
     iteration_duration.............: avg=10.1ms  min=1.4ms    med=9.35ms  max=294.3ms  p(90)=15.11ms p(95)=17.86ms p(99.9)=30.03ms
     iterations.....................: 592980  4936.229289/s
     success_rate...................: 100.00% ✓ 592980      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1745508     ✗ 0     
     data_received..................: 51 GB   424 MB/s
     data_sent......................: 699 MB  5.8 MB/s
     http_req_blocked...............: avg=2.56µs  min=811ns    med=2.01µs  max=4.78ms   p(90)=3.19µs  p(95)=3.81µs   p(99.9)=27.01µs
     http_req_connecting............: avg=162ns   min=0s       med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.11ms min=912.95µs med=9.41ms  max=277.77ms p(90)=15.08ms p(95)=17.68ms  p(99.9)=28.95ms
       { expected_response:true }...: avg=10.11ms min=912.95µs med=9.41ms  max=277.77ms p(90)=15.08ms p(95)=17.68ms  p(99.9)=28.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 581936
     http_req_receiving.............: avg=86.76µs min=24.44µs  med=44.13µs max=188.03ms p(90)=89.5µs  p(95)=195.91µs p(99.9)=5.06ms 
     http_req_sending...............: avg=40.29µs min=4.18µs   med=8.11µs  max=127.28ms p(90)=14.76µs p(95)=104.08µs p(99.9)=4.04ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.98ms  min=840.12µs med=9.31ms  max=258.88ms p(90)=14.9ms  p(95)=17.44ms  p(99.9)=28.54ms
     http_reqs......................: 581936  4844.689492/s
     iteration_duration.............: avg=10.3ms  min=1.36ms   med=9.6ms   max=306.25ms p(90)=15.28ms p(95)=17.9ms   p(99.9)=29.24ms
     iterations.....................: 581836  4843.856979/s
     success_rate...................: 100.00% ✓ 581836      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1725144     ✗ 0     
     data_received..................: 50 GB   419 MB/s
     data_sent......................: 691 MB  5.8 MB/s
     http_req_blocked...............: avg=2.59µs  min=831ns    med=1.88µs  max=10.03ms  p(90)=2.96µs  p(95)=3.53µs   p(99.9)=28.44µs
     http_req_connecting............: avg=285ns   min=0s       med=0s      max=9.99ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.23ms min=928.17µs med=9.59ms  max=269.39ms p(90)=15.11ms p(95)=17.63ms  p(99.9)=28.77ms
       { expected_response:true }...: avg=10.23ms min=928.17µs med=9.59ms  max=269.39ms p(90)=15.11ms p(95)=17.63ms  p(99.9)=28.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 575148
     http_req_receiving.............: avg=90.28µs min=25.1µs   med=45.64µs max=113ms    p(90)=88.4µs  p(95)=198.63µs p(99.9)=5.34ms 
     http_req_sending...............: avg=39.23µs min=4.36µs   med=8.03µs  max=140.92ms p(90)=14.05µs p(95)=100.63µs p(99.9)=3.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.1ms  min=876.8µs  med=9.48ms  max=251.44ms p(90)=14.92ms p(95)=17.4ms   p(99.9)=28.47ms
     http_reqs......................: 575148  4788.125625/s
     iteration_duration.............: avg=10.42ms min=1.23ms   med=9.77ms  max=298.8ms  p(90)=15.31ms p(95)=17.84ms  p(99.9)=29.04ms
     iterations.....................: 575048  4787.293122/s
     success_rate...................: 100.00% ✓ 575048      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1716942     ✗ 0     
     data_received..................: 50 GB   417 MB/s
     data_sent......................: 688 MB  5.7 MB/s
     http_req_blocked...............: avg=3.02µs   min=822ns    med=2.43µs  max=5.14ms   p(90)=3.72µs  p(95)=4.45µs   p(99.9)=29.64µs
     http_req_connecting............: avg=165ns    min=0s       med=0s      max=4.23ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.26ms  min=983.29µs med=9.44ms  max=203.54ms p(90)=15.67ms p(95)=18.54ms  p(99.9)=31.79ms
       { expected_response:true }...: avg=10.26ms  min=983.29µs med=9.44ms  max=203.54ms p(90)=15.67ms p(95)=18.54ms  p(99.9)=31.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 572414
     http_req_receiving.............: avg=101.88µs min=25.39µs  med=49.59µs max=96.81ms  p(90)=97.23µs p(95)=207.03µs p(99.9)=6.46ms 
     http_req_sending...............: avg=44.78µs  min=4.4µs    med=8.97µs  max=82.89ms  p(90)=16.36µs p(95)=106.47µs p(99.9)=4.9ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.11ms  min=907.42µs med=9.32ms  max=196.79ms p(90)=15.45ms p(95)=18.27ms  p(99.9)=31.26ms
     http_reqs......................: 572414  4764.826053/s
     iteration_duration.............: avg=10.47ms  min=1.18ms   med=9.64ms  max=338.04ms p(90)=15.88ms p(95)=18.76ms  p(99.9)=32.1ms 
     iterations.....................: 572314  4763.993644/s
     success_rate...................: 100.00% ✓ 572314      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1671522     ✗ 0     
     data_received..................: 49 GB   406 MB/s
     data_sent......................: 670 MB  5.6 MB/s
     http_req_blocked...............: avg=2.84µs  min=791ns    med=1.94µs  max=7.79ms   p(90)=3.21µs  p(95)=3.89µs   p(99.9)=27.19µs
     http_req_connecting............: avg=455ns   min=0s       med=0s      max=7.77ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.55ms min=1.07ms   med=9.96ms  max=248.18ms p(90)=15.35ms p(95)=17.82ms  p(99.9)=29.38ms
       { expected_response:true }...: avg=10.55ms min=1.07ms   med=9.96ms  max=248.18ms p(90)=15.35ms p(95)=17.82ms  p(99.9)=29.38ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 557274
     http_req_receiving.............: avg=93.24µs min=23.42µs  med=45.53µs max=21.3ms   p(90)=93.68µs p(95)=202.43µs p(99.9)=5.81ms 
     http_req_sending...............: avg=41.4µs  min=4.32µs   med=8.23µs  max=217.6ms  p(90)=15.78µs p(95)=103.9µs  p(99.9)=4.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.42ms min=992.99µs med=9.85ms  max=233.67ms p(90)=15.15ms p(95)=17.57ms  p(99.9)=29ms   
     http_reqs......................: 557274  4638.459932/s
     iteration_duration.............: avg=10.75ms min=1.57ms   med=10.15ms max=310ms    p(90)=15.55ms p(95)=18.03ms  p(99.9)=29.74ms
     iterations.....................: 557174  4637.627584/s
     success_rate...................: 100.00% ✓ 557174      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1654860     ✗ 0     
     data_received..................: 48 GB   402 MB/s
     data_sent......................: 663 MB  5.5 MB/s
     http_req_blocked...............: avg=2.56µs  min=821ns   med=1.98µs  max=5.07ms   p(90)=3.23µs  p(95)=3.93µs   p(99.9)=26.27µs
     http_req_connecting............: avg=157ns   min=0s      med=0s      max=3.52ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.66ms min=1.02ms  med=10.03ms max=286.29ms p(90)=15.65ms p(95)=18.16ms  p(99.9)=30.27ms
       { expected_response:true }...: avg=10.66ms min=1.02ms  med=10.03ms max=286.29ms p(90)=15.65ms p(95)=18.16ms  p(99.9)=30.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 551720
     http_req_receiving.............: avg=97.49µs min=24.95µs med=47.11µs max=154.33ms p(90)=95.35µs p(95)=202.11µs p(99.9)=6.07ms 
     http_req_sending...............: avg=41.82µs min=4.62µs  med=8.38µs  max=176.46ms p(90)=15.9µs  p(95)=103.53µs p(99.9)=4.29ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.52ms min=980.7µs med=9.91ms  max=267.94ms p(90)=15.45ms p(95)=17.92ms  p(99.9)=29.79ms
     http_reqs......................: 551720  4592.474958/s
     iteration_duration.............: avg=10.86ms min=1.69ms  med=10.22ms max=296.84ms p(90)=15.86ms p(95)=18.38ms  p(99.9)=30.56ms
     iterations.....................: 551620  4591.642565/s
     success_rate...................: 100.00% ✓ 551620      ✗ 0     
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

     checks.........................: 100.00% ✓ 1580724     ✗ 0     
     data_received..................: 46 GB   384 MB/s
     data_sent......................: 633 MB  5.3 MB/s
     http_req_blocked...............: avg=2.65µs  min=832ns    med=2.02µs  max=7.31ms   p(90)=3.2µs   p(95)=3.79µs   p(99.9)=28.29µs
     http_req_connecting............: avg=251ns   min=0s       med=0s      max=7.26ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.18ms min=761.36µs med=10.92ms max=291.15ms p(90)=16.64ms p(95)=18.81ms  p(99.9)=29.62ms
       { expected_response:true }...: avg=11.18ms min=761.36µs med=10.92ms max=291.15ms p(90)=16.64ms p(95)=18.81ms  p(99.9)=29.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 527008
     http_req_receiving.............: avg=85.72µs min=24.49µs  med=46.84µs max=170.67ms p(90)=90.68µs p(95)=203.43µs p(99.9)=4.54ms 
     http_req_sending...............: avg=38.47µs min=4.48µs   med=8.47µs  max=112.51ms p(90)=14.61µs p(95)=108.26µs p(99.9)=3.32ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.06ms min=714.05µs med=10.81ms max=289.13ms p(90)=16.48ms p(95)=18.61ms  p(99.9)=29.34ms
     http_reqs......................: 527008  4387.736123/s
     iteration_duration.............: avg=11.37ms min=1.31ms   med=11.1ms  max=302.2ms  p(90)=16.83ms p(95)=19.02ms  p(99.9)=29.83ms
     iterations.....................: 526908  4386.903548/s
     success_rate...................: 100.00% ✓ 526908      ✗ 0     
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

     checks.........................: 100.00% ✓ 1110780     ✗ 0     
     data_received..................: 32 GB   270 MB/s
     data_sent......................: 445 MB  3.7 MB/s
     http_req_blocked...............: avg=2.81µs  min=842ns   med=2.22µs  max=4.01ms   p(90)=3.72µs  p(95)=4.47µs   p(99.9)=34.75µs
     http_req_connecting............: avg=242ns   min=0s      med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=15.99ms min=1.26ms  med=15.94ms max=282.71ms p(90)=21.41ms p(95)=22.91ms  p(99.9)=30.34ms
       { expected_response:true }...: avg=15.99ms min=1.26ms  med=15.94ms max=282.71ms p(90)=21.41ms p(95)=22.91ms  p(99.9)=30.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 370360
     http_req_receiving.............: avg=82.61µs min=25.12µs med=52.19µs max=243.34ms p(90)=95.56µs p(95)=177.03µs p(99.9)=1.31ms 
     http_req_sending...............: avg=33.7µs  min=4.55µs  med=9.54µs  max=103.9ms  p(90)=18.02µs p(95)=107.53µs p(99.9)=1.44ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=15.88ms min=1.18ms  med=15.84ms max=282.19ms p(90)=21.3ms  p(95)=22.8ms   p(99.9)=30.17ms
     http_reqs......................: 370360  3082.015561/s
     iteration_duration.............: avg=16.19ms min=3.31ms  med=16.14ms max=303.4ms  p(90)=21.6ms  p(95)=23.1ms   p(99.9)=30.53ms
     iterations.....................: 370260  3081.183394/s
     success_rate...................: 100.00% ✓ 370260      ✗ 0     
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

     checks.........................: 100.00% ✓ 672261      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 269 MB  2.2 MB/s
     http_req_blocked...............: avg=3.29µs  min=861ns   med=2.34µs  max=3.91ms   p(90)=4.52µs  p(95)=5.53µs   p(99.9)=38.4µs 
     http_req_connecting............: avg=433ns   min=0s      med=0s      max=3.86ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.52ms min=1.93ms  med=25.94ms max=299.97ms p(90)=34.42ms p(95)=37.2ms   p(99.9)=51.36ms
       { expected_response:true }...: avg=26.52ms min=1.93ms  med=25.94ms max=299.97ms p(90)=34.42ms p(95)=37.2ms   p(99.9)=51.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 224187
     http_req_receiving.............: avg=86.56µs min=29.04µs med=58.6µs  max=120.4ms  p(90)=119.4µs p(95)=188.14µs p(99.9)=1.44ms 
     http_req_sending...............: avg=34.01µs min=4.8µs   med=10.1µs  max=101.82ms p(90)=22.74µs p(95)=102.7µs  p(99.9)=1.51ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.4ms  min=1.86ms  med=25.82ms max=299.66ms p(90)=34.3ms  p(95)=37.07ms  p(99.9)=51ms   
     http_reqs......................: 224187  1864.165247/s
     iteration_duration.............: avg=26.76ms min=8.12ms  med=26.16ms max=311ms    p(90)=34.64ms p(95)=37.42ms  p(99.9)=51.67ms
     iterations.....................: 224087  1863.333724/s
     success_rate...................: 100.00% ✓ 224087      ✗ 0     
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

     checks.........................: 100.00% ✓ 548901      ✗ 0     
     data_received..................: 16 GB   133 MB/s
     data_sent......................: 220 MB  1.8 MB/s
     http_req_blocked...............: avg=3.36µs  min=921ns   med=2.49µs  max=3.96ms   p(90)=4.29µs  p(95)=5.04µs   p(99.9)=34.44µs 
     http_req_connecting............: avg=523ns   min=0s      med=0s      max=3.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.54ms min=2.08ms  med=31.68ms max=300.67ms p(90)=46.06ms p(95)=50.75ms  p(99.9)=76.43ms 
       { expected_response:true }...: avg=32.54ms min=2.08ms  med=31.68ms max=300.67ms p(90)=46.06ms p(95)=50.75ms  p(99.9)=76.43ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 183067
     http_req_receiving.............: avg=71.73µs min=25.33µs med=59.13µs max=153.79ms p(90)=97.97µs p(95)=114.55µs p(99.9)=907.11µs
     http_req_sending...............: avg=23.31µs min=4.76µs  med=11.76µs max=181.81ms p(90)=19.59µs p(95)=23.26µs  p(99.9)=757.63µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.45ms min=2.02ms  med=31.59ms max=300.11ms p(90)=45.97ms p(95)=50.66ms  p(99.9)=76.18ms 
     http_reqs......................: 183067  1521.753736/s
     iteration_duration.............: avg=32.78ms min=5.17ms  med=31.9ms  max=311.04ms p(90)=46.27ms p(95)=50.97ms  p(99.9)=76.85ms 
     iterations.....................: 182967  1520.922481/s
     success_rate...................: 100.00% ✓ 182967      ✗ 0     
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

     checks.........................: 100.00% ✓ 532716      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 214 MB  1.8 MB/s
     http_req_blocked...............: avg=6.6µs   min=951ns  med=2.07µs  max=46.03ms  p(90)=3.49µs  p(95)=4.15µs   p(99.9)=28.89µs 
     http_req_connecting............: avg=4.2µs   min=0s     med=0s      max=45.86ms  p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.56ms min=2.07ms med=32.68ms max=262.51ms p(90)=48.48ms p(95)=53.51ms  p(99.9)=77.58ms 
       { expected_response:true }...: avg=33.56ms min=2.07ms med=32.68ms max=262.51ms p(90)=48.48ms p(95)=53.51ms  p(99.9)=77.58ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 177672
     http_req_receiving.............: avg=66.89µs min=25.9µs med=56.63µs max=62.32ms  p(90)=90.81µs p(95)=104.89µs p(99.9)=669.52µs
     http_req_sending...............: avg=25.84µs min=4.69µs med=9.91µs  max=107.43ms p(90)=15.93µs p(95)=19.6µs   p(99.9)=763.73µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.46ms min=2.01ms med=32.6ms  max=233.3ms  p(90)=48.39ms p(95)=53.42ms  p(99.9)=77.28ms 
     http_reqs......................: 177672  1477.254466/s
     iteration_duration.............: avg=33.78ms min=3.18ms med=32.88ms max=291ms    p(90)=48.68ms p(95)=53.71ms  p(99.9)=77.98ms 
     iterations.....................: 177572  1476.423015/s
     success_rate...................: 100.00% ✓ 177572      ✗ 0     
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

     checks.........................: 100.00% ✓ 198414     ✗ 0    
     data_received..................: 5.8 GB  48 MB/s
     data_sent......................: 80 MB   660 kB/s
     http_req_blocked...............: avg=5.13µs  min=1.15µs  med=3.05µs  max=6.32ms   p(90)=4.51µs   p(95)=5.15µs   p(99.9)=42.24µs 
     http_req_connecting............: avg=1.78µs  min=0s      med=0s      max=6.21ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=90.36ms min=3.81ms  med=87.67ms max=296.85ms p(90)=110.07ms p(95)=121.68ms p(99.9)=214.53ms
       { expected_response:true }...: avg=90.36ms min=3.81ms  med=87.67ms max=296.85ms p(90)=110.07ms p(95)=121.68ms p(99.9)=214.53ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 66238
     http_req_receiving.............: avg=80.04µs min=29.52µs med=71.28µs max=88.94ms  p(90)=104.43µs p(95)=116.58µs p(99.9)=562.04µs
     http_req_sending...............: avg=19.95µs min=5.13µs  med=13.91µs max=60.6ms   p(90)=19.92µs  p(95)=22µs     p(99.9)=593.78µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=90.26ms min=3.74ms  med=87.57ms max=295.98ms p(90)=109.95ms p(95)=121.55ms p(99.9)=213.86ms
     http_reqs......................: 66238   549.502722/s
     iteration_duration.............: avg=90.73ms min=28.72ms med=87.93ms max=307.3ms  p(90)=110.33ms p(95)=121.99ms p(99.9)=216.62ms
     iterations.....................: 66138   548.673134/s
     success_rate...................: 100.00% ✓ 66138      ✗ 0    
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

     checks.........................: 100.00% ✓ 190896     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   635 kB/s
     http_req_blocked...............: avg=4.99µs  min=1.19µs  med=3.25µs  max=3.64ms   p(90)=4.75µs   p(95)=5.34µs   p(99.9)=51.52µs 
     http_req_connecting............: avg=1.51µs  min=0s      med=0s      max=3.6ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.9ms  min=4.45ms  med=92ms    max=309.8ms  p(90)=126.64ms p(95)=136.69ms p(99.9)=179.84ms
       { expected_response:true }...: avg=93.9ms  min=4.45ms  med=92ms    max=309.8ms  p(90)=126.64ms p(95)=136.69ms p(99.9)=179.84ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63732
     http_req_receiving.............: avg=84.77µs min=28.67µs med=72.08µs max=136.85ms p(90)=102.62µs p(95)=115.09µs p(99.9)=489.24µs
     http_req_sending...............: avg=22.84µs min=5.61µs  med=14.75µs max=101.02ms p(90)=20.2µs   p(95)=22.19µs  p(99.9)=550.48µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.8ms  min=4.32ms  med=91.89ms max=296.08ms p(90)=126.54ms p(95)=136.58ms p(99.9)=179.05ms
     http_reqs......................: 63732   528.602138/s
     iteration_duration.............: avg=94.3ms  min=14.49ms med=92.28ms max=330.36ms p(90)=126.91ms p(95)=136.95ms p(99.9)=181.24ms
     iterations.....................: 63632   527.772724/s
     success_rate...................: 100.00% ✓ 63632      ✗ 0    
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

     checks.........................: 100.00% ✓ 155718     ✗ 0    
     data_received..................: 4.5 GB  38 MB/s
     data_sent......................: 62 MB   518 kB/s
     http_req_blocked...............: avg=6.06µs   min=1.09µs  med=2.97µs   max=10.4ms   p(90)=4.3µs    p(95)=4.81µs   p(99.9)=73.7µs  
     http_req_connecting............: avg=2.82µs   min=0s      med=0s       max=10.37ms  p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=115.15ms min=5.27ms  med=112.8ms  max=307.25ms p(90)=151.02ms p(95)=162.83ms p(99.9)=211.33ms
       { expected_response:true }...: avg=115.15ms min=5.27ms  med=112.8ms  max=307.25ms p(90)=151.02ms p(95)=162.83ms p(99.9)=211.33ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 52006
     http_req_receiving.............: avg=78.18µs  min=29.51µs med=75.28µs  max=3.16ms   p(90)=104.64µs p(95)=116.93µs p(99.9)=479.7µs 
     http_req_sending...............: avg=21.34µs  min=4.89µs  med=14.98µs  max=83.05ms  p(90)=19.9µs   p(95)=21.67µs  p(99.9)=540.11µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=115.05ms min=5.17ms  med=112.71ms max=306.68ms p(90)=150.92ms p(95)=162.74ms p(99.9)=211.01ms
     http_reqs......................: 52006   430.960548/s
     iteration_duration.............: avg=115.61ms min=22.07ms med=113.07ms max=326.18ms p(90)=151.3ms  p(95)=163.11ms p(99.9)=212.1ms 
     iterations.....................: 51906   430.131873/s
     success_rate...................: 100.00% ✓ 51906      ✗ 0    
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

     checks.........................: 100.00% ✓ 99378      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   330 kB/s
     http_req_blocked...............: avg=6.74µs   min=1.34µs  med=3.54µs   max=4.07ms   p(90)=4.94µs   p(95)=5.51µs   p(99.9)=1.37ms  
     http_req_connecting............: avg=2.95µs   min=0s      med=0s       max=4.03ms   p(90)=0s       p(95)=0s       p(99.9)=1.34ms  
     http_req_duration..............: avg=180.39ms min=7.51ms  med=181.38ms max=383.4ms  p(90)=202.84ms p(95)=208.04ms p(99.9)=269.03ms
       { expected_response:true }...: avg=180.39ms min=7.51ms  med=181.38ms max=383.4ms  p(90)=202.84ms p(95)=208.04ms p(99.9)=269.03ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33226
     http_req_receiving.............: avg=95.6µs   min=35.65µs med=88.28µs  max=121.68ms p(90)=117.69µs p(95)=128.72µs p(99.9)=540.69µs
     http_req_sending...............: avg=21.72µs  min=5.94µs  med=17.34µs  max=21.21ms  p(90)=21.82µs  p(95)=23.61µs  p(99.9)=491.14µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.28ms min=7.42ms  med=181.27ms max=382.98ms p(90)=202.71ms p(95)=207.93ms p(99.9)=268.94ms
     http_reqs......................: 33226   274.663551/s
     iteration_duration.............: avg=181.22ms min=34.62ms med=181.82ms max=401.16ms p(90)=203.15ms p(95)=208.34ms p(99.9)=273.25ms
     iterations.....................: 33126   273.836899/s
     success_rate...................: 100.00% ✓ 33126      ✗ 0    
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

     checks.........................: 100.00% ✓ 94518      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   314 kB/s
     http_req_blocked...............: avg=11.4µs   min=1.05µs  med=3µs      max=7.29ms   p(90)=4.3µs    p(95)=4.8µs    p(99.9)=4.76ms  
     http_req_connecting............: avg=8.13µs   min=0s      med=0s       max=7.27ms   p(90)=0s       p(95)=0s       p(99.9)=4.73ms  
     http_req_duration..............: avg=189.71ms min=6.05ms  med=173.46ms max=802.68ms p(90)=217.54ms p(95)=251.06ms p(99.9)=698.13ms
       { expected_response:true }...: avg=189.71ms min=6.05ms  med=173.46ms max=802.68ms p(90)=217.54ms p(95)=251.06ms p(99.9)=698.13ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31606
     http_req_receiving.............: avg=85.88µs  min=30.55µs med=82.34µs  max=25.06ms  p(90)=110.47µs p(95)=121.46µs p(99.9)=652.64µs
     http_req_sending...............: avg=26.69µs  min=5.17µs  med=15.66µs  max=62.96ms  p(90)=19.47µs  p(95)=21.03µs  p(99.9)=1.62ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=189.59ms min=5.92ms  med=173.34ms max=802.58ms p(90)=217.46ms p(95)=250.96ms p(99.9)=698.06ms
     http_reqs......................: 31606   261.515888/s
     iteration_duration.............: avg=190.54ms min=39.68ms med=173.78ms max=802.89ms p(90)=217.87ms p(95)=252.23ms p(99.9)=698.42ms
     iterations.....................: 31506   260.688463/s
     success_rate...................: 100.00% ✓ 31506      ✗ 0    
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

