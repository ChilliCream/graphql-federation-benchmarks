## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 5,076 | 5,085 | 5,012 | 0.6% | 387 MB | 78.1 KB |  |
| fusion-net-11 | 16.7.3 | 5,016 | 5,047 | 5,000 | 0.3% | 389 MB | 79.4 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,840 | 4,860 | 4,790 | 0.6% | 371 MB | 78.5 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,837 | 4,850 | 4,821 | 0.2% | 388 MB | 82.1 KB |  |
| fusion-aot-11 | 16.7.3 | 4,798 | 4,809 | 4,773 | 0.3% | 133 MB | 28.4 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,661 | 4,688 | 4,655 | 0.3% | 118 MB | 26.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,612 | 4,620 | 4,610 | 0.1% | 139 MB | 30.9 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,542 | 4,548 | 4,536 | 0.1% | 128 MB | 28.9 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,238 | 4,334 | 4,220 | 1.1% | 2,307 MB | 557.3 KB |  |
| hive-router | v0.3.6 | 3,048 | 3,061 | 3,022 | 0.5% | 92 MB | 30.8 KB |  |
| grafbase | 0.53.5 | 1,836 | 1,841 | 1,828 | 0.3% | 112 MB | 62.7 KB |  |
| cosmo | 0.363.0 | 1,503 | 1,504 | 1,503 | 0.0% | 169 MB | 115.0 KB |  |
| caliban | 3.2.0 | 1,450 | 1,491 | 1,326 | 4.9% | 5,870 MB | 4,145.5 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 545 | 549 | 542 | 0.5% | 2,743 MB | 5,154.3 KB |  |
| apollo-router | v2.19.0 | 486 | 487 | 486 | 0.1% | 177 MB | 371.9 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 399 | 399 | 398 | 0.1% | 200 MB | 514.1 KB |  |
| apollo-gateway | 2.14.4 | 275 | 275 | 274 | 0.2% | 2,164 MB | 8,059.5 KB |  |
| hive-gateway | 2.15.3 | 274 | 275 | 271 | 0.6% | 3,502 MB | 13,086.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1828716     ✗ 0     
     data_received..................: 53 GB   444 MB/s
     data_sent......................: 733 MB  6.1 MB/s
     http_req_blocked...............: avg=2.42µs  min=762ns    med=1.87µs  max=5.16ms   p(90)=2.97µs  p(95)=3.58µs   p(99.9)=25.4µs 
     http_req_connecting............: avg=158ns   min=0s       med=0s      max=4.16ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.64ms  min=806.78µs med=8.83ms  max=265.35ms p(90)=14.77ms p(95)=17.47ms  p(99.9)=29.66ms
       { expected_response:true }...: avg=9.64ms  min=806.78µs med=8.83ms  max=265.35ms p(90)=14.77ms p(95)=17.47ms  p(99.9)=29.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 609672
     http_req_receiving.............: avg=89.45µs min=23.82µs  med=44.51µs max=198.03ms p(90)=87.36µs p(95)=185.66µs p(99.9)=5.91ms 
     http_req_sending...............: avg=40.89µs min=4.5µs    med=8.01µs  max=201.9ms  p(90)=14.28µs p(95)=98µs     p(99.9)=4.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.51ms  min=759.63µs med=8.73ms  max=263.36ms p(90)=14.56ms p(95)=17.22ms  p(99.9)=29.08ms
     http_reqs......................: 609672  5076.133849/s
     iteration_duration.............: avg=9.83ms  min=1.04ms   med=9.02ms  max=280.21ms p(90)=14.97ms p(95)=17.69ms  p(99.9)=29.89ms
     iterations.....................: 609572  5075.301249/s
     success_rate...................: 100.00% ✓ 609572      ✗ 0     
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

     checks.........................: 100.00% ✓ 1807293     ✗ 0     
     data_received..................: 53 GB   439 MB/s
     data_sent......................: 724 MB  6.0 MB/s
     http_req_blocked...............: avg=2.45µs  min=772ns    med=1.86µs  max=6.27ms   p(90)=3.01µs  p(95)=3.65µs   p(99.9)=26.21µs
     http_req_connecting............: avg=146ns   min=0s       med=0s      max=3.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.75ms  min=809.16µs med=8.95ms  max=274.48ms p(90)=14.95ms p(95)=17.69ms  p(99.9)=29.97ms
       { expected_response:true }...: avg=9.75ms  min=809.16µs med=8.95ms  max=274.48ms p(90)=14.95ms p(95)=17.69ms  p(99.9)=29.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 602531
     http_req_receiving.............: avg=90.32µs min=23.5µs   med=45.55µs max=28.68ms  p(90)=90.01µs p(95)=193.62µs p(99.9)=5.76ms 
     http_req_sending...............: avg=41.26µs min=4.38µs   med=7.98µs  max=192.04ms p(90)=14.31µs p(95)=99.14µs  p(99.9)=4.48ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.62ms  min=763.8µs  med=8.84ms  max=274.01ms p(90)=14.74ms p(95)=17.44ms  p(99.9)=29.54ms
     http_reqs......................: 602531  5016.532583/s
     iteration_duration.............: avg=9.95ms  min=1ms      med=9.14ms  max=294.34ms p(90)=15.15ms p(95)=17.9ms   p(99.9)=30.26ms
     iterations.....................: 602431  5015.700006/s
     success_rate...................: 100.00% ✓ 602431      ✗ 0     
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

     checks.........................: 100.00% ✓ 1743996     ✗ 0     
     data_received..................: 51 GB   424 MB/s
     data_sent......................: 699 MB  5.8 MB/s
     http_req_blocked...............: avg=3.16µs  min=771ns    med=2.02µs  max=148.76ms p(90)=3.33µs  p(95)=4.1µs    p(99.9)=29.81µs
     http_req_connecting............: avg=641ns   min=0s       med=0s      max=148.61ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.1ms  min=981.75µs med=9.29ms  max=220.96ms p(90)=15.46ms p(95)=18.15ms  p(99.9)=30.63ms
       { expected_response:true }...: avg=10.1ms  min=981.75µs med=9.29ms  max=220.96ms p(90)=15.46ms p(95)=18.15ms  p(99.9)=30.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 581432
     http_req_receiving.............: avg=98.22µs min=25.01µs  med=47.53µs max=90.64ms  p(90)=95.75µs p(95)=196.56µs p(99.9)=6.58ms 
     http_req_sending...............: avg=45.94µs min=4.28µs   med=8.24µs  max=103.86ms p(90)=15.95µs p(95)=101.64µs p(99.9)=5.13ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.96ms  min=901.69µs med=9.17ms  max=213.31ms p(90)=15.24ms p(95)=17.89ms  p(99.9)=30.11ms
     http_reqs......................: 581432  4840.229252/s
     iteration_duration.............: avg=10.31ms min=1.42ms   med=9.49ms  max=281.17ms p(90)=15.66ms p(95)=18.36ms  p(99.9)=30.86ms
     iterations.....................: 581332  4839.396785/s
     success_rate...................: 100.00% ✓ 581332      ✗ 0     
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

     checks.........................: 100.00% ✓ 1743231     ✗ 0     
     data_received..................: 51 GB   423 MB/s
     data_sent......................: 699 MB  5.8 MB/s
     http_req_blocked...............: avg=2.47µs  min=752ns    med=1.9µs  max=5.79ms   p(90)=3.08µs  p(95)=3.79µs   p(99.9)=26.9µs 
     http_req_connecting............: avg=158ns   min=0s       med=0s     max=3.57ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.11ms min=976.79µs med=9.37ms max=295.9ms  p(90)=15.27ms p(95)=17.86ms  p(99.9)=30.28ms
       { expected_response:true }...: avg=10.11ms min=976.79µs med=9.37ms max=295.9ms  p(90)=15.27ms p(95)=17.86ms  p(99.9)=30.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 581177
     http_req_receiving.............: avg=96.53µs min=24.99µs  med=47µs   max=213.87ms p(90)=92.57µs p(95)=191.79µs p(99.9)=6.27ms 
     http_req_sending...............: avg=41.81µs min=4.25µs   med=7.95µs max=104.32ms p(90)=14.95µs p(95)=99.4µs   p(99.9)=4.77ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.97ms  min=886.74µs med=9.25ms max=286.83ms p(90)=15.07ms p(95)=17.61ms  p(99.9)=29.87ms
     http_reqs......................: 581177  4837.957232/s
     iteration_duration.............: avg=10.31ms min=1.49ms   med=9.56ms max=306.23ms p(90)=15.47ms p(95)=18.08ms  p(99.9)=30.51ms
     iterations.....................: 581077  4837.12479/s
     success_rate...................: 100.00% ✓ 581077      ✗ 0     
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

     checks.........................: 100.00% ✓ 1728645     ✗ 0     
     data_received..................: 50 GB   420 MB/s
     data_sent......................: 693 MB  5.8 MB/s
     http_req_blocked...............: avg=2.68µs  min=791ns    med=1.87µs  max=8.82ms   p(90)=2.98µs  p(95)=3.55µs   p(99.9)=25.52µs
     http_req_connecting............: avg=437ns   min=0s       med=0s      max=8.74ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.21ms min=860.4µs  med=9.57ms  max=328.2ms  p(90)=15.04ms p(95)=17.49ms  p(99.9)=28.64ms
       { expected_response:true }...: avg=10.21ms min=860.4µs  med=9.57ms  max=328.2ms  p(90)=15.04ms p(95)=17.49ms  p(99.9)=28.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 576315
     http_req_receiving.............: avg=88.35µs min=24.7µs   med=44.38µs max=115.43ms p(90)=87.08µs p(95)=196.07µs p(99.9)=5.38ms 
     http_req_sending...............: avg=38.42µs min=4.33µs   med=7.97µs  max=137.73ms p(90)=13.87µs p(95)=100.16µs p(99.9)=3.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.08ms min=809.54µs med=9.47ms  max=319.47ms p(90)=14.85ms p(95)=17.26ms  p(99.9)=28.26ms
     http_reqs......................: 576315  4798.09352/s
     iteration_duration.............: avg=10.4ms  min=1.47ms   med=9.75ms  max=340.98ms p(90)=15.24ms p(95)=17.7ms   p(99.9)=28.92ms
     iterations.....................: 576215  4797.260973/s
     success_rate...................: 100.00% ✓ 576215      ✗ 0     
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

     checks.........................: 100.00% ✓ 1679676     ✗ 0     
     data_received..................: 49 GB   408 MB/s
     data_sent......................: 673 MB  5.6 MB/s
     http_req_blocked...............: avg=3.58µs  min=841ns    med=2.19µs  max=88.55ms  p(90)=3.48µs  p(95)=4.14µs   p(99.9)=30.25µs
     http_req_connecting............: avg=990ns   min=0s       med=0s      max=88.47ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.5ms  min=898.12µs med=9.81ms  max=251.39ms p(90)=15.66ms p(95)=18.3ms   p(99.9)=29.92ms
       { expected_response:true }...: avg=10.5ms  min=898.12µs med=9.81ms  max=251.39ms p(90)=15.66ms p(95)=18.3ms   p(99.9)=29.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 559992
     http_req_receiving.............: avg=97.62µs min=25.45µs  med=47.98µs max=110.2ms  p(90)=96.38µs p(95)=215.47µs p(99.9)=5.89ms 
     http_req_sending...............: avg=41.61µs min=4.43µs   med=8.54µs  max=115.76ms p(90)=15.63µs p(95)=108.35µs p(99.9)=4.14ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.37ms min=844µs    med=9.69ms  max=249.22ms p(90)=15.44ms p(95)=18.04ms  p(99.9)=29.49ms
     http_reqs......................: 559992  4661.851534/s
     iteration_duration.............: avg=10.7ms  min=1.08ms   med=10ms    max=287.32ms p(90)=15.86ms p(95)=18.51ms  p(99.9)=30.2ms 
     iterations.....................: 559892  4661.019049/s
     success_rate...................: 100.00% ✓ 559892      ✗ 0     
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

     checks.........................: 100.00% ✓ 1662129     ✗ 0     
     data_received..................: 49 GB   404 MB/s
     data_sent......................: 666 MB  5.5 MB/s
     http_req_blocked...............: avg=2.81µs  min=781ns    med=1.91µs  max=8.4ms    p(90)=3.19µs  p(95)=3.93µs   p(99.9)=27.22µs
     http_req_connecting............: avg=411ns   min=0s       med=0s      max=8.27ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.62ms min=1.05ms   med=10ms    max=267.04ms p(90)=15.53ms p(95)=17.97ms  p(99.9)=30.04ms
       { expected_response:true }...: avg=10.62ms min=1.05ms   med=10ms    max=267.04ms p(90)=15.53ms p(95)=17.97ms  p(99.9)=30.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 554143
     http_req_receiving.............: avg=96.6µs  min=24.55µs  med=46.66µs max=110.7ms  p(90)=97.28µs p(95)=204.6µs  p(99.9)=6.04ms 
     http_req_sending...............: avg=39.89µs min=4.34µs   med=8.03µs  max=166.27ms p(90)=15.49µs p(95)=103.56µs p(99.9)=4.06ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.48ms min=972.17µs med=9.89ms  max=265.97ms p(90)=15.33ms p(95)=17.71ms  p(99.9)=29.63ms
     http_reqs......................: 554143  4612.547866/s
     iteration_duration.............: avg=10.82ms min=1.63ms   med=10.19ms max=298.1ms  p(90)=15.73ms p(95)=18.18ms  p(99.9)=30.28ms
     iterations.....................: 554043  4611.715491/s
     success_rate...................: 100.00% ✓ 554043      ✗ 0     
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

     checks.........................: 100.00% ✓ 1637070     ✗ 0     
     data_received..................: 48 GB   398 MB/s
     data_sent......................: 656 MB  5.5 MB/s
     http_req_blocked...............: avg=3.03µs  min=992ns    med=2.45µs  max=6.15ms   p(90)=3.71µs  p(95)=4.36µs   p(99.9)=31.72µs
     http_req_connecting............: avg=166ns   min=0s       med=0s      max=4.11ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.78ms min=1.02ms   med=10.12ms max=228.55ms p(90)=15.92ms p(95)=18.6ms   p(99.9)=31.21ms
       { expected_response:true }...: avg=10.78ms min=1.02ms   med=10.12ms max=228.55ms p(90)=15.92ms p(95)=18.6ms   p(99.9)=31.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 545790
     http_req_receiving.............: avg=98.91µs min=25.63µs  med=48.23µs max=44.77ms  p(90)=96.66µs p(95)=214.46µs p(99.9)=6ms    
     http_req_sending...............: avg=43.35µs min=4.81µs   med=9.01µs  max=181.05ms p(90)=16.26µs p(95)=108.74µs p(99.9)=4.47ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.63ms min=977.82µs med=10ms    max=219.84ms p(90)=15.71ms p(95)=18.35ms  p(99.9)=30.71ms
     http_reqs......................: 545790  4542.923244/s
     iteration_duration.............: avg=10.98ms min=1.25ms   med=10.31ms max=340.37ms p(90)=16.13ms p(95)=18.82ms  p(99.9)=31.53ms
     iterations.....................: 545690  4542.090886/s
     success_rate...................: 100.00% ✓ 545690      ✗ 0     
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

     checks.........................: 100.00% ✓ 1527084     ✗ 0     
     data_received..................: 45 GB   371 MB/s
     data_sent......................: 612 MB  5.1 MB/s
     http_req_blocked...............: avg=3.19µs  min=992ns    med=2.52µs  max=4.8ms    p(90)=3.94µs  p(95)=4.63µs   p(99.9)=39.82µs
     http_req_connecting............: avg=236ns   min=0s       med=0s      max=4.55ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.57ms min=748.38µs med=11.21ms max=270.78ms p(90)=17.27ms p(95)=19.68ms  p(99.9)=31.25ms
       { expected_response:true }...: avg=11.57ms min=748.38µs med=11.21ms max=270.78ms p(90)=17.27ms p(95)=19.68ms  p(99.9)=31.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 509128
     http_req_receiving.............: avg=99.17µs min=23.67µs  med=49.89µs max=196.35ms p(90)=97.87µs p(95)=220.23µs p(99.9)=5.32ms 
     http_req_sending...............: avg=42.61µs min=4.48µs   med=9.25µs  max=74.46ms  p(90)=16.3µs  p(95)=119.14µs p(99.9)=3.85ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.43ms min=678.4µs  med=11.08ms max=270.33ms p(90)=17.09ms p(95)=19.45ms  p(99.9)=30.89ms
     http_reqs......................: 509128  4238.917338/s
     iteration_duration.............: avg=11.77ms min=1.18ms   med=11.4ms  max=295.89ms p(90)=17.47ms p(95)=19.9ms   p(99.9)=31.53ms
     iterations.....................: 509028  4238.084755/s
     success_rate...................: 100.00% ✓ 509028      ✗ 0     
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

     checks.........................: 100.00% ✓ 1098927     ✗ 0     
     data_received..................: 32 GB   267 MB/s
     data_sent......................: 440 MB  3.7 MB/s
     http_req_blocked...............: avg=2.96µs  min=881ns  med=2.47µs  max=3.17ms   p(90)=4.06µs  p(95)=4.85µs   p(99.9)=38.92µs
     http_req_connecting............: avg=120ns   min=0s     med=0s      max=3.07ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.16ms min=1.42ms med=16.13ms max=279.75ms p(90)=21.62ms p(95)=23.15ms  p(99.9)=30.95ms
       { expected_response:true }...: avg=16.16ms min=1.42ms med=16.13ms max=279.75ms p(90)=21.62ms p(95)=23.15ms  p(99.9)=30.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 366409
     http_req_receiving.............: avg=79.23µs min=25µs   med=52.93µs max=176.64ms p(90)=99.08µs p(95)=194.77µs p(99.9)=1.5ms  
     http_req_sending...............: avg=35.11µs min=4.52µs med=10.12µs max=77.15ms  p(90)=18.45µs p(95)=114.69µs p(99.9)=1.45ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.05ms min=1.34ms med=16.02ms max=278.19ms p(90)=21.5ms  p(95)=23.03ms  p(99.9)=30.79ms
     http_reqs......................: 366409  3048.794692/s
     iteration_duration.............: avg=16.36ms min=2.95ms med=16.33ms max=290.38ms p(90)=21.82ms p(95)=23.35ms  p(99.9)=31.24ms
     iterations.....................: 366309  3047.962617/s
     success_rate...................: 100.00% ✓ 366309      ✗ 0     
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

     checks.........................: 100.00% ✓ 662226      ✗ 0     
     data_received..................: 19 GB   161 MB/s
     data_sent......................: 265 MB  2.2 MB/s
     http_req_blocked...............: avg=3.16µs  min=862ns   med=2.26µs  max=4.2ms    p(90)=4.15µs   p(95)=5.18µs  p(99.9)=34.24µs
     http_req_connecting............: avg=428ns   min=0s      med=0s      max=4.16ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.93ms min=1.85ms  med=26.39ms max=312.54ms p(90)=34.9ms   p(95)=37.69ms p(99.9)=51.79ms
       { expected_response:true }...: avg=26.93ms min=1.85ms  med=26.39ms max=312.54ms p(90)=34.9ms   p(95)=37.69ms p(99.9)=51.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 220842
     http_req_receiving.............: avg=82.41µs min=28.24µs med=57.32µs max=33.27ms  p(90)=116.66µs p(95)=179.2µs p(99.9)=1.38ms 
     http_req_sending...............: avg=32.18µs min=4.81µs  med=9.82µs  max=117.82ms p(90)=22µs     p(95)=95.63µs p(99.9)=1.46ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.82ms min=1.77ms  med=26.28ms max=312.24ms p(90)=34.78ms  p(95)=37.56ms p(99.9)=51.46ms
     http_reqs......................: 220842  1836.422657/s
     iteration_duration.............: avg=27.17ms min=6.64ms  med=26.6ms  max=322.78ms p(90)=35.12ms  p(95)=37.92ms p(99.9)=52.13ms
     iterations.....................: 220742  1835.591102/s
     success_rate...................: 100.00% ✓ 220742      ✗ 0     
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

     checks.........................: 100.00% ✓ 542271      ✗ 0     
     data_received..................: 16 GB   132 MB/s
     data_sent......................: 217 MB  1.8 MB/s
     http_req_blocked...............: avg=3.82µs  min=892ns   med=2.14µs  max=10.44ms  p(90)=3.59µs  p(95)=4.23µs   p(99.9)=25.97µs 
     http_req_connecting............: avg=1.36µs  min=0s      med=0s      max=10.38ms  p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.96ms min=2.04ms  med=32.08ms max=309.39ms p(90)=47.58ms p(95)=52.41ms  p(99.9)=74.85ms 
       { expected_response:true }...: avg=32.96ms min=2.04ms  med=32.08ms max=309.39ms p(90)=47.58ms p(95)=52.41ms  p(99.9)=74.85ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 180857
     http_req_receiving.............: avg=69.51µs min=25.21µs med=57.57µs max=205.81ms p(90)=93.55µs p(95)=107.77µs p(99.9)=695.5µs 
     http_req_sending...............: avg=20.42µs min=4.56µs  med=10.22µs max=77.81ms  p(90)=16.74µs p(95)=20.29µs  p(99.9)=764.42µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.87ms min=1.96ms  med=32ms    max=299.45ms p(90)=47.48ms p(95)=52.32ms  p(99.9)=74.7ms  
     http_reqs......................: 180857  1503.808555/s
     iteration_duration.............: avg=33.18ms min=4.15ms  med=32.28ms max=321.55ms p(90)=47.77ms p(95)=52.6ms   p(99.9)=75.16ms 
     iterations.....................: 180757  1502.977065/s
     success_rate...................: 100.00% ✓ 180757      ✗ 0     
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

     checks.........................: 100.00% ✓ 523002      ✗ 0     
     data_received..................: 15 GB   127 MB/s
     data_sent......................: 210 MB  1.7 MB/s
     http_req_blocked...............: avg=3.24µs  min=962ns   med=2.38µs  max=4.06ms   p(90)=4.09µs  p(95)=4.82µs   p(99.9)=34.68µs 
     http_req_connecting............: avg=519ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.17ms min=1.98ms  med=33.22ms max=301.45ms p(90)=48.59ms p(95)=53.62ms  p(99.9)=80.28ms 
       { expected_response:true }...: avg=34.17ms min=1.98ms  med=33.22ms max=301.45ms p(90)=48.59ms p(95)=53.62ms  p(99.9)=80.28ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 174434
     http_req_receiving.............: avg=69.31µs min=25.82µs med=57.91µs max=85.69ms  p(90)=94.01µs p(95)=109.78µs p(99.9)=785.05µs
     http_req_sending...............: avg=21.19µs min=4.83µs  med=11.16µs max=143.41ms p(90)=17.81µs p(95)=21.4µs   p(99.9)=735.13µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.08ms min=1.93ms  med=33.14ms max=300.81ms p(90)=48.49ms p(95)=53.53ms  p(99.9)=80.2ms  
     http_reqs......................: 174434  1450.390537/s
     iteration_duration.............: avg=34.4ms  min=5.76ms  med=33.43ms max=319.11ms p(90)=48.81ms p(95)=53.83ms  p(99.9)=80.93ms 
     iterations.....................: 174334  1449.559053/s
     success_rate...................: 100.00% ✓ 174334      ✗ 0     
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

     checks.........................: 100.00% ✓ 197103     ✗ 0    
     data_received..................: 5.8 GB  48 MB/s
     data_sent......................: 79 MB   656 kB/s
     http_req_blocked...............: avg=5µs     min=1.07µs  med=3.19µs  max=4.25ms   p(90)=4.7µs    p(95)=5.35µs   p(99.9)=47.69µs 
     http_req_connecting............: avg=1.57µs  min=0s      med=0s      max=4.21ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=90.95ms min=3.9ms   med=88.22ms max=326.3ms  p(90)=109.72ms p(95)=120.34ms p(99.9)=215.41ms
       { expected_response:true }...: avg=90.95ms min=3.9ms   med=88.22ms max=326.3ms  p(90)=109.72ms p(95)=120.34ms p(99.9)=215.41ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65801
     http_req_receiving.............: avg=82.49µs min=28.85µs med=74.44µs max=41.03ms  p(90)=110.12µs p(95)=123.36µs p(99.9)=579.08µs
     http_req_sending...............: avg=23.54µs min=5.41µs  med=14.75µs max=76.59ms  p(90)=20.79µs  p(95)=22.89µs  p(99.9)=590.55µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=90.84ms min=3.76ms  med=88.12ms max=325.88ms p(90)=109.62ms p(95)=120.22ms p(99.9)=215.19ms
     http_reqs......................: 65801   545.883118/s
     iteration_duration.............: avg=91.33ms min=23.83ms med=88.47ms max=341.5ms  p(90)=109.99ms p(95)=120.66ms p(99.9)=217.63ms
     iterations.....................: 65701   545.053521/s
     success_rate...................: 100.00% ✓ 65701      ✗ 0    
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

     checks.........................: 100.00% ✓ 175695     ✗ 0    
     data_received..................: 5.1 GB  43 MB/s
     data_sent......................: 70 MB   584 kB/s
     http_req_blocked...............: avg=4.58µs   min=1.09µs  med=2.92µs   max=3.54ms   p(90)=4.27µs   p(95)=4.82µs   p(99.9)=51.35µs 
     http_req_connecting............: avg=1.48µs   min=0s      med=0s       max=3.51ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=102.06ms min=4.49ms  med=100.2ms  max=308.95ms p(90)=137.71ms p(95)=148.93ms p(99.9)=193.6ms 
       { expected_response:true }...: avg=102.06ms min=4.49ms  med=100.2ms  max=308.95ms p(90)=137.71ms p(95)=148.93ms p(99.9)=193.6ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 58665
     http_req_receiving.............: avg=79.73µs  min=28.21µs med=71.45µs  max=100.86ms p(90)=101.77µs p(95)=114.19µs p(99.9)=511µs   
     http_req_sending...............: avg=25.19µs  min=4.88µs  med=14.61µs  max=136.69ms p(90)=19.89µs  p(95)=21.74µs  p(99.9)=492.52µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.95ms min=4.38ms  med=100.11ms max=295.32ms p(90)=137.61ms p(95)=148.81ms p(99.9)=193.28ms
     http_reqs......................: 58665   486.491771/s
     iteration_duration.............: avg=102.47ms min=14.71ms med=100.49ms max=319.08ms p(90)=137.98ms p(95)=149.22ms p(99.9)=195.09ms
     iterations.....................: 58565   485.6625/s
     success_rate...................: 100.00% ✓ 58565      ✗ 0    
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

     checks.........................: 100.00% ✓ 144213     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   479 kB/s
     http_req_blocked...............: avg=5.24µs   min=1.09µs  med=3.1µs    max=3.48ms   p(90)=4.48µs   p(95)=5.04µs   p(99.9)=473.34µs
     http_req_connecting............: avg=1.94µs   min=0s      med=0s       max=3.44ms   p(90)=0s       p(95)=0s       p(99.9)=376.62µs
     http_req_duration..............: avg=124.36ms min=5.44ms  med=121.95ms max=322.74ms p(90)=162.44ms p(95)=175.23ms p(99.9)=227.22ms
       { expected_response:true }...: avg=124.36ms min=5.44ms  med=121.95ms max=322.74ms p(90)=162.44ms p(95)=175.23ms p(99.9)=227.22ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48171
     http_req_receiving.............: avg=80.58µs  min=30.08µs med=73.7µs   max=105.2ms  p(90)=103.85µs p(95)=115.62µs p(99.9)=483.44µs
     http_req_sending...............: avg=25.61µs  min=4.92µs  med=14.76µs  max=157.07ms p(90)=19.27µs  p(95)=20.95µs  p(99.9)=431.98µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=124.25ms min=5.32ms  med=121.86ms max=322.63ms p(90)=162.34ms p(95)=175.11ms p(99.9)=226.43ms
     http_reqs......................: 48171   399.091366/s
     iteration_duration.............: avg=124.85ms min=24.86ms med=122.27ms max=344.61ms p(90)=162.7ms  p(95)=175.5ms  p(99.9)=229.03ms
     iterations.....................: 48071   398.262877/s
     success_rate...................: 100.00% ✓ 48071      ✗ 0    
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

     checks.........................: 100.00% ✓ 99585      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   330 kB/s
     http_req_blocked...............: avg=6.19µs   min=1.07µs  med=3.08µs   max=4.34ms   p(90)=4.38µs   p(95)=4.93µs   p(99.9)=1.34ms  
     http_req_connecting............: avg=2.93µs   min=0s      med=0s       max=4.3ms    p(90)=0s       p(95)=0s       p(99.9)=1.31ms  
     http_req_duration..............: avg=180.05ms min=7.61ms  med=178.59ms max=385.57ms p(90)=204.29ms p(95)=210.9ms  p(99.9)=276.53ms
       { expected_response:true }...: avg=180.05ms min=7.61ms  med=178.59ms max=385.57ms p(90)=204.29ms p(95)=210.9ms  p(99.9)=276.53ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33295
     http_req_receiving.............: avg=90.12µs  min=26.72µs med=82.74µs  max=113.59ms p(90)=111.18µs p(95)=121.77µs p(99.9)=486.99µs
     http_req_sending...............: avg=25.55µs  min=5.08µs  med=16.18µs  max=88.4ms   p(90)=20.37µs  p(95)=22.25µs  p(99.9)=527.96µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=179.94ms min=7.51ms  med=178.47ms max=385.23ms p(90)=204.2ms  p(95)=210.79ms p(99.9)=275.83ms
     http_reqs......................: 33295   275.216621/s
     iteration_duration.............: avg=180.85ms min=40.54ms med=179.23ms max=395.47ms p(90)=204.57ms p(95)=211.23ms p(99.9)=280.45ms
     iterations.....................: 33195   274.39002/s
     success_rate...................: 100.00% ✓ 33195      ✗ 0    
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

     checks.........................: 100.00% ✓ 99201      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   329 kB/s
     http_req_blocked...............: avg=6.78µs   min=1.55µs  med=3.69µs   max=3.95ms   p(90)=5.15µs   p(95)=5.78µs   p(99.9)=1.34ms  
     http_req_connecting............: avg=2.82µs   min=0s      med=0s       max=3.91ms   p(90)=0s       p(95)=0s       p(99.9)=1.31ms  
     http_req_duration..............: avg=180.79ms min=5.66ms  med=163.33ms max=793.63ms p(90)=207.15ms p(95)=234.39ms p(99.9)=692.93ms
       { expected_response:true }...: avg=180.79ms min=5.66ms  med=163.33ms max=793.63ms p(90)=207.15ms p(95)=234.39ms p(99.9)=692.93ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33167
     http_req_receiving.............: avg=91.99µs  min=33.45µs med=86.58µs  max=42.63ms  p(90)=116.07µs p(95)=127.61µs p(99.9)=683.77µs
     http_req_sending...............: avg=22.26µs  min=5.7µs   med=17.57µs  max=38.5ms   p(90)=22.16µs  p(95)=24µs     p(99.9)=546.13µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.68ms min=5.57ms  med=163.21ms max=793.56ms p(90)=207.03ms p(95)=234.24ms p(99.9)=692.83ms
     http_reqs......................: 33167   274.096508/s
     iteration_duration.............: avg=181.59ms min=73.54ms med=163.66ms max=793.86ms p(90)=207.46ms p(95)=234.91ms p(99.9)=693.29ms
     iterations.....................: 33067   273.270095/s
     success_rate...................: 100.00% ✓ 33067      ✗ 0    
     vus............................: 5       min=5        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

