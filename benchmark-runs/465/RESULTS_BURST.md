## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,738 | 4,768 | 4,602 | 1.6% | 414 MB | 89.5 KB |  |
| fusion-net-11 | 16.7.3 | 4,646 | 4,740 | 4,637 | 1.0% | 418 MB | 92.1 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,629 | 4,631 | 4,617 | 0.1% | 420 MB | 92.9 KB |  |
| fusion-aot-11 | 16.7.3 | 4,524 | 4,535 | 4,436 | 1.0% | 182 MB | 41.1 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,490 | 4,582 | 4,457 | 1.1% | 179 MB | 40.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,450 | 4,554 | 4,420 | 1.4% | 408 MB | 93.9 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,367 | 4,373 | 4,351 | 0.2% | 183 MB | 42.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,259 | 4,279 | 4,247 | 0.3% | 194 MB | 46.5 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,148 | 4,208 | 4,141 | 0.7% | 2,302 MB | 568.2 KB |  |
| hive-router | v0.3.10 | 2,771 | 2,789 | 2,761 | 0.4% | 197 MB | 72.6 KB |  |
| caliban | 3.2.0 | 1,440 | 1,440 | 1,438 | 0.1% | 10,771 MB | 7,659.1 KB |  |
| cosmo | 0.365.2 | 1,301 | 1,303 | 1,296 | 0.2% | 631 MB | 496.4 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 504 | 508 | 499 | 0.7% | 3,163 MB | 6,427.2 KB |  |
| hive-gateway | 2.15.6 | 246 | 247 | 243 | 0.6% | 4,044 MB | 16,835.1 KB |  |
| apollo-gateway | 2.14.4 | 241 | 241 | 240 | 0.2% | 2,491 MB | 10,585.9 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (3495 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (3993 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (148172 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 863628      ✗ 0     
     data_received..................: 25 GB   415 MB/s
     data_sent......................: 347 MB  5.7 MB/s
     http_req_blocked...............: avg=58.68µs  min=792ns    med=2.04µs  max=169.62ms p(90)=3.63µs   p(95)=4.72µs   p(99.9)=20.84ms 
     http_req_connecting............: avg=54.46µs  min=0s       med=0s      max=113.02ms p(90)=0s       p(95)=0s       p(99.9)=20.71ms 
     http_req_duration..............: avg=47.93ms  min=760.43µs med=40.34ms max=320.66ms p(90)=100.99ms p(95)=125.69ms p(99.9)=175.85ms
       { expected_response:true }...: avg=47.93ms  min=760.43µs med=40.34ms max=320.66ms p(90)=100.99ms p(95)=125.69ms p(99.9)=175.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288876
     http_req_receiving.............: avg=330.47µs min=24.63µs  med=50.97µs max=128.76ms p(90)=208.18µs p(95)=361.95µs p(99.9)=43.05ms 
     http_req_sending...............: avg=141.55µs min=3.86µs   med=8.38µs  max=264.99ms p(90)=16µs     p(95)=113.76µs p(99.9)=26.56ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.45ms  min=722.83µs med=40.04ms max=311.75ms p(90)=99.83ms  p(95)=124.49ms p(99.9)=170.31ms
     http_reqs......................: 288876  4738.551464/s
     iteration_duration.............: avg=49.47ms  min=1.21ms   med=41.18ms max=328.72ms p(90)=104.05ms p(95)=130.52ms p(99.9)=199.2ms 
     iterations.....................: 287876  4722.148054/s
     success_rate...................: 100.00% ✓ 287876      ✗ 0     
     vus............................: 56      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 846282      ✗ 0     
     data_received..................: 25 GB   407 MB/s
     data_sent......................: 340 MB  5.6 MB/s
     http_req_blocked...............: avg=79µs     min=961ns    med=2.6µs   max=168.41ms p(90)=4.17µs   p(95)=5.39µs   p(99.9)=31.33ms 
     http_req_connecting............: avg=73.94µs  min=0s       med=0s      max=135.61ms p(90)=0s       p(95)=0s       p(99.9)=30.47ms 
     http_req_duration..............: avg=48.26ms  min=749.48µs med=40.29ms max=253.4ms  p(90)=102.23ms p(95)=126.58ms p(99.9)=180ms   
       { expected_response:true }...: avg=48.26ms  min=749.48µs med=40.29ms max=253.4ms  p(90)=102.23ms p(95)=126.58ms p(99.9)=180ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 283094
     http_req_receiving.............: avg=344.6µs  min=23.13µs  med=53.61µs max=139.61ms p(90)=216.45µs p(95)=372.15µs p(99.9)=47.95ms 
     http_req_sending...............: avg=159.85µs min=4.05µs   med=8.97µs  max=88.92ms  p(90)=17.9µs   p(95)=120.75µs p(99.9)=28.75ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.76ms  min=710.37µs med=39.96ms max=240.54ms p(90)=101.02ms p(95)=125.43ms p(99.9)=176.07ms
     http_reqs......................: 283094  4646.088016/s
     iteration_duration.............: avg=50.47ms  min=1.19ms   med=41.26ms max=388.23ms p(90)=107.81ms p(95)=134.51ms p(99.9)=215.61ms
     iterations.....................: 282094  4629.676195/s
     success_rate...................: 100.00% ✓ 282094      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 845568      ✗ 0     
     data_received..................: 25 GB   405 MB/s
     data_sent......................: 340 MB  5.6 MB/s
     http_req_blocked...............: avg=57.95µs  min=792ns    med=2.04µs  max=110.41ms p(90)=3.66µs   p(95)=4.82µs   p(99.9)=20.35ms 
     http_req_connecting............: avg=54.85µs  min=0s       med=0s      max=110.32ms p(90)=0s       p(95)=0s       p(99.9)=19.98ms 
     http_req_duration..............: avg=48.86ms  min=892.31µs med=41.26ms max=290.33ms p(90)=103.74ms p(95)=128.87ms p(99.9)=181ms   
       { expected_response:true }...: avg=48.86ms  min=892.31µs med=41.26ms max=290.33ms p(90)=103.74ms p(95)=128.87ms p(99.9)=181ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 282856
     http_req_receiving.............: avg=318.6µs  min=23.03µs  med=52.13µs max=104.18ms p(90)=206.99µs p(95)=370.34µs p(99.9)=45.72ms 
     http_req_sending...............: avg=143.82µs min=4.13µs   med=8.66µs  max=180.7ms  p(90)=17.4µs   p(95)=118.22µs p(99.9)=25.2ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.4ms   min=854.08µs med=40.95ms max=264.97ms p(90)=102.69ms p(95)=127.77ms p(99.9)=176.37ms
     http_reqs......................: 282856  4629.003392/s
     iteration_duration.............: avg=50.54ms  min=1.4ms    med=42.06ms max=324.46ms p(90)=107.71ms p(95)=134.3ms  p(99.9)=209.68ms
     iterations.....................: 281856  4612.638162/s
     success_rate...................: 100.00% ✓ 281856      ✗ 0     
     vus............................: 61      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 825633     ✗ 0     
     data_received..................: 24 GB   396 MB/s
     data_sent......................: 332 MB  5.4 MB/s
     http_req_blocked...............: avg=41.05µs  min=792ns    med=1.94µs  max=137.2ms  p(90)=3.47µs   p(95)=4.52µs   p(99.9)=10.53ms 
     http_req_connecting............: avg=37.77µs  min=0s       med=0s      max=122.08ms p(90)=0s       p(95)=0s       p(99.9)=10.26ms 
     http_req_duration..............: avg=50.75ms  min=858.47µs med=42.49ms max=341.16ms p(90)=107.78ms p(95)=133.57ms p(99.9)=186.91ms
       { expected_response:true }...: avg=50.75ms  min=858.47µs med=42.49ms max=341.16ms p(90)=107.78ms p(95)=133.57ms p(99.9)=186.91ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 276211
     http_req_receiving.............: avg=251.63µs min=24.48µs  med=48.62µs max=114.46ms p(90)=211.7µs  p(95)=366µs    p(99.9)=33.99ms 
     http_req_sending...............: avg=111.1µs  min=4.18µs   med=8.23µs  max=101.12ms p(90)=16.27µs  p(95)=119.94µs p(99.9)=20.06ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.39ms  min=803.78µs med=42.26ms max=332.06ms p(90)=107.03ms p(95)=132.71ms p(99.9)=183.94ms
     http_reqs......................: 276211  4524.86647/s
     iteration_duration.............: avg=51.76ms  min=1.2ms    med=43.24ms max=350.68ms p(90)=109.9ms  p(95)=136.16ms p(99.9)=199.33ms
     iterations.....................: 275211  4508.48455/s
     success_rate...................: 100.00% ✓ 275211     ✗ 0     
     vus............................: 58      min=0        max=498 
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 819318      ✗ 0     
     data_received..................: 24 GB   393 MB/s
     data_sent......................: 329 MB  5.4 MB/s
     http_req_blocked...............: avg=59.8µs   min=941ns    med=2.55µs  max=118.68ms p(90)=4.2µs    p(95)=5.41µs   p(99.9)=21.12ms 
     http_req_connecting............: avg=56.19µs  min=0s       med=0s      max=118.61ms p(90)=0s       p(95)=0s       p(99.9)=20.49ms 
     http_req_duration..............: avg=50.53ms  min=842.61µs med=41.75ms max=322.03ms p(90)=110.35ms p(95)=135.89ms p(99.9)=191.26ms
       { expected_response:true }...: avg=50.53ms  min=842.61µs med=41.75ms max=322.03ms p(90)=110.35ms p(95)=135.89ms p(99.9)=191.26ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 274106
     http_req_receiving.............: avg=346.34µs min=24.72µs  med=51.62µs max=109.4ms  p(90)=226.17µs p(95)=400.65µs p(99.9)=49.94ms 
     http_req_sending...............: avg=139.6µs  min=4.16µs   med=9.03µs  max=113.02ms p(90)=18.1µs   p(95)=129.06µs p(99.9)=24.67ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.04ms  min=798.05µs med=41.46ms max=321.82ms p(90)=109.27ms p(95)=134.63ms p(99.9)=183.43ms
     http_reqs......................: 274106  4490.524951/s
     iteration_duration.............: avg=52.16ms  min=1.29ms   med=42.79ms max=331.41ms p(90)=113.4ms  p(95)=140.15ms p(99.9)=214.61ms
     iterations.....................: 273106  4474.142512/s
     success_rate...................: 100.00% ✓ 273106      ✗ 0     
     vus............................: 59      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 813222      ✗ 0     
     data_received..................: 24 GB   389 MB/s
     data_sent......................: 327 MB  5.3 MB/s
     http_req_blocked...............: avg=61.48µs  min=771ns    med=2.52µs  max=128.33ms p(90)=4.2µs    p(95)=5.41µs   p(99.9)=20.58ms 
     http_req_connecting............: avg=57.73µs  min=0s       med=0s      max=128.21ms p(90)=0s       p(95)=0s       p(99.9)=20.15ms 
     http_req_duration..............: avg=50.68ms  min=921.3µs  med=42.08ms max=325.14ms p(90)=107.15ms p(95)=135.11ms p(99.9)=188.33ms
       { expected_response:true }...: avg=50.68ms  min=921.3µs  med=42.08ms max=325.14ms p(90)=107.15ms p(95)=135.11ms p(99.9)=188.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 272074
     http_req_receiving.............: avg=328.07µs min=25.36µs  med=53.33µs max=121.72ms p(90)=224.49µs p(95)=390.04µs p(99.9)=43.89ms 
     http_req_sending...............: avg=144.82µs min=3.94µs   med=9.23µs  max=187.96ms p(90)=19.41µs  p(95)=127.1µs  p(99.9)=25.57ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.21ms  min=870.97µs med=41.76ms max=324.83ms p(90)=105.97ms p(95)=133.64ms p(99.9)=185.26ms
     http_reqs......................: 272074  4450.632767/s
     iteration_duration.............: avg=52.55ms  min=1.42ms   med=42.96ms max=332.85ms p(90)=111.66ms p(95)=141.03ms p(99.9)=218.18ms
     iterations.....................: 271074  4434.274597/s
     success_rate...................: 100.00% ✓ 271074      ✗ 0     
     vus............................: 63      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 798693      ✗ 0     
     data_received..................: 23 GB   382 MB/s
     data_sent......................: 321 MB  5.2 MB/s
     http_req_blocked...............: avg=37.63µs  min=801ns    med=1.97µs  max=84.71ms  p(90)=3.51µs   p(95)=4.63µs   p(99.9)=9.57ms  
     http_req_connecting............: avg=34.61µs  min=0s       med=0s      max=84.65ms  p(90)=0s       p(95)=0s       p(99.9)=9.3ms   
     http_req_duration..............: avg=52.62ms  min=980.86µs med=44.22ms max=320.83ms p(90)=110.52ms p(95)=135.69ms p(99.9)=192.38ms
       { expected_response:true }...: avg=52.62ms  min=980.86µs med=44.22ms max=320.83ms p(90)=110.52ms p(95)=135.69ms p(99.9)=192.38ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 267231
     http_req_receiving.............: avg=282.51µs min=25.86µs  med=49.03µs max=109.33ms p(90)=218.01µs p(95)=366.87µs p(99.9)=37.37ms 
     http_req_sending...............: avg=105.98µs min=3.99µs   med=8.33µs  max=208.65ms p(90)=17.26µs  p(95)=119.68µs p(99.9)=19.16ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.23ms  min=933.41µs med=43.98ms max=309.89ms p(90)=109.71ms p(95)=134.57ms p(99.9)=186.22ms
     http_reqs......................: 267231  4367.422542/s
     iteration_duration.............: avg=53.51ms  min=1.58ms   med=44.9ms  max=331.56ms p(90)=112.41ms p(95)=137.41ms p(99.9)=206.53ms
     iterations.....................: 266231  4351.079294/s
     success_rate...................: 100.00% ✓ 266231      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 779223      ✗ 0     
     data_received..................: 23 GB   373 MB/s
     data_sent......................: 313 MB  5.1 MB/s
     http_req_blocked...............: avg=38.84µs  min=781ns    med=2.01µs  max=92.76ms  p(90)=3.65µs   p(95)=4.84µs   p(99.9)=10.36ms 
     http_req_connecting............: avg=35.73µs  min=0s       med=0s      max=92.7ms   p(90)=0s       p(95)=0s       p(99.9)=10.03ms 
     http_req_duration..............: avg=53.99ms  min=1ms      med=46.32ms max=277.8ms  p(90)=113.25ms p(95)=139.11ms p(99.9)=194.68ms
       { expected_response:true }...: avg=53.99ms  min=1ms      med=46.32ms max=277.8ms  p(90)=113.25ms p(95)=139.11ms p(99.9)=194.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 260741
     http_req_receiving.............: avg=246.68µs min=25.86µs  med=50.1µs  max=116.86ms p(90)=219.09µs p(95)=373.28µs p(99.9)=32.7ms  
     http_req_sending...............: avg=112.76µs min=4.18µs   med=8.36µs  max=148.23ms p(90)=17.78µs  p(95)=123.25µs p(99.9)=20.24ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.63ms  min=954.83µs med=46.07ms max=259.28ms p(90)=112.5ms  p(95)=138.16ms p(99.9)=192.69ms
     http_reqs......................: 260741  4259.689858/s
     iteration_duration.............: avg=54.85ms  min=1.6ms    med=46.86ms max=316.04ms p(90)=114.85ms p(95)=141.09ms p(99.9)=205.28ms
     iterations.....................: 259741  4243.352996/s
     success_rate...................: 100.00% ✓ 259741      ✗ 0     
     vus............................: 67      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 755391      ✗ 0     
     data_received..................: 22 GB   363 MB/s
     data_sent......................: 304 MB  5.0 MB/s
     http_req_blocked...............: avg=55.19µs  min=892ns    med=2.75µs  max=123.73ms p(90)=4.55µs   p(95)=5.76µs   p(99.9)=16.18ms 
     http_req_connecting............: avg=51.49µs  min=0s       med=0s      max=110.63ms p(90)=0s       p(95)=0s       p(99.9)=15.64ms 
     http_req_duration..............: avg=55.12ms  min=704.31µs med=46.07ms max=326.6ms  p(90)=118.21ms p(95)=148.7ms  p(99.9)=215.92ms
       { expected_response:true }...: avg=55.12ms  min=704.31µs med=46.07ms max=326.6ms  p(90)=118.21ms p(95)=148.7ms  p(99.9)=215.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 252797
     http_req_receiving.............: avg=298.72µs min=25.64µs  med=53.07µs max=84.14ms  p(90)=227.71µs p(95)=408.73µs p(99.9)=43.01ms 
     http_req_sending...............: avg=133.19µs min=4.39µs   med=9.8µs   max=200.55ms p(90)=20.1µs   p(95)=137.85µs p(99.9)=22.38ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.69ms  min=659.15µs med=45.79ms max=317.86ms p(90)=117.21ms p(95)=147.77ms p(99.9)=210.81ms
     http_reqs......................: 252797  4148.555178/s
     iteration_duration.............: avg=56.58ms  min=1.36ms   med=46.94ms max=355.74ms p(90)=121.23ms p(95)=152.73ms p(99.9)=234.37ms
     iterations.....................: 251797  4132.144559/s
     success_rate...................: 100.00% ✓ 251797      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 509292      ✗ 0     
     data_received..................: 15 GB   242 MB/s
     data_sent......................: 205 MB  3.3 MB/s
     http_req_blocked...............: avg=15.88µs  min=811ns   med=2.33µs  max=50.55ms  p(90)=4.14µs   p(95)=5.43µs   p(99.9)=1.38ms  
     http_req_connecting............: avg=12.79µs  min=0s      med=0s      max=50.4ms   p(90)=0s       p(95)=0s       p(99.9)=1.28ms  
     http_req_duration..............: avg=83.24ms  min=1.32ms  med=78.28ms max=311.11ms p(90)=162.61ms p(95)=177.39ms p(99.9)=224.05ms
       { expected_response:true }...: avg=83.24ms  min=1.32ms  med=78.28ms max=311.11ms p(90)=162.61ms p(95)=177.39ms p(99.9)=224.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 170764
     http_req_receiving.............: avg=140.85µs min=25.53µs med=56.04µs max=137.43ms p(90)=176.62µs p(95)=353.63µs p(99.9)=13.53ms 
     http_req_sending...............: avg=69.28µs  min=4.57µs  med=10.19µs max=111.02ms p(90)=21.16µs  p(95)=125.74µs p(99.9)=9.09ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=83.03ms  min=1.28ms  med=78.08ms max=310.75ms p(90)=162.35ms p(95)=177.09ms p(99.9)=222.68ms
     http_reqs......................: 170764  2771.971897/s
     iteration_duration.............: avg=83.97ms  min=3.84ms  med=79.17ms max=339.64ms p(90)=163.01ms p(95)=177.8ms  p(99.9)=224.73ms
     iterations.....................: 169764  2755.739132/s
     success_rate...................: 100.00% ✓ 169764      ✗ 0     
     vus............................: 84      min=0         max=492 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 266457      ✗ 0    
     data_received..................: 7.9 GB  126 MB/s
     data_sent......................: 108 MB  1.7 MB/s
     http_req_blocked...............: avg=6.15µs   min=922ns   med=2.82µs   max=14.78ms  p(90)=4.89µs   p(95)=5.87µs   p(99.9)=505.38µs
     http_req_connecting............: avg=2.6µs    min=0s      med=0s       max=14.54ms  p(90)=0s       p(95)=0s       p(99.9)=412.42µs
     http_req_duration..............: avg=158.74ms min=1.94ms  med=134ms    max=999.03ms p(90)=324.83ms p(95)=388.97ms p(99.9)=710.6ms 
       { expected_response:true }...: avg=158.74ms min=1.94ms  med=134ms    max=999.03ms p(90)=324.83ms p(95)=388.97ms p(99.9)=710.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 89819
     http_req_receiving.............: avg=79.28µs  min=27.02µs med=61.38µs  max=137.52ms p(90)=102.46µs p(95)=120.64µs p(99.9)=1.65ms  
     http_req_sending...............: avg=34.96µs  min=5.06µs  med=12.77µs  max=168.63ms p(90)=20.66µs  p(95)=24.45µs  p(99.9)=3.9ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=158.63ms min=1.88ms  med=133.88ms max=998.98ms p(90)=324.74ms p(95)=388.87ms p(99.9)=710.49ms
     http_reqs......................: 89819   1440.406379/s
     iteration_duration.............: avg=160.78ms min=5.99ms  med=136.12ms max=999.2ms  p(90)=326.1ms  p(95)=390.45ms p(99.9)=712.12ms
     iterations.....................: 88819   1424.369612/s
     success_rate...................: 100.00% ✓ 88819       ✗ 0    
     vus............................: 72      min=0         max=494
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 240756      ✗ 0    
     data_received..................: 7.1 GB  114 MB/s
     data_sent......................: 98 MB   1.6 MB/s
     http_req_blocked...............: avg=4.99µs   min=952ns   med=2.18µs   max=5.31ms   p(90)=3.72µs   p(95)=4.64µs   p(99.9)=424.71µs
     http_req_connecting............: avg=2.15µs   min=0s      med=0s       max=5.11ms   p(90)=0s       p(95)=0s       p(99.9)=278.49µs
     http_req_duration..............: avg=175.54ms min=1.98ms  med=174.24ms max=483.73ms p(90)=330.87ms p(95)=354.38ms p(99.9)=418.03ms
       { expected_response:true }...: avg=175.54ms min=1.98ms  med=174.24ms max=483.73ms p(90)=330.87ms p(95)=354.38ms p(99.9)=418.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81252
     http_req_receiving.............: avg=72.8µs   min=27.34µs med=60.6µs   max=18.7ms   p(90)=96.56µs  p(95)=111.34µs p(99.9)=1.03ms  
     http_req_sending...............: avg=28.45µs  min=4.33µs  med=10.01µs  max=151.4ms  p(90)=15.49µs  p(95)=18.62µs  p(99.9)=3.13ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.43ms min=1.92ms  med=174.12ms max=483.65ms p(90)=330.79ms p(95)=354.25ms p(99.9)=417.95ms
     http_reqs......................: 81252   1301.072059/s
     iteration_duration.............: avg=177.95ms min=4.32ms  med=176.75ms max=483.92ms p(90)=331.55ms p(95)=354.96ms p(99.9)=418.56ms
     iterations.....................: 80252   1285.059258/s
     success_rate...................: 100.00% ✓ 80252       ✗ 0    
     vus............................: 78      min=0         max=493
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 94800      ✗ 0    
     data_received..................: 2.9 GB  44 MB/s
     data_sent......................: 39 MB   606 kB/s
     http_req_blocked...............: avg=7.58µs   min=1.12µs  med=3.24µs   max=12.06ms  p(90)=5µs      p(95)=5.99µs   p(99.9)=671.69µs
     http_req_connecting............: avg=3.36µs   min=0s      med=0s       max=12ms     p(90)=0s       p(95)=0s       p(99.9)=639.94µs
     http_req_duration..............: avg=440.41ms min=3.71ms  med=411.62ms max=1.81s    p(90)=873.18ms p(95)=943.37ms p(99.9)=1.4s    
       { expected_response:true }...: avg=440.41ms min=3.71ms  med=411.62ms max=1.81s    p(90)=873.18ms p(95)=943.37ms p(99.9)=1.4s    
     http_req_failed................: 0.00%   ✓ 0          ✗ 32600
     http_req_receiving.............: avg=86.54µs  min=30.93µs med=74.91µs  max=49.25ms  p(90)=112.78µs p(95)=127.96µs p(99.9)=1.19ms  
     http_req_sending...............: avg=34.31µs  min=5.29µs  med=15.01µs  max=107.69ms p(90)=21.53µs  p(95)=24.41µs  p(99.9)=2.47ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=440.29ms min=3.61ms  med=411.52ms max=1.81s    p(90)=873.11ms p(95)=943.28ms p(99.9)=1.4s    
     http_reqs......................: 32600   504.938411/s
     iteration_duration.............: avg=454.58ms min=15.94ms med=432.82ms max=1.81s    p(90)=876.95ms p(95)=945.71ms p(99.9)=1.41s   
     iterations.....................: 31600   489.449503/s
     success_rate...................: 100.00% ✓ 31600      ✗ 0    
     vus............................: 84      min=0        max=498
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 47007      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   296 kB/s
     http_req_blocked...............: avg=14.97µs  min=1.25µs  med=3.72µs   max=11.93ms p(90)=5.59µs   p(95)=7.18µs  p(99.9)=2.34ms
     http_req_connecting............: avg=9.54µs   min=0s      med=0s       max=11.86ms p(90)=0s       p(95)=0s      p(99.9)=2.31ms
     http_req_duration..............: avg=872.89ms min=5.7ms   med=796.48ms max=4.44s   p(90)=1.72s    p(95)=1.98s   p(99.9)=4.05s 
       { expected_response:true }...: avg=872.89ms min=5.7ms   med=796.48ms max=4.44s   p(90)=1.72s    p(95)=1.98s   p(99.9)=4.05s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16669
     http_req_receiving.............: avg=99.01µs  min=35.29µs med=91.6µs   max=10.11ms p(90)=131.93µs p(95)=148.5µs p(99.9)=1.07ms
     http_req_sending...............: avg=27.05µs  min=5.96µs  med=18.49µs  max=14.77ms p(90)=23.88µs  p(95)=27.26µs p(99.9)=1.72ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s      p(99.9)=0s    
     http_req_waiting...............: avg=872.76ms min=5.62ms  med=796.38ms max=4.44s   p(90)=1.72s    p(95)=1.98s   p(99.9)=4.05s 
     http_reqs......................: 16669   246.772282/s
     iteration_duration.............: avg=928.62ms min=43.87ms med=852.73ms max=4.44s   p(90)=1.74s    p(95)=1.99s   p(99.9)=4.07s 
     iterations.....................: 15669   231.968018/s
     success_rate...................: 100.00% ✓ 15669      ✗ 0    
     vus............................: 91      min=0        max=500
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 46608      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   290 kB/s
     http_req_blocked...............: avg=14.68µs  min=1.19µs  med=3.21µs   max=10.85ms  p(90)=4.94µs   p(95)=6.47µs   p(99.9)=2.14ms  
     http_req_connecting............: avg=9.62µs   min=0s      med=0s       max=10.79ms  p(90)=0s       p(95)=0s       p(99.9)=2.04ms  
     http_req_duration..............: avg=878.42ms min=7.47ms  med=809.15ms max=2.94s    p(90)=1.8s     p(95)=1.9s     p(99.9)=2.58s   
       { expected_response:true }...: avg=878.42ms min=7.47ms  med=809.15ms max=2.94s    p(90)=1.8s     p(95)=1.9s     p(99.9)=2.58s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16536
     http_req_receiving.............: avg=99.89µs  min=33.26µs med=85.05µs  max=130.4ms  p(90)=123.46µs p(95)=139.77µs p(99.9)=952.33µs
     http_req_sending...............: avg=39.61µs  min=5.47µs  med=16.57µs  max=122.94ms p(90)=21.85µs  p(95)=25.57µs  p(99.9)=2.84ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=878.28ms min=7.36ms  med=809.05ms max=2.94s    p(90)=1.8s     p(95)=1.9s     p(99.9)=2.58s   
     http_reqs......................: 16536   241.667412/s
     iteration_duration.............: avg=934.98ms min=58.59ms med=878.61ms max=2.94s    p(90)=1.81s    p(95)=1.92s    p(99.9)=2.6s    
     iterations.....................: 15536   227.052788/s
     success_rate...................: 100.00% ✓ 15536      ✗ 0    
     vus............................: 75      min=0        max=496
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

