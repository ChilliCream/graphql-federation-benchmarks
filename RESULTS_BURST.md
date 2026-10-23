## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-fed | 16.7.0-p.36 | 3,687 | 3,909 | 3,666 | 2.2% |  |
| fusion-nightly-net11 | 16.7.0-p.36 | 3,656 | 3,863 | 3,604 | 2.1% |  |
| fusion-nightly | 16.7.0-p.36 | 3,631 | 3,787 | 3,555 | 2.2% |  |
| feddi-gateway | 3c75a7db8876 | 3,007 | 3,127 | 2,975 | 1.7% |  |
| fusion | 16.6.9 | 2,395 | 2,472 | 2,367 | 1.4% |  |
| hive-router | v0.3.5 | 2,285 | 2,442 | 2,266 | 2.7% |  |
| caliban | 3.2.0 | 1,268 | 1,306 | 1,258 | 1.2% |  |
| cosmo | 0.359.0 | 1,259 | 1,313 | 1,239 | 1.9% |  |
| hive-gateway-router-runtime | 2.15.2 | 470 | 482 | 466 | 1.2% |  |
| hive-gateway | 2.15.2 | 244 | 249 | 241 | 0.9% |  |
| apollo-gateway | 2.14.4 | 232 | 235 | 231 | 0.5% |  |
| apollo-router | v2.18.0 | — | — | — | — | non-compatible response (36498 across 9/9 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | non-compatible response (9636 across 9/9 runs) |
| grafbase | 0.53.5 | — | — | — | — | non-compatible response (358312 across 9/9 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.36)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 678183      ✗ 0     
     data_received..................: 20 GB   323 MB/s
     data_sent......................: 273 MB  4.4 MB/s
     http_req_blocked...............: avg=82.04µs  min=781ns   med=2.18µs  max=250.02ms p(90)=3.95µs   p(95)=5.19µs   p(99.9)=31.99ms 
     http_req_connecting............: avg=78.87µs  min=0s      med=0s      max=249.94ms p(90)=0s       p(95)=0s       p(99.9)=31.85ms 
     http_req_duration..............: avg=61ms     min=1.21ms  med=53.22ms max=345.82ms p(90)=124.37ms p(95)=152.61ms p(99.9)=221.66ms
       { expected_response:true }...: avg=61ms     min=1.21ms  med=53.22ms max=345.82ms p(90)=124.37ms p(95)=152.61ms p(99.9)=221.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 227061
     http_req_receiving.............: avg=857.68µs min=52.09µs med=88.33µs max=260.96ms p(90)=1.74ms   p(95)=3.94ms   p(99.9)=51.33ms 
     http_req_sending...............: avg=149.82µs min=4.37µs  med=9µs     max=112.71ms p(90)=18.42µs  p(95)=120.94µs p(99.9)=28.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=59.99ms  min=1.13ms  med=52.35ms max=314.72ms p(90)=123.26ms p(95)=151.18ms p(99.9)=215.03ms
     http_reqs......................: 227061  3687.097575/s
     iteration_duration.............: avg=63.03ms  min=1.94ms  med=54.4ms  max=413.4ms  p(90)=128.75ms p(95)=157.59ms p(99.9)=244.7ms 
     iterations.....................: 226061  3670.859218/s
     success_rate...................: 100.00% ✓ 226061      ✗ 0     
     vus............................: 83      min=0         max=492 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.36)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 670086      ✗ 0     
     data_received..................: 20 GB   321 MB/s
     data_sent......................: 270 MB  4.4 MB/s
     http_req_blocked...............: avg=68.03µs  min=821ns    med=2.11µs  max=119.22ms p(90)=3.75µs   p(95)=4.89µs   p(99.9)=28.49ms 
     http_req_connecting............: avg=64.28µs  min=0s       med=0s      max=118.97ms p(90)=0s       p(95)=0s       p(99.9)=28.12ms 
     http_req_duration..............: avg=61.92ms  min=1.08ms   med=54.6ms  max=320.3ms  p(90)=124.46ms p(95)=151.31ms p(99.9)=214.73ms
       { expected_response:true }...: avg=61.92ms  min=1.08ms   med=54.6ms  max=320.3ms  p(90)=124.46ms p(95)=151.31ms p(99.9)=214.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 224362
     http_req_receiving.............: avg=1.44ms   min=50.06µs  med=88.65µs max=170.65ms p(90)=4.37ms   p(95)=7.5ms    p(99.9)=53.89ms 
     http_req_sending...............: avg=139.67µs min=4.39µs   med=8.77µs  max=90.66ms  p(90)=18.1µs   p(95)=120.09µs p(99.9)=26.65ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=60.34ms  min=943.43µs med=52.85ms max=305.03ms p(90)=123.23ms p(95)=150.12ms p(99.9)=210.81ms
     http_reqs......................: 224362  3656.914609/s
     iteration_duration.............: avg=63.8ms   min=1.7ms    med=55.92ms max=396.08ms p(90)=128.22ms p(95)=155.52ms p(99.9)=235.97ms
     iterations.....................: 223362  3640.615438/s
     success_rate...................: 100.00% ✓ 223362      ✗ 0     
     vus............................: 73      min=0         max=494 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.36)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 666441      ✗ 0     
     data_received..................: 20 GB   318 MB/s
     data_sent......................: 268 MB  4.4 MB/s
     http_req_blocked...............: avg=61.26µs  min=781ns   med=2.08µs  max=110.14ms p(90)=3.78µs   p(95)=4.99µs   p(99.9)=23.9ms  
     http_req_connecting............: avg=57.43µs  min=0s      med=0s      max=109.96ms p(90)=0s       p(95)=0s       p(99.9)=23.75ms 
     http_req_duration..............: avg=62.74ms  min=1.12ms  med=54.64ms max=289.78ms p(90)=127.15ms p(95)=154.15ms p(99.9)=222.56ms
       { expected_response:true }...: avg=62.74ms  min=1.12ms  med=54.64ms max=289.78ms p(90)=127.15ms p(95)=154.15ms p(99.9)=222.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 223147
     http_req_receiving.............: avg=1.1ms    min=52.58µs med=86.76µs max=252.7ms  p(90)=2.78ms   p(95)=5.02ms   p(99.9)=58.3ms  
     http_req_sending...............: avg=125.28µs min=4.59µs  med=8.57µs  max=108.97ms p(90)=18.07µs  p(95)=119.81µs p(99.9)=23.93ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=61.51ms  min=1.02ms  med=53.57ms max=289.69ms p(90)=126.1ms  p(95)=153.07ms p(99.9)=211.45ms
     http_reqs......................: 223147  3631.593227/s
     iteration_duration.............: avg=64.14ms  min=1.78ms  med=55.63ms max=384.48ms p(90)=129.54ms p(95)=157.11ms p(99.9)=235.47ms
     iterations.....................: 222147  3615.318784/s
     success_rate...................: 100.00% ✓ 222147      ✗ 0     
     vus............................: 77      min=0         max=493 
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

     checks.........................: 100.00% ✓ 549660      ✗ 0     
     data_received..................: 16 GB   263 MB/s
     data_sent......................: 221 MB  3.6 MB/s
     http_req_blocked...............: avg=44.62µs  min=1.09µs   med=3.03µs  max=145.85ms p(90)=5.06µs   p(95)=6.4µs    p(99.9)=12.48ms 
     http_req_connecting............: avg=40.1µs   min=0s       med=0s      max=133.86ms p(90)=0s       p(95)=0s       p(99.9)=11.87ms 
     http_req_duration..............: avg=76.54ms  min=942.59µs med=67.77ms max=340.38ms p(90)=152.68ms p(95)=179.34ms p(99.9)=270.57ms
       { expected_response:true }...: avg=76.54ms  min=942.59µs med=67.77ms max=340.38ms p(90)=152.68ms p(95)=179.34ms p(99.9)=270.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 184220
     http_req_receiving.............: avg=295.14µs min=28.06µs  med=56.27µs max=101.04ms p(90)=225.47µs p(95)=432.16µs p(99.9)=42.4ms  
     http_req_sending...............: avg=122.4µs  min=5.43µs   med=11.11µs max=205.74ms p(90)=23.61µs  p(95)=149.34µs p(99.9)=22.79ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=76.13ms  min=889.13µs med=67.43ms max=340.31ms p(90)=151.84ms p(95)=178.24ms p(99.9)=268.3ms 
     http_reqs......................: 184220  3007.501721/s
     iteration_duration.............: avg=77.79ms  min=1.41ms   med=68.95ms max=393.78ms p(90)=154.37ms p(95)=181.68ms p(99.9)=281.44ms
     iterations.....................: 183220  2991.176122/s
     success_rate...................: 100.00% ✓ 183220      ✗ 0     
     vus............................: 68      min=0         max=496 
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

     checks.........................: 100.00% ✓ 441417      ✗ 0     
     data_received..................: 13 GB   210 MB/s
     data_sent......................: 178 MB  2.9 MB/s
     http_req_blocked...............: avg=18.34µs min=1.08µs  med=2.74µs  max=56.55ms  p(90)=4.63µs   p(95)=5.97µs   p(99.9)=2.22ms  
     http_req_connecting............: avg=14.83µs min=0s      med=0s      max=56.47ms  p(90)=0s       p(95)=0s       p(99.9)=2.15ms  
     http_req_duration..............: avg=96ms    min=1.4ms   med=91.77ms max=317.96ms p(90)=181.52ms p(95)=195.75ms p(99.9)=232.03ms
       { expected_response:true }...: avg=96ms    min=1.4ms   med=91.77ms max=317.96ms p(90)=181.52ms p(95)=195.75ms p(99.9)=232.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 148139
     http_req_receiving.............: avg=2.2ms   min=53.48µs med=1.64ms  max=189.57ms p(90)=4.86ms   p(95)=6.15ms   p(99.9)=30ms    
     http_req_sending...............: avg=75.98µs min=4.59µs  med=10.27µs max=248.95ms p(90)=23.38µs  p(95)=125.29µs p(99.9)=10.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.72ms min=1.32ms  med=89.25ms max=293ms    p(90)=179.1ms  p(95)=193.69ms p(99.9)=230.71ms
     http_reqs......................: 148139  2395.870819/s
     iteration_duration.............: avg=96.91ms min=4.45ms  med=92.82ms max=335.1ms  p(90)=182.04ms p(95)=196.15ms p(99.9)=232.67ms
     iterations.....................: 147139  2379.697692/s
     success_rate...................: 100.00% ✓ 147139      ✗ 0     
     vus............................: 94      min=0         max=500 
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

     checks.........................: 100.00% ✓ 421893      ✗ 0     
     data_received..................: 12 GB   200 MB/s
     data_sent......................: 170 MB  2.7 MB/s
     http_req_blocked...............: avg=24.4µs   min=1.17µs  med=3.22µs  max=67.47ms  p(90)=5.22µs   p(95)=6.62µs   p(99.9)=2.19ms  
     http_req_connecting............: avg=19.87µs  min=0s      med=0s      max=67.4ms   p(90)=0s       p(95)=0s       p(99.9)=2.1ms   
     http_req_duration..............: avg=100.39ms min=1.61ms  med=95.2ms  max=333.2ms  p(90)=196.2ms  p(95)=213.48ms p(99.9)=268.27ms
       { expected_response:true }...: avg=100.39ms min=1.61ms  med=95.2ms  max=333.2ms  p(90)=196.2ms  p(95)=213.48ms p(99.9)=268.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 141631
     http_req_receiving.............: avg=160.16µs min=27.61µs med=61.47µs max=61.3ms   p(90)=167.02µs p(95)=400.16µs p(99.9)=17.43ms 
     http_req_sending...............: avg=78.25µs  min=4.97µs  med=12.32µs max=108.08ms p(90)=23.41µs  p(95)=142.99µs p(99.9)=10.48ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.15ms min=1.56ms  med=94.96ms max=332.94ms p(90)=195.93ms p(95)=213.15ms p(99.9)=267.05ms
     http_reqs......................: 141631  2285.624174/s
     iteration_duration.............: avg=101.39ms min=4.64ms  med=96.39ms max=343.6ms  p(90)=196.76ms p(95)=214.11ms p(99.9)=269.68ms
     iterations.....................: 140631  2269.486293/s
     success_rate...................: 100.00% ✓ 140631      ✗ 0     
     vus............................: 55      min=0         max=498 
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

     checks.........................: 100.00% ✓ 236799      ✗ 0    
     data_received..................: 7.0 GB  111 MB/s
     data_sent......................: 96 MB   1.5 MB/s
     http_req_blocked...............: avg=5.76µs   min=862ns   med=2.53µs   max=8.7ms    p(90)=4.46µs   p(95)=5.51µs   p(99.9)=460.79µs
     http_req_connecting............: avg=2.43µs   min=0s      med=0s       max=8.63ms   p(90)=0s       p(95)=0s       p(99.9)=394.44µs
     http_req_duration..............: avg=178.49ms min=2.53ms  med=151.36ms max=982.6ms  p(90)=371.48ms p(95)=437.07ms p(99.9)=740.69ms
       { expected_response:true }...: avg=178.49ms min=2.53ms  med=151.36ms max=982.6ms  p(90)=371.48ms p(95)=437.07ms p(99.9)=740.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 79933
     http_req_receiving.............: avg=78.86µs  min=28.72µs med=63.02µs  max=111.78ms p(90)=101.43µs p(95)=117.66µs p(99.9)=2.09ms  
     http_req_sending...............: avg=34.22µs  min=4.83µs  med=11.1µs   max=242.3ms  p(90)=17.77µs  p(95)=21.47µs  p(99.9)=3.68ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=178.37ms min=2.43ms  med=151.23ms max=982.52ms p(90)=371.31ms p(95)=436.97ms p(99.9)=740.62ms
     http_reqs......................: 79933   1268.539529/s
     iteration_duration.............: avg=181ms    min=6.95ms  med=154.13ms max=982.87ms p(90)=372.87ms p(95)=438.23ms p(99.9)=741.06ms
     iterations.....................: 78933   1252.669493/s
     success_rate...................: 100.00% ✓ 78933       ✗ 0    
     vus............................: 57      min=0         max=498
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

     checks.........................: 100.00% ✓ 234288      ✗ 0    
     data_received..................: 6.9 GB  110 MB/s
     data_sent......................: 95 MB   1.5 MB/s
     http_req_blocked...............: avg=5.52µs   min=862ns   med=2.33µs   max=12.52ms  p(90)=4.08µs   p(95)=5.06µs   p(99.9)=494.98µs
     http_req_connecting............: avg=2.5µs    min=0s      med=0s       max=12.47ms  p(90)=0s       p(95)=0s       p(99.9)=442.14µs
     http_req_duration..............: avg=180.34ms min=2.13ms  med=177.31ms max=487.98ms p(90)=344.9ms  p(95)=370.62ms p(99.9)=439.88ms
       { expected_response:true }...: avg=180.34ms min=2.13ms  med=177.31ms max=487.98ms p(90)=344.9ms  p(95)=370.62ms p(99.9)=439.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 79096
     http_req_receiving.............: avg=75.13µs  min=26.52µs med=60.56µs  max=63.51ms  p(90)=100.48µs p(95)=117.2µs  p(99.9)=1.29ms  
     http_req_sending...............: avg=26.01µs  min=5.07µs  med=10.69µs  max=60.12ms  p(90)=17.19µs  p(95)=20.87µs  p(99.9)=3.38ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.24ms min=2.05ms  med=177.2ms  max=487.91ms p(90)=344.81ms p(95)=370.53ms p(99.9)=439.8ms 
     http_reqs......................: 79096   1259.341615/s
     iteration_duration.............: avg=182.88ms min=5.46ms  med=180.1ms  max=488.29ms p(90)=345.73ms p(95)=371.29ms p(99.9)=440.1ms 
     iterations.....................: 78096   1243.419929/s
     success_rate...................: 100.00% ✓ 78096       ✗ 0    
     vus............................: 94      min=0         max=500
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

     checks.........................: 100.00% ✓ 89199      ✗ 0    
     data_received..................: 2.7 GB  41 MB/s
     data_sent......................: 37 MB   565 kB/s
     http_req_blocked...............: avg=15.8µs   min=1µs     med=2.98µs   max=15.88ms p(90)=4.71µs   p(95)=5.72µs   p(99.9)=5.51ms  
     http_req_connecting............: avg=11.64µs  min=0s      med=0s       max=15.8ms  p(90)=0s       p(95)=0s       p(99.9)=5.27ms  
     http_req_duration..............: avg=467.66ms min=4.47ms  med=431.59ms max=1.97s   p(90)=921.82ms p(95)=1.01s    p(99.9)=1.48s   
       { expected_response:true }...: avg=467.66ms min=4.47ms  med=431.59ms max=1.97s   p(90)=921.82ms p(95)=1.01s    p(99.9)=1.48s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 30733
     http_req_receiving.............: avg=86.38µs  min=28.97µs med=78.07µs  max=6.14ms  p(90)=116.76µs p(95)=131.99µs p(99.9)=988.46µs
     http_req_sending...............: avg=24.39µs  min=4.77µs  med=14.32µs  max=29.55ms p(90)=20.73µs  p(95)=23.37µs  p(99.9)=2.18ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=467.54ms min=4.38ms  med=431.32ms max=1.97s   p(90)=921.69ms p(95)=1.01s    p(99.9)=1.48s   
     http_reqs......................: 30733   470.41342/s
     iteration_duration.............: avg=483.6ms  min=19.32ms med=450.91ms max=1.97s   p(90)=925.56ms p(95)=1.01s    p(99.9)=1.49s   
     iterations.....................: 29733   455.106961/s
     success_rate...................: 100.00% ✓ 29733      ✗ 0    
     vus............................: 71      min=0        max=497
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

     checks.........................: 100.00% ✓ 46617      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   293 kB/s
     http_req_blocked...............: avg=12.45µs  min=1.5µs   med=3.95µs   max=8.56ms  p(90)=5.99µs   p(95)=7.74µs  p(99.9)=1.06ms
     http_req_connecting............: avg=6.56µs   min=0s      med=0s       max=8.5ms   p(90)=0s       p(95)=0s      p(99.9)=1.01ms
     http_req_duration..............: avg=880.29ms min=5.94ms  med=799.07ms max=4.92s   p(90)=1.74s    p(95)=2.02s   p(99.9)=4.03s 
       { expected_response:true }...: avg=880.29ms min=5.94ms  med=799.07ms max=4.92s   p(90)=1.74s    p(95)=2.02s   p(99.9)=4.03s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16539
     http_req_receiving.............: avg=108.97µs min=38.52µs med=95.39µs  max=35.45ms p(90)=136.05µs p(95)=153.9µs p(99.9)=1.72ms
     http_req_sending...............: avg=37.31µs  min=6.46µs  med=19.08µs  max=51.88ms p(90)=24.83µs  p(95)=28.9µs  p(99.9)=3.26ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s      p(99.9)=0s    
     http_req_waiting...............: avg=880.14ms min=5.84ms  med=798.9ms  max=4.92s   p(90)=1.74s    p(95)=2.02s   p(99.9)=4.03s 
     http_reqs......................: 16539   244.07258/s
     iteration_duration.............: avg=937.02ms min=43.34ms med=867.83ms max=4.93s   p(90)=1.77s    p(95)=2.04s   p(99.9)=4.11s 
     iterations.....................: 15539   229.315184/s
     success_rate...................: 100.00% ✓ 15539      ✗ 0    
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

     checks.........................: 100.00% ✓ 45048      ✗ 0    
     data_received..................: 1.4 GB  20 MB/s
     data_sent......................: 19 MB   280 kB/s
     http_req_blocked...............: avg=15.31µs  min=1.2µs   med=3.05µs   max=7.79ms  p(90)=4.79µs   p(95)=6.43µs   p(99.9)=2.57ms
     http_req_connecting............: avg=10.31µs  min=0s      med=0s       max=7.38ms  p(90)=0s       p(95)=0s       p(99.9)=2.54ms
     http_req_duration..............: avg=906.85ms min=7.71ms  med=861.66ms max=3.26s   p(90)=1.84s    p(95)=1.96s    p(99.9)=2.84s 
       { expected_response:true }...: avg=906.85ms min=7.71ms  med=861.66ms max=3.26s   p(90)=1.84s    p(95)=1.96s    p(99.9)=2.84s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16016
     http_req_receiving.............: avg=95.63µs  min=34.36µs med=86.75µs  max=20.09ms p(90)=125.73µs p(95)=141.03µs p(99.9)=1.2ms 
     http_req_sending...............: avg=34.3µs   min=5.12µs  med=15.92µs  max=65.73ms p(90)=21.34µs  p(95)=24.76µs  p(99.9)=3.16ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=906.72ms min=7.63ms  med=861.58ms max=3.26s   p(90)=1.84s    p(95)=1.96s    p(99.9)=2.84s 
     http_reqs......................: 16016   232.875333/s
     iteration_duration.............: avg=967.2ms  min=40.83ms med=915.34ms max=3.27s   p(90)=1.85s    p(95)=1.97s    p(99.9)=2.84s 
     iterations.....................: 15016   218.335165/s
     success_rate...................: 100.00% ✓ 15016      ✗ 0    
     vus............................: 95      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

