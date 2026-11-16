## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.14 | 4,763 | 4,773 | 4,668 | 0.9% | 410 MB | 88.0 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.14 | 4,736 | 4,785 | 4,665 | 1.2% | 421 MB | 90.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.14 | 4,725 | 4,741 | 4,550 | 1.7% | 153 MB | 33.1 KB |  |
| fusion-net-11 | 16.7.5 | 4,680 | 4,714 | 4,554 | 1.7% | 416 MB | 91.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.14 | 4,614 | 4,655 | 4,537 | 1.0% | 166 MB | 36.8 KB |  |
| fusion-aot-11 | 16.7.5 | 4,448 | 4,551 | 4,428 | 1.1% | 167 MB | 38.4 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,445 | 4,570 | 4,427 | 1.4% | 427 MB | 98.3 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,237 | 4,264 | 4,237 | 0.3% | 168 MB | 40.5 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,047 | 4,070 | 3,963 | 1.0% | 2,311 MB | 584.9 KB |  |
| hive-router | v0.3.10 | 2,781 | 2,794 | 2,760 | 0.4% | 165 MB | 60.9 KB |  |
| caliban | 3.2.0 | 1,422 | 1,423 | 1,420 | 0.1% | 10,604 MB | 7,636.3 KB |  |
| cosmo | 0.365.2 | 1,297 | 1,301 | 1,295 | 0.2% | 674 MB | 531.7 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 495 | 497 | 491 | 0.5% | 3,162 MB | 6,540.9 KB |  |
| hive-gateway | 2.15.6 | 250 | 253 | 249 | 0.7% | 4,144 MB | 16,975.0 KB |  |
| apollo-gateway | 2.14.4 | 240 | 241 | 238 | 0.5% | 2,473 MB | 10,553.3 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (13879 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (4819 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (150756 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.14)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 867636      ✗ 0     
     data_received..................: 25 GB   417 MB/s
     data_sent......................: 349 MB  5.7 MB/s
     http_req_blocked...............: avg=66.6µs   min=821ns    med=2.11µs  max=139.86ms p(90)=3.68µs   p(95)=4.75µs   p(99.9)=24.52ms 
     http_req_connecting............: avg=62.78µs  min=0s       med=0s      max=139.8ms  p(90)=0s       p(95)=0s       p(99.9)=23.78ms 
     http_req_duration..............: avg=47.27ms  min=741.86µs med=39.67ms max=487.44ms p(90)=99.88ms  p(95)=123.76ms p(99.9)=207.57ms
       { expected_response:true }...: avg=47.27ms  min=741.86µs med=39.67ms max=487.44ms p(90)=99.88ms  p(95)=123.76ms p(99.9)=207.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290212
     http_req_receiving.............: avg=504.29µs min=25.96µs  med=51.89µs max=401.64ms p(90)=210.16µs p(95)=362.66µs p(99.9)=65.57ms 
     http_req_sending...............: avg=152.25µs min=4.04µs   med=8.52µs  max=360.13ms p(90)=16.15µs  p(95)=115.28µs p(99.9)=27.4ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.62ms  min=693.49µs med=39.35ms max=313.29ms p(90)=98.59ms  p(95)=122.32ms p(99.9)=173.06ms
     http_reqs......................: 290212  4763.45787/s
     iteration_duration.............: avg=49.25ms  min=1.22ms   med=40.66ms max=556.01ms p(90)=104.44ms p(95)=130.49ms p(99.9)=236.8ms 
     iterations.....................: 289212  4747.044152/s
     success_rate...................: 100.00% ✓ 289212      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.14)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 862992      ✗ 0     
     data_received..................: 25 GB   415 MB/s
     data_sent......................: 347 MB  5.7 MB/s
     http_req_blocked...............: avg=69.41µs  min=802ns    med=2.23µs  max=142.1ms  p(90)=3.75µs   p(95)=4.82µs   p(99.9)=27.3ms  
     http_req_connecting............: avg=65.88µs  min=0s       med=0s      max=141.95ms p(90)=0s       p(95)=0s       p(99.9)=26.81ms 
     http_req_duration..............: avg=47.55ms  min=754.71µs med=39.87ms max=323.31ms p(90)=100.24ms p(95)=125.12ms p(99.9)=182.68ms
       { expected_response:true }...: avg=47.55ms  min=754.71µs med=39.87ms max=323.31ms p(90)=100.24ms p(95)=125.12ms p(99.9)=182.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288664
     http_req_receiving.............: avg=341.24µs min=25.29µs  med=52.47µs max=132.32ms p(90)=210.04µs p(95)=361.58µs p(99.9)=48.14ms 
     http_req_sending...............: avg=150.46µs min=3.99µs   med=8.68µs  max=200.68ms p(90)=16.04µs  p(95)=114.68µs p(99.9)=28.23ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.06ms  min=716.91µs med=39.55ms max=322.9ms  p(90)=99.02ms  p(95)=123.84ms p(99.9)=174.54ms
     http_reqs......................: 288664  4736.844489/s
     iteration_duration.............: avg=49.51ms  min=1.29ms   med=40.72ms max=374.48ms p(90)=105.01ms p(95)=131.94ms p(99.9)=208.08ms
     iterations.....................: 287664  4720.434946/s
     success_rate...................: 100.00% ✓ 287664      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.14)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 861333      ✗ 0     
     data_received..................: 25 GB   414 MB/s
     data_sent......................: 346 MB  5.7 MB/s
     http_req_blocked...............: avg=60.94µs  min=802ns    med=2.02µs  max=173.13ms p(90)=3.66µs   p(95)=4.78µs   p(99.9)=21.48ms 
     http_req_connecting............: avg=57.78µs  min=0s       med=0s      max=173.04ms p(90)=0s       p(95)=0s       p(99.9)=20.91ms 
     http_req_duration..............: avg=48.14ms  min=793.49µs med=40.26ms max=322.75ms p(90)=103.16ms p(95)=128.18ms p(99.9)=184.27ms
       { expected_response:true }...: avg=48.14ms  min=793.49µs med=40.26ms max=322.75ms p(90)=103.16ms p(95)=128.18ms p(99.9)=184.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288111
     http_req_receiving.............: avg=319.75µs min=25.05µs  med=50.97µs max=113.2ms  p(90)=213.04µs p(95)=377.26µs p(99.9)=44.1ms  
     http_req_sending...............: avg=137.64µs min=3.97µs   med=8.4µs   max=195.14ms p(90)=16.48µs  p(95)=119.67µs p(99.9)=25.17ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.68ms  min=751.97µs med=39.95ms max=299.59ms p(90)=102.11ms p(95)=127.11ms p(99.9)=178.56ms
     http_reqs......................: 288111  4725.590453/s
     iteration_duration.............: avg=49.61ms  min=1.27ms   med=41.05ms max=331.68ms p(90)=105.82ms p(95)=132.67ms p(99.9)=205.09ms
     iterations.....................: 287111  4709.188474/s
     success_rate...................: 100.00% ✓ 287111      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 853410      ✗ 0     
     data_received..................: 25 GB   410 MB/s
     data_sent......................: 343 MB  5.6 MB/s
     http_req_blocked...............: avg=61.2µs   min=791ns    med=2.02µs  max=121.53ms p(90)=3.63µs   p(95)=4.77µs   p(99.9)=22.39ms 
     http_req_connecting............: avg=57.86µs  min=0s       med=0s      max=121.42ms p(90)=0s       p(95)=0s       p(99.9)=22.27ms 
     http_req_duration..............: avg=48.49ms  min=764.8µs  med=40.73ms max=257.69ms p(90)=102.53ms p(95)=127.04ms p(99.9)=182.3ms 
       { expected_response:true }...: avg=48.49ms  min=764.8µs  med=40.73ms max=257.69ms p(90)=102.53ms p(95)=127.04ms p(99.9)=182.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 285470
     http_req_receiving.............: avg=344.24µs min=24.99µs  med=51.13µs max=132.7ms  p(90)=209.99µs p(95)=368.2µs  p(99.9)=50.17ms 
     http_req_sending...............: avg=140.29µs min=4.19µs   med=8.4µs   max=146.01ms p(90)=16.86µs  p(95)=118.09µs p(99.9)=25.48ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48ms     min=726.77µs med=40.43ms max=235.46ms p(90)=101.4ms  p(95)=125.78ms p(99.9)=175.3ms 
     http_reqs......................: 285470  4680.901791/s
     iteration_duration.............: avg=50.07ms  min=1.18ms   med=41.6ms  max=361.3ms  p(90)=106.03ms p(95)=131.38ms p(99.9)=202.64ms
     iterations.....................: 284470  4664.504615/s
     success_rate...................: 100.00% ✓ 284470      ✗ 0     
     vus............................: 56      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.14)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 841494      ✗ 0     
     data_received..................: 25 GB   404 MB/s
     data_sent......................: 338 MB  5.5 MB/s
     http_req_blocked...............: avg=57.37µs  min=851ns    med=2.16µs  max=120.65ms p(90)=3.87µs   p(95)=5.05µs   p(99.9)=18.89ms 
     http_req_connecting............: avg=53.81µs  min=0s       med=0s      max=120.54ms p(90)=0s       p(95)=0s       p(99.9)=18.15ms 
     http_req_duration..............: avg=49.16ms  min=800.71µs med=40.83ms max=387.61ms p(90)=105.83ms p(95)=131.83ms p(99.9)=198.01ms
       { expected_response:true }...: avg=49.16ms  min=800.71µs med=40.83ms max=387.61ms p(90)=105.83ms p(95)=131.83ms p(99.9)=198.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281498
     http_req_receiving.............: avg=359.59µs min=24.66µs  med=51.13µs max=248.97ms p(90)=214.46µs p(95)=381.22µs p(99.9)=50.09ms 
     http_req_sending...............: avg=142.69µs min=4.16µs   med=8.61µs  max=247.23ms p(90)=17.35µs  p(95)=123.25µs p(99.9)=25.26ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.66ms  min=756.66µs med=40.54ms max=267.17ms p(90)=104.72ms p(95)=130.48ms p(99.9)=186.6ms 
     http_reqs......................: 281498  4614.590546/s
     iteration_duration.............: avg=50.78ms  min=1.34ms   med=41.75ms max=387.81ms p(90)=108.91ms p(95)=136.34ms p(99.9)=221.1ms 
     iterations.....................: 280498  4598.197568/s
     success_rate...................: 100.00% ✓ 280498      ✗ 0     
     vus............................: 56      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 811692      ✗ 0     
     data_received..................: 24 GB   389 MB/s
     data_sent......................: 326 MB  5.3 MB/s
     http_req_blocked...............: avg=56.31µs  min=902ns    med=2.53µs  max=131.79ms p(90)=4.12µs   p(95)=5.25µs   p(99.9)=19.13ms 
     http_req_connecting............: avg=52.06µs  min=0s       med=0s      max=115.78ms p(90)=0s       p(95)=0s       p(99.9)=18.91ms 
     http_req_duration..............: avg=51.15ms  min=823.74µs med=42.82ms max=254.66ms p(90)=110.59ms p(95)=137.62ms p(99.9)=196.76ms
       { expected_response:true }...: avg=51.15ms  min=823.74µs med=42.82ms max=254.66ms p(90)=110.59ms p(95)=137.62ms p(99.9)=196.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 271564
     http_req_receiving.............: avg=343.36µs min=25.07µs  med=51.22µs max=108.57ms p(90)=235.71µs p(95)=410.58µs p(99.9)=50.91ms 
     http_req_sending...............: avg=134.47µs min=4.45µs   med=9.1µs   max=153.96ms p(90)=18.3µs   p(95)=130.48µs p(99.9)=23.93ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.68ms  min=783.81µs med=42.52ms max=254.58ms p(90)=109.63ms p(95)=136.42ms p(99.9)=186.61ms
     http_reqs......................: 271564  4448.272801/s
     iteration_duration.............: avg=52.65ms  min=1.47ms   med=43.54ms max=350.41ms p(90)=113.29ms p(95)=140.82ms p(99.9)=225.76ms
     iterations.....................: 270564  4431.892601/s
     success_rate...................: 100.00% ✓ 270564      ✗ 0     
     vus............................: 59      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 812154      ✗ 0     
     data_received..................: 24 GB   389 MB/s
     data_sent......................: 326 MB  5.3 MB/s
     http_req_blocked...............: avg=76.48µs  min=952ns    med=2.71µs  max=214.64ms p(90)=4.42µs   p(95)=5.67µs   p(99.9)=28.47ms 
     http_req_connecting............: avg=72.53µs  min=0s       med=0s      max=209.49ms p(90)=0s       p(95)=0s       p(99.9)=27.87ms 
     http_req_duration..............: avg=50.83ms  min=917.56µs med=42.33ms max=271.03ms p(90)=107.51ms p(95)=134.07ms p(99.9)=190.64ms
       { expected_response:true }...: avg=50.83ms  min=917.56µs med=42.33ms max=271.03ms p(90)=107.51ms p(95)=134.07ms p(99.9)=190.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 271718
     http_req_receiving.............: avg=357.88µs min=26.12µs  med=54.62µs max=148.17ms p(90)=224.57µs p(95)=394.34µs p(99.9)=47.3ms  
     http_req_sending...............: avg=162.07µs min=4.13µs   med=9.53µs  max=153.02ms p(90)=19.41µs  p(95)=128.35µs p(99.9)=30.22ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.31ms  min=871.49µs med=41.99ms max=270.95ms p(90)=106.34ms p(95)=132.67ms p(99.9)=186.18ms
     http_reqs......................: 271718  4445.698183/s
     iteration_duration.............: avg=52.61ms  min=1.5ms    med=43.22ms max=355.35ms p(90)=111.92ms p(95)=140.27ms p(99.9)=214.53ms
     iterations.....................: 270718  4429.336742/s
     success_rate...................: 100.00% ✓ 270718      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 775041      ✗ 0     
     data_received..................: 23 GB   371 MB/s
     data_sent......................: 312 MB  5.1 MB/s
     http_req_blocked...............: avg=54.57µs  min=851ns    med=2.56µs  max=115.8ms  p(90)=4.37µs   p(95)=5.63µs   p(99.9)=18.32ms 
     http_req_connecting............: avg=50.33µs  min=0s       med=0s      max=115.61ms p(90)=0s       p(95)=0s       p(99.9)=17.77ms 
     http_req_duration..............: avg=53.6ms   min=989.42µs med=44.72ms max=334.92ms p(90)=115.55ms p(95)=143.13ms p(99.9)=198.99ms
       { expected_response:true }...: avg=53.6ms   min=989.42µs med=44.72ms max=334.92ms p(90)=115.55ms p(95)=143.13ms p(99.9)=198.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 259347
     http_req_receiving.............: avg=310.48µs min=27.72µs  med=52.11µs max=211.98ms p(90)=238.21µs p(95)=416.97µs p(99.9)=40.99ms 
     http_req_sending...............: avg=135.53µs min=4.19µs   med=9.14µs  max=123.24ms p(90)=18.85µs  p(95)=135.49µs p(99.9)=24.8ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.15ms  min=937.72µs med=44.44ms max=334.58ms p(90)=114.52ms p(95)=141.95ms p(99.9)=195.3ms 
     http_reqs......................: 259347  4237.556793/s
     iteration_duration.............: avg=55.14ms  min=1.56ms   med=45.58ms max=354.1ms  p(90)=118.72ms p(95)=146.93ms p(99.9)=230.78ms
     iterations.....................: 258347  4221.21746/s
     success_rate...................: 100.00% ✓ 258347      ✗ 0     
     vus............................: 65      min=0         max=496 
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

     checks.........................: 100.00% ✓ 737037      ✗ 0     
     data_received..................: 22 GB   354 MB/s
     data_sent......................: 296 MB  4.9 MB/s
     http_req_blocked...............: avg=38.15µs  min=802ns    med=2.11µs  max=103.15ms p(90)=3.66µs   p(95)=4.76µs   p(99.9)=6.79ms  
     http_req_connecting............: avg=34.87µs  min=0s       med=0s      max=95.18ms  p(90)=0s       p(95)=0s       p(99.9)=6.4ms   
     http_req_duration..............: avg=56.91ms  min=719.28µs med=47.5ms  max=326.6ms  p(90)=118.73ms p(95)=144.53ms p(99.9)=219.71ms
       { expected_response:true }...: avg=56.91ms  min=719.28µs med=47.5ms  max=326.6ms  p(90)=118.73ms p(95)=144.53ms p(99.9)=219.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 246679
     http_req_receiving.............: avg=241.17µs min=26.36µs  med=50.58µs max=76.17ms  p(90)=208.79µs p(95)=365.05µs p(99.9)=36.28ms 
     http_req_sending...............: avg=111.32µs min=4.35µs   med=8.94µs  max=136.15ms p(90)=17.73µs  p(95)=123.33µs p(99.9)=19.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=56.56ms  min=666.92µs med=47.24ms max=318.24ms p(90)=118.06ms p(95)=143.66ms p(99.9)=216.91ms
     http_reqs......................: 246679  4047.135456/s
     iteration_duration.............: avg=57.99ms  min=1.27ms   med=48.47ms max=335.83ms p(90)=120.47ms p(95)=147ms    p(99.9)=228.02ms
     iterations.....................: 245679  4030.728971/s
     success_rate...................: 100.00% ✓ 245679      ✗ 0     
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

     checks.........................: 100.00% ✓ 509847     ✗ 0     
     data_received..................: 15 GB   243 MB/s
     data_sent......................: 205 MB  3.3 MB/s
     http_req_blocked...............: avg=25.51µs  min=1.05µs  med=3.03µs  max=72.88ms  p(90)=4.97µs   p(95)=6.32µs   p(99.9)=2.33ms  
     http_req_connecting............: avg=21.34µs  min=0s      med=0s      max=67.21ms  p(90)=0s       p(95)=0s       p(99.9)=2.19ms  
     http_req_duration..............: avg=83.11ms  min=1.19ms  med=75.52ms max=325.86ms p(90)=163.8ms  p(95)=181.42ms p(99.9)=239.14ms
       { expected_response:true }...: avg=83.11ms  min=1.19ms  med=75.52ms max=325.86ms p(90)=163.8ms  p(95)=181.42ms p(99.9)=239.14ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 170949
     http_req_receiving.............: avg=184.87µs min=27.46µs med=59.67µs max=154.92ms p(90)=216.78µs p(95)=403.58µs p(99.9)=20.58ms 
     http_req_sending...............: avg=87.52µs  min=4.56µs  med=11.35µs max=184.58ms p(90)=22.08µs  p(95)=142.16µs p(99.9)=12.14ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.84ms  min=1.14ms  med=75.27ms max=285.4ms  p(90)=163.47ms p(95)=180.88ms p(99.9)=237.48ms
     http_reqs......................: 170949  2781.04969/s
     iteration_duration.............: avg=83.88ms  min=2.82ms  med=76.45ms max=347.89ms p(90)=164.3ms  p(95)=181.95ms p(99.9)=239.87ms
     iterations.....................: 169949  2764.78139/s
     success_rate...................: 100.00% ✓ 169949     ✗ 0     
     vus............................: 78      min=0        max=493 
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 263442      ✗ 0    
     data_received..................: 7.8 GB  124 MB/s
     data_sent......................: 107 MB  1.7 MB/s
     http_req_blocked...............: avg=6.53µs   min=1.11µs  med=3.42µs   max=16.7ms   p(90)=5.48µs   p(95)=6.55µs   p(99.9)=441.34µs
     http_req_connecting............: avg=2.37µs   min=0s      med=0s       max=16.48ms  p(90)=0s       p(95)=0s       p(99.9)=328.16µs
     http_req_duration..............: avg=160.61ms min=1.95ms  med=128.34ms max=1.06s    p(90)=343.73ms p(95)=412.05ms p(99.9)=761.2ms 
       { expected_response:true }...: avg=160.61ms min=1.95ms  med=128.34ms max=1.06s    p(90)=343.73ms p(95)=412.05ms p(99.9)=761.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 88814
     http_req_receiving.............: avg=82.96µs  min=27.96µs med=64.77µs  max=27.42ms  p(90)=104.93µs p(95)=123.27µs p(99.9)=2ms     
     http_req_sending...............: avg=41µs     min=5.11µs  med=14.3µs   max=164.76ms p(90)=21.79µs  p(95)=26.15µs  p(99.9)=4.93ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=160.49ms min=1.89ms  med=128.21ms max=1.06s    p(90)=343.6ms  p(95)=411.95ms p(99.9)=761.09ms
     http_reqs......................: 88814   1422.622284/s
     iteration_duration.............: avg=162.7ms  min=6.04ms  med=130.56ms max=1.06s    p(90)=345.09ms p(95)=413.36ms p(99.9)=762.48ms
     iterations.....................: 87814   1406.604288/s
     success_rate...................: 100.00% ✓ 87814       ✗ 0    
     vus............................: 76      min=0         max=493
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

     checks.........................: 100.00% ✓ 240132      ✗ 0    
     data_received..................: 7.1 GB  114 MB/s
     data_sent......................: 97 MB   1.6 MB/s
     http_req_blocked...............: avg=6.17µs   min=1.12µs  med=2.8µs    max=17.09ms  p(90)=4.47µs   p(95)=5.42µs   p(99.9)=496.79µs
     http_req_connecting............: avg=2.7µs    min=0s      med=0s       max=17.04ms  p(90)=0s       p(95)=0s       p(99.9)=442.4µs 
     http_req_duration..............: avg=175.97ms min=1.99ms  med=173.56ms max=492.82ms p(90)=333.28ms p(95)=356.85ms p(99.9)=435.75ms
       { expected_response:true }...: avg=175.97ms min=1.99ms  med=173.56ms max=492.82ms p(90)=333.28ms p(95)=356.85ms p(99.9)=435.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81044
     http_req_receiving.............: avg=77.3µs   min=26.59µs med=61.96µs  max=119.04ms p(90)=99.02µs  p(95)=115.05µs p(99.9)=1.2ms   
     http_req_sending...............: avg=32.54µs  min=4.93µs  med=11.67µs  max=167.04ms p(90)=17.62µs  p(95)=21µs     p(99.9)=3.47ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.86ms min=1.94ms  med=173.43ms max=492.73ms p(90)=333.2ms  p(95)=356.76ms p(99.9)=435.68ms
     http_reqs......................: 81044   1297.432958/s
     iteration_duration.............: avg=178.41ms min=4.39ms  med=176.41ms max=493.02ms p(90)=334.16ms p(95)=357.52ms p(99.9)=435.98ms
     iterations.....................: 80044   1281.423963/s
     success_rate...................: 100.00% ✓ 80044       ✗ 0    
     vus............................: 77      min=0         max=493
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

     checks.........................: 100.00% ✓ 92865      ✗ 0    
     data_received..................: 2.8 GB  43 MB/s
     data_sent......................: 38 MB   594 kB/s
     http_req_blocked...............: avg=9µs      min=1.01µs  med=2.54µs   max=11.06ms  p(90)=4.19µs   p(95)=5.11µs   p(99.9)=1.76ms
     http_req_connecting............: avg=5.49µs   min=0s      med=0s       max=10.92ms  p(90)=0s       p(95)=0s       p(99.9)=1.7ms 
     http_req_duration..............: avg=449.4ms  min=3.71ms  med=411.26ms max=1.74s    p(90)=901.69ms p(95)=982.27ms p(99.9)=1.41s 
       { expected_response:true }...: avg=449.4ms  min=3.71ms  med=411.26ms max=1.74s    p(90)=901.69ms p(95)=982.27ms p(99.9)=1.41s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 31955
     http_req_receiving.............: avg=80.1µs   min=25.83µs med=66.93µs  max=83.64ms  p(90)=105.64µs p(95)=119.95µs p(99.9)=1.06ms
     http_req_sending...............: avg=26.98µs  min=4.82µs  med=12.49µs  max=204.69ms p(90)=18.88µs  p(95)=21.27µs  p(99.9)=1.65ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=449.3ms  min=3.65ms  med=411.18ms max=1.74s    p(90)=901.61ms p(95)=982.17ms p(99.9)=1.41s 
     http_reqs......................: 31955   495.070177/s
     iteration_duration.............: avg=464.13ms min=21.42ms med=430.64ms max=1.74s    p(90)=906.37ms p(95)=986.3ms  p(99.9)=1.42s 
     iterations.....................: 30955   479.577447/s
     success_rate...................: 100.00% ✓ 30955      ✗ 0    
     vus............................: 82      min=0        max=500
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

     checks.........................: 100.00% ✓ 47727      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   301 kB/s
     http_req_blocked...............: avg=18.99µs  min=1.04µs  med=3.3µs    max=9.92ms  p(90)=5.15µs   p(95)=6.71µs   p(99.9)=4.33ms  
     http_req_connecting............: avg=13.81µs  min=0s      med=0s       max=9.86ms  p(90)=0s       p(95)=0s       p(99.9)=4.29ms  
     http_req_duration..............: avg=861.16ms min=5.69ms  med=777.23ms max=4.48s   p(90)=1.72s    p(95)=1.96s    p(99.9)=3.93s   
       { expected_response:true }...: avg=861.16ms min=5.69ms  med=777.23ms max=4.48s   p(90)=1.72s    p(95)=1.96s    p(99.9)=3.93s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16909
     http_req_receiving.............: avg=95.7µs   min=31.62µs med=89.76µs  max=12.65ms p(90)=126.37µs p(95)=142.62µs p(99.9)=919.21µs
     http_req_sending...............: avg=26.3µs   min=5.55µs  med=17.57µs  max=6.33ms  p(90)=22.69µs  p(95)=25.95µs  p(99.9)=1.84ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=861.04ms min=5.61ms  med=777.15ms max=4.48s   p(90)=1.72s    p(95)=1.96s    p(99.9)=3.93s   
     http_reqs......................: 16909   250.775256/s
     iteration_duration.............: avg=915.3ms  min=33.88ms med=841.92ms max=4.49s   p(90)=1.74s    p(95)=1.99s    p(99.9)=3.94s   
     iterations.....................: 15909   235.944382/s
     success_rate...................: 100.00% ✓ 15909      ✗ 0    
     vus............................: 81      min=0        max=500
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

     checks.........................: 100.00% ✓ 46458      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   289 kB/s
     http_req_blocked...............: avg=19.25µs  min=1.14µs  med=3.17µs   max=11.63ms p(90)=4.85µs   p(95)=6.31µs   p(99.9)=4.97ms  
     http_req_connecting............: avg=13.82µs  min=0s      med=0s       max=11.45ms p(90)=0s       p(95)=0s       p(99.9)=4.68ms  
     http_req_duration..............: avg=881.55ms min=7.62ms  med=792.73ms max=3s      p(90)=1.8s     p(95)=1.93s    p(99.9)=2.75s   
       { expected_response:true }...: avg=881.55ms min=7.62ms  med=792.73ms max=3s      p(90)=1.8s     p(95)=1.93s    p(99.9)=2.75s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16486
     http_req_receiving.............: avg=93.5µs   min=31.64µs med=88.17µs  max=3.73ms  p(90)=126.28µs p(95)=140.81µs p(99.9)=854.48µs
     http_req_sending...............: avg=24.77µs  min=5.25µs  med=16.59µs  max=7.4ms   p(90)=21.54µs  p(95)=24.94µs  p(99.9)=2.67ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=881.43ms min=7.53ms  med=792.61ms max=3s      p(90)=1.8s     p(95)=1.93s    p(99.9)=2.75s   
     http_reqs......................: 16486   240.567342/s
     iteration_duration.............: avg=938.42ms min=38.25ms med=870.42ms max=3s      p(90)=1.81s    p(95)=1.93s    p(99.9)=2.77s   
     iterations.....................: 15486   225.975121/s
     success_rate...................: 100.00% ✓ 15486      ✗ 0    
     vus............................: 83      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

