## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-net-10 | 16.7.0-p.31 | 3,072 | 3,158 | 3,040 | 1.3% |  |
| feddi-gateway | 3c75a7db8876 | 3,061 | 3,184 | 3,051 | 1.5% |  |
| fusion-nightly-net-11 | 16.7.0-p.31 | 2,999 | 3,082 | 2,971 | 1.1% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.31 | 2,765 | 2,920 | 2,730 | 2.2% |  |
| fusion-net-10 | 16.6.9 | 2,385 | 2,482 | 2,373 | 1.6% |  |
| hive-router | v0.3.5 | 2,290 | 2,421 | 2,261 | 2.5% |  |
| caliban | 3.2.0 | 1,306 | 1,371 | 1,298 | 1.9% |  |
| cosmo | 0.359.0 | 1,296 | 1,347 | 1,291 | 1.6% |  |
| hive-gateway-router-runtime | 2.15.2 | 455 | 467 | 452 | 1.2% |  |
| hive-gateway | 2.15.2 | 246 | 251 | 243 | 0.9% |  |
| apollo-gateway | 2.14.4 | 234 | 239 | 233 | 1.0% |  |
| apollo-router | v2.18.0 | — | — | — | — | non-compatible response (24291 across 9/9 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | non-compatible response (11194 across 9/9 runs) |
| grafbase | 0.53.5 | — | — | — | — | non-compatible response (248250 across 9/9 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.31)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 564432      ✗ 0     
     data_received..................: 17 GB   270 MB/s
     data_sent......................: 227 MB  3.7 MB/s
     http_req_blocked...............: avg=32.32µs min=751ns   med=2.14µs   max=78.71ms  p(90)=4.07µs   p(95)=5.42µs   p(99.9)=5.9ms   
     http_req_connecting............: avg=29.15µs min=0s      med=0s       max=78.63ms  p(90)=0s       p(95)=0s       p(99.9)=5.83ms  
     http_req_duration..............: avg=75.06ms min=1.22ms  med=68.86ms  max=316.34ms p(90)=146.13ms p(95)=166.6ms  p(99.9)=227.84ms
       { expected_response:true }...: avg=75.06ms min=1.22ms  med=68.86ms  max=316.34ms p(90)=146.13ms p(95)=166.6ms  p(99.9)=227.84ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 189144
     http_req_receiving.............: avg=1.86ms  min=51.03µs med=347.66µs max=68.93ms  p(90)=4.83ms   p(95)=6.44ms   p(99.9)=36.17ms 
     http_req_sending...............: avg=88.79µs min=4.38µs  med=8.85µs   max=167.48ms p(90)=22.19µs  p(95)=121.6µs  p(99.9)=13.42ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=73.1ms  min=1.14ms  med=66.49ms  max=315.91ms p(90)=144.18ms p(95)=165.45ms p(99.9)=224.63ms
     http_reqs......................: 189144  3072.95612/s
     iteration_duration.............: avg=75.76ms min=2.66ms  med=69.53ms  max=366.18ms p(90)=146.66ms p(95)=167.23ms p(99.9)=230.35ms
     iterations.....................: 188144  3056.709471/s
     success_rate...................: 100.00% ✓ 188144      ✗ 0     
     vus............................: 81      min=0         max=492 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 559173      ✗ 0     
     data_received..................: 16 GB   268 MB/s
     data_sent......................: 225 MB  3.7 MB/s
     http_req_blocked...............: avg=39.29µs  min=831ns    med=2.54µs  max=115.66ms p(90)=4.5µs    p(95)=5.75µs   p(99.9)=6.86ms  
     http_req_connecting............: avg=35.07µs  min=0s       med=0s      max=95.91ms  p(90)=0s       p(95)=0s       p(99.9)=6.15ms  
     http_req_duration..............: avg=75.4ms   min=932.84µs med=66.78ms max=337.74ms p(90)=150.31ms p(95)=174.43ms p(99.9)=258.87ms
       { expected_response:true }...: avg=75.4ms   min=932.84µs med=66.78ms max=337.74ms p(90)=150.31ms p(95)=174.43ms p(99.9)=258.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 187391
     http_req_receiving.............: avg=218.32µs min=26.31µs  med=53.5µs  max=197.23ms p(90)=183.76µs p(95)=383.79µs p(99.9)=29.78ms 
     http_req_sending...............: avg=98.21µs  min=4.69µs   med=9.75µs  max=153.77ms p(90)=19.66µs  p(95)=131.02µs p(99.9)=17.67ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=75.09ms  min=860.32µs med=66.5ms  max=337.68ms p(90)=149.74ms p(95)=173.74ms p(99.9)=256.71ms
     http_reqs......................: 187391  3061.493811/s
     iteration_duration.............: avg=76.47ms  min=1.46ms   med=67.92ms max=353.68ms p(90)=151.39ms p(95)=175.77ms p(99.9)=270.52ms
     iterations.....................: 186391  3045.156347/s
     success_rate...................: 100.00% ✓ 186391      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.31)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 550365      ✗ 0     
     data_received..................: 16 GB   263 MB/s
     data_sent......................: 222 MB  3.6 MB/s
     http_req_blocked...............: avg=36.76µs min=751ns   med=2.13µs  max=263.09ms p(90)=3.96µs   p(95)=5.44µs   p(99.9)=5.81ms  
     http_req_connecting............: avg=32.13µs min=0s      med=0s      max=90.88ms  p(90)=0s       p(95)=0s       p(99.9)=5.33ms  
     http_req_duration..............: avg=76.93ms min=1.24ms  med=70.36ms max=314.18ms p(90)=147.72ms p(95)=166.28ms p(99.9)=239.22ms
       { expected_response:true }...: avg=76.93ms min=1.24ms  med=70.36ms max=314.18ms p(90)=147.72ms p(95)=166.28ms p(99.9)=239.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 184455
     http_req_receiving.............: avg=3.9ms   min=52.97µs med=2.64ms  max=130.1ms  p(90)=8.63ms   p(95)=11.3ms   p(99.9)=48.89ms 
     http_req_sending...............: avg=89.04µs min=4.64µs  med=8.95µs  max=181.76ms p(90)=22.51µs  p(95)=116.11µs p(99.9)=13.86ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=72.94ms min=1.15ms  med=65.46ms max=313.94ms p(90)=143.33ms p(95)=163.21ms p(99.9)=235.2ms 
     http_reqs......................: 184455  2999.192388/s
     iteration_duration.............: avg=77.69ms min=3.03ms  med=71.11ms max=331.13ms p(90)=148.3ms  p(95)=167.11ms p(99.9)=242.11ms
     iterations.....................: 183455  2982.932637/s
     success_rate...................: 100.00% ✓ 183455      ✗ 0     
     vus............................: 79      min=0         max=492 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.31)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 510231      ✗ 0     
     data_received..................: 15 GB   243 MB/s
     data_sent......................: 206 MB  3.3 MB/s
     http_req_blocked...............: avg=26.5µs  min=842ns   med=2.23µs   max=66.41ms  p(90)=4.18µs   p(95)=5.54µs   p(99.9)=4.91ms  
     http_req_connecting............: avg=23.33µs min=0s      med=0s       max=66.32ms  p(90)=0s       p(95)=0s       p(99.9)=4.25ms  
     http_req_duration..............: avg=83.04ms min=1.47ms  med=77.49ms  max=313.45ms p(90)=159.31ms p(95)=177.84ms p(99.9)=242.98ms
       { expected_response:true }...: avg=83.04ms min=1.47ms  med=77.49ms  max=313.45ms p(90)=159.31ms p(95)=177.84ms p(99.9)=242.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 171077
     http_req_receiving.............: avg=1.74ms  min=53.39µs med=668.28µs max=273.36ms p(90)=4.19ms   p(95)=5.56ms   p(99.9)=34.75ms 
     http_req_sending...............: avg=77.37µs min=4.54µs  med=9.19µs   max=65.53ms  p(90)=22.9µs   p(95)=121.08µs p(99.9)=11.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=81.22ms min=1.38ms  med=75.51ms  max=313.14ms p(90)=157.52ms p(95)=176.25ms p(99.9)=239.98ms
     http_reqs......................: 171077  2765.533491/s
     iteration_duration.............: avg=83.82ms min=2.94ms  med=78.31ms  max=337.29ms p(90)=159.87ms p(95)=178.48ms p(99.9)=243.84ms
     iterations.....................: 170077  2749.36806/s
     success_rate...................: 100.00% ✓ 170077      ✗ 0     
     vus............................: 25      min=0         max=500 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-10 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 439656      ✗ 0     
     data_received..................: 13 GB   209 MB/s
     data_sent......................: 177 MB  2.9 MB/s
     http_req_blocked...............: avg=14.77µs min=902ns   med=2.2µs   max=48.27ms  p(90)=4.03µs   p(95)=5.26µs   p(99.9)=1.58ms  
     http_req_connecting............: avg=11.4µs  min=0s      med=0s      max=48.2ms   p(90)=0s       p(95)=0s       p(99.9)=1.48ms  
     http_req_duration..............: avg=96.37ms min=1.54ms  med=92.74ms max=299.06ms p(90)=181.82ms p(95)=196.25ms p(99.9)=240.03ms
       { expected_response:true }...: avg=96.37ms min=1.54ms  med=92.74ms max=299.06ms p(90)=181.82ms p(95)=196.25ms p(99.9)=240.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 147552
     http_req_receiving.............: avg=2.28ms  min=52.66µs med=1.76ms  max=237.4ms  p(90)=4.94ms   p(95)=6.23ms   p(99.9)=28.03ms 
     http_req_sending...............: avg=60.58µs min=4.81µs  med=9.21µs  max=47.5ms   p(90)=22.02µs  p(95)=112.49µs p(99.9)=8.05ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.03ms min=1.45ms  med=90.12ms max=268.53ms p(90)=179.24ms p(95)=193.84ms p(99.9)=238.61ms
     http_reqs......................: 147552  2385.510855/s
     iteration_duration.............: avg=97.28ms min=4.74ms  med=93.72ms max=328.14ms p(90)=182.28ms p(95)=196.75ms p(99.9)=240.74ms
     iterations.....................: 146552  2369.3436/s
     success_rate...................: 100.00% ✓ 146552      ✗ 0     
     vus............................: 95      min=0         max=500 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 421578      ✗ 0     
     data_received..................: 12 GB   200 MB/s
     data_sent......................: 170 MB  2.8 MB/s
     http_req_blocked...............: avg=14.43µs  min=892ns   med=2.42µs  max=44.06ms  p(90)=4.25µs   p(95)=5.58µs   p(99.9)=1.23ms  
     http_req_connecting............: avg=11.23µs  min=0s      med=0s      max=44.01ms  p(90)=0s       p(95)=0s       p(99.9)=1.11ms  
     http_req_duration..............: avg=100.52ms min=1.39ms  med=94.91ms max=349.21ms p(90)=194.32ms p(95)=208.31ms p(99.9)=247.72ms
       { expected_response:true }...: avg=100.52ms min=1.39ms  med=94.91ms max=349.21ms p(90)=194.32ms p(95)=208.31ms p(99.9)=247.72ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 141526
     http_req_receiving.............: avg=116.97µs min=27.48µs med=57.75µs max=38.69ms  p(90)=129.72µs p(95)=339.37µs p(99.9)=7.89ms  
     http_req_sending...............: avg=62.41µs  min=4.85µs  med=10.66µs max=188.71ms p(90)=21.04µs  p(95)=118.61µs p(99.9)=7.79ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.34ms min=1.34ms  med=94.73ms max=348.68ms p(90)=194.13ms p(95)=208.03ms p(99.9)=247.27ms
     http_reqs......................: 141526  2290.001011/s
     iteration_duration.............: avg=101.48ms min=4.93ms  med=95.98ms max=366.44ms p(90)=194.76ms p(95)=208.74ms p(99.9)=248.68ms
     iterations.....................: 140526  2273.820231/s
     success_rate...................: 100.00% ✓ 140526      ✗ 0     
     vus............................: 94      min=0         max=500 
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

     checks.........................: 100.00% ✓ 243444      ✗ 0    
     data_received..................: 7.2 GB  114 MB/s
     data_sent......................: 99 MB   1.6 MB/s
     http_req_blocked...............: avg=6.07µs   min=1.03µs  med=2.7µs    max=17.39ms  p(90)=4.62µs   p(95)=5.67µs   p(99.9)=496.29µs
     http_req_connecting............: avg=2.64µs   min=0s      med=0s       max=17.33ms  p(90)=0s       p(95)=0s       p(99.9)=454.13µs
     http_req_duration..............: avg=173.7ms  min=2.38ms  med=138.43ms max=994.78ms p(90)=371.11ms p(95)=439.99ms p(99.9)=718.64ms
       { expected_response:true }...: avg=173.7ms  min=2.38ms  med=138.43ms max=994.78ms p(90)=371.11ms p(95)=439.99ms p(99.9)=718.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 82148
     http_req_receiving.............: avg=79.26µs  min=28.91µs med=62.85µs  max=28.78ms  p(90)=102.33µs p(95)=119.91µs p(99.9)=2.08ms  
     http_req_sending...............: avg=33.15µs  min=5.15µs  med=12.02µs  max=152.12ms p(90)=19.61µs  p(95)=23.56µs  p(99.9)=3.61ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=173.59ms min=2.32ms  med=138.33ms max=994.72ms p(90)=370.93ms p(95)=439.88ms p(99.9)=718.55ms
     http_reqs......................: 82148   1306.180265/s
     iteration_duration.............: avg=176.09ms min=7.19ms  med=141.12ms max=994.98ms p(90)=372.8ms  p(95)=441.43ms p(99.9)=718.99ms
     iterations.....................: 81148   1290.279936/s
     success_rate...................: 100.00% ✓ 81148       ✗ 0    
     vus............................: 52      min=0         max=499
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.359.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 241713      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 98 MB   1.6 MB/s
     http_req_blocked...............: avg=7.39µs   min=1.22µs  med=3.13µs   max=17.31ms  p(90)=5.11µs   p(95)=6.22µs   p(99.9)=454.55µs
     http_req_connecting............: avg=3.33µs   min=0s      med=0s       max=17.25ms  p(90)=0s       p(95)=0s       p(99.9)=386.09µs
     http_req_duration..............: avg=174.83ms min=2.2ms   med=173.99ms max=505.52ms p(90)=330.6ms  p(95)=353.46ms p(99.9)=422.03ms
       { expected_response:true }...: avg=174.83ms min=2.2ms   med=173.99ms max=505.52ms p(90)=330.6ms  p(95)=353.46ms p(99.9)=422.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81571
     http_req_receiving.............: avg=87.61µs  min=29.48µs med=68.96µs  max=121.73ms p(90)=110.14µs p(95)=128.66µs p(99.9)=1.85ms  
     http_req_sending...............: avg=38.96µs  min=5.23µs  med=13.01µs  max=121.64ms p(90)=20.6µs   p(95)=25.2µs   p(99.9)=4.58ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=174.7ms  min=2.13ms  med=173.85ms max=505.45ms p(90)=330.48ms p(95)=353.33ms p(99.9)=421.94ms
     http_reqs......................: 81571   1296.836088/s
     iteration_duration.............: avg=177.24ms min=5.32ms  med=176.72ms max=505.76ms p(90)=331.47ms p(95)=354.03ms p(99.9)=422.45ms
     iterations.....................: 80571   1280.937839/s
     success_rate...................: 100.00% ✓ 80571       ✗ 0    
     vus............................: 52      min=0         max=499
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 86217      ✗ 0    
     data_received..................: 2.6 GB  40 MB/s
     data_sent......................: 36 MB   547 kB/s
     http_req_blocked...............: avg=8.47µs   min=1.1µs   med=2.7µs    max=13.6ms   p(90)=4.35µs   p(95)=5.31µs   p(99.9)=1.12ms  
     http_req_connecting............: avg=4.75µs   min=0s      med=0s       max=13.54ms  p(90)=0s       p(95)=0s       p(99.9)=1.06ms  
     http_req_duration..............: avg=483.19ms min=4.25ms  med=448.58ms max=2.07s    p(90)=954.34ms p(95)=1.03s    p(99.9)=1.57s   
       { expected_response:true }...: avg=483.19ms min=4.25ms  med=448.58ms max=2.07s    p(90)=954.34ms p(95)=1.03s    p(99.9)=1.57s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 29739
     http_req_receiving.............: avg=86.42µs  min=30.34µs med=71.4µs   max=176.55ms p(90)=110.19µs p(95)=124.53µs p(99.9)=941.54µs
     http_req_sending...............: avg=33.37µs  min=5.15µs  med=12.89µs  max=134ms    p(90)=19.39µs  p(95)=21.89µs  p(99.9)=2.6ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=483.07ms min=4.12ms  med=448.5ms  max=2.07s    p(90)=954.25ms p(95)=1.03s    p(99.9)=1.57s   
     http_reqs......................: 29739   455.93061/s
     iteration_duration.............: avg=500.21ms min=25.67ms med=470.62ms max=2.08s    p(90)=959.92ms p(95)=1.04s    p(99.9)=1.58s   
     iterations.....................: 28739   440.599543/s
     success_rate...................: 100.00% ✓ 28739      ✗ 0    
     vus............................: 65      min=0        max=496
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 46920      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   295 kB/s
     http_req_blocked...............: avg=12.51µs  min=1.19µs  med=3.43µs   max=3.06ms p(90)=5.23µs   p(95)=6.82µs   p(99.9)=1.63ms  
     http_req_connecting............: avg=7.31µs   min=0s      med=0s       max=3.01ms p(90)=0s       p(95)=0s       p(99.9)=1.54ms  
     http_req_duration..............: avg=873.9ms  min=5.8ms   med=772.34ms max=4.72s  p(90)=1.78s    p(95)=2.02s    p(99.9)=3.98s   
       { expected_response:true }...: avg=873.9ms  min=5.8ms   med=772.34ms max=4.72s  p(90)=1.78s    p(95)=2.02s    p(99.9)=3.98s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16640
     http_req_receiving.............: avg=97.47µs  min=33.51µs med=93.17µs  max=7.06ms p(90)=130.19µs p(95)=144.95µs p(99.9)=524.05µs
     http_req_sending...............: avg=25.45µs  min=5.59µs  med=17.97µs  max=9.78ms p(90)=23.16µs  p(95)=26.75µs  p(99.9)=2.14ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s     p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=873.78ms min=5.71ms  med=772.23ms max=4.72s  p(90)=1.78s    p(95)=2.02s    p(99.9)=3.98s   
     http_reqs......................: 16640   246.155308/s
     iteration_duration.............: avg=929.8ms  min=37.48ms med=838.14ms max=4.73s  p(90)=1.79s    p(95)=2.04s    p(99.9)=4.05s   
     iterations.....................: 15640   231.362321/s
     success_rate...................: 100.00% ✓ 15640      ✗ 0    
     vus............................: 86      min=0        max=500
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

     checks.........................: 100.00% ✓ 45579      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 19 MB   282 kB/s
     http_req_blocked...............: avg=14.89µs  min=1.1µs   med=3.37µs   max=10.02ms p(90)=5.25µs   p(95)=6.86µs   p(99.9)=2.28ms
     http_req_connecting............: avg=9.75µs   min=0s      med=0s       max=9.95ms  p(90)=0s       p(95)=0s       p(99.9)=2.25ms
     http_req_duration..............: avg=897.27ms min=7.97ms  med=823.25ms max=3.16s   p(90)=1.84s    p(95)=1.98s    p(99.9)=2.84s 
       { expected_response:true }...: avg=897.27ms min=7.97ms  med=823.25ms max=3.16s   p(90)=1.84s    p(95)=1.98s    p(99.9)=2.84s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16193
     http_req_receiving.............: avg=104.95µs min=30.53µs med=91.46µs  max=91.44ms p(90)=130.52µs p(95)=147.06µs p(99.9)=1.41ms
     http_req_sending...............: avg=34.56µs  min=5.75µs  med=17.22µs  max=86.38ms p(90)=22.98µs  p(95)=26.75µs  p(99.9)=2.59ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=897.13ms min=7.88ms  med=823.13ms max=3.16s   p(90)=1.84s    p(95)=1.98s    p(99.9)=2.84s 
     http_reqs......................: 16193   234.629134/s
     iteration_duration.............: avg=956.3ms  min=55.63ms med=903.75ms max=3.17s   p(90)=1.85s    p(95)=1.99s    p(99.9)=2.85s 
     iterations.....................: 15193   220.139593/s
     success_rate...................: 100.00% ✓ 15193      ✗ 0    
     vus............................: 56      min=0        max=499
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

