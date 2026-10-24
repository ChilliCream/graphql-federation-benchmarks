## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-fed-net-11 | 16.7.0-p.38 | 3,756 | 3,969 | 3,645 | 2.8% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.38 | 3,720 | 3,962 | 3,641 | 2.7% |  |
| fusion-nightly-net-11 | 16.7.0-p.38 | 3,698 | 3,895 | 3,657 | 2.1% |  |
| fusion-nightly-aot-11 | 16.7.0-p.38 | 3,693 | 3,834 | 3,601 | 1.9% |  |
| fusion-nightly-net-10 | 16.7.0-p.38 | 3,653 | 3,867 | 3,607 | 2.3% |  |
| fusion-nightly-fed-aot-11 | 16.7.0-p.38 | 3,555 | 3,740 | 3,531 | 2.1% |  |
| feddi-gateway | 3c75a7db8876 | 3,040 | 3,145 | 3,020 | 1.4% |  |
| fusion-net-11 | 16.6.9 | 2,456 | 2,528 | 2,444 | 1.3% |  |
| fusion-net-10 | 16.6.9 | 2,444 | 2,554 | 2,433 | 1.7% |  |
| hive-router | v0.3.5 | 2,317 | 2,483 | 2,284 | 2.9% |  |
| fusion-fed-net-11 | 16.6.9 | 2,308 | 2,386 | 2,296 | 1.3% |  |
| fusion-fed-net-10 | 16.6.9 | 2,229 | 2,321 | 2,219 | 1.6% |  |
| fusion-aot-11 | 16.6.9 | 2,107 | 2,175 | 2,098 | 1.3% |  |
| fusion-fed-aot-11 | 16.6.9 | 1,882 | 1,946 | 1,847 | 1.6% |  |
| caliban | 3.2.0 | 1,294 | 1,346 | 1,280 | 1.9% |  |
| cosmo | 0.361.0 | 1,292 | 1,350 | 1,276 | 1.9% |  |
| hive-gateway-router-runtime | 2.15.2 | 461 | 474 | 458 | 1.3% |  |
| apollo-gateway | 2.14.4 | 237 | 241 | 235 | 0.8% |  |
| hive-gateway | 2.15.2 | 230 | 238 | 227 | 1.4% |  |
| apollo-router | v2.18.0 | — | — | — | — | non-compatible response (26240 across 9/9 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | non-compatible response (7921 across 8/8 runs) |
| grafbase | 0.53.5 | — | — | — | — | non-compatible response (339908 across 9/9 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 689256      ✗ 0     
     data_received..................: 20 GB   329 MB/s
     data_sent......................: 277 MB  4.5 MB/s
     http_req_blocked...............: avg=79.41µs  min=811ns  med=2.17µs  max=140.09ms p(90)=3.84µs   p(95)=4.99µs   p(99.9)=32.91ms 
     http_req_connecting............: avg=75.77µs  min=0s     med=0s      max=139.8ms  p(90)=0s       p(95)=0s       p(99.9)=32.43ms 
     http_req_duration..............: avg=59.6ms   min=1.17ms med=51.32ms max=343.66ms p(90)=121.87ms p(95)=149.23ms p(99.9)=216.01ms
       { expected_response:true }...: avg=59.6ms   min=1.17ms med=51.32ms max=343.66ms p(90)=121.87ms p(95)=149.23ms p(99.9)=216.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 230752
     http_req_receiving.............: avg=1.11ms   min=55.4µs med=87.86µs max=284.44ms p(90)=2.35ms   p(95)=5.51ms   p(99.9)=66.18ms 
     http_req_sending...............: avg=156.71µs min=4.44µs med=8.95µs  max=150.75ms p(90)=17.47µs  p(95)=119.12µs p(99.9)=28.96ms 
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=58.33ms  min=1.1ms  med=50.1ms  max=320.31ms p(90)=120.43ms p(95)=147.97ms p(99.9)=203.26ms
     http_reqs......................: 230752  3756.560488/s
     iteration_duration.............: avg=62.02ms  min=1.91ms med=52.9ms  max=373.58ms p(90)=127.41ms p(95)=156.71ms p(99.9)=250.64ms
     iterations.....................: 229752  3740.280844/s
     success_rate...................: 100.00% ✓ 229752      ✗ 0     
     vus............................: 77      min=0         max=493 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 683940      ✗ 0     
     data_received..................: 20 GB   326 MB/s
     data_sent......................: 275 MB  4.5 MB/s
     http_req_blocked...............: avg=92.95µs  min=852ns   med=2.29µs  max=181.89ms p(90)=4.23µs   p(95)=5.53µs   p(99.9)=42.18ms 
     http_req_connecting............: avg=89.22µs  min=0s      med=0s      max=181.79ms p(90)=0s       p(95)=0s       p(99.9)=41.8ms  
     http_req_duration..............: avg=60.08ms  min=1.24ms  med=51.67ms max=335.65ms p(90)=123.77ms p(95)=150.56ms p(99.9)=215.3ms 
       { expected_response:true }...: avg=60.08ms  min=1.24ms  med=51.67ms max=335.65ms p(90)=123.77ms p(95)=150.56ms p(99.9)=215.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 228980
     http_req_receiving.............: avg=827.88µs min=48.43µs med=88.13µs max=308.41ms p(90)=1.22ms   p(95)=3.75ms   p(99.9)=54.91ms 
     http_req_sending...............: avg=170µs    min=4.57µs  med=9.07µs  max=156.42ms p(90)=19.48µs  p(95)=124.6µs  p(99.9)=33.97ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=59.08ms  min=1.14ms  med=50.95ms max=318.51ms p(90)=122.3ms  p(95)=149.16ms p(99.9)=208.39ms
     http_reqs......................: 228980  3720.406005/s
     iteration_duration.............: avg=62.5ms   min=1.95ms  med=52.78ms max=388.36ms p(90)=129.55ms p(95)=158.17ms p(99.9)=247.13ms
     iterations.....................: 227980  3704.158272/s
     success_rate...................: 100.00% ✓ 227980      ✗ 0     
     vus............................: 82      min=0         max=492 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 676032      ✗ 0     
     data_received..................: 20 GB   324 MB/s
     data_sent......................: 272 MB  4.4 MB/s
     http_req_blocked...............: avg=93.89µs  min=881ns    med=2.82µs  max=148.35ms p(90)=4.6µs    p(95)=5.85µs   p(99.9)=37.52ms 
     http_req_connecting............: avg=89.5µs   min=0s       med=0s      max=140.18ms p(90)=0s       p(95)=0s       p(99.9)=37.31ms 
     http_req_duration..............: avg=60.52ms  min=888.89µs med=52.74ms max=330.41ms p(90)=124.15ms p(95)=152.16ms p(99.9)=217.64ms
       { expected_response:true }...: avg=60.52ms  min=888.89µs med=52.74ms max=330.41ms p(90)=124.15ms p(95)=152.16ms p(99.9)=217.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 226344
     http_req_receiving.............: avg=1.3ms    min=47.67µs  med=88.89µs max=138.96ms p(90)=2.77ms   p(95)=6.88ms   p(99.9)=66.16ms 
     http_req_sending...............: avg=169.27µs min=4.1µs    med=9.7µs   max=116.49ms p(90)=19.85µs  p(95)=129.11µs p(99.9)=32.8ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=59.05ms  min=784.89µs med=51.32ms max=309.76ms p(90)=122.73ms p(95)=150.96ms p(99.9)=212.83ms
     http_reqs......................: 226344  3698.5225/s
     iteration_duration.............: avg=63.23ms  min=1.77ms   med=54.31ms max=382.59ms p(90)=129.85ms p(95)=158.7ms  p(99.9)=267.78ms
     iterations.....................: 225344  3682.182228/s
     success_rate...................: 100.00% ✓ 225344      ✗ 0     
     vus............................: 65      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 675369      ✗ 0     
     data_received..................: 20 GB   324 MB/s
     data_sent......................: 272 MB  4.4 MB/s
     http_req_blocked...............: avg=65.76µs  min=811ns    med=2.09µs  max=113.27ms p(90)=3.81µs   p(95)=5.05µs   p(99.9)=25.73ms 
     http_req_connecting............: avg=62.52µs  min=0s       med=0s      max=109.67ms p(90)=0s       p(95)=0s       p(99.9)=25.67ms 
     http_req_duration..............: avg=61.72ms  min=948.17µs med=53.81ms max=323.68ms p(90)=125.44ms p(95)=151.63ms p(99.9)=216.55ms
       { expected_response:true }...: avg=61.72ms  min=948.17µs med=53.81ms max=323.68ms p(90)=125.44ms p(95)=151.63ms p(99.9)=216.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 226123
     http_req_receiving.............: avg=2.08ms   min=48.26µs  med=89.97µs max=214.13ms p(90)=6.99ms   p(95)=10.41ms  p(99.9)=55.82ms 
     http_req_sending...............: avg=129.44µs min=4.28µs   med=8.66µs  max=108.28ms p(90)=18.81µs  p(95)=118.9µs  p(99.9)=24.03ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=59.51ms  min=845.17µs med=50.91ms max=307.63ms p(90)=123.83ms p(95)=150.29ms p(99.9)=213.47ms
     http_reqs......................: 226123  3693.844534/s
     iteration_duration.............: avg=63.29ms  min=1.69ms   med=54.89ms max=350.73ms p(90)=128.51ms p(95)=155.61ms p(99.9)=232.53ms
     iterations.....................: 225123  3677.50898/s
     success_rate...................: 100.00% ✓ 225123      ✗ 0     
     vus............................: 66      min=0         max=495 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 667959      ✗ 0     
     data_received..................: 20 GB   320 MB/s
     data_sent......................: 269 MB  4.4 MB/s
     http_req_blocked...............: avg=90.12µs  min=1.04µs   med=2.75µs  max=151.76ms p(90)=4.43µs   p(95)=5.6µs    p(99.9)=37.36ms 
     http_req_connecting............: avg=86.1µs   min=0s       med=0s      max=151.55ms p(90)=0s       p(95)=0s       p(99.9)=36.86ms 
     http_req_duration..............: avg=61.29ms  min=906.32µs med=52.88ms max=337.21ms p(90)=126.63ms p(95)=154.93ms p(99.9)=222.16ms
       { expected_response:true }...: avg=61.29ms  min=906.32µs med=52.88ms max=337.21ms p(90)=126.63ms p(95)=154.93ms p(99.9)=222.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 223653
     http_req_receiving.............: avg=1.1ms    min=49.51µs  med=89.65µs max=228.37ms p(90)=2.51ms   p(95)=5.4ms    p(99.9)=57.6ms  
     http_req_sending...............: avg=166.86µs min=4.34µs   med=9.49µs  max=110.89ms p(90)=18.92µs  p(95)=128.93µs p(99.9)=31.71ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=60.02ms  min=800.97µs med=51.83ms max=314.47ms p(90)=125.36ms p(95)=153.52ms p(99.9)=213.2ms 
     http_reqs......................: 223653  3653.53491/s
     iteration_duration.............: avg=64ms     min=1.59ms   med=54.53ms max=439.77ms p(90)=132.28ms p(95)=162.3ms  p(99.9)=251.69ms
     iterations.....................: 222653  3637.199181/s
     success_rate...................: 100.00% ✓ 222653      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 653292      ✗ 0     
     data_received..................: 19 GB   312 MB/s
     data_sent......................: 263 MB  4.3 MB/s
     http_req_blocked...............: avg=88.29µs  min=842ns   med=2.85µs  max=149.95ms p(90)=4.8µs    p(95)=6.14µs   p(99.9)=36.94ms 
     http_req_connecting............: avg=83.53µs  min=0s      med=0s      max=149.88ms p(90)=0s       p(95)=0s       p(99.9)=36.59ms 
     http_req_duration..............: avg=63.47ms  min=1.26ms  med=54.49ms max=336.62ms p(90)=132.32ms p(95)=163.14ms p(99.9)=227.41ms
       { expected_response:true }...: avg=63.47ms  min=1.26ms  med=54.49ms max=336.62ms p(90)=132.32ms p(95)=163.14ms p(99.9)=227.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 218764
     http_req_receiving.............: avg=1.48ms   min=50.45µs med=94.05µs max=170.48ms p(90)=4.49ms   p(95)=7.22ms   p(99.9)=62.96ms 
     http_req_sending...............: avg=157.35µs min=4.49µs  med=10.03µs max=135.52ms p(90)=22.13µs  p(95)=137.42µs p(99.9)=29.86ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=61.82ms  min=1.18ms  med=52.53ms max=335.69ms p(90)=130.91ms p(95)=161.79ms p(99.9)=220.15ms
     http_reqs......................: 218764  3555.069469/s
     iteration_duration.............: avg=65.42ms  min=2.03ms  med=55.39ms max=430.6ms  p(90)=137.07ms p(95)=168.2ms  p(99.9)=266.52ms
     iterations.....................: 217764  3538.818763/s
     success_rate...................: 100.00% ✓ 217764      ✗ 0     
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

     checks.........................: 100.00% ✓ 555381      ✗ 0     
     data_received..................: 16 GB   266 MB/s
     data_sent......................: 224 MB  3.7 MB/s
     http_req_blocked...............: avg=35.58µs  min=832ns    med=2.52µs  max=114.35ms p(90)=4.39µs   p(95)=5.64µs   p(99.9)=5.7ms   
     http_req_connecting............: avg=31.71µs  min=0s       med=0s      max=114.24ms p(90)=0s       p(95)=0s       p(99.9)=5.39ms  
     http_req_duration..............: avg=75.93ms  min=870.33µs med=67.66ms max=389.82ms p(90)=150.13ms p(95)=175.61ms p(99.9)=265.76ms
       { expected_response:true }...: avg=75.93ms  min=870.33µs med=67.66ms max=389.82ms p(90)=150.13ms p(95)=175.61ms p(99.9)=265.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 186127
     http_req_receiving.............: avg=236.52µs min=27.12µs  med=52.93µs max=99.1ms   p(90)=186.04µs p(95)=381.12µs p(99.9)=39.35ms 
     http_req_sending...............: avg=100.13µs min=4.8µs    med=10µs    max=273.06ms p(90)=19.88µs  p(95)=132.03µs p(99.9)=17.43ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=75.59ms  min=821.56µs med=67.38ms max=359.1ms  p(90)=149.52ms p(95)=174.63ms p(99.9)=262.95ms
     http_reqs......................: 186127  3040.730222/s
     iteration_duration.............: avg=76.99ms  min=1.48ms   med=68.54ms max=390ms    p(90)=151.6ms  p(95)=177.68ms p(99.9)=272.22ms
     iterations.....................: 185127  3024.393365/s
     success_rate...................: 100.00% ✓ 185127      ✗ 0     
     vus............................: 67      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 451755      ✗ 0     
     data_received..................: 13 GB   215 MB/s
     data_sent......................: 182 MB  2.9 MB/s
     http_req_blocked...............: avg=17.91µs min=851ns   med=2.2µs   max=51.55ms  p(90)=4.39µs   p(95)=5.72µs   p(99.9)=2.15ms  
     http_req_connecting............: avg=14.82µs min=0s      med=0s      max=51.41ms  p(90)=0s       p(95)=0s       p(99.9)=2.11ms  
     http_req_duration..............: avg=93.8ms  min=1.41ms  med=89.1ms  max=360.12ms p(90)=179.17ms p(95)=191.79ms p(99.9)=234.26ms
       { expected_response:true }...: avg=93.8ms  min=1.41ms  med=89.1ms  max=360.12ms p(90)=179.17ms p(95)=191.79ms p(99.9)=234.26ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 151585
     http_req_receiving.............: avg=4.42ms  min=52.89µs med=4.51ms  max=253.78ms p(90)=7.8ms    p(95)=10.11ms  p(99.9)=39.03ms 
     http_req_sending...............: avg=71.73µs min=4.6µs   med=9.17µs  max=246.12ms p(90)=24.08µs  p(95)=113.9µs  p(99.9)=9.21ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=89.3ms  min=1.35ms  med=83.65ms max=359.69ms p(90)=174.06ms p(95)=187.8ms  p(99.9)=232.65ms
     http_reqs......................: 151585  2456.054971/s
     iteration_duration.............: avg=94.68ms min=2.72ms  med=90.05ms max=369.44ms p(90)=179.59ms p(95)=192.21ms p(99.9)=234.76ms
     iterations.....................: 150585  2439.852477/s
     success_rate...................: 100.00% ✓ 150585      ✗ 0     
     vus............................: 90      min=0         max=500 
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

     checks.........................: 100.00% ✓ 451176      ✗ 0     
     data_received..................: 13 GB   214 MB/s
     data_sent......................: 182 MB  2.9 MB/s
     http_req_blocked...............: avg=20.27µs min=852ns   med=2.34µs  max=64.78ms  p(90)=4.55µs   p(95)=5.81µs   p(99.9)=2.14ms  
     http_req_connecting............: avg=17.15µs min=0s      med=0s      max=64.59ms  p(90)=0s       p(95)=0s       p(99.9)=2.04ms  
     http_req_duration..............: avg=93.92ms min=1.49ms  med=90.07ms max=324.27ms p(90)=178.84ms p(95)=192.01ms p(99.9)=248.5ms 
       { expected_response:true }...: avg=93.92ms min=1.49ms  med=90.07ms max=324.27ms p(90)=178.84ms p(95)=192.01ms p(99.9)=248.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 151392
     http_req_receiving.............: avg=2.13ms  min=52.49µs med=1.56ms  max=61.19ms  p(90)=4.77ms   p(95)=6.05ms   p(99.9)=30.87ms 
     http_req_sending...............: avg=67.94µs min=4.58µs  med=9.28µs  max=146.25ms p(90)=23.52µs  p(95)=120.21µs p(99.9)=8.99ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.72ms min=1.41ms  med=87.61ms max=324.03ms p(90)=176.47ms p(95)=189.91ms p(99.9)=247.21ms
     http_reqs......................: 151392  2444.990201/s
     iteration_duration.............: avg=94.81ms min=3.76ms  med=91.08ms max=346ms    p(90)=179.28ms p(95)=192.48ms p(99.9)=249.16ms
     iterations.....................: 150392  2428.840139/s
     success_rate...................: 100.00% ✓ 150392      ✗ 0     
     vus............................: 51      min=0         max=499 
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

     checks.........................: 100.00% ✓ 427518      ✗ 0     
     data_received..................: 13 GB   203 MB/s
     data_sent......................: 172 MB  2.8 MB/s
     http_req_blocked...............: avg=15.32µs  min=882ns   med=2.37µs  max=59.21ms  p(90)=4.16µs   p(95)=5.47µs   p(99.9)=771.09µs
     http_req_connecting............: avg=12.21µs  min=0s      med=0s      max=59.02ms  p(90)=0s       p(95)=0s       p(99.9)=632.23µs
     http_req_duration..............: avg=99.11ms  min=1.43ms  med=93.73ms max=312.58ms p(90)=191.49ms p(95)=206.74ms p(99.9)=254.82ms
       { expected_response:true }...: avg=99.11ms  min=1.43ms  med=93.73ms max=312.58ms p(90)=191.49ms p(95)=206.74ms p(99.9)=254.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 143506
     http_req_receiving.............: avg=126.42µs min=27.31µs med=56.71µs max=45.94ms  p(90)=122.18µs p(95)=331.77µs p(99.9)=12.33ms 
     http_req_sending...............: avg=59.59µs  min=4.67µs  med=10.34µs max=115.37ms p(90)=19.53µs  p(95)=115.02µs p(99.9)=8.11ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=98.93ms  min=1.38ms  med=93.56ms max=312.43ms p(90)=191.31ms p(95)=206.51ms p(99.9)=254.23ms
     http_reqs......................: 143506  2317.665474/s
     iteration_duration.............: avg=100.06ms min=3.63ms  med=94.84ms max=357.36ms p(90)=192.03ms p(95)=207.2ms  p(99.9)=255.13ms
     iterations.....................: 142506  2301.51517/s
     success_rate...................: 100.00% ✓ 142506      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 426900      ✗ 0     
     data_received..................: 13 GB   202 MB/s
     data_sent......................: 172 MB  2.8 MB/s
     http_req_blocked...............: avg=18.45µs  min=871ns   med=2.46µs  max=44.08ms  p(90)=4.87µs   p(95)=6.05µs   p(99.9)=1.64ms  
     http_req_connecting............: avg=15.12µs  min=0s      med=0s      max=43.95ms  p(90)=0s       p(95)=0s       p(99.9)=1.48ms  
     http_req_duration..............: avg=99.24ms  min=1.7ms   med=95.69ms max=340.64ms p(90)=190.08ms p(95)=202.52ms p(99.9)=239.23ms
       { expected_response:true }...: avg=99.24ms  min=1.7ms   med=95.69ms max=340.64ms p(90)=190.08ms p(95)=202.52ms p(99.9)=239.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 143300
     http_req_receiving.............: avg=4.62ms   min=53.33µs med=4.79ms  max=256.26ms p(90)=7.83ms   p(95)=10.05ms  p(99.9)=38.08ms 
     http_req_sending...............: avg=71.8µs   min=4.7µs   med=9.88µs  max=138.08ms p(90)=26.44µs  p(95)=119.79µs p(99.9)=9.1ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.54ms  min=1.62ms  med=89.69ms max=340.5ms  p(90)=184.58ms p(95)=197.54ms p(99.9)=237.66ms
     http_reqs......................: 143300  2308.694811/s
     iteration_duration.............: avg=100.21ms min=3.31ms  med=96.77ms max=348.7ms  p(90)=190.48ms p(95)=202.99ms p(99.9)=241.09ms
     iterations.....................: 142300  2292.583891/s
     success_rate...................: 100.00% ✓ 142300      ✗ 0     
     vus............................: 60      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-10 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 412302      ✗ 0     
     data_received..................: 12 GB   195 MB/s
     data_sent......................: 166 MB  2.7 MB/s
     http_req_blocked...............: avg=20.89µs  min=881ns   med=2.28µs  max=80.04ms  p(90)=4.32µs   p(95)=5.57µs   p(99.9)=1.79ms  
     http_req_connecting............: avg=17.33µs  min=0s      med=0s      max=79.76ms  p(90)=0s       p(95)=0s       p(99.9)=1.65ms  
     http_req_duration..............: avg=102.75ms min=1.65ms  med=98.83ms max=293.1ms  p(90)=194.16ms p(95)=208.06ms p(99.9)=256.22ms
       { expected_response:true }...: avg=102.75ms min=1.65ms  med=98.83ms max=293.1ms  p(90)=194.16ms p(95)=208.06ms p(99.9)=256.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 138434
     http_req_receiving.............: avg=2.36ms   min=53.27µs med=1.88ms  max=58.88ms  p(90)=5.12ms   p(95)=6.4ms    p(99.9)=27.74ms 
     http_req_sending...............: avg=63.94µs  min=4.69µs  med=9.37µs  max=141.07ms p(90)=22.81µs  p(95)=111.52µs p(99.9)=7.87ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.32ms min=1.58ms  med=96.07ms max=289.63ms p(90)=191.54ms p(95)=205.49ms p(99.9)=254.58ms
     http_reqs......................: 138434  2229.642965/s
     iteration_duration.............: avg=103.76ms min=5.97ms  med=99.9ms  max=345.17ms p(90)=194.66ms p(95)=208.49ms p(99.9)=257.47ms
     iterations.....................: 137434  2213.536785/s
     success_rate...................: 100.00% ✓ 137434      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 388689      ✗ 0     
     data_received..................: 11 GB   185 MB/s
     data_sent......................: 157 MB  2.5 MB/s
     http_req_blocked...............: avg=12.62µs  min=841ns   med=2.25µs   max=45.12ms  p(90)=4.57µs   p(95)=5.66µs   p(99.9)=1.63ms  
     http_req_connecting............: avg=9.58µs   min=0s      med=0s       max=45.05ms  p(90)=0s       p(95)=0s       p(99.9)=1.56ms  
     http_req_duration..............: avg=108.98ms min=1.56ms  med=104.37ms max=342.7ms  p(90)=206.55ms p(95)=218.65ms p(99.9)=261.11ms
       { expected_response:true }...: avg=108.98ms min=1.56ms  med=104.37ms max=342.7ms  p(90)=206.55ms p(95)=218.65ms p(99.9)=261.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 130563
     http_req_receiving.............: avg=5.8ms    min=53.26µs med=6.09ms   max=318.04ms p(90)=8.85ms   p(95)=10.96ms  p(99.9)=35.99ms 
     http_req_sending...............: avg=57.49µs  min=4.48µs  med=9.2µs    max=162.28ms p(90)=23.51µs  p(95)=105.81µs p(99.9)=7.23ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=103.12ms min=1.47ms  med=97.62ms  max=322.22ms p(90)=199.88ms p(95)=211.84ms p(99.9)=259.1ms 
     http_reqs......................: 130563  2107.810197/s
     iteration_duration.............: avg=110.08ms min=4.93ms  med=105.67ms max=351.11ms p(90)=207.01ms p(95)=219.11ms p(99.9)=261.72ms
     iterations.....................: 129563  2091.666189/s
     success_rate...................: 100.00% ✓ 129563      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 348495      ✗ 0     
     data_received..................: 10 GB   165 MB/s
     data_sent......................: 141 MB  2.3 MB/s
     http_req_blocked...............: avg=9.54µs   min=832ns   med=2.3µs    max=46.03ms  p(90)=4.57µs   p(95)=5.58µs   p(99.9)=1.1ms   
     http_req_connecting............: avg=6.43µs   min=0s      med=0s       max=45.97ms  p(90)=0s       p(95)=0s       p(99.9)=1.02ms  
     http_req_duration..............: avg=121.5ms  min=1.87ms  med=117.62ms max=300.02ms p(90)=230.74ms p(95)=245.54ms p(99.9)=274.99ms
       { expected_response:true }...: avg=121.5ms  min=1.87ms  med=117.62ms max=300.02ms p(90)=230.74ms p(95)=245.54ms p(99.9)=274.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 117165
     http_req_receiving.............: avg=6.4ms    min=57.18µs med=6.85ms   max=276.65ms p(90)=9.2ms    p(95)=10.88ms  p(99.9)=35.33ms 
     http_req_sending...............: avg=46.52µs  min=4.94µs  med=9.34µs   max=77.02ms  p(90)=21.25µs  p(95)=71.98µs  p(99.9)=6.25ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=115.06ms min=1.79ms  med=110.14ms max=292.24ms p(90)=223.22ms p(95)=238.05ms p(99.9)=267.09ms
     http_reqs......................: 117165  1882.280992/s
     iteration_duration.............: avg=122.81ms min=4.59ms  med=119.28ms max=362.92ms p(90)=231.21ms p(95)=245.97ms p(99.9)=275.9ms 
     iterations.....................: 116165  1866.215776/s
     success_rate...................: 100.00% ✓ 116165      ✗ 0     
     vus............................: 68      min=0         max=495 
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

     checks.........................: 100.00% ✓ 241053      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 98 MB   1.6 MB/s
     http_req_blocked...............: avg=7.53µs   min=1.21µs  med=3.32µs   max=33.68ms  p(90)=5.27µs   p(95)=6.37µs   p(99.9)=848.9µs 
     http_req_connecting............: avg=3.52µs   min=0s      med=0s       max=33.62ms  p(90)=0s       p(95)=0s       p(99.9)=753.29µs
     http_req_duration..............: avg=175.39ms min=2.3ms   med=140.27ms max=979.19ms p(90)=370ms    p(95)=436.85ms p(99.9)=724.92ms
       { expected_response:true }...: avg=175.39ms min=2.3ms   med=140.27ms max=979.19ms p(90)=370ms    p(95)=436.85ms p(99.9)=724.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81351
     http_req_receiving.............: avg=87.87µs  min=30.73µs med=66.8µs   max=268.07ms p(90)=105.47µs p(95)=122.26µs p(99.9)=2.08ms  
     http_req_sending...............: avg=39.53µs  min=5.53µs  med=13.48µs  max=248.4ms  p(90)=20.41µs  p(95)=24.26µs  p(99.9)=4.28ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.26ms min=2.25ms  med=140.13ms max=979.09ms p(90)=369.9ms  p(95)=436.76ms p(99.9)=724.85ms
     http_reqs......................: 81351   1294.513325/s
     iteration_duration.............: avg=177.83ms min=7.28ms  med=143.12ms max=979.4ms  p(90)=371.51ms p(95)=438.36ms p(99.9)=725.55ms
     iterations.....................: 80351   1278.600634/s
     success_rate...................: 100.00% ✓ 80351       ✗ 0    
     vus............................: 95      min=0         max=500
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.361.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 240672      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 98 MB   1.6 MB/s
     http_req_blocked...............: avg=5.75µs   min=881ns   med=2.42µs   max=16.11ms  p(90)=4.24µs   p(95)=5.25µs   p(99.9)=458.53µs
     http_req_connecting............: avg=2.6µs    min=0s      med=0s       max=16.06ms  p(90)=0s       p(95)=0s       p(99.9)=367.25µs
     http_req_duration..............: avg=175.56ms min=2.16ms  med=174.46ms max=561.21ms p(90)=329.35ms p(95)=353.64ms p(99.9)=456.22ms
       { expected_response:true }...: avg=175.56ms min=2.16ms  med=174.46ms max=561.21ms p(90)=329.35ms p(95)=353.64ms p(99.9)=456.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81224
     http_req_receiving.............: avg=76.68µs  min=27.34µs med=61.69µs  max=35.42ms  p(90)=102.37µs p(95)=119.65µs p(99.9)=1.31ms  
     http_req_sending...............: avg=32.76µs  min=4.87µs  med=11.15µs  max=153.63ms p(90)=18.3µs   p(95)=21.96µs  p(99.9)=3.45ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.45ms min=2.07ms  med=174.34ms max=561.14ms p(90)=329.23ms p(95)=353.55ms p(99.9)=456.15ms
     http_reqs......................: 81224   1292.086568/s
     iteration_duration.............: avg=177.99ms min=4.38ms  med=177.08ms max=561.41ms p(90)=330ms    p(95)=354.32ms p(99.9)=457.07ms
     iterations.....................: 80224   1276.178874/s
     success_rate...................: 100.00% ✓ 80224       ✗ 0    
     vus............................: 44      min=0         max=500
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

     checks.........................: 100.00% ✓ 87321      ✗ 0    
     data_received..................: 2.6 GB  40 MB/s
     data_sent......................: 36 MB   554 kB/s
     http_req_blocked...............: avg=8.66µs   min=1.2µs   med=3.21µs   max=18.84ms  p(90)=4.95µs   p(95)=6.07µs   p(99.9)=702.85µs
     http_req_connecting............: avg=4.3µs    min=0s      med=0s       max=18.7ms   p(90)=0s       p(95)=0s       p(99.9)=624.51µs
     http_req_duration..............: avg=477.16ms min=4.28ms  med=443.97ms max=2.09s    p(90)=940.83ms p(95)=1.03s    p(99.9)=1.56s   
       { expected_response:true }...: avg=477.16ms min=4.28ms  med=443.97ms max=2.09s    p(90)=940.83ms p(95)=1.03s    p(99.9)=1.56s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 30107
     http_req_receiving.............: avg=94.34µs  min=32.53µs med=76.42µs  max=104.57ms p(90)=114.27µs p(95)=127.71µs p(99.9)=1.1ms   
     http_req_sending...............: avg=36.41µs  min=5.83µs  med=14.7µs   max=153.78ms p(90)=21.19µs  p(95)=23.96µs  p(99.9)=2.25ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=477.03ms min=4.21ms  med=443.84ms max=2.09s    p(90)=940.7ms  p(95)=1.03s    p(99.9)=1.56s   
     http_reqs......................: 30107   461.610455/s
     iteration_duration.............: avg=493.77ms min=20.11ms med=465.18ms max=2.09s    p(90)=946.9ms  p(95)=1.03s    p(99.9)=1.58s   
     iterations.....................: 29107   446.278125/s
     success_rate...................: 100.00% ✓ 29107      ✗ 0    
     vus............................: 65      min=0        max=497
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

     checks.........................: 100.00% ✓ 46041      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   285 kB/s
     http_req_blocked...............: avg=11.17µs  min=1.45µs  med=3.68µs   max=1.71ms  p(90)=5.7µs    p(95)=7.65µs   p(99.9)=926.6µs 
     http_req_connecting............: avg=5.5µs    min=0s      med=0s       max=1.69ms  p(90)=0s       p(95)=0s       p(99.9)=896.42µs
     http_req_duration..............: avg=888.34ms min=7.78ms  med=810.42ms max=3.08s   p(90)=1.81s    p(95)=1.94s    p(99.9)=2.67s   
       { expected_response:true }...: avg=888.34ms min=7.78ms  med=810.42ms max=3.08s   p(90)=1.81s    p(95)=1.94s    p(99.9)=2.67s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16347
     http_req_receiving.............: avg=98.56µs  min=37.36µs med=91.1µs   max=8.06ms  p(90)=132.27µs p(95)=149.28µs p(99.9)=872.61µs
     http_req_sending...............: avg=33.83µs  min=5.96µs  med=17.7µs   max=31.29ms p(90)=23.79µs  p(95)=27.8µs   p(99.9)=5.95ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=888.21ms min=7.65ms  med=810.25ms max=3.08s   p(90)=1.81s    p(95)=1.94s    p(99.9)=2.67s   
     http_reqs......................: 16347   237.842178/s
     iteration_duration.............: avg=946.16ms min=33.1ms  med=882.69ms max=3.09s   p(90)=1.83s    p(95)=1.95s    p(99.9)=2.67s   
     iterations.....................: 15347   223.292586/s
     success_rate...................: 100.00% ✓ 15347      ✗ 0    
     vus............................: 90      min=0        max=500
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

     checks.........................: 100.00% ✓ 44031      ✗ 0    
     data_received..................: 1.4 GB  20 MB/s
     data_sent......................: 19 MB   277 kB/s
     http_req_blocked...............: avg=15.77µs  min=1.52µs  med=3.77µs   max=7.87ms  p(90)=5.68µs  p(95)=7.54µs   p(99.9)=2.31ms
     http_req_connecting............: avg=10.17µs  min=0s      med=0s       max=7.77ms  p(90)=0s      p(95)=0s       p(99.9)=2.28ms
     http_req_duration..............: avg=930.63ms min=6.25ms  med=839.02ms max=5.13s   p(90)=1.84s   p(95)=2.06s    p(99.9)=4.7s  
       { expected_response:true }...: avg=930.63ms min=6.25ms  med=839.02ms max=5.13s   p(90)=1.84s   p(95)=2.06s    p(99.9)=4.7s  
     http_req_failed................: 0.00%   ✓ 0          ✗ 15677
     http_req_receiving.............: avg=98.82µs  min=39.35µs med=90.58µs  max=6.62ms  p(90)=128.3µs p(95)=143.77µs p(99.9)=1.58ms
     http_req_sending...............: avg=37.99µs  min=6.47µs  med=18.02µs  max=58.65ms p(90)=23.55µs p(95)=27.48µs  p(99.9)=3.16ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s      p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=930.49ms min=6.11ms  med=838.83ms max=5.13s   p(90)=1.84s   p(95)=2.06s    p(99.9)=4.7s  
     http_reqs......................: 15677   230.594971/s
     iteration_duration.............: avg=994.05ms min=14.82ms med=910.55ms max=5.13s   p(90)=1.87s   p(95)=2.08s    p(99.9)=4.74s 
     iterations.....................: 14677   215.885845/s
     success_rate...................: 100.00% ✓ 14677      ✗ 0    
     vus............................: 42      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

