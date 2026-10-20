## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 3,132 | 3,253 | 3,113 | 1.5% |  |
| fusion-nightly-net11 | 16.7.0-p.30 | 2,997 | 3,100 | 2,976 | 1.5% |  |
| fusion-nightly | 16.7.0-p.30 | 2,819 | 2,945 | 2,795 | 1.8% |  |
| fusion-nightly-fed | 16.7.0-p.30 | 2,450 | 2,547 | 2,422 | 1.7% |  |
| fusion | 16.6.9 | 2,344 | 2,446 | 2,324 | 1.8% |  |
| hive-router | v0.3.5 | 2,260 | 2,436 | 2,238 | 3.1% |  |
| caliban | 3.2.0 | 1,292 | 1,355 | 1,286 | 2.0% |  |
| cosmo | 0.359.0 | 1,288 | 1,329 | 1,282 | 1.5% |  |
| hive-gateway-router-runtime | 2.15.2 | 457 | 470 | 455 | 1.1% |  |
| hive-gateway | 2.15.2 | 238 | 243 | 236 | 1.0% |  |
| apollo-gateway | 2.14.4 | 237 | 243 | 236 | 0.9% |  |
| apollo-router | v2.18.0 | — | — | — | — | non-compatible response (34240 across 9/9 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | non-compatible response (7017 across 9/9 runs) |
| grafbase | 0.53.5 | — | — | — | — | non-compatible response (273330 across 9/9 runs) |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 572235      ✗ 0     
     data_received..................: 17 GB   274 MB/s
     data_sent......................: 230 MB  3.8 MB/s
     http_req_blocked...............: avg=39.99µs min=792ns    med=2.3µs   max=98.55ms  p(90)=4.29µs   p(95)=5.64µs   p(99.9)=8.12ms  
     http_req_connecting............: avg=36.6µs  min=0s       med=0s      max=98.39ms  p(90)=0s       p(95)=0s       p(99.9)=7.91ms  
     http_req_duration..............: avg=73.78ms min=863.32µs med=65.94ms max=328.82ms p(90)=146.45ms p(95)=169.25ms p(99.9)=247.16ms
       { expected_response:true }...: avg=73.78ms min=863.32µs med=65.94ms max=328.82ms p(90)=146.45ms p(95)=169.25ms p(99.9)=247.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 191745
     http_req_receiving.............: avg=216µs   min=24.62µs  med=52.93µs max=101.99ms p(90)=201.69µs p(95)=390.13µs p(99.9)=31.19ms 
     http_req_sending...............: avg=107.7µs min=4.6µs    med=9.64µs  max=230.33ms p(90)=20.98µs  p(95)=134.32µs p(99.9)=19.27ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=73.45ms min=816.16µs med=65.64ms max=328.29ms p(90)=145.97ms p(95)=168.49ms p(99.9)=246.03ms
     http_reqs......................: 191745  3132.820117/s
     iteration_duration.............: avg=74.72ms min=1.46ms   med=66.79ms max=346.65ms p(90)=147.58ms p(95)=170.79ms p(99.9)=260.74ms
     iterations.....................: 190745  3116.481646/s
     success_rate...................: 100.00% ✓ 190745      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.30)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 550437      ✗ 0     
     data_received..................: 16 GB   263 MB/s
     data_sent......................: 222 MB  3.6 MB/s
     http_req_blocked...............: avg=34.42µs min=842ns   med=2.21µs   max=82.2ms   p(90)=4.2µs    p(95)=5.58µs   p(99.9)=5.95ms  
     http_req_connecting............: avg=31.1µs  min=0s      med=0s       max=82.13ms  p(90)=0s       p(95)=0s       p(99.9)=5.81ms  
     http_req_duration..............: avg=76.94ms min=1.21ms  med=69.99ms  max=409.96ms p(90)=150.69ms p(95)=174.39ms p(99.9)=266.3ms 
       { expected_response:true }...: avg=76.94ms min=1.21ms  med=69.99ms  max=409.96ms p(90)=150.69ms p(95)=174.39ms p(99.9)=266.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 184479
     http_req_receiving.............: avg=1.5ms   min=51.69µs med=102.97µs max=310.35ms p(90)=3.91ms   p(95)=6.48ms   p(99.9)=46.09ms 
     http_req_sending...............: avg=90.58µs min=4.51µs  med=9.05µs   max=231.34ms p(90)=22.01µs  p(95)=123.38µs p(99.9)=14.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=75.34ms min=1.13ms  med=68.17ms  max=409.88ms p(90)=148.84ms p(95)=172.8ms  p(99.9)=260.63ms
     http_reqs......................: 184479  2997.155988/s
     iteration_duration.............: avg=77.68ms min=2.71ms  med=70.84ms  max=410.15ms p(90)=151.39ms p(95)=175.06ms p(99.9)=267.66ms
     iterations.....................: 183479  2980.909391/s
     success_rate...................: 100.00% ✓ 183479      ✗ 0     
     vus............................: 82      min=0         max=492 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.30)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 518412      ✗ 0     
     data_received..................: 15 GB   247 MB/s
     data_sent......................: 209 MB  3.4 MB/s
     http_req_blocked...............: avg=36.48µs  min=982ns   med=2.78µs  max=110.33ms p(90)=4.54µs   p(95)=5.81µs   p(99.9)=6.65ms  
     http_req_connecting............: avg=32.53µs  min=0s      med=0s      max=110.13ms p(90)=0s       p(95)=0s       p(99.9)=6.15ms  
     http_req_duration..............: avg=81.66ms  min=1.28ms  med=66.81ms max=1.58s    p(90)=160.22ms p(95)=195.33ms p(99.9)=669.44ms
       { expected_response:true }...: avg=81.66ms  min=1.28ms  med=66.81ms max=1.58s    p(90)=160.22ms p(95)=195.33ms p(99.9)=669.44ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 173804
     http_req_receiving.............: avg=2.28ms   min=52.58µs med=98.73µs max=699.32ms p(90)=2.2ms    p(95)=6.95ms   p(99.9)=157.35ms
     http_req_sending...............: avg=102.95µs min=4.55µs  med=10.1µs  max=263.94ms p(90)=20.46µs  p(95)=129.84µs p(99.9)=16.29ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=79.27ms  min=1.2ms   med=65.19ms max=1.58s    p(90)=155.88ms p(95)=189.11ms p(99.9)=653.48ms
     http_reqs......................: 173804  2819.047882/s
     iteration_duration.............: avg=82.54ms  min=2.6ms   med=67.56ms max=1.58s    p(90)=161.2ms  p(95)=197.24ms p(99.9)=676.13ms
     iterations.....................: 172804  2802.828187/s
     success_rate...................: 100.00% ✓ 172804      ✗ 0     
     vus............................: 85      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.30)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 453222      ✗ 0     
     data_received..................: 13 GB   215 MB/s
     data_sent......................: 183 MB  2.9 MB/s
     http_req_blocked...............: avg=22.32µs min=842ns   med=2.29µs  max=90.38ms  p(90)=4.37µs   p(95)=5.59µs   p(99.9)=1.42ms  
     http_req_connecting............: avg=18.93µs min=0s      med=0s      max=90.23ms  p(90)=0s       p(95)=0s       p(99.9)=1.26ms  
     http_req_duration..............: avg=93.5ms  min=1.65ms  med=79.7ms  max=1.17s    p(90)=181.07ms p(95)=213.51ms p(99.9)=588.62ms
       { expected_response:true }...: avg=93.5ms  min=1.65ms  med=79.7ms  max=1.17s    p(90)=181.07ms p(95)=213.51ms p(99.9)=588.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 152074
     http_req_receiving.............: avg=2.35ms  min=51.58µs med=108.9µs max=792.48ms p(90)=2.75ms   p(95)=8.17ms   p(99.9)=126.04ms
     http_req_sending...............: avg=74.95µs min=4.66µs  med=9.59µs  max=168.44ms p(90)=21.53µs  p(95)=116.4µs  p(99.9)=10.41ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.07ms min=1.56ms  med=78.01ms max=1.17s    p(90)=177.43ms p(95)=206.55ms p(99.9)=566.96ms
     http_reqs......................: 152074  2450.553405/s
     iteration_duration.............: avg=94.43ms min=3.16ms  med=80.74ms max=1.17s    p(90)=181.73ms p(95)=214.53ms p(99.9)=589.08ms
     iterations.....................: 151074  2434.439188/s
     success_rate...................: 100.00% ✓ 151074      ✗ 0     
     vus............................: 60      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 432786      ✗ 0     
     data_received..................: 13 GB   206 MB/s
     data_sent......................: 175 MB  2.8 MB/s
     http_req_blocked...............: avg=20.09µs min=891ns   med=2.65µs   max=97.22ms  p(90)=4.41µs   p(95)=5.55µs   p(99.9)=2.22ms  
     http_req_connecting............: avg=16.39µs min=0s      med=0s       max=97.12ms  p(90)=0s       p(95)=0s       p(99.9)=2.13ms  
     http_req_duration..............: avg=97.95ms min=1.49ms  med=84.54ms  max=1.46s    p(90)=188.04ms p(95)=220.4ms  p(99.9)=660.78ms
       { expected_response:true }...: avg=97.95ms min=1.49ms  med=84.54ms  max=1.46s    p(90)=188.04ms p(95)=220.4ms  p(99.9)=660.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 145262
     http_req_receiving.............: avg=1.8ms   min=51.75µs med=108.68µs max=591.63ms p(90)=1.85ms   p(95)=5.28ms   p(99.9)=159.43ms
     http_req_sending...............: avg=72.52µs min=5.01µs  med=10.08µs  max=127.45ms p(90)=19.34µs  p(95)=120.91µs p(99.9)=9.92ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.08ms min=1.42ms  med=83.34ms  max=1.46s    p(90)=185.64ms p(95)=216.05ms p(99.9)=656.67ms
     http_reqs......................: 145262  2344.133561/s
     iteration_duration.............: avg=98.93ms min=3.09ms  med=85.62ms  max=1.46s    p(90)=188.71ms p(95)=221.22ms p(99.9)=665.52ms
     iterations.....................: 144262  2327.996281/s
     success_rate...................: 100.00% ✓ 144262      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 417651      ✗ 0     
     data_received..................: 12 GB   198 MB/s
     data_sent......................: 168 MB  2.7 MB/s
     http_req_blocked...............: avg=14.63µs  min=962ns   med=2.45µs  max=53.63ms  p(90)=4.3µs    p(95)=5.61µs   p(99.9)=1.47ms  
     http_req_connecting............: avg=11.37µs  min=0s      med=0s      max=53.56ms  p(90)=0s       p(95)=0s       p(99.9)=1.38ms  
     http_req_duration..............: avg=101.47ms min=1.55ms  med=96.45ms max=301.41ms p(90)=195.72ms p(95)=211.17ms p(99.9)=262.27ms
       { expected_response:true }...: avg=101.47ms min=1.55ms  med=96.45ms max=301.41ms p(90)=195.72ms p(95)=211.17ms p(99.9)=262.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 140217
     http_req_receiving.............: avg=116.68µs min=26.66µs med=56.57µs max=156.25ms p(90)=123.66µs p(95)=334.19µs p(99.9)=8.1ms   
     http_req_sending...............: avg=62.99µs  min=4.78µs  med=10.59µs max=194.85ms p(90)=20.29µs  p(95)=117.11µs p(99.9)=7.64ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=101.29ms min=1.5ms   med=96.25ms max=301.32ms p(90)=195.51ms p(95)=210.93ms p(99.9)=261.27ms
     http_reqs......................: 140217  2260.236227/s
     iteration_duration.............: avg=102.44ms min=3.9ms   med=97.59ms max=321.21ms p(90)=196.25ms p(95)=211.59ms p(99.9)=263.29ms
     iterations.....................: 139217  2244.116668/s
     success_rate...................: 100.00% ✓ 139217      ✗ 0     
     vus............................: 59      min=0         max=498 
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

     checks.........................: 100.00% ✓ 240507      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 98 MB   1.6 MB/s
     http_req_blocked...............: avg=6.8µs    min=1.03µs  med=2.7µs    max=36.34ms  p(90)=4.65µs   p(95)=5.68µs   p(99.9)=477.44µs
     http_req_connecting............: avg=3.41µs   min=0s      med=0s       max=36.27ms  p(90)=0s       p(95)=0s       p(99.9)=414.85µs
     http_req_duration..............: avg=175.84ms min=2.18ms  med=145.37ms max=889.72ms p(90)=368.67ms p(95)=433.81ms p(99.9)=705.58ms
       { expected_response:true }...: avg=175.84ms min=2.18ms  med=145.37ms max=889.72ms p(90)=368.67ms p(95)=433.81ms p(99.9)=705.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81169
     http_req_receiving.............: avg=80.84µs  min=29.02µs med=63.6µs   max=27.45ms  p(90)=104.87µs p(95)=123.4µs  p(99.9)=2.23ms  
     http_req_sending...............: avg=38.13µs  min=5.26µs  med=12.15µs  max=194.09ms p(90)=19.93µs  p(95)=23.9µs   p(99.9)=3.94ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.72ms min=2.1ms   med=145.26ms max=889.6ms  p(90)=368.56ms p(95)=433.74ms p(99.9)=705.51ms
     http_reqs......................: 81169   1292.627254/s
     iteration_duration.............: avg=178.29ms min=7.47ms  med=147.98ms max=890.06ms p(90)=370.28ms p(95)=435.49ms p(99.9)=706.42ms
     iterations.....................: 80169   1276.702119/s
     success_rate...................: 100.00% ✓ 80169       ✗ 0    
     vus............................: 93      min=0         max=500
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

     checks.........................: 100.00% ✓ 239937      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 97 MB   1.5 MB/s
     http_req_blocked...............: avg=5.85µs   min=982ns  med=2.35µs   max=20.56ms  p(90)=4.11µs   p(95)=5.11µs   p(99.9)=486.42µs
     http_req_connecting............: avg=2.82µs   min=0s     med=0s       max=20.5ms   p(90)=0s       p(95)=0s       p(99.9)=419.78µs
     http_req_duration..............: avg=176.14ms min=2.29ms med=174.71ms max=551.16ms p(90)=334.38ms p(95)=361.11ms p(99.9)=463.58ms
       { expected_response:true }...: avg=176.14ms min=2.29ms med=174.71ms max=551.16ms p(90)=334.38ms p(95)=361.11ms p(99.9)=463.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 80979
     http_req_receiving.............: avg=78.93µs  min=25.5µs med=62.61µs  max=54.69ms  p(90)=102.9µs  p(95)=119.34µs p(99.9)=1.46ms  
     http_req_sending...............: avg=29.37µs  min=5µs    med=10.83µs  max=92.37ms  p(90)=17.81µs  p(95)=21.84µs  p(99.9)=3.75ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=176.03ms min=2.24ms med=174.57ms max=551.07ms p(90)=334.28ms p(95)=360.98ms p(99.9)=462.93ms
     http_reqs......................: 80979   1288.565364/s
     iteration_duration.............: avg=178.57ms min=5.75ms med=177.48ms max=551.36ms p(90)=335.16ms p(95)=361.76ms p(99.9)=463.9ms 
     iterations.....................: 79979   1272.653024/s
     success_rate...................: 100.00% ✓ 79979       ✗ 0    
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

     checks.........................: 100.00% ✓ 86403      ✗ 0    
     data_received..................: 2.6 GB  40 MB/s
     data_sent......................: 36 MB   549 kB/s
     http_req_blocked...............: avg=13.58µs  min=1.23µs  med=3.48µs   max=10.32ms p(90)=5.33µs   p(95)=6.46µs   p(99.9)=2.92ms  
     http_req_connecting............: avg=8.91µs   min=0s      med=0s       max=10.27ms p(90)=0s       p(95)=0s       p(99.9)=2.89ms  
     http_req_duration..............: avg=482.57ms min=4.4ms   med=442.95ms max=2.24s   p(90)=966.51ms p(95)=1.04s    p(99.9)=1.55s   
       { expected_response:true }...: avg=482.57ms min=4.4ms   med=442.95ms max=2.24s   p(90)=966.51ms p(95)=1.04s    p(99.9)=1.55s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 29801
     http_req_receiving.............: avg=85.98µs  min=29.23µs med=77.94µs  max=6.04ms  p(90)=115.46µs p(95)=130.49µs p(99.9)=920.07µs
     http_req_sending...............: avg=37µs     min=5.6µs   med=16.02µs  max=97.38ms p(90)=22.46µs  p(95)=25.34µs  p(99.9)=4.54ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=482.45ms min=4.27ms  med=442.86ms max=2.24s   p(90)=966.4ms  p(95)=1.04s    p(99.9)=1.55s   
     http_reqs......................: 29801   457.05752/s
     iteration_duration.............: avg=499.53ms min=22.74ms med=462.45ms max=2.25s   p(90)=972.74ms p(95)=1.04s    p(99.9)=1.57s   
     iterations.....................: 28801   441.720534/s
     success_rate...................: 100.00% ✓ 28801      ✗ 0    
     vus............................: 67      min=0        max=496
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

     checks.........................: 100.00% ✓ 45354      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 19 MB   286 kB/s
     http_req_blocked...............: avg=27.87µs  min=1.14µs  med=3.27µs   max=9.28ms  p(90)=5.01µs   p(95)=6.57µs   p(99.9)=6.87ms
     http_req_connecting............: avg=22.65µs  min=0s      med=0s       max=9.23ms  p(90)=0s       p(95)=0s       p(99.9)=6.84ms
     http_req_duration..............: avg=904.51ms min=5.68ms  med=816.69ms max=6.16s   p(90)=1.8s     p(95)=2.05s    p(99.9)=4.33s 
       { expected_response:true }...: avg=904.51ms min=5.68ms  med=816.69ms max=6.16s   p(90)=1.8s     p(95)=2.05s    p(99.9)=4.33s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16118
     http_req_receiving.............: avg=106.28µs min=34.21µs med=91.56µs  max=63.05ms p(90)=129.44µs p(95)=143.98µs p(99.9)=1.77ms
     http_req_sending...............: avg=29.1µs   min=5.17µs  med=17.1µs   max=23.59ms p(90)=22µs     p(95)=25.67µs  p(99.9)=2.43ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=904.37ms min=5.55ms  med=816.58ms max=6.16s   p(90)=1.8s     p(95)=2.05s    p(99.9)=4.33s 
     http_reqs......................: 16118   238.22202/s
     iteration_duration.............: avg=964.36ms min=39.22ms med=881.82ms max=6.17s   p(90)=1.83s    p(95)=2.08s    p(99.9)=4.35s 
     iterations.....................: 15118   223.442146/s
     success_rate...................: 100.00% ✓ 15118      ✗ 0    
     vus............................: 82      min=0        max=500
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

     checks.........................: 100.00% ✓ 45921      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   285 kB/s
     http_req_blocked...............: avg=13.82µs  min=1.12µs  med=3.28µs   max=7.89ms   p(90)=5.15µs   p(95)=6.86µs   p(99.9)=2.03ms
     http_req_connecting............: avg=8.87µs   min=0s      med=0s       max=7.81ms   p(90)=0s       p(95)=0s       p(99.9)=2.02ms
     http_req_duration..............: avg=890.6ms  min=7.84ms  med=802.5ms  max=3.06s    p(90)=1.84s    p(95)=1.94s    p(99.9)=2.69s 
       { expected_response:true }...: avg=890.6ms  min=7.84ms  med=802.5ms  max=3.06s    p(90)=1.84s    p(95)=1.94s    p(99.9)=2.69s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16307
     http_req_receiving.............: avg=101.5µs  min=33.83µs med=91.39µs  max=27.88ms  p(90)=130.03µs p(95)=145.75µs p(99.9)=1.1ms 
     http_req_sending...............: avg=56.17µs  min=5.37µs  med=16.97µs  max=216.75ms p(90)=22.49µs  p(95)=26.28µs  p(99.9)=5.4ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=890.45ms min=7.73ms  med=802.37ms max=3.06s    p(90)=1.84s    p(95)=1.94s    p(99.9)=2.69s 
     http_reqs......................: 16307   237.036156/s
     iteration_duration.............: avg=948.79ms min=36.21ms med=878.61ms max=3.08s    p(90)=1.85s    p(95)=1.95s    p(99.9)=2.71s 
     iterations.....................: 15307   222.500303/s
     success_rate...................: 100.00% ✓ 15307      ✗ 0    
     vus............................: 96      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

