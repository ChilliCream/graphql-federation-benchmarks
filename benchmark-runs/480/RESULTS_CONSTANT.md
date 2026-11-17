## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.15 | 5,487 | 5,530 | 5,462 | 0.5% | 395 MB | 73.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.15 | 5,296 | 5,311 | 5,280 | 0.2% | 121 MB | 23.4 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.15 | 5,287 | 5,314 | 5,276 | 0.3% | 388 MB | 75.1 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.15 | 5,153 | 5,169 | 5,106 | 0.5% | 131 MB | 25.9 KB |  |
| fusion-net-11 | 16.7.5 | 5,109 | 5,138 | 5,083 | 0.5% | 379 MB | 76.0 KB |  |
| feddi-gateway | 2026-11-03-0517 | 4,897 | 4,929 | 4,874 | 0.5% | 2,288 MB | 478.4 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,889 | 4,901 | 4,886 | 0.1% | 391 MB | 81.9 KB |  |
| fusion-aot-11 | 16.7.5 | 4,795 | 4,886 | 4,751 | 1.3% | 139 MB | 29.7 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,477 | 4,485 | 4,444 | 0.4% | 138 MB | 31.6 KB |  |
| hive-router | v0.3.13 | 2,905 | 2,926 | 2,904 | 0.3% | 89 MB | 31.2 KB |  |
| grafbase | 0.53.5 | 1,859 | 1,866 | 1,856 | 0.2% | 116 MB | 63.6 KB |  |
| caliban | 3.2.1 | 1,584 | 1,585 | 1,582 | 0.1% | 6,183 MB | 3,996.9 KB |  |
| cosmo | 0.372.0 | 1,502 | 1,505 | 1,501 | 0.1% | 168 MB | 114.6 KB |  |
| hive-gateway-router-runtime | 2.15.8 | 596 | 597 | 595 | 0.1% | 2,627 MB | 4,514.1 KB |  |
| apollo-router | v2.19.1 | 532 | 532 | 531 | 0.1% | 176 MB | 337.8 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 430 | 430 | 427 | 0.3% | 201 MB | 478.0 KB |  |
| hive-gateway | 2.15.8 | 289 | 290 | 287 | 0.4% | 3,512 MB | 12,444.5 KB |  |
| apollo-gateway | 2.14.4 | 271 | 272 | 268 | 0.6% | 2,135 MB | 8,067.8 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1976811     ✗ 0     
     data_received..................: 58 GB   480 MB/s
     data_sent......................: 792 MB  6.6 MB/s
     http_req_blocked...............: avg=2.94µs  min=892ns   med=2.35µs  max=12.72ms  p(90)=3.56µs  p(95)=4.19µs   p(99.9)=31.72µs
     http_req_connecting............: avg=141ns   min=0s      med=0s      max=3.52ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.89ms  min=780.6µs med=7.9ms   max=282.77ms p(90)=14.46ms p(95)=17.85ms  p(99.9)=30.77ms
       { expected_response:true }...: avg=8.89ms  min=780.6µs med=7.9ms   max=282.77ms p(90)=14.46ms p(95)=17.85ms  p(99.9)=30.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 659037
     http_req_receiving.............: avg=98.41µs min=24.86µs med=46.57µs max=170.94ms p(90)=87.47µs p(95)=193µs    p(99.9)=6.83ms 
     http_req_sending...............: avg=44.39µs min=4.39µs  med=8.62µs  max=226.54ms p(90)=14.28µs p(95)=101.66µs p(99.9)=5.25ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.75ms  min=731.5µs med=7.8ms   max=282.09ms p(90)=14.21ms p(95)=17.54ms  p(99.9)=30.23ms
     http_reqs......................: 659037  5487.074476/s
     iteration_duration.............: avg=9.09ms  min=1.17ms  med=8.09ms  max=294.74ms p(90)=14.67ms p(95)=18.07ms  p(99.9)=31.06ms
     iterations.....................: 658937  5486.241886/s
     success_rate...................: 100.00% ✓ 658937      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1907964     ✗ 0     
     data_received..................: 56 GB   463 MB/s
     data_sent......................: 765 MB  6.4 MB/s
     http_req_blocked...............: avg=2.78µs  min=861ns    med=2.01µs  max=9.02ms   p(90)=3.16µs  p(95)=3.76µs   p(99.9)=28.23µs
     http_req_connecting............: avg=381ns   min=0s       med=0s      max=8.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.23ms  min=831.49µs med=8.32ms  max=257.33ms p(90)=14.78ms p(95)=17.94ms  p(99.9)=30.6ms 
       { expected_response:true }...: avg=9.23ms  min=831.49µs med=8.32ms  max=257.33ms p(90)=14.78ms p(95)=17.94ms  p(99.9)=30.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 636088
     http_req_receiving.............: avg=91.61µs min=25.02µs  med=44.98µs max=150.1ms  p(90)=86.52µs p(95)=191.08µs p(99.9)=5.95ms 
     http_req_sending...............: avg=42.28µs min=4.29µs   med=8.28µs  max=223.98ms p(90)=13.94µs p(95)=100.71µs p(99.9)=4.82ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.09ms  min=791.2µs  med=8.21ms  max=256.59ms p(90)=14.56ms p(95)=17.67ms  p(99.9)=30.14ms
     http_reqs......................: 636088  5296.038806/s
     iteration_duration.............: avg=9.42ms  min=1.23ms   med=8.5ms   max=267.61ms p(90)=14.99ms p(95)=18.16ms  p(99.9)=30.87ms
     iterations.....................: 635988  5295.206211/s
     success_rate...................: 100.00% ✓ 635988      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1905003     ✗ 0     
     data_received..................: 56 GB   463 MB/s
     data_sent......................: 763 MB  6.4 MB/s
     http_req_blocked...............: avg=2.56µs  min=782ns    med=1.96µs  max=5.74ms   p(90)=3.08µs  p(95)=3.67µs   p(99.9)=28.15µs
     http_req_connecting............: avg=190ns   min=0s       med=0s      max=4.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.24ms  min=829.55µs med=8.35ms  max=273.98ms p(90)=14.64ms p(95)=17.69ms  p(99.9)=30.15ms
       { expected_response:true }...: avg=9.24ms  min=829.55µs med=8.35ms  max=273.98ms p(90)=14.64ms p(95)=17.69ms  p(99.9)=30.15ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 635101
     http_req_receiving.............: avg=92.14µs min=25.33µs  med=46.32µs max=63.01ms  p(90)=88.04µs p(95)=190.64µs p(99.9)=5.88ms 
     http_req_sending...............: avg=41.55µs min=4.07µs   med=8.14µs  max=226.47ms p(90)=13.97µs p(95)=100.26µs p(99.9)=4.63ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.11ms  min=760.06µs med=8.24ms  max=273.6ms  p(90)=14.42ms p(95)=17.43ms  p(99.9)=29.77ms
     http_reqs......................: 635101  5287.729666/s
     iteration_duration.............: avg=9.43ms  min=1.02ms   med=8.53ms  max=295.25ms p(90)=14.85ms p(95)=17.91ms  p(99.9)=30.41ms
     iterations.....................: 635001  5286.897085/s
     success_rate...................: 100.00% ✓ 635001      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1856877     ✗ 0     
     data_received..................: 54 GB   451 MB/s
     data_sent......................: 744 MB  6.2 MB/s
     http_req_blocked...............: avg=3.61µs  min=832ns    med=1.9µs   max=68.88ms  p(90)=3µs     p(95)=3.57µs   p(99.9)=26.96µs
     http_req_connecting............: avg=1.32µs  min=0s       med=0s      max=68.75ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.49ms  min=859.09µs med=8.62ms  max=221.48ms p(90)=15.04ms p(95)=17.99ms  p(99.9)=30.3ms 
       { expected_response:true }...: avg=9.49ms  min=859.09µs med=8.62ms  max=221.48ms p(90)=15.04ms p(95)=17.99ms  p(99.9)=30.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 619059
     http_req_receiving.............: avg=91.41µs min=24.96µs  med=47.46µs max=23ms     p(90)=88.31µs p(95)=196.4µs  p(99.9)=5.56ms 
     http_req_sending...............: avg=40.89µs min=4.33µs   med=8.07µs  max=91.44ms  p(90)=13.74µs p(95)=100.16µs p(99.9)=4.29ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.35ms  min=809.19µs med=8.51ms  max=219.75ms p(90)=14.84ms p(95)=17.75ms  p(99.9)=29.88ms
     http_reqs......................: 619059  5153.883934/s
     iteration_duration.............: avg=9.68ms  min=1.17ms   med=8.81ms  max=289.57ms p(90)=15.24ms p(95)=18.2ms   p(99.9)=30.59ms
     iterations.....................: 618959  5153.051399/s
     success_rate...................: 100.00% ✓ 618959      ✗ 0     
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

     checks.........................: 100.00% ✓ 1840794     ✗ 0     
     data_received..................: 54 GB   447 MB/s
     data_sent......................: 738 MB  6.1 MB/s
     http_req_blocked...............: avg=2.56µs  min=812ns    med=2.01µs  max=6.4ms    p(90)=3.25µs  p(95)=3.89µs   p(99.9)=29.33µs
     http_req_connecting............: avg=146ns   min=0s       med=0s      max=3.5ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.57ms  min=820.79µs med=8.64ms  max=266.59ms p(90)=15.01ms p(95)=18.06ms  p(99.9)=30.81ms
       { expected_response:true }...: avg=9.57ms  min=820.79µs med=8.64ms  max=266.59ms p(90)=15.01ms p(95)=18.06ms  p(99.9)=30.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 613698
     http_req_receiving.............: avg=94.27µs min=23.91µs  med=45.64µs max=21.74ms  p(90)=91.24µs p(95)=195.46µs p(99.9)=6.09ms 
     http_req_sending...............: avg=42.41µs min=4.23µs   med=8.11µs  max=132.27ms p(90)=14.6µs  p(95)=101.16µs p(99.9)=4.76ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.43ms  min=754.99µs med=8.52ms  max=266.1ms  p(90)=14.79ms p(95)=17.8ms   p(99.9)=30.37ms
     http_reqs......................: 613698  5109.501663/s
     iteration_duration.............: avg=9.76ms  min=1.25ms   med=8.83ms  max=295.56ms p(90)=15.22ms p(95)=18.27ms  p(99.9)=31.07ms
     iterations.....................: 613598  5108.669087/s
     success_rate...................: 100.00% ✓ 613598      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-03-0517)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1764204     ✗ 0     
     data_received..................: 51 GB   428 MB/s
     data_sent......................: 707 MB  5.9 MB/s
     http_req_blocked...............: avg=2.71µs  min=812ns    med=2.12µs  max=5.19ms   p(90)=3.47µs  p(95)=4.15µs   p(99.9)=28.3µs 
     http_req_connecting............: avg=150ns   min=0s       med=0s      max=3.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.99ms  min=736.26µs med=9.28ms  max=283.82ms p(90)=14.93ms p(95)=18.3ms   p(99.9)=29.22ms
       { expected_response:true }...: avg=9.99ms  min=736.26µs med=9.28ms  max=283.82ms p(90)=14.93ms p(95)=18.3ms   p(99.9)=29.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 588168
     http_req_receiving.............: avg=94.17µs min=25.93µs  med=47.21µs max=190.31ms p(90)=91.82µs p(95)=201.57µs p(99.9)=6.18ms 
     http_req_sending...............: avg=42.64µs min=4.61µs   med=8.5µs   max=152.88ms p(90)=15.3µs  p(95)=109.02µs p(99.9)=4.58ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.85ms  min=666.3µs  med=9.19ms  max=283.34ms p(90)=14.67ms p(95)=18.06ms  p(99.9)=28.74ms
     http_reqs......................: 588168  4897.250608/s
     iteration_duration.............: avg=10.19ms min=1.24ms   med=9.46ms  max=297.04ms p(90)=15.15ms p(95)=18.51ms  p(99.9)=29.46ms
     iterations.....................: 588068  4896.41798/s
     success_rate...................: 100.00% ✓ 588068      ✗ 0     
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

     checks.........................: 100.00% ✓ 1761636     ✗ 0     
     data_received..................: 51 GB   428 MB/s
     data_sent......................: 706 MB  5.9 MB/s
     http_req_blocked...............: avg=2.73µs  min=801ns    med=1.99µs  max=10.56ms  p(90)=3.3µs   p(95)=4.07µs   p(99.9)=27.08µs
     http_req_connecting............: avg=271ns   min=0s       med=0s      max=7.74ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10ms    min=989.57µs med=9.16ms  max=276.51ms p(90)=15.38ms p(95)=18.18ms  p(99.9)=31.27ms
       { expected_response:true }...: avg=10ms    min=989.57µs med=9.16ms  max=276.51ms p(90)=15.38ms p(95)=18.18ms  p(99.9)=31.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 587312
     http_req_receiving.............: avg=98.82µs min=24.43µs  med=47.39µs max=150.4ms  p(90)=95.85µs p(95)=198.66µs p(99.9)=6.37ms 
     http_req_sending...............: avg=43.22µs min=4.24µs   med=8.34µs  max=60.81ms  p(90)=15.85µs p(95)=102.7µs  p(99.9)=4.87ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.86ms  min=914.68µs med=9.04ms  max=265.19ms p(90)=15.16ms p(95)=17.92ms  p(99.9)=30.91ms
     http_reqs......................: 587312  4889.121295/s
     iteration_duration.............: avg=10.2ms  min=1.51ms   med=9.35ms  max=297.07ms p(90)=15.59ms p(95)=18.4ms   p(99.9)=31.54ms
     iterations.....................: 587212  4888.288837/s
     success_rate...................: 100.00% ✓ 587212      ✗ 0     
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

     checks.........................: 100.00% ✓ 1727778     ✗ 0     
     data_received..................: 50 GB   420 MB/s
     data_sent......................: 692 MB  5.8 MB/s
     http_req_blocked...............: avg=2.48µs  min=831ns    med=1.94µs max=4.68ms   p(90)=3.01µs  p(95)=3.54µs   p(99.9)=26.3µs 
     http_req_connecting............: avg=169ns   min=0s       med=0s     max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.21ms min=905.1µs  med=9.5ms  max=275.58ms p(90)=15.23ms p(95)=17.75ms  p(99.9)=29ms   
       { expected_response:true }...: avg=10.21ms min=905.1µs  med=9.5ms  max=275.58ms p(90)=15.23ms p(95)=17.75ms  p(99.9)=29ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 576026
     http_req_receiving.............: avg=94.45µs min=25.31µs  med=46.4µs max=119.66ms p(90)=92.76µs p(95)=211.68µs p(99.9)=5.7ms  
     http_req_sending...............: avg=39.42µs min=4.53µs   med=8.23µs max=169.84ms p(90)=13.95µs p(95)=100.75µs p(99.9)=3.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.08ms min=847.49µs med=9.39ms max=275ms    p(90)=15.03ms p(95)=17.52ms  p(99.9)=28.6ms 
     http_reqs......................: 576026  4795.457094/s
     iteration_duration.............: avg=10.4ms  min=1.29ms   med=9.68ms max=287.04ms p(90)=15.43ms p(95)=17.96ms  p(99.9)=29.26ms
     iterations.....................: 575926  4794.624587/s
     success_rate...................: 100.00% ✓ 575926      ✗ 0     
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

     checks.........................: 100.00% ✓ 1613619     ✗ 0     
     data_received..................: 47 GB   392 MB/s
     data_sent......................: 647 MB  5.4 MB/s
     http_req_blocked...............: avg=3.83µs   min=811ns   med=2.41µs  max=148.98ms p(90)=3.76µs   p(95)=4.44µs   p(99.9)=33.86µs
     http_req_connecting............: avg=984ns    min=0s      med=0s      max=144.92ms p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.94ms  min=1.09ms  med=10.25ms max=258.95ms p(90)=16.18ms  p(95)=18.84ms  p(99.9)=31.5ms 
       { expected_response:true }...: avg=10.94ms  min=1.09ms  med=10.25ms max=258.95ms p(90)=16.18ms  p(95)=18.84ms  p(99.9)=31.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 537973
     http_req_receiving.............: avg=103.88µs min=25.36µs med=47.81µs max=126.46ms p(90)=100.48µs p(95)=224.27µs p(99.9)=6.74ms 
     http_req_sending...............: avg=43.71µs  min=4.41µs  med=8.97µs  max=217.99ms p(90)=16.55µs  p(95)=109.61µs p(99.9)=4.38ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.79ms  min=1.01ms  med=10.13ms max=254.51ms p(90)=15.96ms  p(95)=18.58ms  p(99.9)=31.05ms
     http_reqs......................: 537973  4477.888674/s
     iteration_duration.............: avg=11.14ms  min=1.66ms  med=10.44ms max=288.8ms  p(90)=16.39ms  p(95)=19.06ms  p(99.9)=31.81ms
     iterations.....................: 537873  4477.056311/s
     success_rate...................: 100.00% ✓ 537873      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.13)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1047216     ✗ 0     
     data_received..................: 31 GB   254 MB/s
     data_sent......................: 420 MB  3.5 MB/s
     http_req_blocked...............: avg=2.75µs  min=902ns   med=2.16µs  max=5.24ms   p(90)=3.52µs  p(95)=4.21µs   p(99.9)=26.77µs
     http_req_connecting............: avg=281ns   min=0s      med=0s      max=5.11ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.98ms min=1.22ms  med=16.83ms max=268.7ms  p(90)=24.01ms p(95)=25.94ms  p(99.9)=33.64ms
       { expected_response:true }...: avg=16.98ms min=1.22ms  med=16.83ms max=268.7ms  p(90)=24.01ms p(95)=25.94ms  p(99.9)=33.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 349172
     http_req_receiving.............: avg=66.17µs min=24.94µs med=48.91µs max=30ms     p(90)=85.85µs p(95)=125.97µs p(99.9)=1.06ms 
     http_req_sending...............: avg=30.65µs min=4.51µs  med=9.35µs  max=181.88ms p(90)=15.7µs  p(95)=91.96µs  p(99.9)=1.14ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.89ms min=1.14ms  med=16.73ms max=256.39ms p(90)=23.92ms p(95)=25.85ms  p(99.9)=33.49ms
     http_reqs......................: 349172  2905.915655/s
     iteration_duration.............: avg=17.17ms min=2.38ms  med=17.02ms max=291.12ms p(90)=24.2ms  p(95)=26.13ms  p(99.9)=33.87ms
     iterations.....................: 349072  2905.083425/s
     success_rate...................: 100.00% ✓ 349072      ✗ 0     
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

     checks.........................: 100.00% ✓ 670464      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 269 MB  2.2 MB/s
     http_req_blocked...............: avg=3.8µs   min=802ns   med=2.15µs  max=8ms      p(90)=4.15µs   p(95)=5.23µs   p(99.9)=34.94µs
     http_req_connecting............: avg=1.08µs  min=0s      med=0s      max=7.81ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.6ms  min=1.89ms  med=26.09ms max=260.01ms p(90)=34.5ms   p(95)=37.23ms  p(99.9)=50.31ms
       { expected_response:true }...: avg=26.6ms  min=1.89ms  med=26.09ms max=260.01ms p(90)=34.5ms   p(95)=37.23ms  p(99.9)=50.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 223588
     http_req_receiving.............: avg=82.17µs min=27.68µs med=55.78µs max=150.86ms p(90)=116.41µs p(95)=179.19µs p(99.9)=1.37ms 
     http_req_sending...............: avg=31.05µs min=4.34µs  med=9.23µs  max=81.85ms  p(90)=21.54µs  p(95)=93.79µs  p(99.9)=1.63ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.49ms min=1.79ms  med=25.98ms max=258.05ms p(90)=34.38ms  p(95)=37.1ms   p(99.9)=50.16ms
     http_reqs......................: 223588  1859.253356/s
     iteration_duration.............: avg=26.83ms min=5.47ms  med=26.3ms  max=302.96ms p(90)=34.72ms  p(95)=37.45ms  p(99.9)=50.63ms
     iterations.....................: 223488  1858.421803/s
     success_rate...................: 100.00% ✓ 223488      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 571551      ✗ 0     
     data_received..................: 17 GB   139 MB/s
     data_sent......................: 229 MB  1.9 MB/s
     http_req_blocked...............: avg=3.31µs  min=942ns   med=2.44µs  max=3.62ms   p(90)=4.25µs  p(95)=5.07µs   p(99.9)=28.94µs 
     http_req_connecting............: avg=521ns   min=0s      med=0s      max=3.58ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=31.25ms min=2.01ms  med=30.38ms max=291.33ms p(90)=44.09ms p(95)=48.61ms  p(99.9)=71.45ms 
       { expected_response:true }...: avg=31.25ms min=2.01ms  med=30.38ms max=291.33ms p(90)=44.09ms p(95)=48.61ms  p(99.9)=71.45ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 190617
     http_req_receiving.............: avg=73.68µs min=26.99µs med=60.74µs max=103.83ms p(90)=100.3µs p(95)=118.17µs p(99.9)=895.89µs
     http_req_sending...............: avg=22.72µs min=4.84µs  med=11.65µs max=153.81ms p(90)=19.28µs p(95)=23.37µs  p(99.9)=791.81µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=31.15ms min=1.96ms  med=30.29ms max=290.83ms p(90)=43.99ms p(95)=48.51ms  p(99.9)=71.29ms 
     http_reqs......................: 190617  1584.463229/s
     iteration_duration.............: avg=31.48ms min=5.45ms  med=30.6ms  max=303.55ms p(90)=44.31ms p(95)=48.83ms  p(99.9)=71.82ms 
     iterations.....................: 190517  1583.632/s
     success_rate...................: 100.00% ✓ 190517      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.372.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 541620      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 217 MB  1.8 MB/s
     http_req_blocked...............: avg=4.44µs  min=1.12µs  med=2.64µs  max=9.16ms   p(90)=4.16µs  p(95)=4.85µs   p(99.9)=36.17µs 
     http_req_connecting............: avg=1.45µs  min=0s      med=0s      max=9.11ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33ms    min=1.99ms  med=32.13ms max=299.27ms p(90)=47.53ms p(95)=52.31ms  p(99.9)=73.58ms 
       { expected_response:true }...: avg=33ms    min=1.99ms  med=32.13ms max=299.27ms p(90)=47.53ms p(95)=52.31ms  p(99.9)=73.58ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 180640
     http_req_receiving.............: avg=73.28µs min=25.83µs med=61.12µs max=233.67ms p(90)=97.94µs p(95)=113.99µs p(99.9)=721.61µs
     http_req_sending...............: avg=23.35µs min=4.74µs  med=11.54µs max=71.1ms   p(90)=17.98µs p(95)=22.01µs  p(99.9)=801.88µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.9ms  min=1.91ms  med=32.04ms max=298.84ms p(90)=47.43ms p(95)=52.21ms  p(99.9)=73.25ms 
     http_reqs......................: 180640  1502.015293/s
     iteration_duration.............: avg=33.22ms min=4.46ms  med=32.34ms max=313.91ms p(90)=47.73ms p(95)=52.52ms  p(99.9)=73.85ms 
     iterations.....................: 180540  1501.183796/s
     success_rate...................: 100.00% ✓ 180540      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 215211     ✗ 0    
     data_received..................: 6.3 GB  52 MB/s
     data_sent......................: 86 MB   716 kB/s
     http_req_blocked...............: avg=4.61µs  min=1.18µs med=3.08µs  max=3.43ms   p(90)=4.55µs   p(95)=5.18µs   p(99.9)=43.09µs 
     http_req_connecting............: avg=1.26µs  min=0s     med=0s      max=3.39ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=83.31ms min=3.61ms med=80.32ms max=318.32ms p(90)=100.9ms  p(95)=111.65ms p(99.9)=211.43ms
       { expected_response:true }...: avg=83.31ms min=3.61ms med=80.32ms max=318.32ms p(90)=100.9ms  p(95)=111.65ms p(99.9)=211.43ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 71837
     http_req_receiving.............: avg=80.8µs  min=30.5µs med=72µs    max=83.13ms  p(90)=104.26µs p(95)=116.58µs p(99.9)=571.6µs 
     http_req_sending...............: avg=23.74µs min=5.25µs med=13.77µs max=102.23ms p(90)=19.48µs  p(95)=21.58µs  p(99.9)=564.96µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=83.21ms min=3.51ms med=80.23ms max=317.94ms p(90)=100.79ms p(95)=111.51ms p(99.9)=211.16ms
     http_reqs......................: 71837   596.234792/s
     iteration_duration.............: avg=83.65ms min=8.37ms med=80.56ms max=334.67ms p(90)=101.15ms p(95)=111.93ms p(99.9)=212.52ms
     iterations.....................: 71737   595.404809/s
     success_rate...................: 100.00% ✓ 71737      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 192363     ✗ 0    
     data_received..................: 5.6 GB  47 MB/s
     data_sent......................: 77 MB   640 kB/s
     http_req_blocked...............: avg=7.05µs  min=1.16µs  med=3.31µs  max=9.13ms   p(90)=4.83µs   p(95)=5.44µs   p(99.9)=51.37µs 
     http_req_connecting............: avg=3.28µs  min=0s      med=0s      max=8.95ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.18ms min=4.42ms  med=91.2ms  max=316.58ms p(90)=125.79ms p(95)=135.97ms p(99.9)=177.64ms
       { expected_response:true }...: avg=93.18ms min=4.42ms  med=91.2ms  max=316.58ms p(90)=125.79ms p(95)=135.97ms p(99.9)=177.64ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64221
     http_req_receiving.............: avg=85.67µs min=28.84µs med=73.41µs max=213.02ms p(90)=104.14µs p(95)=116.56µs p(99.9)=554.21µs
     http_req_sending...............: avg=28.26µs min=5.45µs  med=15.14µs max=164.52ms p(90)=20.69µs  p(95)=22.78µs  p(99.9)=707.16µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.07ms min=4.34ms  med=91.1ms  max=311.02ms p(90)=125.69ms p(95)=135.85ms p(99.9)=176.3ms 
     http_reqs......................: 64221   532.575234/s
     iteration_duration.............: avg=93.59ms min=25.21ms med=91.48ms max=328.87ms p(90)=126.06ms p(95)=136.3ms  p(99.9)=179.61ms
     iterations.....................: 64121   531.745949/s
     success_rate...................: 100.00% ✓ 64121      ✗ 0    
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

     checks.........................: 100.00% ✓ 155424     ✗ 0    
     data_received..................: 4.5 GB  38 MB/s
     data_sent......................: 62 MB   516 kB/s
     http_req_blocked...............: avg=5.07µs   min=1.13µs  med=3.07µs   max=3.45ms   p(90)=4.44µs   p(95)=4.95µs   p(99.9)=129.89µs
     http_req_connecting............: avg=1.75µs   min=0s      med=0s       max=3.43ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=115.37ms min=5.31ms  med=112.98ms max=320.78ms p(90)=151.05ms p(95)=162.81ms p(99.9)=211.22ms
       { expected_response:true }...: avg=115.37ms min=5.31ms  med=112.98ms max=320.78ms p(90)=151.05ms p(95)=162.81ms p(99.9)=211.22ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51908
     http_req_receiving.............: avg=80.86µs  min=27.76µs med=76.26µs  max=104.74ms p(90)=105.53µs p(95)=117.35µs p(99.9)=492.79µs
     http_req_sending...............: avg=23.52µs  min=5.15µs  med=15.15µs  max=101.8ms  p(90)=19.98µs  p(95)=21.79µs  p(99.9)=490.46µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=115.27ms min=5.19ms  med=112.88ms max=320.3ms  p(90)=150.95ms p(95)=162.7ms  p(99.9)=210.87ms
     http_reqs......................: 51908   430.095002/s
     iteration_duration.............: avg=115.84ms min=29.43ms med=113.3ms  max=355.76ms p(90)=151.32ms p(95)=163.12ms p(99.9)=212.09ms
     iterations.....................: 51808   429.26643/s
     success_rate...................: 100.00% ✓ 51808      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 104766     ✗ 0    
     data_received..................: 3.1 GB  25 MB/s
     data_sent......................: 42 MB   348 kB/s
     http_req_blocked...............: avg=6.4µs    min=1.29µs  med=3.53µs   max=3.86ms   p(90)=4.96µs   p(95)=5.59µs   p(99.9)=1.09ms  
     http_req_connecting............: avg=2.62µs   min=0s      med=0s       max=3.8ms    p(90)=0s       p(95)=0s       p(99.9)=1.07ms  
     http_req_duration..............: avg=171.15ms min=5.72ms  med=152.82ms max=792.91ms p(90)=195.25ms p(95)=222.38ms p(99.9)=702.36ms
       { expected_response:true }...: avg=171.15ms min=5.72ms  med=152.82ms max=792.91ms p(90)=195.25ms p(95)=222.38ms p(99.9)=702.36ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 35022
     http_req_receiving.............: avg=95.7µs   min=36.49µs med=84.2µs   max=59.84ms  p(90)=114.03µs p(95)=124.94µs p(99.9)=725.72µs
     http_req_sending...............: avg=24.4µs   min=6.3µs   med=17.6µs   max=82.16ms  p(90)=22.24µs  p(95)=24µs     p(99.9)=659.97µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=171.03ms min=5.6ms   med=152.7ms  max=792.79ms p(90)=195.16ms p(95)=222.23ms p(99.9)=702.27ms
     http_reqs......................: 35022   289.900397/s
     iteration_duration.............: avg=171.9ms  min=57.78ms med=153.15ms max=793.18ms p(90)=195.63ms p(95)=222.8ms  p(99.9)=702.67ms
     iterations.....................: 34922   289.072631/s
     success_rate...................: 100.00% ✓ 34922      ✗ 0    
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

     checks.........................: 100.00% ✓ 98352      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   326 kB/s
     http_req_blocked...............: avg=6.46µs   min=1.32µs  med=3.33µs   max=3.99ms   p(90)=4.66µs   p(95)=5.24µs   p(99.9)=1.34ms  
     http_req_connecting............: avg=2.92µs   min=0s      med=0s       max=3.95ms   p(90)=0s       p(95)=0s       p(99.9)=1.32ms  
     http_req_duration..............: avg=182.29ms min=7.6ms   med=175.2ms  max=384.53ms p(90)=210.49ms p(95)=216.29ms p(99.9)=288.57ms
       { expected_response:true }...: avg=182.29ms min=7.6ms   med=175.2ms  max=384.53ms p(90)=210.49ms p(95)=216.29ms p(99.9)=288.57ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32884
     http_req_receiving.............: avg=94.07µs  min=35.33µs med=84.91µs  max=197.51ms p(90)=114.32µs p(95)=125.51µs p(99.9)=502.66µs
     http_req_sending...............: avg=23.8µs   min=5.88µs  med=16.71µs  max=48.35ms  p(90)=21.16µs  p(95)=23.03µs  p(99.9)=519.84µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.17ms min=7.44ms  med=175.1ms  max=384.27ms p(90)=210.38ms p(95)=216.16ms p(99.9)=288.46ms
     http_reqs......................: 32884   271.83011/s
     iteration_duration.............: avg=183.11ms min=38.63ms med=175.49ms max=394.76ms p(90)=210.77ms p(95)=216.61ms p(99.9)=289.58ms
     iterations.....................: 32784   271.003477/s
     success_rate...................: 100.00% ✓ 32784      ✗ 0    
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

