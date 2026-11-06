## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 5,122 | 5,145 | 5,069 | 0.7% | 393 MB | 78.6 KB |  |
| fusion-net-11 | 16.7.3 | 5,012 | 5,057 | 4,984 | 0.7% | 373 MB | 76.3 KB |  |
| fusion-aot-11 | 16.7.3 | 4,892 | 4,904 | 4,886 | 0.1% | 139 MB | 29.2 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,828 | 4,852 | 4,800 | 0.5% | 400 MB | 84.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,753 | 4,796 | 4,717 | 0.6% | 393 MB | 84.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,681 | 4,683 | 4,677 | 0.0% | 122 MB | 26.6 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,623 | 4,639 | 4,609 | 0.3% | 126 MB | 27.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,595 | 4,612 | 4,584 | 0.2% | 128 MB | 28.6 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,204 | 4,356 | 4,092 | 2.5% | 2,304 MB | 561.3 KB |  |
| hive-router | v0.3.10 | 3,045 | 3,066 | 3,030 | 0.5% | 92 MB | 30.8 KB |  |
| grafbase | 0.53.5 | 1,836 | 1,855 | 1,823 | 0.8% | 104 MB | 57.8 KB |  |
| cosmo | 0.365.2 | 1,503 | 1,504 | 1,500 | 0.1% | 167 MB | 113.5 KB |  |
| caliban | 3.2.0 | 1,429 | 1,430 | 1,426 | 0.1% | 4,390 MB | 3,145.5 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 550 | 551 | 548 | 0.2% | 2,746 MB | 5,111.8 KB |  |
| apollo-router | v2.19.0 | 530 | 531 | 529 | 0.2% | 172 MB | 332.1 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 430 | 430 | 429 | 0.1% | 199 MB | 472.9 KB |  |
| apollo-gateway | 2.14.4 | 273 | 273 | 272 | 0.2% | 2,171 MB | 8,142.9 KB |  |
| hive-gateway | 2.15.6 | 265 | 266 | 263 | 0.4% | 3,700 MB | 14,297.7 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1845390     ✗ 0     
     data_received..................: 54 GB   448 MB/s
     data_sent......................: 740 MB  6.2 MB/s
     http_req_blocked...............: avg=2.62µs  min=792ns    med=1.93µs max=13.84ms  p(90)=3.09µs  p(95)=3.75µs  p(99.9)=27.1µs 
     http_req_connecting............: avg=162ns   min=0s       med=0s     max=3.93ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=9.54ms  min=796.49µs med=8.69ms max=276.59ms p(90)=14.76ms p(95)=17.61ms p(99.9)=29.94ms
       { expected_response:true }...: avg=9.54ms  min=796.49µs med=8.69ms max=276.59ms p(90)=14.76ms p(95)=17.61ms p(99.9)=29.94ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 615230
     http_req_receiving.............: avg=92.56µs min=24.64µs  med=45.2µs max=179.15ms p(90)=89.3µs  p(95)=187.3µs p(99.9)=6.17ms 
     http_req_sending...............: avg=41.45µs min=4.5µs    med=8.11µs max=154.16ms p(90)=14.36µs p(95)=98.1µs  p(99.9)=4.7ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=9.41ms  min=745.86µs med=8.58ms max=276.32ms p(90)=14.55ms p(95)=17.35ms p(99.9)=29.43ms
     http_reqs......................: 615230  5122.173662/s
     iteration_duration.............: avg=9.74ms  min=1.14ms   med=8.88ms max=289.72ms p(90)=14.97ms p(95)=17.83ms p(99.9)=30.22ms
     iterations.....................: 615130  5121.341099/s
     success_rate...................: 100.00% ✓ 615130      ✗ 0     
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

     checks.........................: 100.00% ✓ 1806045     ✗ 0     
     data_received..................: 53 GB   439 MB/s
     data_sent......................: 724 MB  6.0 MB/s
     http_req_blocked...............: avg=3.86µs  min=932ns    med=2.43µs  max=68.42ms  p(90)=3.76µs  p(95)=4.45µs   p(99.9)=33.57µs
     http_req_connecting............: avg=933ns   min=0s       med=0s      max=68.31ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.75ms  min=804.09µs med=8.82ms  max=225.64ms p(90)=15.26ms p(95)=18.35ms  p(99.9)=31.29ms
       { expected_response:true }...: avg=9.75ms  min=804.09µs med=8.82ms  max=225.64ms p(90)=15.26ms p(95)=18.35ms  p(99.9)=31.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 602115
     http_req_receiving.............: avg=98.08µs min=23.89µs  med=47.32µs max=54.05ms  p(90)=92.73µs p(95)=201.99µs p(99.9)=6.62ms 
     http_req_sending...............: avg=47.79µs min=4.57µs   med=8.92µs  max=144.7ms  p(90)=15.7µs  p(95)=107.41µs p(99.9)=5.11ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.6ms   min=762.22µs med=8.7ms   max=212.95ms p(90)=15.02ms p(95)=18.07ms  p(99.9)=30.8ms 
     http_reqs......................: 602115  5012.961761/s
     iteration_duration.............: avg=9.95ms  min=1.23ms   med=9.01ms  max=290.79ms p(90)=15.47ms p(95)=18.58ms  p(99.9)=31.59ms
     iterations.....................: 602015  5012.129202/s
     success_rate...................: 100.00% ✓ 602015      ✗ 0     
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

     checks.........................: 100.00% ✓ 1762758     ✗ 0     
     data_received..................: 51 GB   428 MB/s
     data_sent......................: 706 MB  5.9 MB/s
     http_req_blocked...............: avg=2.37µs  min=802ns    med=1.8µs   max=6.78ms   p(90)=2.92µs  p(95)=3.48µs   p(99.9)=25.9µs 
     http_req_connecting............: avg=152ns   min=0s       med=0s      max=3.53ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.01ms min=926.72µs med=9.33ms  max=266.94ms p(90)=14.85ms p(95)=17.36ms  p(99.9)=28.38ms
       { expected_response:true }...: avg=10.01ms min=926.72µs med=9.33ms  max=266.94ms p(90)=14.85ms p(95)=17.36ms  p(99.9)=28.38ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 587686
     http_req_receiving.............: avg=85.52µs min=22.17µs  med=43.43µs max=211.32ms p(90)=87.99µs p(95)=195.23µs p(99.9)=5.09ms 
     http_req_sending...............: avg=38.68µs min=4.24µs   med=7.79µs  max=201.56ms p(90)=13.98µs p(95)=100.8µs  p(99.9)=3.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.89ms  min=850.13µs med=9.23ms  max=266.39ms p(90)=14.66ms p(95)=17.12ms  p(99.9)=27.97ms
     http_reqs......................: 587686  4892.491805/s
     iteration_duration.............: avg=10.2ms  min=1.1ms    med=9.52ms  max=278.89ms p(90)=15.04ms p(95)=17.57ms  p(99.9)=28.67ms
     iterations.....................: 587586  4891.659304/s
     success_rate...................: 100.00% ✓ 587586      ✗ 0     
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

     checks.........................: 100.00% ✓ 1739997     ✗ 0     
     data_received..................: 51 GB   423 MB/s
     data_sent......................: 697 MB  5.8 MB/s
     http_req_blocked...............: avg=3µs      min=922ns    med=2.37µs  max=7.14ms   p(90)=3.67µs  p(95)=4.41µs   p(99.9)=31.81µs
     http_req_connecting............: avg=160ns    min=0s       med=0s      max=3.77ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.12ms  min=978.81µs med=9.28ms  max=272.81ms p(90)=15.56ms p(95)=18.48ms  p(99.9)=31.63ms
       { expected_response:true }...: avg=10.12ms  min=978.81µs med=9.28ms  max=272.81ms p(90)=15.56ms p(95)=18.48ms  p(99.9)=31.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 580099
     http_req_receiving.............: avg=101.61µs min=25.57µs  med=48.74µs max=183.87ms p(90)=97.47µs p(95)=204.62µs p(99.9)=6.55ms 
     http_req_sending...............: avg=44.78µs  min=4.44µs   med=8.51µs  max=71.71ms  p(90)=15.73µs p(95)=106.39µs p(99.9)=5.03ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.98ms   min=899.4µs  med=9.16ms  max=255.63ms p(90)=15.34ms p(95)=18.21ms  p(99.9)=31.17ms
     http_reqs......................: 580099  4828.908453/s
     iteration_duration.............: avg=10.33ms  min=1.36ms   med=9.47ms  max=297.03ms p(90)=15.78ms p(95)=18.7ms   p(99.9)=31.86ms
     iterations.....................: 579999  4828.076025/s
     success_rate...................: 100.00% ✓ 579999      ✗ 0     
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

     checks.........................: 100.00% ✓ 1712970     ✗ 0     
     data_received..................: 50 GB   416 MB/s
     data_sent......................: 686 MB  5.7 MB/s
     http_req_blocked...............: avg=3.11µs   min=952ns    med=2.48µs  max=11.05ms  p(90)=3.81µs  p(95)=4.54µs   p(99.9)=32.8µs 
     http_req_connecting............: avg=155ns    min=0s       med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.28ms  min=991µs    med=9.42ms  max=288.59ms p(90)=15.82ms p(95)=18.78ms  p(99.9)=31.74ms
       { expected_response:true }...: avg=10.28ms  min=991µs    med=9.42ms  max=288.59ms p(90)=15.82ms p(95)=18.78ms  p(99.9)=31.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 571090
     http_req_receiving.............: avg=105.17µs min=26.56µs  med=50.04µs max=57.88ms  p(90)=98.47µs p(95)=207.57µs p(99.9)=7.13ms 
     http_req_sending...............: avg=45.2µs   min=4.53µs   med=8.94µs  max=95.12ms  p(90)=16.22µs p(95)=107.13µs p(99.9)=5.03ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.13ms  min=938.48µs med=9.3ms   max=272.12ms p(90)=15.59ms p(95)=18.49ms  p(99.9)=31.21ms
     http_reqs......................: 571090  4753.68359/s
     iteration_duration.............: avg=10.49ms  min=1.23ms   med=9.62ms  max=301.89ms p(90)=16.04ms p(95)=19.01ms  p(99.9)=32.02ms
     iterations.....................: 570990  4752.851202/s
     success_rate...................: 100.00% ✓ 570990      ✗ 0     
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

     checks.........................: 100.00% ✓ 1686684     ✗ 0     
     data_received..................: 49 GB   410 MB/s
     data_sent......................: 676 MB  5.6 MB/s
     http_req_blocked...............: avg=2.42µs  min=791ns    med=1.9µs   max=4.12ms   p(90)=2.99µs  p(95)=3.56µs   p(99.9)=25.44µs
     http_req_connecting............: avg=156ns   min=0s       med=0s      max=3.37ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.47ms min=888.68µs med=9.84ms  max=268.91ms p(90)=15.33ms p(95)=17.73ms  p(99.9)=28.95ms
       { expected_response:true }...: avg=10.47ms min=888.68µs med=9.84ms  max=268.91ms p(90)=15.33ms p(95)=17.73ms  p(99.9)=28.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 562328
     http_req_receiving.............: avg=93.4µs  min=24.99µs  med=46.97µs max=153.09ms p(90)=92.44µs p(95)=205.21µs p(99.9)=5.54ms 
     http_req_sending...............: avg=39.45µs min=4.21µs   med=8.2µs   max=153.6ms  p(90)=14.58µs p(95)=102.61µs p(99.9)=3.77ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.33ms min=839.73µs med=9.73ms  max=268.24ms p(90)=15.14ms p(95)=17.5ms   p(99.9)=28.55ms
     http_reqs......................: 562328  4681.170684/s
     iteration_duration.............: avg=10.66ms min=1.58ms   med=10.03ms max=285.49ms p(90)=15.53ms p(95)=17.94ms  p(99.9)=29.19ms
     iterations.....................: 562228  4680.338221/s
     success_rate...................: 100.00% ✓ 562228      ✗ 0     
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

     checks.........................: 100.00% ✓ 1666197     ✗ 0     
     data_received..................: 49 GB   405 MB/s
     data_sent......................: 668 MB  5.6 MB/s
     http_req_blocked...............: avg=3.02µs  min=872ns   med=2.32µs  max=13.67ms  p(90)=3.69µs  p(95)=4.41µs   p(99.9)=34.18µs
     http_req_connecting............: avg=232ns   min=0s      med=0s      max=13.53ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.58ms min=1.08ms  med=9.87ms  max=254.48ms p(90)=15.74ms p(95)=18.51ms  p(99.9)=30.9ms 
       { expected_response:true }...: avg=10.58ms min=1.08ms  med=9.87ms  max=254.48ms p(90)=15.74ms p(95)=18.51ms  p(99.9)=30.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 555499
     http_req_receiving.............: avg=98.78µs min=26.06µs med=47.35µs max=137.37ms p(90)=98.8µs  p(95)=213.23µs p(99.9)=6.11ms 
     http_req_sending...............: avg=47.15µs min=4.53µs  med=8.77µs  max=168.56ms p(90)=17.05µs p(95)=110.37µs p(99.9)=4.97ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.44ms min=1.01ms  med=9.76ms  max=254.23ms p(90)=15.52ms p(95)=18.22ms  p(99.9)=30.42ms
     http_reqs......................: 555499  4623.730648/s
     iteration_duration.............: avg=10.79ms min=1.57ms  med=10.07ms max=283.32ms p(90)=15.95ms p(95)=18.73ms  p(99.9)=31.16ms
     iterations.....................: 555399  4622.898292/s
     success_rate...................: 100.00% ✓ 555399      ✗ 0     
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

     checks.........................: 100.00% ✓ 1656063     ✗ 0     
     data_received..................: 48 GB   402 MB/s
     data_sent......................: 664 MB  5.5 MB/s
     http_req_blocked...............: avg=2.63µs  min=821ns    med=1.99µs  max=7.28ms   p(90)=3.32µs  p(95)=4.08µs   p(99.9)=28.81µs
     http_req_connecting............: avg=175ns   min=0s       med=0s      max=3.72ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.65ms min=1.03ms   med=9.99ms  max=265.26ms p(90)=15.66ms p(95)=18.24ms  p(99.9)=30.09ms
       { expected_response:true }...: avg=10.65ms min=1.03ms   med=9.99ms  max=265.26ms p(90)=15.66ms p(95)=18.24ms  p(99.9)=30.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 552121
     http_req_receiving.............: avg=99.29µs min=24.54µs  med=46.39µs max=122.29ms p(90)=96.61µs p(95)=203.41µs p(99.9)=6.71ms 
     http_req_sending...............: avg=43.49µs min=4.28µs   med=8.2µs   max=226.58ms p(90)=16.29µs p(95)=105.27µs p(99.9)=4.53ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.51ms min=993.09µs med=9.88ms  max=265.03ms p(90)=15.44ms p(95)=17.98ms  p(99.9)=29.57ms
     http_reqs......................: 552121  4595.534919/s
     iteration_duration.............: avg=10.85ms min=1.43ms   med=10.19ms max=289.88ms p(90)=15.87ms p(95)=18.46ms  p(99.9)=30.35ms
     iterations.....................: 552021  4594.702577/s
     success_rate...................: 100.00% ✓ 552021      ✗ 0     
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

     checks.........................: 100.00% ✓ 1514565     ✗ 0     
     data_received..................: 44 GB   367 MB/s
     data_sent......................: 607 MB  5.1 MB/s
     http_req_blocked...............: avg=3.16µs  min=962ns    med=2.47µs  max=4.57ms   p(90)=3.84µs  p(95)=4.5µs    p(99.9)=36.74µs
     http_req_connecting............: avg=235ns   min=0s       med=0s      max=4.16ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.68ms min=766.59µs med=11.37ms max=290.86ms p(90)=17.01ms p(95)=19.26ms  p(99.9)=29.84ms
       { expected_response:true }...: avg=11.68ms min=766.59µs med=11.37ms max=290.86ms p(90)=17.01ms p(95)=19.26ms  p(99.9)=29.84ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 504955
     http_req_receiving.............: avg=87.64µs min=24.92µs  med=48.78µs max=105.94ms p(90)=94.43µs p(95)=214.59µs p(99.9)=4.33ms 
     http_req_sending...............: avg=40.69µs min=4.62µs   med=9.25µs  max=202.23ms p(90)=16.1µs  p(95)=116.43µs p(99.9)=3.27ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.55ms min=725µs    med=11.26ms max=289.41ms p(90)=16.85ms p(95)=19.05ms  p(99.9)=29.61ms
     http_reqs......................: 504955  4204.120978/s
     iteration_duration.............: avg=11.87ms min=1.29ms   med=11.56ms max=302.73ms p(90)=17.22ms p(95)=19.47ms  p(99.9)=30.09ms
     iterations.....................: 504855  4203.288404/s
     success_rate...................: 100.00% ✓ 504855      ✗ 0     
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

     checks.........................: 100.00% ✓ 1097748     ✗ 0     
     data_received..................: 32 GB   266 MB/s
     data_sent......................: 440 MB  3.7 MB/s
     http_req_blocked...............: avg=3.38µs  min=951ns   med=2.38µs  max=8.09ms   p(90)=3.82µs  p(95)=4.55µs   p(99.9)=35µs   
     http_req_connecting............: avg=629ns   min=0s      med=0s      max=8.05ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.18ms min=1.39ms  med=16.18ms max=283.76ms p(90)=21.68ms p(95)=23.2ms   p(99.9)=30.89ms
       { expected_response:true }...: avg=16.18ms min=1.39ms  med=16.18ms max=283.76ms p(90)=21.68ms p(95)=23.2ms   p(99.9)=30.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 366016
     http_req_receiving.............: avg=77.99µs min=25.76µs med=52.13µs max=133.11ms p(90)=97.42µs p(95)=190.38µs p(99.9)=1.42ms 
     http_req_sending...............: avg=36.56µs min=4.73µs  med=10.28µs max=127.26ms p(90)=18.86µs p(95)=114.15µs p(99.9)=1.44ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.06ms min=1.31ms  med=16.07ms max=267.23ms p(90)=21.57ms p(95)=23.07ms  p(99.9)=30.58ms
     http_reqs......................: 366016  3045.583376/s
     iteration_duration.............: avg=16.38ms min=3.19ms  med=16.38ms max=304.47ms p(90)=21.88ms p(95)=23.4ms   p(99.9)=31.13ms
     iterations.....................: 365916  3044.751285/s
     success_rate...................: 100.00% ✓ 365916      ✗ 0     
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

     checks.........................: 100.00% ✓ 662322      ✗ 0     
     data_received..................: 19 GB   161 MB/s
     data_sent......................: 265 MB  2.2 MB/s
     http_req_blocked...............: avg=4.08µs  min=992ns  med=3µs     max=5.99ms   p(90)=5.15µs   p(95)=6.22µs   p(99.9)=45.68µs
     http_req_connecting............: avg=576ns   min=0s     med=0s      max=4.42ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.92ms min=1.85ms med=26.32ms max=302.59ms p(90)=34.81ms  p(95)=37.61ms  p(99.9)=51.61ms
       { expected_response:true }...: avg=26.92ms min=1.85ms med=26.32ms max=302.59ms p(90)=34.81ms  p(95)=37.61ms  p(99.9)=51.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 220874
     http_req_receiving.............: avg=89.5µs  min=26.8µs med=63.66µs max=170.47ms p(90)=121.88µs p(95)=180.76µs p(99.9)=1.44ms 
     http_req_sending...............: avg=35.87µs min=4.72µs med=11.8µs  max=190.19ms p(90)=23.58µs  p(95)=97.27µs  p(99.9)=1.62ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.79ms min=1.8ms  med=26.2ms  max=280.89ms p(90)=34.68ms  p(95)=37.48ms  p(99.9)=51.11ms
     http_reqs......................: 220874  1836.635836/s
     iteration_duration.............: avg=27.16ms min=6.71ms med=26.54ms max=311.17ms p(90)=35.04ms  p(95)=37.84ms  p(99.9)=51.94ms
     iterations.....................: 220774  1835.804305/s
     success_rate...................: 100.00% ✓ 220774      ✗ 0     
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

     checks.........................: 100.00% ✓ 542121      ✗ 0     
     data_received..................: 16 GB   132 MB/s
     data_sent......................: 217 MB  1.8 MB/s
     http_req_blocked...............: avg=3.18µs  min=1.06µs  med=2.64µs  max=1.77ms   p(90)=4.21µs  p(95)=4.91µs   p(99.9)=36.65µs 
     http_req_connecting............: avg=219ns   min=0s      med=0s      max=1.75ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.97ms min=2.02ms  med=32.03ms max=286.23ms p(90)=47.61ms p(95)=52.52ms  p(99.9)=76.06ms 
       { expected_response:true }...: avg=32.97ms min=2.02ms  med=32.03ms max=286.23ms p(90)=47.61ms p(95)=52.52ms  p(99.9)=76.06ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 180807
     http_req_receiving.............: avg=73.17µs min=25.48µs med=61.02µs max=189.17ms p(90)=97.73µs p(95)=114.14µs p(99.9)=743.96µs
     http_req_sending...............: avg=25.36µs min=4.93µs  med=11.14µs max=208.86ms p(90)=17.52µs p(95)=21.69µs  p(99.9)=799.19µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.87ms min=1.94ms  med=31.94ms max=285.95ms p(90)=47.51ms p(95)=52.42ms  p(99.9)=75.76ms 
     http_reqs......................: 180807  1503.363505/s
     iteration_duration.............: avg=33.19ms min=4.15ms  med=32.24ms max=297.35ms p(90)=47.8ms  p(95)=52.72ms  p(99.9)=76.35ms 
     iterations.....................: 180707  1502.532031/s
     success_rate...................: 100.00% ✓ 180707      ✗ 0     
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

     checks.........................: 100.00% ✓ 515502      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.73µs  min=932ns   med=2.35µs  max=9.76ms   p(90)=3.97µs  p(95)=4.67µs   p(99.9)=30.49µs 
     http_req_connecting............: avg=969ns   min=0s      med=0s      max=7.37ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.67ms min=2.12ms  med=33.71ms max=278.74ms p(90)=49.29ms p(95)=54.33ms  p(99.9)=81.56ms 
       { expected_response:true }...: avg=34.67ms min=2.12ms  med=33.71ms max=278.74ms p(90)=49.29ms p(95)=54.33ms  p(99.9)=81.56ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 171934
     http_req_receiving.............: avg=69.73µs min=26.74µs med=59.17µs max=52.51ms  p(90)=94.58µs p(95)=110.03µs p(99.9)=784.14µs
     http_req_sending...............: avg=20.48µs min=4.61µs  med=10.91µs max=187.23ms p(90)=17.57µs p(95)=21µs     p(99.9)=711.1µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.58ms min=2.02ms  med=33.63ms max=277.89ms p(90)=49.2ms  p(95)=54.24ms  p(99.9)=81.39ms 
     http_reqs......................: 171934  1429.522264/s
     iteration_duration.............: avg=34.9ms  min=6.11ms  med=33.92ms max=287.96ms p(90)=49.5ms  p(95)=54.54ms  p(99.9)=82.29ms 
     iterations.....................: 171834  1428.690827/s
     success_rate...................: 100.00% ✓ 171834      ✗ 0     
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

     checks.........................: 100.00% ✓ 198735     ✗ 0    
     data_received..................: 5.8 GB  48 MB/s
     data_sent......................: 80 MB   661 kB/s
     http_req_blocked...............: avg=5.76µs  min=1.03µs  med=2.68µs  max=91.34ms  p(90)=4.16µs   p(95)=4.74µs   p(99.9)=46.2µs  
     http_req_connecting............: avg=1.47µs  min=0s      med=0s      max=4.01ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=90.21ms min=3.91ms  med=87.31ms max=338.88ms p(90)=109.63ms p(95)=121.21ms p(99.9)=215.81ms
       { expected_response:true }...: avg=90.21ms min=3.91ms  med=87.31ms max=338.88ms p(90)=109.63ms p(95)=121.21ms p(99.9)=215.81ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 66345
     http_req_receiving.............: avg=76.93µs min=26.74µs med=66.9µs  max=115.92ms p(90)=101.53µs p(95)=114.79µs p(99.9)=549.74µs
     http_req_sending...............: avg=20.92µs min=4.82µs  med=13.04µs max=165.17ms p(90)=18.59µs  p(95)=20.5µs   p(99.9)=551.47µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=90.11ms min=3.77ms  med=87.21ms max=316.02ms p(90)=109.53ms p(95)=121.1ms  p(99.9)=215.43ms
     http_reqs......................: 66345   550.41958/s
     iteration_duration.............: avg=90.58ms min=28.84ms med=87.56ms max=347.18ms p(90)=109.87ms p(95)=121.48ms p(99.9)=219.23ms
     iterations.....................: 66245   549.589948/s
     success_rate...................: 100.00% ✓ 66245      ✗ 0    
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

     checks.........................: 100.00% ✓ 191610     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   637 kB/s
     http_req_blocked...............: avg=5.03µs  min=1.13µs  med=3.39µs  max=4.06ms   p(90)=4.92µs   p(95)=5.51µs   p(99.9)=45.54µs 
     http_req_connecting............: avg=1.43µs  min=0s      med=0s      max=4.01ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.55ms min=4.37ms  med=91.38ms max=308.38ms p(90)=126.39ms p(95)=136.62ms p(99.9)=177.67ms
       { expected_response:true }...: avg=93.55ms min=4.37ms  med=91.38ms max=308.38ms p(90)=126.39ms p(95)=136.62ms p(99.9)=177.67ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63970
     http_req_receiving.............: avg=83.46µs min=29.17µs med=74.39µs max=118.81ms p(90)=104.73µs p(95)=116.89µs p(99.9)=594.24µs
     http_req_sending...............: avg=22.28µs min=4.9µs   med=15.51µs max=63.16ms  p(90)=20.84µs  p(95)=22.86µs  p(99.9)=568.76µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.44ms min=4.31ms  med=91.28ms max=303.45ms p(90)=126.3ms  p(95)=136.49ms p(99.9)=177.04ms
     http_reqs......................: 63970   530.555676/s
     iteration_duration.............: avg=93.95ms min=24.9ms  med=91.67ms max=327.88ms p(90)=126.68ms p(95)=136.94ms p(99.9)=179.64ms
     iterations.....................: 63870   529.726294/s
     success_rate...................: 100.00% ✓ 63870      ✗ 0    
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

     checks.........................: 100.00% ✓ 155535     ✗ 0    
     data_received..................: 4.5 GB  38 MB/s
     data_sent......................: 62 MB   517 kB/s
     http_req_blocked...............: avg=5.38µs   min=1.25µs  med=3.31µs   max=3.68ms   p(90)=4.76µs   p(95)=5.33µs   p(99.9)=89.94µs 
     http_req_connecting............: avg=1.82µs   min=0s      med=0s       max=3.64ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=115.27ms min=5.35ms  med=112.96ms max=306.46ms p(90)=150.77ms p(95)=162.6ms  p(99.9)=211.99ms
       { expected_response:true }...: avg=115.27ms min=5.35ms  med=112.96ms max=306.46ms p(90)=150.77ms p(95)=162.6ms  p(99.9)=211.99ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51945
     http_req_receiving.............: avg=81.54µs  min=30.88µs med=78.31µs  max=24.65ms  p(90)=107.82µs p(95)=119.27µs p(99.9)=494.83µs
     http_req_sending...............: avg=28.28µs  min=5.69µs  med=16.15µs  max=115.11ms p(90)=21.34µs  p(95)=23.26µs  p(99.9)=542.8µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=115.16ms min=5.27ms  med=112.86ms max=305.96ms p(90)=150.68ms p(95)=162.48ms p(99.9)=211.87ms
     http_reqs......................: 51945   430.462252/s
     iteration_duration.............: avg=115.74ms min=27.57ms med=113.26ms max=327.01ms p(90)=151.05ms p(95)=162.87ms p(99.9)=213.34ms
     iterations.....................: 51845   429.633564/s
     success_rate...................: 100.00% ✓ 51845      ✗ 0    
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

     checks.........................: 100.00% ✓ 98985      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   329 kB/s
     http_req_blocked...............: avg=6.55µs   min=1.27µs  med=3.26µs   max=4.25ms   p(90)=4.56µs   p(95)=5.1µs    p(99.9)=1.43ms  
     http_req_connecting............: avg=3.03µs   min=0s      med=0s       max=4.21ms   p(90)=0s       p(95)=0s       p(99.9)=1.39ms  
     http_req_duration..............: avg=181.13ms min=7.52ms  med=185.78ms max=353.9ms  p(90)=195.09ms p(95)=200.12ms p(99.9)=269.65ms
       { expected_response:true }...: avg=181.13ms min=7.52ms  med=185.78ms max=353.9ms  p(90)=195.09ms p(95)=200.12ms p(99.9)=269.65ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33095
     http_req_receiving.............: avg=91.86µs  min=34.2µs  med=81.71µs  max=101.88ms p(90)=110.77µs p(95)=121.1µs  p(99.9)=524.55µs
     http_req_sending...............: avg=20.95µs  min=5.82µs  med=16.42µs  max=35ms     p(90)=20.75µs  p(95)=22.44µs  p(99.9)=446.42µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.02ms min=7.43ms  med=185.68ms max=349.42ms p(90)=194.98ms p(95)=200.01ms p(99.9)=269.42ms
     http_reqs......................: 33095   273.63865/s
     iteration_duration.............: avg=181.93ms min=34.21ms med=186.04ms max=362.72ms p(90)=195.38ms p(95)=200.42ms p(99.9)=272.05ms
     iterations.....................: 32995   272.811823/s
     success_rate...................: 100.00% ✓ 32995      ✗ 0    
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

     checks.........................: 100.00% ✓ 96081      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=11.88µs  min=1.45µs  med=3.51µs   max=9.37ms   p(90)=4.9µs    p(95)=5.51µs   p(99.9)=3.94ms  
     http_req_connecting............: avg=7.67µs   min=0s      med=0s       max=9.22ms   p(90)=0s       p(95)=0s       p(99.9)=3.51ms  
     http_req_duration..............: avg=186.66ms min=5.96ms  med=168.97ms max=825ms    p(90)=213.07ms p(95)=239.22ms p(99.9)=717.01ms
       { expected_response:true }...: avg=186.66ms min=5.96ms  med=168.97ms max=825ms    p(90)=213.07ms p(95)=239.22ms p(99.9)=717.01ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32127
     http_req_receiving.............: avg=92.55µs  min=35.55µs med=84.32µs  max=106.72ms p(90)=113.64µs p(95)=124.86µs p(99.9)=756.86µs
     http_req_sending...............: avg=23.99µs  min=6.27µs  med=16.55µs  max=41.63ms  p(90)=20.94µs  p(95)=22.69µs  p(99.9)=650.46µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.54ms min=5.84ms  med=168.86ms max=824.89ms p(90)=212.97ms p(95)=239.07ms p(99.9)=716.9ms 
     http_reqs......................: 32127   265.143182/s
     iteration_duration.............: avg=187.5ms  min=20.08ms med=169.32ms max=825.26ms p(90)=213.43ms p(95)=239.92ms p(99.9)=717.33ms
     iterations.....................: 32027   264.317885/s
     success_rate...................: 100.00% ✓ 32027      ✗ 0    
     vus............................: 10      min=10       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

