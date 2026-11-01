## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,708 | 4,767 | 4,683 | 0.7% | 423 MB | 92.0 KB |  |
| fusion-net-11 | 16.7.3 | 4,671 | 4,693 | 4,661 | 0.3% | 425 MB | 93.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,594 | 4,601 | 4,584 | 0.2% | 400 MB | 89.3 KB |  |
| fusion-aot-11 | 16.7.3 | 4,549 | 4,566 | 4,457 | 1.0% | 178 MB | 40.0 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,458 | 4,468 | 4,444 | 0.2% | 167 MB | 38.3 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,414 | 4,422 | 4,372 | 0.5% | 184 MB | 42.6 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,377 | 4,414 | 4,364 | 0.4% | 407 MB | 95.1 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,290 | 4,297 | 4,271 | 0.3% | 186 MB | 44.4 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,261 | 4,286 | 4,101 | 1.8% | 2,297 MB | 552.0 KB |  |
| hive-router | v0.3.6 | 2,733 | 2,734 | 2,727 | 0.1% | 178 MB | 66.6 KB |  |
| caliban | 3.2.0 | 1,374 | 1,378 | 1,373 | 0.2% | 10,750 MB | 8,011.7 KB |  |
| cosmo | 0.363.0 | 1,351 | 1,356 | 1,349 | 0.2% | 605 MB | 458.3 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 483 | 487 | 478 | 0.7% | 3,153 MB | 6,685.3 KB |  |
| hive-gateway | 2.15.3 | 240 | 244 | 237 | 1.1% | 3,752 MB | 16,009.5 KB |  |
| apollo-gateway | 2.14.4 | 239 | 240 | 239 | 0.2% | 2,462 MB | 10,547.4 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (10120 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (8416 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (155313 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 857766      ✗ 0     
     data_received..................: 25 GB   412 MB/s
     data_sent......................: 345 MB  5.7 MB/s
     http_req_blocked...............: avg=66.85µs  min=781ns    med=2.12µs  max=165.05ms p(90)=3.72µs   p(95)=4.89µs   p(99.9)=24.9ms  
     http_req_connecting............: avg=63.62µs  min=0s       med=0s      max=164.99ms p(90)=0s       p(95)=0s       p(99.9)=24.83ms 
     http_req_duration..............: avg=48.11ms  min=759.81µs med=40.04ms max=301.8ms  p(90)=101.18ms p(95)=125.43ms p(99.9)=181.8ms 
       { expected_response:true }...: avg=48.11ms  min=759.81µs med=40.04ms max=301.8ms  p(90)=101.18ms p(95)=125.43ms p(99.9)=181.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 286922
     http_req_receiving.............: avg=331.84µs min=22.83µs  med=52.68µs max=123.4ms  p(90)=205.06µs p(95)=359.91µs p(99.9)=46ms    
     http_req_sending...............: avg=150.9µs  min=4.1µs    med=8.57µs  max=231.73ms p(90)=17.05µs  p(95)=115.44µs p(99.9)=27.37ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.63ms  min=711.75µs med=39.71ms max=301.58ms p(90)=99.98ms  p(95)=124.12ms p(99.9)=178.32ms
     http_reqs......................: 286922  4708.196981/s
     iteration_duration.............: avg=49.82ms  min=1.16ms   med=40.8ms  max=332.05ms p(90)=105.38ms p(95)=130.86ms p(99.9)=202.09ms
     iterations.....................: 285922  4691.787654/s
     success_rate...................: 100.00% ✓ 285922      ✗ 0     
     vus............................: 54      min=0         max=499 
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

     checks.........................: 100.00% ✓ 851079      ✗ 0     
     data_received..................: 25 GB   409 MB/s
     data_sent......................: 342 MB  5.6 MB/s
     http_req_blocked...............: avg=64.67µs  min=802ns    med=2.1µs   max=133.3ms  p(90)=3.72µs   p(95)=4.86µs   p(99.9)=22.38ms 
     http_req_connecting............: avg=61.33µs  min=0s       med=0s      max=133.14ms p(90)=0s       p(95)=0s       p(99.9)=21.48ms 
     http_req_duration..............: avg=48.53ms  min=764.32µs med=41.18ms max=315.08ms p(90)=101.93ms p(95)=125.76ms p(99.9)=176.44ms
       { expected_response:true }...: avg=48.53ms  min=764.32µs med=41.18ms max=315.08ms p(90)=101.93ms p(95)=125.76ms p(99.9)=176.44ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 284693
     http_req_receiving.............: avg=331.84µs min=23.96µs  med=52.41µs max=135.14ms p(90)=212.89µs p(95)=370.35µs p(99.9)=44.24ms 
     http_req_sending...............: avg=146.4µs  min=4.12µs   med=8.72µs  max=121.01ms p(90)=17.01µs  p(95)=117.02µs p(99.9)=25.79ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.05ms  min=714.17µs med=40.84ms max=314.88ms p(90)=100.77ms p(95)=124.68ms p(99.9)=172.61ms
     http_reqs......................: 284693  4671.288255/s
     iteration_duration.............: avg=50.21ms  min=1.33ms   med=41.86ms max=334.46ms p(90)=106.11ms p(95)=131.4ms  p(99.9)=204.19ms
     iterations.....................: 283693  4654.880096/s
     success_rate...................: 100.00% ✓ 283693      ✗ 0     
     vus............................: 55      min=0         max=498 
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

     checks.........................: 100.00% ✓ 839238      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=57.67µs  min=801ns    med=2.05µs  max=133.1ms  p(90)=3.75µs   p(95)=4.92µs   p(99.9)=20.68ms 
     http_req_connecting............: avg=54.17µs  min=0s       med=0s      max=132.81ms p(90)=0s       p(95)=0s       p(99.9)=20.28ms 
     http_req_duration..............: avg=49.26ms  min=907.08µs med=41.14ms max=322.43ms p(90)=105.13ms p(95)=129.67ms p(99.9)=180.88ms
       { expected_response:true }...: avg=49.26ms  min=907.08µs med=41.14ms max=322.43ms p(90)=105.13ms p(95)=129.67ms p(99.9)=180.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280746
     http_req_receiving.............: avg=321.87µs min=22.32µs  med=51.95µs max=111.76ms p(90)=216.11µs p(95)=376.25µs p(99.9)=46.44ms 
     http_req_sending...............: avg=139.92µs min=4.11µs   med=8.47µs  max=189.5ms  p(90)=17.86µs  p(95)=119.88µs p(99.9)=25.82ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.8ms   min=864.27µs med=40.86ms max=321.45ms p(90)=104.06ms p(95)=128.4ms  p(99.9)=174.83ms
     http_reqs......................: 280746  4594.059854/s
     iteration_duration.............: avg=50.92ms  min=1.44ms   med=42.16ms max=332.42ms p(90)=108.39ms p(95)=134.37ms p(99.9)=202.41ms
     iterations.....................: 279746  4577.696095/s
     success_rate...................: 100.00% ✓ 279746      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 829971      ✗ 0     
     data_received..................: 24 GB   398 MB/s
     data_sent......................: 334 MB  5.5 MB/s
     http_req_blocked...............: avg=47.24µs  min=811ns    med=1.98µs  max=89.84ms  p(90)=3.55µs   p(95)=4.64µs   p(99.9)=16.58ms 
     http_req_connecting............: avg=43.59µs  min=0s       med=0s      max=89.68ms  p(90)=0s       p(95)=0s       p(99.9)=15.62ms 
     http_req_duration..............: avg=50.33ms  min=833.13µs med=42.11ms max=291.13ms p(90)=107.4ms  p(95)=131.95ms p(99.9)=181.8ms 
       { expected_response:true }...: avg=50.33ms  min=833.13µs med=42.11ms max=291.13ms p(90)=107.4ms  p(95)=131.95ms p(99.9)=181.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 277657
     http_req_receiving.............: avg=277.05µs min=26.03µs  med=48.55µs max=152.9ms  p(90)=215.44µs p(95)=368.94µs p(99.9)=38.74ms 
     http_req_sending...............: avg=122.11µs min=4.26µs   med=8.24µs  max=112.62ms p(90)=16.91µs  p(95)=122.66µs p(99.9)=21.68ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.93ms  min=784.93µs med=41.87ms max=290.96ms p(90)=106.48ms p(95)=130.96ms p(99.9)=178.42ms
     http_reqs......................: 277657  4549.540245/s
     iteration_duration.............: avg=51.49ms  min=1.07ms   med=42.88ms max=335.15ms p(90)=109.79ms p(95)=134.31ms p(99.9)=207.01ms
     iterations.....................: 276657  4533.154776/s
     success_rate...................: 100.00% ✓ 276657      ✗ 0     
     vus............................: 58      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 813312      ✗ 0     
     data_received..................: 24 GB   390 MB/s
     data_sent......................: 327 MB  5.4 MB/s
     http_req_blocked...............: avg=56.47µs  min=822ns    med=2.56µs  max=111.61ms p(90)=4.18µs   p(95)=5.3µs    p(99.9)=18ms    
     http_req_connecting............: avg=52.86µs  min=0s       med=0s      max=111.51ms p(90)=0s       p(95)=0s       p(99.9)=17.68ms 
     http_req_duration..............: avg=51.27ms  min=825.35µs med=42.74ms max=325.29ms p(90)=110ms    p(95)=137.44ms p(99.9)=193.81ms
       { expected_response:true }...: avg=51.27ms  min=825.35µs med=42.74ms max=325.29ms p(90)=110ms    p(95)=137.44ms p(99.9)=193.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 272104
     http_req_receiving.............: avg=314.32µs min=24.68µs  med=50.87µs max=216.98ms p(90)=224.67µs p(95)=396.94µs p(99.9)=41.26ms 
     http_req_sending...............: avg=137.92µs min=4µs      med=9.01µs  max=284.71ms p(90)=17.85µs  p(95)=129.41µs p(99.9)=24.1ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.82ms  min=782.22µs med=42.47ms max=295.48ms p(90)=108.95ms p(95)=136.28ms p(99.9)=188.14ms
     http_reqs......................: 272104  4458.11743/s
     iteration_duration.............: avg=52.54ms  min=1.33ms   med=43.46ms max=338.32ms p(90)=112.73ms p(95)=140.89ms p(99.9)=209.26ms
     iterations.....................: 271104  4441.733557/s
     success_rate...................: 100.00% ✓ 271104      ✗ 0     
     vus............................: 59      min=0         max=498 
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

     checks.........................: 100.00% ✓ 807561      ✗ 0     
     data_received..................: 24 GB   386 MB/s
     data_sent......................: 325 MB  5.3 MB/s
     http_req_blocked...............: avg=50.3µs  min=821ns    med=2.06µs  max=114.23ms p(90)=3.86µs   p(95)=5.12µs   p(99.9)=16.13ms 
     http_req_connecting............: avg=47.09µs min=0s       med=0s      max=114.03ms p(90)=0s       p(95)=0s       p(99.9)=16.03ms 
     http_req_duration..............: avg=51.52ms min=992.44µs med=43.49ms max=288.45ms p(90)=109.95ms p(95)=135.9ms  p(99.9)=190.41ms
       { expected_response:true }...: avg=51.52ms min=992.44µs med=43.49ms max=288.45ms p(90)=109.95ms p(95)=135.9ms  p(99.9)=190.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 270187
     http_req_receiving.............: avg=287.1µs min=26.42µs  med=49.93µs max=185.28ms p(90)=219.34µs p(95)=382.2µs  p(99.9)=42.66ms 
     http_req_sending...............: avg=126.6µs min=4.16µs   med=8.52µs  max=119.57ms p(90)=19.13µs  p(95)=125.99µs p(99.9)=22.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.1ms  min=930.96µs med=43.23ms max=248.17ms p(90)=109.01ms p(95)=134.93ms p(99.9)=182.91ms
     http_reqs......................: 270187  4414.572197/s
     iteration_duration.............: avg=52.91ms min=1.58ms   med=44.35ms max=310.77ms p(90)=112.84ms p(95)=139.15ms p(99.9)=218.61ms
     iterations.....................: 269187  4398.233246/s
     success_rate...................: 100.00% ✓ 269187      ✗ 0     
     vus............................: 66      min=0         max=496 
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

     checks.........................: 100.00% ✓ 799662      ✗ 0     
     data_received..................: 23 GB   383 MB/s
     data_sent......................: 321 MB  5.3 MB/s
     http_req_blocked...............: avg=70.36µs  min=1µs      med=2.68µs  max=145.35ms p(90)=4.36µs   p(95)=5.57µs   p(99.9)=26.25ms 
     http_req_connecting............: avg=66.2µs   min=0s       med=0s      max=145.06ms p(90)=0s       p(95)=0s       p(99.9)=25.87ms 
     http_req_duration..............: avg=51.8ms   min=906.73µs med=43.52ms max=345.26ms p(90)=110ms    p(95)=137.16ms p(99.9)=193.68ms
       { expected_response:true }...: avg=51.8ms   min=906.73µs med=43.52ms max=345.26ms p(90)=110ms    p(95)=137.16ms p(99.9)=193.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 267554
     http_req_receiving.............: avg=367µs    min=25.73µs  med=55.61µs max=141.63ms p(90)=232.12µs p(95)=405.52µs p(99.9)=52.32ms 
     http_req_sending...............: avg=154.23µs min=4.41µs   med=9.46µs  max=147.28ms p(90)=18.84µs  p(95)=131.99µs p(99.9)=27.43ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.28ms  min=856.96µs med=43.18ms max=345.04ms p(90)=108.84ms p(95)=135.98ms p(99.9)=185.9ms 
     http_reqs......................: 267554  4377.602706/s
     iteration_duration.............: avg=53.44ms  min=1.46ms   med=44.4ms  max=356.72ms p(90)=113.83ms p(95)=141.94ms p(99.9)=219.51ms
     iterations.....................: 266554  4361.241139/s
     success_rate...................: 100.00% ✓ 266554      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 784773      ✗ 0     
     data_received..................: 23 GB   375 MB/s
     data_sent......................: 316 MB  5.2 MB/s
     http_req_blocked...............: avg=37.27µs  min=821ns    med=2µs     max=92.39ms  p(90)=3.53µs   p(95)=4.67µs   p(99.9)=7.85ms  
     http_req_connecting............: avg=34.26µs  min=0s       med=0s      max=92.15ms  p(90)=0s       p(95)=0s       p(99.9)=7.63ms  
     http_req_duration..............: avg=53.53ms  min=975.35µs med=45.41ms max=313.15ms p(90)=112.28ms p(95)=137.96ms p(99.9)=193.91ms
       { expected_response:true }...: avg=53.53ms  min=975.35µs med=45.41ms max=313.15ms p(90)=112.28ms p(95)=137.96ms p(99.9)=193.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 262591
     http_req_receiving.............: avg=236.37µs min=25.35µs  med=49.89µs max=79.37ms  p(90)=217.65µs p(95)=367.22µs p(99.9)=30.44ms 
     http_req_sending...............: avg=103.71µs min=4.19µs   med=8.25µs  max=164.71ms p(90)=17.18µs  p(95)=119.82µs p(99.9)=18.36ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.19ms  min=932.12µs med=45.15ms max=312.62ms p(90)=111.61ms p(95)=137.1ms  p(99.9)=188.96ms
     http_reqs......................: 262591  4290.465655/s
     iteration_duration.............: avg=54.46ms  min=1.66ms   med=46.03ms max=324.19ms p(90)=114.11ms p(95)=139.95ms p(99.9)=206.69ms
     iterations.....................: 261591  4274.126688/s
     success_rate...................: 100.00% ✓ 261591      ✗ 0     
     vus............................: 66      min=0         max=496 
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

     checks.........................: 100.00% ✓ 776175      ✗ 0     
     data_received..................: 23 GB   373 MB/s
     data_sent......................: 312 MB  5.1 MB/s
     http_req_blocked...............: avg=49.13µs  min=781ns    med=2.15µs  max=153.74ms p(90)=3.8µs    p(95)=4.89µs   p(99.9)=13.85ms 
     http_req_connecting............: avg=45.8µs   min=0s       med=0s      max=153.69ms p(90)=0s       p(95)=0s       p(99.9)=13.58ms 
     http_req_duration..............: avg=53.88ms  min=693.19µs med=45.45ms max=276.04ms p(90)=114.1ms  p(95)=141.98ms p(99.9)=210.5ms 
       { expected_response:true }...: avg=53.88ms  min=693.19µs med=45.45ms max=276.04ms p(90)=114.1ms  p(95)=141.98ms p(99.9)=210.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 259725
     http_req_receiving.............: avg=266.77µs min=23.98µs  med=51.13µs max=95.61ms  p(90)=211.29µs p(95)=374.15µs p(99.9)=37.96ms 
     http_req_sending...............: avg=121.88µs min=3.92µs   med=8.92µs  max=136.05ms p(90)=17.71µs  p(95)=124.26µs p(99.9)=22.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.49ms  min=657.67µs med=45.17ms max=272.08ms p(90)=113.27ms p(95)=140.98ms p(99.9)=205.12ms
     http_reqs......................: 259725  4261.690955/s
     iteration_duration.............: avg=55.06ms  min=1.28ms   med=46.16ms max=302.6ms  p(90)=116.89ms p(95)=145.26ms p(99.9)=221.79ms
     iterations.....................: 258725  4245.282481/s
     success_rate...................: 100.00% ✓ 258725      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 502161      ✗ 0     
     data_received..................: 15 GB   239 MB/s
     data_sent......................: 202 MB  3.3 MB/s
     http_req_blocked...............: avg=16.07µs  min=861ns   med=2.36µs  max=66.28ms  p(90)=4.16µs   p(95)=5.44µs   p(99.9)=1.07ms  
     http_req_connecting............: avg=12.94µs  min=0s      med=0s      max=66.03ms  p(90)=0s       p(95)=0s       p(99.9)=989.05µs
     http_req_duration..............: avg=84.42ms  min=1.33ms  med=79.15ms max=345.6ms  p(90)=164.41ms p(95)=177.84ms p(99.9)=230.83ms
       { expected_response:true }...: avg=84.42ms  min=1.33ms  med=79.15ms max=345.6ms  p(90)=164.41ms p(95)=177.84ms p(99.9)=230.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 168387
     http_req_receiving.............: avg=151.45µs min=24.84µs med=54.6µs  max=54.46ms  p(90)=181.44µs p(95)=360.68µs p(99.9)=17.38ms 
     http_req_sending...............: avg=70.24µs  min=4.3µs   med=10.04µs max=158.22ms p(90)=21.31µs  p(95)=126.12µs p(99.9)=8.45ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=84.2ms   min=1.27ms  med=78.94ms max=335.66ms p(90)=164.17ms p(95)=177.51ms p(99.9)=226.29ms
     http_reqs......................: 168387  2733.465261/s
     iteration_duration.............: avg=85.17ms  min=2.42ms  med=80.07ms max=354.25ms p(90)=164.83ms p(95)=178.19ms p(99.9)=231.71ms
     iterations.....................: 167387  2717.232029/s
     success_rate...................: 100.00% ✓ 167387      ✗ 0     
     vus............................: 84      min=0         max=493 
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

     checks.........................: 100.00% ✓ 254283      ✗ 0    
     data_received..................: 7.5 GB  120 MB/s
     data_sent......................: 103 MB  1.7 MB/s
     http_req_blocked...............: avg=6.06µs   min=1.12µs  med=3.1µs    max=16.8ms   p(90)=4.97µs   p(95)=5.99µs   p(99.9)=267.76µs
     http_req_connecting............: avg=2.27µs   min=0s      med=0s       max=16.53ms  p(90)=0s       p(95)=0s       p(99.9)=196.65µs
     http_req_duration..............: avg=166.31ms min=2.01ms  med=137.5ms  max=959.87ms p(90)=349.19ms p(95)=417.51ms p(99.9)=741.71ms
       { expected_response:true }...: avg=166.31ms min=2.01ms  med=137.5ms  max=959.87ms p(90)=349.19ms p(95)=417.51ms p(99.9)=741.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 85761
     http_req_receiving.............: avg=82.49µs  min=28.13µs med=64.19µs  max=164.46ms p(90)=101.96µs p(95)=119.05µs p(99.9)=1.94ms  
     http_req_sending...............: avg=38.39µs  min=5.14µs  med=12.35µs  max=258.96ms p(90)=18.61µs  p(95)=22.53µs  p(99.9)=4.05ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=166.19ms min=1.95ms  med=137.37ms max=959.79ms p(90)=349.08ms p(95)=417.32ms p(99.9)=741.64ms
     http_reqs......................: 85761   1374.380289/s
     iteration_duration.............: avg=168.52ms min=6.45ms  med=139.84ms max=960.08ms p(90)=350.65ms p(95)=419.18ms p(99.9)=744.12ms
     iterations.....................: 84761   1358.354586/s
     success_rate...................: 100.00% ✓ 84761       ✗ 0    
     vus............................: 76      min=0         max=494
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 250179      ✗ 0    
     data_received..................: 7.4 GB  118 MB/s
     data_sent......................: 101 MB  1.6 MB/s
     http_req_blocked...............: avg=5.02µs   min=902ns   med=2.28µs   max=24.61ms  p(90)=3.93µs   p(95)=4.89µs   p(99.9)=331.81µs
     http_req_connecting............: avg=2.1µs    min=0s      med=0s       max=24.55ms  p(90)=0s       p(95)=0s       p(99.9)=203.97µs
     http_req_duration..............: avg=168.99ms min=2.01ms  med=166.95ms max=445.8ms  p(90)=319.7ms  p(95)=342.18ms p(99.9)=408.39ms
       { expected_response:true }...: avg=168.99ms min=2.01ms  med=166.95ms max=445.8ms  p(90)=319.7ms  p(95)=342.18ms p(99.9)=408.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 84393
     http_req_receiving.............: avg=75.85µs  min=27.39µs med=60.18µs  max=166.04ms p(90)=97.43µs  p(95)=112.58µs p(99.9)=1.19ms  
     http_req_sending...............: avg=29.94µs  min=4.79µs  med=10.39µs  max=142.52ms p(90)=17.06µs  p(95)=20.58µs  p(99.9)=3.27ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=168.88ms min=1.95ms  med=166.85ms max=445.75ms p(90)=319.61ms p(95)=342.1ms  p(99.9)=408.3ms 
     http_reqs......................: 84393   1351.672852/s
     iteration_duration.............: avg=171.25ms min=4.92ms  med=169.57ms max=445.98ms p(90)=320.52ms p(95)=342.68ms p(99.9)=408.82ms
     iterations.....................: 83393   1335.656442/s
     success_rate...................: 100.00% ✓ 83393       ✗ 0    
     vus............................: 77      min=0         max=493
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 90924      ✗ 0    
     data_received..................: 2.7 GB  42 MB/s
     data_sent......................: 38 MB   581 kB/s
     http_req_blocked...............: avg=8.11µs   min=1.16µs  med=3.09µs   max=11.2ms   p(90)=4.74µs   p(95)=5.81µs   p(99.9)=739.23µs
     http_req_connecting............: avg=3.88µs   min=0s      med=0s       max=11.13ms  p(90)=0s       p(95)=0s       p(99.9)=697.53µs
     http_req_duration..............: avg=458.58ms min=3.83ms  med=425.72ms max=1.79s    p(90)=902.42ms p(95)=982.03ms p(99.9)=1.47s   
       { expected_response:true }...: avg=458.58ms min=3.83ms  med=425.72ms max=1.79s    p(90)=902.42ms p(95)=982.03ms p(99.9)=1.47s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 31308
     http_req_receiving.............: avg=89.89µs  min=29.76µs med=71.59µs  max=124.08ms p(90)=108.34µs p(95)=123.03µs p(99.9)=1.1ms   
     http_req_sending...............: avg=32.36µs  min=5.33µs  med=14.16µs  max=76.14ms  p(90)=20.74µs  p(95)=23.59µs  p(99.9)=2.85ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=458.46ms min=3.78ms  med=425.65ms max=1.79s    p(90)=902.33ms p(95)=981.95ms p(99.9)=1.47s   
     http_reqs......................: 31308   483.958775/s
     iteration_duration.............: avg=473.93ms min=21.35ms med=445.61ms max=1.8s     p(90)=906.47ms p(95)=986.5ms  p(99.9)=1.48s   
     iterations.....................: 30308   468.500784/s
     success_rate...................: 100.00% ✓ 30308      ✗ 0    
     vus............................: 88      min=0        max=500
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 45678      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   288 kB/s
     http_req_blocked...............: avg=14.77µs  min=1.27µs  med=3.57µs   max=7.28ms  p(90)=5.4µs    p(95)=7.16µs   p(99.9)=2.14ms
     http_req_connecting............: avg=9.43µs   min=0s      med=0s       max=7.22ms  p(90)=0s       p(95)=0s       p(99.9)=2.11ms
     http_req_duration..............: avg=897.09ms min=5.71ms  med=801.62ms max=5.04s   p(90)=1.79s    p(95)=2s       p(99.9)=4.12s 
       { expected_response:true }...: avg=897.09ms min=5.71ms  med=801.62ms max=5.04s   p(90)=1.79s    p(95)=2s       p(99.9)=4.12s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16226
     http_req_receiving.............: avg=105.16µs min=33.57µs med=88.73µs  max=66.5ms  p(90)=127.52µs p(95)=144.34µs p(99.9)=3.01ms
     http_req_sending...............: avg=38.19µs  min=6.17µs  med=16.96µs  max=69.57ms p(90)=22.36µs  p(95)=25.96µs  p(99.9)=5.38ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=896.95ms min=5.63ms  med=801.52ms max=5.04s   p(90)=1.79s    p(95)=2s       p(99.9)=4.12s 
     http_reqs......................: 16226   240.212228/s
     iteration_duration.............: avg=956.03ms min=27.27ms med=884.19ms max=5.05s   p(90)=1.81s    p(95)=2.02s    p(99.9)=4.14s 
     iterations.....................: 15226   225.408073/s
     success_rate...................: 100.00% ✓ 15226      ✗ 0    
     vus............................: 84      min=0        max=500
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

     checks.........................: 100.00% ✓ 46179      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   288 kB/s
     http_req_blocked...............: avg=14.04µs  min=1.11µs  med=3.09µs   max=3.65ms   p(90)=4.69µs   p(95)=6.15µs   p(99.9)=2.33ms
     http_req_connecting............: avg=9.37µs   min=0s      med=0s       max=3.61ms   p(90)=0s       p(95)=0s       p(99.9)=2.27ms
     http_req_duration..............: avg=885.27ms min=7.49ms  med=805.38ms max=3s       p(90)=1.8s     p(95)=1.93s    p(99.9)=2.63s 
       { expected_response:true }...: avg=885.27ms min=7.49ms  med=805.38ms max=3s       p(90)=1.8s     p(95)=1.93s    p(99.9)=2.63s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16393
     http_req_receiving.............: avg=100.85µs min=33.25µs med=86.1µs   max=100.64ms p(90)=123.23µs p(95)=138.32µs p(99.9)=1.05ms
     http_req_sending...............: avg=55.79µs  min=5.34µs  med=15.72µs  max=150.21ms p(90)=20.4µs   p(95)=23.86µs  p(99.9)=4.42ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=885.11ms min=7.41ms  med=805.29ms max=3s       p(90)=1.8s     p(95)=1.93s    p(99.9)=2.63s 
     http_reqs......................: 16393   239.679028/s
     iteration_duration.............: avg=942.81ms min=50.26ms med=876.32ms max=3s       p(90)=1.82s    p(95)=1.94s    p(99.9)=2.65s 
     iterations.....................: 15393   225.058213/s
     success_rate...................: 100.00% ✓ 15393      ✗ 0    
     vus............................: 76      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

