## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,730 | 4,738 | 4,707 | 0.3% | 406 MB | 87.9 KB |  |
| fusion-net-11 | 16.7.3 | 4,673 | 4,679 | 4,536 | 1.3% | 398 MB | 87.1 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,533 | 4,558 | 4,516 | 0.4% | 173 MB | 39.1 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,522 | 4,605 | 4,490 | 1.0% | 418 MB | 94.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,504 | 4,579 | 4,407 | 1.7% | 421 MB | 95.7 KB |  |
| fusion-aot-11 | 16.7.3 | 4,416 | 4,445 | 4,387 | 0.5% | 156 MB | 36.1 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,399 | 4,425 | 4,315 | 1.1% | 185 MB | 43.2 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,313 | 4,319 | 4,252 | 0.6% | 182 MB | 43.3 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,186 | 4,275 | 4,146 | 1.2% | 2,302 MB | 563.1 KB |  |
| hive-router | v0.3.6 | 2,566 | 2,579 | 2,555 | 0.4% | 169 MB | 67.6 KB |  |
| cosmo | 0.363.0 | 1,369 | 1,374 | 1,366 | 0.2% | 675 MB | 504.7 KB |  |
| caliban | 3.2.0 | 1,368 | 1,369 | 1,367 | 0.1% | 10,627 MB | 7,954.6 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 480 | 480 | 474 | 0.5% | 3,145 MB | 6,708.9 KB |  |
| hive-gateway | 2.15.3 | 253 | 254 | 252 | 0.3% | 3,823 MB | 15,472.0 KB |  |
| apollo-gateway | 2.14.4 | 236 | 237 | 236 | 0.2% | 2,481 MB | 10,766.1 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (10631 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (5485 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (176264 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 861903      ✗ 0     
     data_received..................: 25 GB   414 MB/s
     data_sent......................: 346 MB  5.7 MB/s
     http_req_blocked...............: avg=60.98µs  min=771ns    med=2.02µs  max=117.94ms p(90)=3.65µs   p(95)=4.78µs   p(99.9)=21.94ms 
     http_req_connecting............: avg=57.39µs  min=0s       med=0s      max=117.7ms  p(90)=0s       p(95)=0s       p(99.9)=21.04ms 
     http_req_duration..............: avg=48.18ms  min=771.66µs med=40.5ms  max=316.93ms p(90)=101.22ms p(95)=124.95ms p(99.9)=177.03ms
       { expected_response:true }...: avg=48.18ms  min=771.66µs med=40.5ms  max=316.93ms p(90)=101.22ms p(95)=124.95ms p(99.9)=177.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288301
     http_req_receiving.............: avg=323.36µs min=25.5µs   med=51.11µs max=197.4ms  p(90)=203.96µs p(95)=359.95µs p(99.9)=43.03ms 
     http_req_sending...............: avg=136.35µs min=4.14µs   med=8.5µs   max=196.82ms p(90)=16.93µs  p(95)=116.29µs p(99.9)=23.73ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.72ms  min=716.61µs med=40.2ms  max=289.71ms p(90)=100.22ms p(95)=123.78ms p(99.9)=170.98ms
     http_reqs......................: 288301  4730.349189/s
     iteration_duration.............: avg=49.57ms  min=1.23ms   med=41.15ms max=327.23ms p(90)=104.01ms p(95)=129.34ms p(99.9)=196.13ms
     iterations.....................: 287301  4713.941514/s
     success_rate...................: 100.00% ✓ 287301      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 851541      ✗ 0     
     data_received..................: 25 GB   409 MB/s
     data_sent......................: 342 MB  5.6 MB/s
     http_req_blocked...............: avg=59.97µs  min=812ns    med=2.05µs  max=122.84ms p(90)=3.58µs   p(95)=4.65µs   p(99.9)=21.15ms 
     http_req_connecting............: avg=57.1µs   min=0s       med=0s      max=122.76ms p(90)=0s       p(95)=0s       p(99.9)=21.07ms 
     http_req_duration..............: avg=48.38ms  min=754.73µs med=40.77ms max=325.42ms p(90)=101.42ms p(95)=126.43ms p(99.9)=178.16ms
       { expected_response:true }...: avg=48.38ms  min=754.73µs med=40.77ms max=325.42ms p(90)=101.42ms p(95)=126.43ms p(99.9)=178.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 284847
     http_req_receiving.............: avg=317.83µs min=21.36µs  med=52.4µs  max=114.98ms p(90)=209.52µs p(95)=367.01µs p(99.9)=42.71ms 
     http_req_sending...............: avg=146.5µs  min=4.12µs   med=8.53µs  max=158.29ms p(90)=16.5µs   p(95)=115.27µs p(99.9)=25.94ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.91ms  min=714.61µs med=40.44ms max=322.46ms p(90)=100.29ms p(95)=125.3ms  p(99.9)=172.94ms
     http_reqs......................: 284847  4673.69119/s
     iteration_duration.............: avg=50.18ms  min=1.2ms    med=41.75ms max=399.53ms p(90)=105.59ms p(95)=132.04ms p(99.9)=213.01ms
     iterations.....................: 283847  4657.283465/s
     success_rate...................: 100.00% ✓ 283847      ✗ 0     
     vus............................: 54      min=0         max=499 
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

     checks.........................: 100.00% ✓ 826935      ✗ 0     
     data_received..................: 24 GB   397 MB/s
     data_sent......................: 332 MB  5.4 MB/s
     http_req_blocked...............: avg=44.48µs  min=841ns    med=1.98µs  max=111.21ms p(90)=3.5µs    p(95)=4.57µs   p(99.9)=13.74ms 
     http_req_connecting............: avg=41.27µs  min=0s       med=0s      max=111.14ms p(90)=0s       p(95)=0s       p(99.9)=13.27ms 
     http_req_duration..............: avg=50.35ms  min=837.18µs med=42.15ms max=303.08ms p(90)=106.92ms p(95)=132.79ms p(99.9)=189.09ms
       { expected_response:true }...: avg=50.35ms  min=837.18µs med=42.15ms max=303.08ms p(90)=106.92ms p(95)=132.79ms p(99.9)=189.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 276645
     http_req_receiving.............: avg=293.03µs min=24.5µs   med=49.47µs max=213.29ms p(90)=218.65µs p(95)=372.61µs p(99.9)=40.88ms 
     http_req_sending...............: avg=116.97µs min=4.07µs   med=8.39µs  max=106.36ms p(90)=16.8µs   p(95)=121.84µs p(99.9)=21.69ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.94ms  min=789.07µs med=41.91ms max=302.67ms p(90)=106.1ms  p(95)=131.78ms p(99.9)=181.05ms
     http_reqs......................: 276645  4533.361701/s
     iteration_duration.............: avg=51.67ms  min=1.41ms   med=43.04ms max=316.87ms p(90)=109.69ms p(95)=135.78ms p(99.9)=208.66ms
     iterations.....................: 275645  4516.974773/s
     success_rate...................: 100.00% ✓ 275645      ✗ 0     
     vus............................: 58      min=0         max=498 
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

     checks.........................: 100.00% ✓ 825978      ✗ 0     
     data_received..................: 24 GB   396 MB/s
     data_sent......................: 332 MB  5.4 MB/s
     http_req_blocked...............: avg=67.35µs  min=801ns    med=2.57µs  max=128.62ms p(90)=4.24µs   p(95)=5.47µs   p(99.9)=22.86ms 
     http_req_connecting............: avg=63.87µs  min=0s       med=0s      max=128.46ms p(90)=0s       p(95)=0s       p(99.9)=22.61ms 
     http_req_duration..............: avg=49.9ms   min=898.76µs med=42.06ms max=272.86ms p(90)=105.73ms p(95)=130.88ms p(99.9)=186.31ms
       { expected_response:true }...: avg=49.9ms   min=898.76µs med=42.06ms max=272.86ms p(90)=105.73ms p(95)=130.88ms p(99.9)=186.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 276326
     http_req_receiving.............: avg=334.89µs min=27.1µs   med=53.87µs max=175.38ms p(90)=217.95µs p(95)=383.65µs p(99.9)=45.07ms 
     http_req_sending...............: avg=151.22µs min=4.04µs   med=9.42µs  max=123.49ms p(90)=18.82µs  p(95)=123.3µs  p(99.9)=27.21ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.41ms  min=858.58µs med=41.72ms max=272.8ms  p(90)=104.54ms p(95)=129.71ms p(99.9)=182.65ms
     http_reqs......................: 276326  4522.536654/s
     iteration_duration.............: avg=51.73ms  min=1.47ms   med=42.9ms  max=360.82ms p(90)=109.83ms p(95)=137.03ms p(99.9)=208.05ms
     iterations.....................: 275326  4506.169983/s
     success_rate...................: 100.00% ✓ 275326      ✗ 0     
     vus............................: 63      min=0         max=497 
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

     checks.........................: 100.00% ✓ 822741      ✗ 0     
     data_received..................: 24 GB   394 MB/s
     data_sent......................: 331 MB  5.4 MB/s
     http_req_blocked...............: avg=61.86µs  min=801ns    med=2.43µs  max=122.69ms p(90)=4.11µs   p(95)=5.29µs   p(99.9)=21.71ms 
     http_req_connecting............: avg=58.2µs   min=0s       med=0s      max=114.46ms p(90)=0s       p(95)=0s       p(99.9)=21.43ms 
     http_req_duration..............: avg=50.49ms  min=893.95µs med=42.45ms max=300.09ms p(90)=107.6ms  p(95)=133.29ms p(99.9)=190.93ms
       { expected_response:true }...: avg=50.49ms  min=893.95µs med=42.45ms max=300.09ms p(90)=107.6ms  p(95)=133.29ms p(99.9)=190.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 275247
     http_req_receiving.............: avg=337.35µs min=24.54µs  med=52.68µs max=126.61ms p(90)=218.64µs p(95)=388.13µs p(99.9)=42.6ms  
     http_req_sending...............: avg=147.95µs min=4.27µs   med=8.99µs  max=249.06ms p(90)=18.4µs   p(95)=124.48µs p(99.9)=26.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.01ms  min=850.27µs med=42.15ms max=299.42ms p(90)=106.52ms p(95)=131.93ms p(99.9)=186.04ms
     http_reqs......................: 275247  4504.498969/s
     iteration_duration.............: avg=51.94ms  min=1.41ms   med=43.19ms max=336.25ms p(90)=110.75ms p(95)=137.24ms p(99.9)=211.84ms
     iterations.....................: 274247  4488.133672/s
     success_rate...................: 100.00% ✓ 274247      ✗ 0     
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

     checks.........................: 100.00% ✓ 805533      ✗ 0     
     data_received..................: 24 GB   387 MB/s
     data_sent......................: 324 MB  5.3 MB/s
     http_req_blocked...............: avg=55.8µs   min=852ns    med=2.51µs  max=108.97ms p(90)=4.2µs    p(95)=5.33µs   p(99.9)=17.69ms 
     http_req_connecting............: avg=52.32µs  min=0s       med=0s      max=108.89ms p(90)=0s       p(95)=0s       p(99.9)=17.42ms 
     http_req_duration..............: avg=51.25ms  min=825.87µs med=42.87ms max=280.71ms p(90)=109.98ms p(95)=136.38ms p(99.9)=189.09ms
       { expected_response:true }...: avg=51.25ms  min=825.87µs med=42.87ms max=280.71ms p(90)=109.98ms p(95)=136.38ms p(99.9)=189.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 269511
     http_req_receiving.............: avg=289.03µs min=25.84µs  med=51.63µs max=161.47ms p(90)=219.22µs p(95)=393.17µs p(99.9)=37.62ms 
     http_req_sending...............: avg=133.01µs min=4.05µs   med=9.13µs  max=175.38ms p(90)=17.91µs  p(95)=129.74µs p(99.9)=24ms    
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.83ms  min=782.58µs med=42.61ms max=259.06ms p(90)=108.97ms p(95)=135.35ms p(99.9)=185.28ms
     http_reqs......................: 269511  4416.822483/s
     iteration_duration.............: avg=53.05ms  min=1.43ms   med=43.72ms max=330.22ms p(90)=113.55ms p(95)=140.94ms p(99.9)=233.15ms
     iterations.....................: 268511  4400.4342/s
     success_rate...................: 100.00% ✓ 268511      ✗ 0     
     vus............................: 58      min=0         max=498 
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

     checks.........................: 100.00% ✓ 804780      ✗ 0     
     data_received..................: 24 GB   385 MB/s
     data_sent......................: 324 MB  5.3 MB/s
     http_req_blocked...............: avg=48.19µs  min=822ns    med=2.06µs  max=136.25ms p(90)=3.84µs   p(95)=5.06µs   p(99.9)=14.43ms 
     http_req_connecting............: avg=44.23µs  min=0s       med=0s      max=98.61ms  p(90)=0s       p(95)=0s       p(99.9)=13.73ms 
     http_req_duration..............: avg=51.83ms  min=985.38µs med=43.49ms max=323.41ms p(90)=110.79ms p(95)=136.43ms p(99.9)=189.28ms
       { expected_response:true }...: avg=51.83ms  min=985.38µs med=43.49ms max=323.41ms p(90)=110.79ms p(95)=136.43ms p(99.9)=189.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 269260
     http_req_receiving.............: avg=267.88µs min=21.71µs  med=49.92µs max=143.34ms p(90)=221.39µs p(95)=381.44µs p(99.9)=36.38ms 
     http_req_sending...............: avg=123.8µs  min=4.22µs   med=8.42µs  max=136.27ms p(90)=18.66µs  p(95)=126.74µs p(99.9)=21.77ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.44ms  min=940.18µs med=43.22ms max=314.48ms p(90)=109.95ms p(95)=135.34ms p(99.9)=185.41ms
     http_reqs......................: 269260  4399.418429/s
     iteration_duration.............: avg=53.1ms   min=1.55ms   med=44.28ms max=337.47ms p(90)=113.28ms p(95)=139.61ms p(99.9)=214.93ms
     iterations.....................: 268260  4383.079506/s
     success_rate...................: 100.00% ✓ 268260      ✗ 0     
     vus............................: 66      min=0         max=496 
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

     checks.........................: 100.00% ✓ 789072      ✗ 0     
     data_received..................: 23 GB   377 MB/s
     data_sent......................: 317 MB  5.2 MB/s
     http_req_blocked...............: avg=40.4µs   min=812ns    med=2.11µs  max=107.91ms p(90)=3.81µs   p(95)=5.01µs   p(99.9)=11.5ms  
     http_req_connecting............: avg=37µs     min=0s       med=0s      max=107.73ms p(90)=0s       p(95)=0s       p(99.9)=10.96ms 
     http_req_duration..............: avg=53.12ms  min=991.75µs med=45.12ms max=322.8ms  p(90)=111.7ms  p(95)=137.69ms p(99.9)=192.58ms
       { expected_response:true }...: avg=53.12ms  min=991.75µs med=45.12ms max=322.8ms  p(90)=111.7ms  p(95)=137.69ms p(99.9)=192.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 264024
     http_req_receiving.............: avg=254.49µs min=25.19µs  med=50.32µs max=151.4ms  p(90)=219.84µs p(95)=376.58µs p(99.9)=32.23ms 
     http_req_sending...............: avg=111.27µs min=4.47µs   med=8.64µs  max=81.02ms  p(90)=18.87µs  p(95)=124.01µs p(99.9)=19.53ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=52.76ms  min=941.33µs med=44.85ms max=322.56ms p(90)=110.91ms p(95)=136.86ms p(99.9)=190.19ms
     http_reqs......................: 264024  4313.042904/s
     iteration_duration.............: avg=54.16ms  min=1.54ms   med=45.85ms max=344.46ms p(90)=114ms    p(95)=140.47ms p(99.9)=210.52ms
     iterations.....................: 263024  4296.707105/s
     success_rate...................: 100.00% ✓ 263024      ✗ 0     
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

     checks.........................: 100.00% ✓ 762429      ✗ 0     
     data_received..................: 22 GB   366 MB/s
     data_sent......................: 307 MB  5.0 MB/s
     http_req_blocked...............: avg=44.45µs  min=812ns    med=2.21µs  max=96.29ms  p(90)=4.01µs   p(95)=5.25µs   p(99.9)=10.73ms 
     http_req_connecting............: avg=41.3µs   min=0s       med=0s      max=96.1ms   p(90)=0s       p(95)=0s       p(99.9)=10.4ms  
     http_req_duration..............: avg=54.82ms  min=699.28µs med=45.05ms max=326.55ms p(90)=115.83ms p(95)=145.32ms p(99.9)=223.05ms
       { expected_response:true }...: avg=54.82ms  min=699.28µs med=45.05ms max=326.55ms p(90)=115.83ms p(95)=145.32ms p(99.9)=223.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 255143
     http_req_receiving.............: avg=259.27µs min=24.87µs  med=50.68µs max=82.76ms  p(90)=208.11µs p(95)=371.39µs p(99.9)=37.58ms 
     http_req_sending...............: avg=117.93µs min=4.25µs   med=9.01µs  max=144.45ms p(90)=18.77µs  p(95)=125.45µs p(99.9)=21.42ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.45ms  min=656.12µs med=44.79ms max=325.96ms p(90)=115.04ms p(95)=144.43ms p(99.9)=218.94ms
     http_reqs......................: 255143  4186.17845/s
     iteration_duration.............: avg=56.06ms  min=1.21ms   med=45.96ms max=335.82ms p(90)=118.22ms p(95)=148.12ms p(99.9)=236.51ms
     iterations.....................: 254143  4169.771265/s
     success_rate...................: 100.00% ✓ 254143      ✗ 0     
     vus............................: 55      min=0         max=498 
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

     checks.........................: 100.00% ✓ 471366      ✗ 0     
     data_received..................: 14 GB   225 MB/s
     data_sent......................: 190 MB  3.1 MB/s
     http_req_blocked...............: avg=17.35µs  min=922ns   med=2.82µs  max=51.61ms  p(90)=4.69µs   p(95)=5.95µs   p(99.9)=1.53ms  
     http_req_connecting............: avg=13.59µs  min=0s      med=0s      max=51.42ms  p(90)=0s       p(95)=0s       p(99.9)=1.37ms  
     http_req_duration..............: avg=89.91ms  min=1.32ms  med=84.12ms max=294.68ms p(90)=175ms    p(95)=190.84ms p(99.9)=236.92ms
       { expected_response:true }...: avg=89.91ms  min=1.32ms  med=84.12ms max=294.68ms p(90)=175ms    p(95)=190.84ms p(99.9)=236.92ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 158122
     http_req_receiving.............: avg=145.49µs min=26.84µs med=58.27µs max=44.97ms  p(90)=185.73µs p(95)=387.1µs  p(99.9)=13.47ms 
     http_req_sending...............: avg=72.69µs  min=4.41µs  med=10.96µs max=260.88ms p(90)=21.92µs  p(95)=137.15µs p(99.9)=9.16ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=89.69ms  min=1.27ms  med=83.91ms max=293.95ms p(90)=174.7ms  p(95)=190.45ms p(99.9)=236.35ms
     http_reqs......................: 158122  2566.849214/s
     iteration_duration.............: avg=90.74ms  min=3.78ms  med=85.1ms  max=375.82ms p(90)=175.45ms p(95)=191.27ms p(99.9)=237.78ms
     iterations.....................: 157122  2550.615867/s
     success_rate...................: 100.00% ✓ 157122      ✗ 0     
     vus............................: 85      min=0         max=495 
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

     checks.........................: 100.00% ✓ 253440      ✗ 0    
     data_received..................: 7.5 GB  120 MB/s
     data_sent......................: 103 MB  1.6 MB/s
     http_req_blocked...............: avg=5.19µs   min=1.02µs  med=2.51µs   max=11.94ms  p(90)=4.39µs   p(95)=5.36µs   p(99.9)=393.22µs
     http_req_connecting............: avg=1.99µs   min=0s      med=0s       max=11.87ms  p(90)=0s       p(95)=0s       p(99.9)=328.18µs
     http_req_duration..............: avg=166.85ms min=1.98ms  med=165.76ms max=519.55ms p(90)=316.12ms p(95)=339.7ms  p(99.9)=426.02ms
       { expected_response:true }...: avg=166.85ms min=1.98ms  med=165.76ms max=519.55ms p(90)=316.12ms p(95)=339.7ms  p(99.9)=426.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 85480
     http_req_receiving.............: avg=74.1µs   min=26.69µs med=60.16µs  max=39.85ms  p(90)=96.88µs  p(95)=111.48µs p(99.9)=1.13ms  
     http_req_sending...............: avg=31.21µs  min=4.7µs   med=11.56µs  max=106.83ms p(90)=18.4µs   p(95)=21.82µs  p(99.9)=3.42ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=166.74ms min=1.92ms  med=165.65ms max=518.49ms p(90)=316.01ms p(95)=339.58ms p(99.9)=425.68ms
     http_reqs......................: 85480   1369.595942/s
     iteration_duration.............: avg=169.05ms min=4.51ms  med=168.28ms max=519.74ms p(90)=316.93ms p(95)=340.22ms p(99.9)=426.45ms
     iterations.....................: 84480   1353.573528/s
     success_rate...................: 100.00% ✓ 84480       ✗ 0    
     vus............................: 75      min=0         max=494
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

     checks.........................: 100.00% ✓ 253269      ✗ 0    
     data_received..................: 7.5 GB  120 MB/s
     data_sent......................: 103 MB  1.6 MB/s
     http_req_blocked...............: avg=4.97µs   min=972ns   med=2.29µs   max=12.87ms  p(90)=4µs      p(95)=4.98µs   p(99.9)=323.35µs
     http_req_connecting............: avg=2µs      min=0s      med=0s       max=12.81ms  p(90)=0s       p(95)=0s       p(99.9)=217.09µs
     http_req_duration..............: avg=166.98ms min=2.02ms  med=140.78ms max=982.33ms p(90)=347.77ms p(95)=414.53ms p(99.9)=705.9ms 
       { expected_response:true }...: avg=166.98ms min=2.02ms  med=140.78ms max=982.33ms p(90)=347.77ms p(95)=414.53ms p(99.9)=705.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 85423
     http_req_receiving.............: avg=74.07µs  min=26.25µs med=59.58µs  max=215.13ms p(90)=94.96µs  p(95)=108.84µs p(99.9)=1.58ms  
     http_req_sending...............: avg=30.14µs  min=4.74µs  med=10.95µs  max=171.66ms p(90)=17.12µs  p(95)=20.5µs   p(99.9)=3.03ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=166.88ms min=1.96ms  med=140.68ms max=982.27ms p(90)=347.7ms  p(95)=414.47ms p(99.9)=705.83ms
     http_reqs......................: 85423   1368.094404/s
     iteration_duration.............: avg=169.2ms  min=6.2ms   med=143.22ms max=982.52ms p(90)=349.31ms p(95)=415.79ms p(99.9)=707.13ms
     iterations.....................: 84423   1352.078877/s
     success_rate...................: 100.00% ✓ 84423       ✗ 0    
     vus............................: 78      min=0         max=493
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

     checks.........................: 100.00% ✓ 90276      ✗ 0    
     data_received..................: 2.7 GB  42 MB/s
     data_sent......................: 37 MB   577 kB/s
     http_req_blocked...............: avg=8.4µs    min=1.08µs  med=2.45µs   max=10.04ms p(90)=4.07µs   p(95)=4.98µs   p(99.9)=1.22ms  
     http_req_connecting............: avg=4.94µs   min=0s      med=0s       max=9.98ms  p(90)=0s       p(95)=0s       p(99.9)=1.2ms   
     http_req_duration..............: avg=462.05ms min=3.81ms  med=424.12ms max=1.94s   p(90)=915.7ms  p(95)=992.1ms  p(99.9)=1.5s    
       { expected_response:true }...: avg=462.05ms min=3.81ms  med=424.12ms max=1.94s   p(90)=915.7ms  p(95)=992.1ms  p(99.9)=1.5s    
     http_req_failed................: 0.00%   ✓ 0          ✗ 31092
     http_req_receiving.............: avg=77.58µs  min=28.59µs med=65.7µs   max=67.59ms p(90)=103.04µs p(95)=116.84µs p(99.9)=856.98µs
     http_req_sending...............: avg=25.04µs  min=4.97µs  med=12.64µs  max=72.27ms p(90)=19.08µs  p(95)=21.44µs  p(99.9)=1.68ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=461.94ms min=3.76ms  med=424.05ms max=1.94s   p(90)=915.59ms p(95)=992ms    p(99.9)=1.49s   
     http_reqs......................: 31092   480.392196/s
     iteration_duration.............: avg=477.58ms min=14.02ms med=446.41ms max=1.94s   p(90)=919.55ms p(95)=996.49ms p(99.9)=1.52s   
     iterations.....................: 30092   464.941527/s
     success_rate...................: 100.00% ✓ 30092      ✗ 0    
     vus............................: 89      min=0        max=500
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

     checks.........................: 100.00% ✓ 48120      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 21 MB   304 kB/s
     http_req_blocked...............: avg=14.49µs  min=1.6µs   med=3.78µs   max=9.76ms p(90)=5.68µs  p(95)=7.16µs   p(99.9)=2.09ms
     http_req_connecting............: avg=8.8µs    min=0s      med=0s       max=9.68ms p(90)=0s      p(95)=0s       p(99.9)=2.05ms
     http_req_duration..............: avg=854.26ms min=5.73ms  med=763.9ms  max=4.71s  p(90)=1.74s   p(95)=1.98s    p(99.9)=4.02s 
       { expected_response:true }...: avg=854.26ms min=5.73ms  med=763.9ms  max=4.71s  p(90)=1.74s   p(95)=1.98s    p(99.9)=4.02s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 17040
     http_req_receiving.............: avg=115.74µs min=37.29µs med=94.01µs  max=67.1ms p(90)=132.4µs p(95)=149.39µs p(99.9)=1.21ms
     http_req_sending...............: avg=33.68µs  min=6.98µs  med=18.2µs   max=39.4ms p(90)=23.83µs p(95)=27.67µs  p(99.9)=2.8ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s     p(90)=0s      p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=854.11ms min=5.63ms  med=763.78ms max=4.71s  p(90)=1.74s   p(95)=1.98s    p(99.9)=4.02s 
     http_reqs......................: 17040   253.001064/s
     iteration_duration.............: avg=907.58ms min=46.99ms med=828.92ms max=4.71s  p(90)=1.76s   p(95)=2s       p(99.9)=4.03s 
     iterations.....................: 16040   238.153584/s
     success_rate...................: 100.00% ✓ 16040      ✗ 0    
     vus............................: 72      min=0        max=500
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

     checks.........................: 100.00% ✓ 45870      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   284 kB/s
     http_req_blocked...............: avg=15µs     min=1.25µs  med=3.42µs   max=13.86ms p(90)=5.12µs   p(95)=6.74µs   p(99.9)=2.49ms  
     http_req_connecting............: avg=9.86µs   min=0s      med=0s       max=13.8ms  p(90)=0s       p(95)=0s       p(99.9)=2.45ms  
     http_req_duration..............: avg=891.38ms min=7.74ms  med=805.38ms max=3.12s   p(90)=1.81s    p(95)=1.96s    p(99.9)=2.76s   
       { expected_response:true }...: avg=891.38ms min=7.74ms  med=805.38ms max=3.12s   p(90)=1.81s    p(95)=1.96s    p(99.9)=2.76s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16290
     http_req_receiving.............: avg=92.73µs  min=31.35µs med=83.69µs  max=20.93ms p(90)=121.34µs p(95)=137.32µs p(99.9)=705.21µs
     http_req_sending...............: avg=31.9µs   min=6.06µs  med=16.14µs  max=47.33ms p(90)=21.56µs  p(95)=25.04µs  p(99.9)=2.91ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=891.26ms min=7.66ms  med=805.27ms max=3.12s   p(90)=1.81s    p(95)=1.96s    p(99.9)=2.76s   
     http_reqs......................: 16290   236.978614/s
     iteration_duration.............: avg=949.61ms min=28.08ms med=899.35ms max=3.12s   p(90)=1.82s    p(95)=1.98s    p(99.9)=2.78s   
     iterations.....................: 15290   222.431124/s
     success_rate...................: 100.00% ✓ 15290      ✗ 0    
     vus............................: 91      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

