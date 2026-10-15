## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 2 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 1 runs are measured. Results are ranked by **median RPS** across the 1 measured runs, with best/worst/CV% reported for transparency.

This scenario is a burst stress test with peaks up to **500 VUs** over **120s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion | 16.6.8 | 2,546 | 2,546 | 2,546 | 0.0% |  |
| fusion-nightly-net11 | 16.7.0-p.27 | 2,484 | 2,484 | 2,484 | 0.0% |  |
| fusion-nightly | 16.7.0-p.27 | 2,443 | 2,443 | 2,443 | 0.0% |  |
| hive-router | v0.3.5 | 2,434 | 2,434 | 2,434 | 0.0% |  |
| fusion-nightly-fed | 16.7.0-p.27 | 2,348 | 2,348 | 2,348 | 0.0% |  |
| caliban | 3.2.0 | 1,429 | 1,429 | 1,429 | 0.0% |  |
| cosmo | 0.359.0 | 1,356 | 1,356 | 1,356 | 0.0% |  |
| hive-gateway-router-runtime | 2.15.2 | 485 | 485 | 485 | 0.0% |  |
| apollo-gateway | 2.14.4 | 239 | 239 | 239 | 0.0% |  |
| hive-gateway | 2.15.2 | 238 | 238 | 238 | 0.0% |  |
| apollo-router | v2.18.0 | — | — | — | — | non-compatible response (1289 across 1/1 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | non-compatible response (1023 across 1/1 runs) |
| feddi | — | — | — | — | — | not run |
| grafbase | 0.53.5 | — | — | — | — | non-compatible response (40829 across 1/1 runs) |


### Details

<details>
  <summary>Summary for: fusion (HotChocolate subgraphs) (16.6.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 468555      ✗ 0     
     data_received..................: 14 GB   223 MB/s
     data_sent......................: 189 MB  3.1 MB/s
     http_req_blocked...............: avg=15.55µs min=882ns   med=2.19µs  max=64.21ms  p(90)=3.76µs   p(95)=4.85µs   p(99.9)=1.67ms  
     http_req_connecting............: avg=12.53µs min=0s      med=0s      max=64.14ms  p(90)=0s       p(95)=0s       p(99.9)=1.56ms  
     http_req_duration..............: avg=90.52ms min=1.42ms  med=79.1ms  max=1.7s     p(90)=171.74ms p(95)=201.27ms p(99.9)=803.4ms 
       { expected_response:true }...: avg=90.52ms min=1.42ms  med=79.1ms  max=1.7s     p(90)=171.74ms p(95)=201.27ms p(99.9)=803.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 157185
     http_req_receiving.............: avg=1.4ms   min=48.42µs med=99.27µs max=760.17ms p(90)=1.57ms   p(95)=4.35ms   p(99.9)=81.95ms 
     http_req_sending...............: avg=64.25µs min=4.25µs  med=9.21µs  max=213.07ms p(90)=18.07µs  p(95)=106.12µs p(99.9)=8.46ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=89.05ms min=1.35ms  med=77.91ms max=1.67s    p(90)=169.6ms  p(95)=197.25ms p(99.9)=772.8ms 
     http_reqs......................: 157185  2546.372194/s
     iteration_duration.............: avg=91.35ms min=2.76ms  med=80.04ms max=1.7s     p(90)=172.29ms p(95)=201.94ms p(99.9)=803.78ms
     iterations.....................: 156185  2530.172352/s
     success_rate...................: 100.00% ✓ 156185      ✗ 0     
     vus............................: 93      min=0         max=500 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 456453      ✗ 0     
     data_received..................: 13 GB   218 MB/s
     data_sent......................: 184 MB  3.0 MB/s
     http_req_blocked...............: avg=13.04µs min=882ns   med=2.25µs   max=57.66ms  p(90)=3.85µs   p(95)=4.95µs   p(99.9)=1.5ms   
     http_req_connecting............: avg=9.98µs  min=0s      med=0s       max=57.61ms  p(90)=0s       p(95)=0s       p(99.9)=1.44ms  
     http_req_duration..............: avg=92.86ms min=1.34ms  med=88.66ms  max=410.84ms p(90)=177.78ms p(95)=193.67ms p(99.9)=270.32ms
       { expected_response:true }...: avg=92.86ms min=1.34ms  med=88.66ms  max=410.84ms p(90)=177.78ms p(95)=193.67ms p(99.9)=270.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 153151
     http_req_receiving.............: avg=1.44ms  min=51.87µs med=190.45µs max=193.49ms p(90)=3.4ms    p(95)=5.28ms   p(99.9)=33.28ms 
     http_req_sending...............: avg=60.05µs min=4.38µs  med=9.02µs   max=192.95ms p(90)=18.48µs  p(95)=103.56µs p(99.9)=7.29ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.36ms min=1.26ms  med=87.1ms   max=403.74ms p(90)=176.03ms p(95)=191.76ms p(99.9)=264.95ms
     http_reqs......................: 153151  2484.239057/s
     iteration_duration.............: avg=93.71ms min=4.04ms  med=89.63ms  max=411.11ms p(90)=178.21ms p(95)=194.12ms p(99.9)=271ms   
     iterations.....................: 152151  2468.018209/s
     success_rate...................: 100.00% ✓ 152151      ✗ 0     
     vus............................: 86      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 449598      ✗ 0     
     data_received..................: 13 GB   214 MB/s
     data_sent......................: 181 MB  2.9 MB/s
     http_req_blocked...............: avg=17.97µs min=962ns   med=2.68µs   max=73.11ms  p(90)=4.26µs   p(95)=5.39µs   p(99.9)=1.54ms  
     http_req_connecting............: avg=14.58µs min=0s      med=0s       max=72.93ms  p(90)=0s       p(95)=0s       p(99.9)=1.49ms  
     http_req_duration..............: avg=94.36ms min=1.44ms  med=80.53ms  max=1.24s    p(90)=179.51ms p(95)=209.06ms p(99.9)=963.31ms
       { expected_response:true }...: avg=94.36ms min=1.44ms  med=80.53ms  max=1.24s    p(90)=179.51ms p(95)=209.06ms p(99.9)=963.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 150866
     http_req_receiving.............: avg=1.69ms  min=51.61µs med=108.48µs max=931.61ms p(90)=1.78ms   p(95)=4.65ms   p(99.9)=144.66ms
     http_req_sending...............: avg=66.87µs min=4.35µs  med=9.72µs   max=177.3ms  p(90)=18.21µs  p(95)=114.33µs p(99.9)=9.18ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.6ms  min=1.34ms  med=79.33ms  max=1.24s    p(90)=177.05ms p(95)=204.68ms p(99.9)=930.3ms 
     http_reqs......................: 150866  2443.605004/s
     iteration_duration.............: avg=95.24ms min=2.64ms  med=81.44ms  max=1.24s    p(90)=180.1ms  p(95)=209.77ms p(99.9)=963.87ms
     iterations.....................: 149866  2427.407816/s
     success_rate...................: 100.00% ✓ 149866      ✗ 0     
     vus............................: 91      min=0         max=499 
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

     checks.........................: 100.00% ✓ 448254      ✗ 0     
     data_received..................: 13 GB   213 MB/s
     data_sent......................: 181 MB  2.9 MB/s
     http_req_blocked...............: avg=10.1µs   min=912ns   med=2.23µs  max=34.74ms  p(90)=3.86µs   p(95)=5.05µs   p(99.9)=777.29µs
     http_req_connecting............: avg=7.22µs   min=0s      med=0s      max=34.58ms  p(90)=0s       p(95)=0s       p(99.9)=693.98µs
     http_req_duration..............: avg=94.56ms  min=1.45ms  med=88.91ms max=328.81ms p(90)=183.58ms p(95)=197.48ms p(99.9)=232.06ms
       { expected_response:true }...: avg=94.56ms  min=1.45ms  med=88.91ms max=328.81ms p(90)=183.58ms p(95)=197.48ms p(99.9)=232.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 150418
     http_req_receiving.............: avg=104.11µs min=26.24µs med=52.88µs max=205.51ms p(90)=114.97µs p(95)=316.61µs p(99.9)=6.51ms  
     http_req_sending...............: avg=57.76µs  min=4.46µs  med=9.62µs  max=194.5ms  p(90)=18.59µs  p(95)=113.42µs p(99.9)=6.92ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.39ms  min=1.4ms   med=88.77ms max=312.84ms p(90)=183.39ms p(95)=197.26ms p(99.9)=231.33ms
     http_reqs......................: 150418  2434.454654/s
     iteration_duration.............: avg=95.42ms  min=3.36ms  med=89.91ms max=339.21ms p(90)=184.02ms p(95)=197.83ms p(99.9)=233.12ms
     iterations.....................: 149418  2418.270058/s
     success_rate...................: 100.00% ✓ 149418      ✗ 0     
     vus............................: 92      min=0         max=500 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 433914      ✗ 0     
     data_received..................: 13 GB   206 MB/s
     data_sent......................: 175 MB  2.8 MB/s
     http_req_blocked...............: avg=14.39µs min=851ns   med=2.3µs    max=95.79ms  p(90)=4.09µs   p(95)=5.25µs   p(99.9)=1.3ms   
     http_req_connecting............: avg=11.28µs min=0s      med=0s       max=95.62ms  p(90)=0s       p(95)=0s       p(99.9)=1.21ms  
     http_req_duration..............: avg=97.65ms min=1.63ms  med=85.83ms  max=1.49s    p(90)=184.66ms p(95)=212.99ms p(99.9)=637.94ms
       { expected_response:true }...: avg=97.65ms min=1.63ms  med=85.83ms  max=1.49s    p(90)=184.66ms p(95)=212.99ms p(99.9)=637.94ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 145638
     http_req_receiving.............: avg=1.42ms  min=50.51µs med=103.48µs max=504.69ms p(90)=1.65ms   p(95)=4.1ms    p(99.9)=126.89ms
     http_req_sending...............: avg=65.5µs  min=4.44µs  med=9.54µs   max=147.86ms p(90)=19.8µs   p(95)=108.18µs p(99.9)=8.5ms   
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.17ms min=1.57ms  med=84.64ms  max=1.49s    p(90)=182.92ms p(95)=209.77ms p(99.9)=621.08ms
     http_reqs......................: 145638  2348.889752/s
     iteration_duration.............: avg=98.65ms min=2.94ms  med=86.92ms  max=1.49s    p(90)=185.35ms p(95)=213.7ms  p(99.9)=638.41ms
     iterations.....................: 144638  2332.761477/s
     success_rate...................: 100.00% ✓ 144638      ✗ 0     
     vus............................: 57      min=0         max=498 
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

     checks.........................: 100.00% ✓ 265608      ✗ 0    
     data_received..................: 7.8 GB  125 MB/s
     data_sent......................: 108 MB  1.7 MB/s
     http_req_blocked...............: avg=6.22µs   min=1µs     med=2.69µs   max=21.17ms  p(90)=4.83µs   p(95)=5.92µs   p(99.9)=574.1µs 
     http_req_connecting............: avg=2.83µs   min=0s      med=0s       max=21.1ms   p(90)=0s       p(95)=0s       p(99.9)=492.1µs 
     http_req_duration..............: avg=159.28ms min=2.18ms  med=129.48ms max=843.38ms p(90)=340.29ms p(95)=403.86ms p(99.9)=663.5ms 
       { expected_response:true }...: avg=159.28ms min=2.18ms  med=129.48ms max=843.38ms p(90)=340.29ms p(95)=403.86ms p(99.9)=663.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 89536
     http_req_receiving.............: avg=149.78µs min=27.27µs med=62.37µs  max=263.86ms p(90)=104.65µs p(95)=124.66µs p(99.9)=2.82ms  
     http_req_sending...............: avg=33.08µs  min=4.77µs  med=12.21µs  max=46.29ms  p(90)=20.56µs  p(95)=24.64µs  p(99.9)=4.34ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=159.1ms  min=2.12ms  med=129.2ms  max=843.3ms  p(90)=340.08ms p(95)=403.76ms p(99.9)=663.44ms
     http_reqs......................: 89536   1429.981915/s
     iteration_duration.............: avg=161.33ms min=4.07ms  med=131.65ms max=843.6ms  p(90)=341.83ms p(95)=404.96ms p(99.9)=664.5ms 
     iterations.....................: 88536   1414.010888/s
     success_rate...................: 100.00% ✓ 88536       ✗ 0    
     vus............................: 84      min=0         max=498
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

     checks.........................: 100.00% ✓ 251577      ✗ 0    
     data_received..................: 7.4 GB  119 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=6.52µs   min=1.05µs  med=2.75µs   max=43.87ms  p(90)=4.52µs   p(95)=5.58µs   p(99.9)=457.02µs
     http_req_connecting............: avg=3.12µs   min=0s      med=0s       max=43.81ms  p(90)=0s       p(95)=0s       p(99.9)=384.48µs
     http_req_duration..............: avg=168.05ms min=2.1ms   med=166.68ms max=514.12ms p(90)=317.67ms p(95)=341.31ms p(99.9)=435.13ms
       { expected_response:true }...: avg=168.05ms min=2.1ms   med=166.68ms max=514.12ms p(90)=317.67ms p(95)=341.31ms p(99.9)=435.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 84859
     http_req_receiving.............: avg=82.07µs  min=27.21µs med=64.61µs  max=62.58ms  p(90)=103.63µs p(95)=120.97µs p(99.9)=1.67ms  
     http_req_sending...............: avg=35.05µs  min=4.55µs  med=11.59µs  max=159.73ms p(90)=18.56µs  p(95)=22.66µs  p(99.9)=4.17ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.93ms min=2.04ms  med=166.55ms max=514.04ms p(90)=317.55ms p(95)=341.22ms p(99.9)=435.08ms
     http_reqs......................: 84859   1356.919339/s
     iteration_duration.............: avg=170.29ms min=5.5ms   med=169.22ms max=514.29ms p(90)=318.4ms  p(95)=341.82ms p(99.9)=436.59ms
     iterations.....................: 83859   1340.929057/s
     success_rate...................: 100.00% ✓ 83859       ✗ 0    
     vus............................: 82      min=0         max=495
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

     checks.........................: 100.00% ✓ 91725      ✗ 0    
     data_received..................: 2.8 GB  43 MB/s
     data_sent......................: 38 MB   583 kB/s
     http_req_blocked...............: avg=9.63µs   min=1.17µs  med=3.31µs   max=8.36ms   p(90)=5.04µs   p(95)=6.14µs   p(99.9)=1.67ms  
     http_req_connecting............: avg=5.19µs   min=0s      med=0s       max=8.31ms   p(90)=0s       p(95)=0s       p(99.9)=1.63ms  
     http_req_duration..............: avg=454.77ms min=4.04ms  med=429.26ms max=2.04s    p(90)=892.18ms p(95)=977.83ms p(99.9)=1.43s   
       { expected_response:true }...: avg=454.77ms min=4.04ms  med=429.26ms max=2.04s    p(90)=892.18ms p(95)=977.83ms p(99.9)=1.43s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 31575
     http_req_receiving.............: avg=89.15µs  min=27.68µs med=75.23µs  max=199.53ms p(90)=112.53µs p(95)=126.64µs p(99.9)=756.98µs
     http_req_sending...............: avg=28.81µs  min=5.49µs  med=15.38µs  max=108.44ms p(90)=21.71µs  p(95)=24.52µs  p(99.9)=2.21ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=454.66ms min=3.97ms  med=429.13ms max=2.04s    p(90)=892.1ms  p(95)=977.72ms p(99.9)=1.43s   
     http_reqs......................: 31575   485.982066/s
     iteration_duration.............: avg=469.89ms min=14.68ms med=445.91ms max=2.04s    p(90)=896.8ms  p(95)=982.02ms p(99.9)=1.44s   
     iterations.....................: 30575   470.59071/s
     success_rate...................: 100.00% ✓ 30575      ✗ 0    
     vus............................: 55      min=0        max=499
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

     checks.........................: 100.00% ✓ 46263      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   287 kB/s
     http_req_blocked...............: avg=13.78µs  min=1.15µs  med=3.15µs   max=9.29ms   p(90)=4.84µs   p(95)=6.33µs   p(99.9)=2.15ms  
     http_req_connecting............: avg=8.99µs   min=0s      med=0s       max=9.23ms   p(90)=0s       p(95)=0s       p(99.9)=2ms     
     http_req_duration..............: avg=884.62ms min=7.53ms  med=809.51ms max=3.36s    p(90)=1.81s    p(95)=1.97s    p(99.9)=2.66s   
       { expected_response:true }...: avg=884.62ms min=7.53ms  med=809.51ms max=3.36s    p(90)=1.81s    p(95)=1.97s    p(99.9)=2.66s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16421
     http_req_receiving.............: avg=92.32µs  min=32.69µs med=86.22µs  max=4.28ms   p(90)=123.36µs p(95)=138.76µs p(99.9)=962.38µs
     http_req_sending...............: avg=40.8µs   min=5.18µs  med=15.98µs  max=126.25ms p(90)=21.14µs  p(95)=24.48µs  p(99.9)=3.23ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=884.49ms min=7.45ms  med=809.42ms max=3.36s    p(90)=1.81s    p(95)=1.97s    p(99.9)=2.66s   
     http_reqs......................: 16421   239.374317/s
     iteration_duration.............: avg=941.98ms min=20.94ms med=893.28ms max=3.36s    p(90)=1.83s    p(95)=1.98s    p(99.9)=2.67s   
     iterations.....................: 15421   224.796988/s
     success_rate...................: 100.00% ✓ 15421      ✗ 0    
     vus............................: 82      min=0        max=500
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

     checks.........................: 100.00% ✓ 45432      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 19 MB   286 kB/s
     http_req_blocked...............: avg=13.63µs  min=1.02µs  med=3.02µs   max=8.98ms  p(90)=4.69µs   p(95)=6.2µs    p(99.9)=2.34ms
     http_req_connecting............: avg=9.04µs   min=0s      med=0s       max=8.92ms  p(90)=0s       p(95)=0s       p(99.9)=2.32ms
     http_req_duration..............: avg=902.38ms min=5.88ms  med=826.07ms max=5s      p(90)=1.79s    p(95)=2.04s    p(99.9)=4.26s 
       { expected_response:true }...: avg=902.38ms min=5.88ms  med=826.07ms max=5s      p(90)=1.79s    p(95)=2.04s    p(99.9)=4.26s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16144
     http_req_receiving.............: avg=96.08µs  min=32.79µs med=82.71µs  max=44.64ms p(90)=119.44µs p(95)=134.48µs p(99.9)=1.7ms 
     http_req_sending...............: avg=29µs     min=5.47µs  med=15.27µs  max=38.74ms p(90)=20.55µs  p(95)=23.8µs   p(99.9)=4.59ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=902.26ms min=5.76ms  med=825.96ms max=5s      p(90)=1.79s    p(95)=2.04s    p(99.9)=4.26s 
     http_reqs......................: 16144   238.072087/s
     iteration_duration.............: avg=961.92ms min=35.24ms med=899.05ms max=5s      p(90)=1.82s    p(95)=2.05s    p(99.9)=4.27s 
     iterations.....................: 15144   223.325302/s
     success_rate...................: 100.00% ✓ 15144      ✗ 0    
     vus............................: 97      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

