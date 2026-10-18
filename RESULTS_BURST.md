## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 3,119 | 3,227 | 3,093 | 1.5% |  |
| fusion-nightly-net11 | 16.7.0-p.28 | 2,617 | 2,735 | 2,598 | 1.8% |  |
| fusion-nightly | 16.7.0-p.28 | 2,582 | 2,712 | 2,573 | 1.8% |  |
| hive-router | v0.3.5 | 2,454 | 2,582 | 2,424 | 2.4% |  |
| fusion | 16.6.8 | 2,406 | 2,511 | 2,400 | 1.6% |  |
| fusion-nightly-fed | 16.7.0-p.28 | 2,364 | 2,474 | 2,355 | 1.7% |  |
| cosmo | 0.359.0 | 1,289 | 1,351 | 1,277 | 1.9% |  |
| caliban | 3.2.0 | 1,281 | 1,343 | 1,273 | 2.0% |  |
| hive-gateway-router-runtime | 2.15.2 | 478 | 489 | 476 | 1.0% |  |
| hive-gateway | 2.15.2 | 243 | 248 | 241 | 1.0% |  |
| apollo-gateway | 2.14.4 | 232 | 239 | 230 | 1.1% |  |
| apollo-router | v2.18.0 | — | — | — | — | non-compatible response (33808 across 9/9 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | non-compatible response (6732 across 9/9 runs) |
| grafbase | 0.53.5 | — | — | — | — | non-compatible response (267914 across 9/9 runs) |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 570033      ✗ 0     
     data_received..................: 17 GB   273 MB/s
     data_sent......................: 229 MB  3.7 MB/s
     http_req_blocked...............: avg=48.4µs   min=881ns    med=2.63µs  max=106.1ms  p(90)=4.74µs   p(95)=6.05µs   p(99.9)=14.41ms 
     http_req_connecting............: avg=44.03µs  min=0s       med=0s      max=103.18ms p(90)=0s       p(95)=0s       p(99.9)=14.11ms 
     http_req_duration..............: avg=73.86ms  min=909.61µs med=63.94ms max=332.25ms p(90)=150.34ms p(95)=177.89ms p(99.9)=265.71ms
       { expected_response:true }...: avg=73.86ms  min=909.61µs med=63.94ms max=332.25ms p(90)=150.34ms p(95)=177.89ms p(99.9)=265.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 191011
     http_req_receiving.............: avg=251.11µs min=27.73µs  med=55.08µs max=87.93ms  p(90)=220.02µs p(95)=413.66µs p(99.9)=35.45ms 
     http_req_sending...............: avg=124.29µs min=4.67µs   med=10.18µs max=206.57ms p(90)=21.99µs  p(95)=143.61µs p(99.9)=21.73ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=73.48ms  min=853.23µs med=63.64ms max=332.2ms  p(90)=149.6ms  p(95)=177ms    p(99.9)=262.35ms
     http_reqs......................: 191011  3119.620198/s
     iteration_duration.............: avg=75.01ms  min=1.46ms   med=64.86ms max=354.15ms p(90)=151.98ms p(95)=180.11ms p(99.9)=275.02ms
     iterations.....................: 190011  3103.288048/s
     success_rate...................: 100.00% ✓ 190011      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 481092      ✗ 0     
     data_received..................: 14 GB   230 MB/s
     data_sent......................: 194 MB  3.1 MB/s
     http_req_blocked...............: avg=30.69µs min=1.05µs  med=2.95µs  max=67.43ms  p(90)=4.85µs   p(95)=6.14µs   p(99.9)=5.36ms  
     http_req_connecting............: avg=26.61µs min=0s      med=0s      max=67.24ms  p(90)=0s       p(95)=0s       p(99.9)=5.2ms   
     http_req_duration..............: avg=88.03ms min=1.35ms  med=81.96ms max=348.63ms p(90)=170.09ms p(95)=191.35ms p(99.9)=271.35ms
       { expected_response:true }...: avg=88.03ms min=1.35ms  med=81.96ms max=348.63ms p(90)=170.09ms p(95)=191.35ms p(99.9)=271.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 161364
     http_req_receiving.............: avg=1.61ms  min=53.58µs med=132.8µs max=333.14ms p(90)=3.92ms   p(95)=6.37ms   p(99.9)=44.02ms 
     http_req_sending...............: avg=87.84µs min=4.74µs  med=10.47µs max=176.78ms p(90)=21.92µs  p(95)=133.36µs p(99.9)=12.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=86.33ms min=1.26ms  med=80.02ms max=341.02ms p(90)=168.22ms p(95)=189.33ms p(99.9)=268.57ms
     http_reqs......................: 161364  2617.524527/s
     iteration_duration.............: avg=88.9ms  min=4.24ms  med=82.88ms max=357.69ms p(90)=170.68ms p(95)=192.12ms p(99.9)=273.39ms
     iterations.....................: 160364  2601.303285/s
     success_rate...................: 100.00% ✓ 160364      ✗ 0     
     vus............................: 87      min=0         max=493 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 475674      ✗ 0     
     data_received..................: 14 GB   227 MB/s
     data_sent......................: 192 MB  3.1 MB/s
     http_req_blocked...............: avg=26.57µs min=1.11µs  med=2.89µs  max=85.76ms  p(90)=4.73µs   p(95)=5.98µs   p(99.9)=3.91ms  
     http_req_connecting............: avg=22.48µs min=0s      med=0s      max=85.56ms  p(90)=0s       p(95)=0s       p(99.9)=3.56ms  
     http_req_duration..............: avg=89.13ms min=1.37ms  med=73.03ms max=1.63s    p(90)=167.99ms p(95)=206.75ms p(99.9)=1.13s   
       { expected_response:true }...: avg=89.13ms min=1.37ms  med=73.03ms max=1.63s    p(90)=167.99ms p(95)=206.75ms p(99.9)=1.13s   
     http_req_failed................: 0.00%   ✓ 0           ✗ 159558
     http_req_receiving.............: avg=3.23ms  min=52.76µs med=108.8µs max=1.24s    p(90)=3.08ms   p(95)=11.12ms  p(99.9)=320.46ms
     http_req_sending...............: avg=82.32µs min=4.66µs  med=10.3µs  max=189.43ms p(90)=20.44µs  p(95)=124.5µs  p(99.9)=11.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=85.81ms min=1.29ms  med=71.14ms max=1.63s    p(90)=162.74ms p(95)=196.86ms p(99.9)=1.05s   
     http_reqs......................: 159558  2582.669172/s
     iteration_duration.............: avg=90ms    min=2.48ms  med=74ms    max=1.63s    p(90)=168.81ms p(95)=207.64ms p(99.9)=1.13s   
     iterations.....................: 158558  2566.482775/s
     success_rate...................: 100.00% ✓ 158558      ✗ 0     
     vus............................: 92      min=0         max=499 
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

     checks.........................: 100.00% ✓ 453267      ✗ 0     
     data_received..................: 13 GB   215 MB/s
     data_sent......................: 183 MB  2.9 MB/s
     http_req_blocked...............: avg=17.4µs  min=902ns   med=2.42µs  max=65.23ms  p(90)=4.27µs   p(95)=5.61µs   p(99.9)=1.63ms  
     http_req_connecting............: avg=13.89µs min=0s      med=0s      max=65.14ms  p(90)=0s       p(95)=0s       p(99.9)=1.46ms  
     http_req_duration..............: avg=93.5ms  min=1.44ms  med=88.88ms max=283.32ms p(90)=180.38ms p(95)=194.97ms p(99.9)=244.56ms
       { expected_response:true }...: avg=93.5ms  min=1.44ms  med=88.88ms max=283.32ms p(90)=180.38ms p(95)=194.97ms p(99.9)=244.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 152089
     http_req_receiving.............: avg=140.2µs min=27.03µs med=55.53µs max=79.68ms  p(90)=149.55µs p(95)=357.7µs  p(99.9)=13.28ms 
     http_req_sending...............: avg=65.36µs min=4.75µs  med=10.44µs max=145.98ms p(90)=21.57µs  p(95)=124.45µs p(99.9)=8.49ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.29ms min=1.4ms   med=88.7ms  max=276.27ms p(90)=180.11ms p(95)=194.62ms p(99.9)=243.83ms
     http_reqs......................: 152089  2454.386907/s
     iteration_duration.............: avg=94.37ms min=4.31ms  med=89.94ms max=300.32ms p(90)=180.87ms p(95)=195.43ms p(99.9)=245.53ms
     iterations.....................: 151089  2438.249074/s
     success_rate...................: 100.00% ✓ 151089      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion (HotChocolate subgraphs) (16.6.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 443886      ✗ 0     
     data_received..................: 13 GB   211 MB/s
     data_sent......................: 179 MB  2.9 MB/s
     http_req_blocked...............: avg=20.36µs min=862ns  med=2.27µs  max=91.13ms p(90)=4.11µs   p(95)=5.31µs   p(99.9)=2.15ms  
     http_req_connecting............: avg=17.11µs min=0s     med=0s      max=91.03ms p(90)=0s       p(95)=0s       p(99.9)=2.1ms   
     http_req_duration..............: avg=95.5ms  min=1.55ms med=81.8ms  max=1.61s   p(90)=175.13ms p(95)=210.58ms p(99.9)=942.11ms
       { expected_response:true }...: avg=95.5ms  min=1.55ms med=81.8ms  max=1.61s   p(90)=175.13ms p(95)=210.58ms p(99.9)=942.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 148962
     http_req_receiving.............: avg=1.43ms  min=51.7µs med=101.7µs max=1.29s   p(90)=1.49ms   p(95)=3.99ms   p(99.9)=107.07ms
     http_req_sending...............: avg=68.6µs  min=4.66µs med=9.3µs   max=97.64ms p(90)=20.29µs  p(95)=111.65µs p(99.9)=9.19ms  
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94ms    min=1.44ms med=80.58ms max=1.57s   p(90)=173.3ms  p(95)=207.98ms p(99.9)=892.23ms
     http_reqs......................: 148962  2406.529507/s
     iteration_duration.............: avg=96.41ms min=3.06ms med=82.86ms max=1.61s   p(90)=175.82ms p(95)=211.43ms p(99.9)=945.51ms
     iterations.....................: 147962  2390.374182/s
     success_rate...................: 100.00% ✓ 147962      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 437154      ✗ 0     
     data_received..................: 13 GB   207 MB/s
     data_sent......................: 176 MB  2.8 MB/s
     http_req_blocked...............: avg=19.57µs min=832ns   med=2.26µs   max=78.34ms  p(90)=4.25µs   p(95)=5.51µs   p(99.9)=1.46ms  
     http_req_connecting............: avg=16.39µs min=0s      med=0s       max=78.25ms  p(90)=0s       p(95)=0s       p(99.9)=1.38ms  
     http_req_duration..............: avg=97ms    min=1.64ms  med=82.53ms  max=1.04s    p(90)=186.21ms p(95)=216.65ms p(99.9)=647.19ms
       { expected_response:true }...: avg=97ms    min=1.64ms  med=82.53ms  max=1.04s    p(90)=186.21ms p(95)=216.65ms p(99.9)=647.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 146718
     http_req_receiving.............: avg=2.09ms  min=52.86µs med=110.77µs max=547.77ms p(90)=2.65ms   p(95)=7.08ms   p(99.9)=111.4ms 
     http_req_sending...............: avg=72.21µs min=4.85µs  med=9.43µs   max=156.98ms p(90)=20.51µs  p(95)=111.8µs  p(99.9)=9.81ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.83ms min=1.56ms  med=80.93ms  max=1s       p(90)=182.59ms p(95)=210.55ms p(99.9)=636.25ms
     http_reqs......................: 146718  2364.540139/s
     iteration_duration.............: avg=97.92ms min=3.06ms  med=83.67ms  max=1.04s    p(90)=186.84ms p(95)=217.37ms p(99.9)=647.54ms
     iterations.....................: 145718  2348.423915/s
     success_rate...................: 100.00% ✓ 145718      ✗ 0     
     vus............................: 59      min=0         max=498 
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

     checks.........................: 100.00% ✓ 240303      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 97 MB   1.5 MB/s
     http_req_blocked...............: avg=7.43µs   min=1µs     med=2.48µs   max=102.6ms  p(90)=4.35µs   p(95)=5.44µs   p(99.9)=695µs   
     http_req_connecting............: avg=2.91µs   min=0s      med=0s       max=13.64ms  p(90)=0s       p(95)=0s       p(99.9)=471.71µs
     http_req_duration..............: avg=175.87ms min=2.34ms  med=173.53ms max=491.94ms p(90)=334.79ms p(95)=360.25ms p(99.9)=428.04ms
       { expected_response:true }...: avg=175.87ms min=2.34ms  med=173.53ms max=491.94ms p(90)=334.79ms p(95)=360.25ms p(99.9)=428.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81101
     http_req_receiving.............: avg=83.87µs  min=27.53µs med=66.2µs   max=99.6ms   p(90)=107.44µs p(95)=125.11µs p(99.9)=1.67ms  
     http_req_sending...............: avg=30.96µs  min=5.17µs  med=11.41µs  max=68.53ms  p(90)=18.98µs  p(95)=23.11µs  p(99.9)=3.77ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.76ms min=2.22ms  med=173.43ms max=491.86ms p(90)=334.68ms p(95)=360.16ms p(99.9)=427.97ms
     http_reqs......................: 81101   1289.775315/s
     iteration_duration.............: avg=178.31ms min=4.95ms  med=176.34ms max=492.12ms p(90)=335.7ms  p(95)=360.77ms p(99.9)=428.34ms
     iterations.....................: 80101   1273.871993/s
     success_rate...................: 100.00% ✓ 80101       ✗ 0    
     vus............................: 48      min=0         max=499
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

     checks.........................: 100.00% ✓ 238425      ✗ 0    
     data_received..................: 7.0 GB  112 MB/s
     data_sent......................: 97 MB   1.5 MB/s
     http_req_blocked...............: avg=6.29µs   min=932ns   med=2.59µs   max=19.43ms  p(90)=4.55µs   p(95)=5.62µs   p(99.9)=522.25µs
     http_req_connecting............: avg=3.01µs   min=0s      med=0s       max=19.35ms  p(90)=0s       p(95)=0s       p(99.9)=453.15µs
     http_req_duration..............: avg=177.33ms min=2.19ms  med=148.53ms max=916.42ms p(90)=371.75ms p(95)=437.26ms p(99.9)=700.79ms
       { expected_response:true }...: avg=177.33ms min=2.19ms  med=148.53ms max=916.42ms p(90)=371.75ms p(95)=437.26ms p(99.9)=700.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 80475
     http_req_receiving.............: avg=81.33µs  min=27.92µs med=62.69µs  max=110.77ms p(90)=101.89µs p(95)=118.83µs p(99.9)=1.87ms  
     http_req_sending...............: avg=36.29µs  min=5.18µs  med=11.52µs  max=196.36ms p(90)=18.4µs   p(95)=22.28µs  p(99.9)=3.8ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=177.21ms min=2.08ms  med=148.34ms max=916.36ms p(90)=371.64ms p(95)=437.16ms p(99.9)=700.74ms
     http_reqs......................: 80475   1281.095881/s
     iteration_duration.............: avg=179.81ms min=8.12ms  med=151.36ms max=916.62ms p(90)=373.19ms p(95)=438.64ms p(99.9)=701.78ms
     iterations.....................: 79475   1265.176702/s
     success_rate...................: 100.00% ✓ 79475       ✗ 0    
     vus............................: 96      min=0         max=500
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

     checks.........................: 100.00% ✓ 90471      ✗ 0    
     data_received..................: 2.7 GB  42 MB/s
     data_sent......................: 37 MB   575 kB/s
     http_req_blocked...............: avg=9.39µs   min=1.04µs  med=2.91µs   max=12.55ms  p(90)=4.66µs   p(95)=5.75µs   p(99.9)=1.5ms 
     http_req_connecting............: avg=5.46µs   min=0s      med=0s       max=12.49ms  p(90)=0s       p(95)=0s       p(99.9)=1.48ms
     http_req_duration..............: avg=461.12ms min=4.23ms  med=430.16ms max=2.06s    p(90)=911.4ms  p(95)=995.02ms p(99.9)=1.47s 
       { expected_response:true }...: avg=461.12ms min=4.23ms  med=430.16ms max=2.06s    p(90)=911.4ms  p(95)=995.02ms p(99.9)=1.47s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 31157
     http_req_receiving.............: avg=86.09µs  min=28.7µs  med=76.06µs  max=54.22ms  p(90)=114.45µs p(95)=128.29µs p(99.9)=1ms   
     http_req_sending...............: avg=40.9µs   min=4.83µs  med=14.3µs   max=141.54ms p(90)=21.09µs  p(95)=23.76µs  p(99.9)=2.91ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=460.99ms min=4.11ms  med=430.05ms max=2.06s    p(90)=911.34ms p(95)=994.9ms  p(99.9)=1.47s 
     http_reqs......................: 31157   478.651093/s
     iteration_duration.............: avg=476.62ms min=28.74ms med=448.01ms max=2.06s    p(90)=916.94ms p(95)=998.79ms p(99.9)=1.49s 
     iterations.....................: 30157   463.288539/s
     success_rate...................: 100.00% ✓ 30157      ✗ 0    
     vus............................: 61      min=0        max=498
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

     checks.........................: 100.00% ✓ 46299      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   292 kB/s
     http_req_blocked...............: avg=14.6µs   min=1.18µs  med=3.46µs   max=12.08ms  p(90)=5.29µs   p(95)=6.92µs   p(99.9)=2.06ms
     http_req_connecting............: avg=9.44µs   min=0s      med=0s       max=11.85ms  p(90)=0s       p(95)=0s       p(99.9)=1.97ms
     http_req_duration..............: avg=885.82ms min=5.85ms  med=791.45ms max=4.68s    p(90)=1.75s    p(95)=2.04s    p(99.9)=4.17s 
       { expected_response:true }...: avg=885.82ms min=5.85ms  med=791.45ms max=4.68s    p(90)=1.75s    p(95)=2.04s    p(99.9)=4.17s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16433
     http_req_receiving.............: avg=107.29µs min=34.32µs med=94.95µs  max=89.22ms  p(90)=133.89µs p(95)=149.63µs p(99.9)=1.29ms
     http_req_sending...............: avg=40.64µs  min=5.4µs   med=17.57µs  max=128.17ms p(90)=22.92µs  p(95)=26.74µs  p(99.9)=2.89ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=885.67ms min=5.76ms  med=791.31ms max=4.68s    p(90)=1.75s    p(95)=2.04s    p(99.9)=4.17s 
     http_reqs......................: 16433   243.604033/s
     iteration_duration.............: avg=943.33ms min=26.33ms med=868.62ms max=4.69s    p(90)=1.78s    p(95)=2.07s    p(99.9)=4.19s 
     iterations.....................: 15433   228.779958/s
     success_rate...................: 100.00% ✓ 15433      ✗ 0    
     vus............................: 77      min=0        max=500
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

     checks.........................: 100.00% ✓ 44898      ✗ 0    
     data_received..................: 1.4 GB  20 MB/s
     data_sent......................: 19 MB   279 kB/s
     http_req_blocked...............: avg=13.91µs  min=1.14µs  med=3.25µs   max=4.75ms   p(90)=5.03µs   p(95)=6.48µs   p(99.9)=2.09ms 
     http_req_connecting............: avg=8.89µs   min=0s      med=0s       max=4.63ms   p(90)=0s       p(95)=0s       p(99.9)=1.84ms 
     http_req_duration..............: avg=909.85ms min=7.74ms  med=837.75ms max=3.24s    p(90)=1.87s    p(95)=1.99s    p(99.9)=2.9s   
       { expected_response:true }...: avg=909.85ms min=7.74ms  med=837.75ms max=3.24s    p(90)=1.87s    p(95)=1.99s    p(99.9)=2.9s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 15966
     http_req_receiving.............: avg=214.57µs min=31.73µs med=87.42µs  max=129.34ms p(90)=125.55µs p(95)=141.88µs p(99.9)=51.59ms
     http_req_sending...............: avg=29.17µs  min=5.4µs   med=16.38µs  max=56.64ms  p(90)=21.74µs  p(95)=25.32µs  p(99.9)=3.1ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=909.6ms  min=7.66ms  med=837.62ms max=3.24s    p(90)=1.87s    p(95)=1.99s    p(99.9)=2.9s   
     http_reqs......................: 15966   232.105317/s
     iteration_duration.............: avg=970.58ms min=61.12ms med=920.95ms max=3.25s    p(90)=1.88s    p(95)=2s       p(99.9)=2.91s  
     iterations.....................: 14966   217.567843/s
     success_rate...................: 100.00% ✓ 14966      ✗ 0    
     vus............................: 92      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

