## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 4,702 | 4,724 | 4,652 | 0.6% | 403 MB | 87.8 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,665 | 4,667 | 4,583 | 0.8% | 396 MB | 86.9 KB |  |
| fusion-aot-11 | 16.7.3 | 4,595 | 4,627 | 4,502 | 1.3% | 181 MB | 40.4 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,565 | 4,584 | 4,540 | 0.4% | 416 MB | 93.3 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,557 | 4,574 | 4,541 | 0.3% | 157 MB | 35.4 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,519 | 4,625 | 4,478 | 1.5% | 423 MB | 95.7 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,409 | 4,414 | 4,353 | 0.6% | 162 MB | 37.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,382 | 4,397 | 4,360 | 0.4% | 151 MB | 35.2 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,197 | 4,276 | 4,167 | 1.2% | 2,299 MB | 561.0 KB |  |
| hive-router | v0.3.10 | 2,783 | 2,795 | 2,777 | 0.3% | 164 MB | 60.5 KB |  |
| caliban | 3.2.0 | 1,413 | 1,425 | 1,357 | 2.3% | 10,747 MB | 7,788.1 KB |  |
| cosmo | 0.365.2 | 1,296 | 1,296 | 1,294 | 0.1% | 656 MB | 518.3 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 496 | 497 | 493 | 0.3% | 3,162 MB | 6,528.5 KB |  |
| apollo-gateway | 2.14.4 | 239 | 240 | 239 | 0.2% | 2,454 MB | 10,515.7 KB |  |
| hive-gateway | 2.15.6 | 239 | 243 | 238 | 0.9% | 3,810 MB | 16,324.3 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (7104 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (3828 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (152004 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 856815      ✗ 0     
     data_received..................: 25 GB   412 MB/s
     data_sent......................: 344 MB  5.7 MB/s
     http_req_blocked...............: avg=60.49µs  min=781ns    med=2.11µs  max=131.75ms p(90)=3.69µs   p(95)=4.78µs   p(99.9)=21.98ms 
     http_req_connecting............: avg=56.9µs   min=0s       med=0s      max=118.78ms p(90)=0s       p(95)=0s       p(99.9)=21.3ms  
     http_req_duration..............: avg=48.04ms  min=762.79µs med=40.77ms max=408.97ms p(90)=101.07ms p(95)=124.52ms p(99.9)=174.78ms
       { expected_response:true }...: avg=48.04ms  min=762.79µs med=40.77ms max=408.97ms p(90)=101.07ms p(95)=124.52ms p(99.9)=174.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 286605
     http_req_receiving.............: avg=340.52µs min=22.81µs  med=52.1µs  max=300.98ms p(90)=207.26µs p(95)=361.35µs p(99.9)=47.03ms 
     http_req_sending...............: avg=144.21µs min=4.03µs   med=8.72µs  max=334.94ms p(90)=16.65µs  p(95)=115.63µs p(99.9)=25.79ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.56ms  min=718.22µs med=40.44ms max=256.69ms p(90)=99.9ms   p(95)=123.34ms p(99.9)=170.3ms 
     http_reqs......................: 286605  4702.973193/s
     iteration_duration.............: avg=49.87ms  min=1.16ms   med=41.61ms max=426.6ms  p(90)=105.64ms p(95)=130.39ms p(99.9)=199ms   
     iterations.....................: 285605  4686.563943/s
     success_rate...................: 100.00% ✓ 285605      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 850143      ✗ 0     
     data_received..................: 25 GB   408 MB/s
     data_sent......................: 342 MB  5.6 MB/s
     http_req_blocked...............: avg=59.33µs  min=761ns    med=2.05µs  max=131.96ms p(90)=3.7µs    p(95)=4.84µs   p(99.9)=20.72ms 
     http_req_connecting............: avg=55.83µs  min=0s       med=0s      max=131.57ms p(90)=0s       p(95)=0s       p(99.9)=20.23ms 
     http_req_duration..............: avg=48.73ms  min=765.88µs med=41.03ms max=304.63ms p(90)=103.44ms p(95)=128.52ms p(99.9)=179.02ms
       { expected_response:true }...: avg=48.73ms  min=765.88µs med=41.03ms max=304.63ms p(90)=103.44ms p(95)=128.52ms p(99.9)=179.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 284381
     http_req_receiving.............: avg=337.7µs  min=25.18µs  med=51.31µs max=194.65ms p(90)=212.98µs p(95)=374.39µs p(99.9)=47.5ms  
     http_req_sending...............: avg=137.04µs min=4.07µs   med=8.55µs  max=205.6ms  p(90)=16.56µs  p(95)=118µs    p(99.9)=24.49ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.25ms  min=720.99µs med=40.71ms max=304.3ms  p(90)=102.34ms p(95)=127.3ms  p(99.9)=173.08ms
     http_reqs......................: 284381  4665.788765/s
     iteration_duration.............: avg=50.26ms  min=1.27ms   med=41.83ms max=331.32ms p(90)=106.57ms p(95)=132.33ms p(99.9)=211.44ms
     iterations.....................: 283381  4649.381942/s
     success_rate...................: 100.00% ✓ 283381      ✗ 0     
     vus............................: 55      min=0         max=498 
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

     checks.........................: 100.00% ✓ 838212      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=56.12µs  min=792ns    med=2.01µs  max=134.19ms p(90)=3.59µs   p(95)=4.7µs    p(99.9)=18.62ms 
     http_req_connecting............: avg=51.73µs  min=0s       med=0s      max=112.46ms p(90)=0s       p(95)=0s       p(99.9)=17.93ms 
     http_req_duration..............: avg=49.67ms  min=822.39µs med=41.48ms max=313.96ms p(90)=106.36ms p(95)=131.39ms p(99.9)=184.01ms
       { expected_response:true }...: avg=49.67ms  min=822.39µs med=41.48ms max=313.96ms p(90)=106.36ms p(95)=131.39ms p(99.9)=184.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280404
     http_req_receiving.............: avg=312.99µs min=25.34µs  med=49.61µs max=208.83ms p(90)=214.04µs p(95)=377.09µs p(99.9)=44.02ms 
     http_req_sending...............: avg=134.52µs min=4.19µs   med=8.46µs  max=262.31ms p(90)=17.36µs  p(95)=122.63µs p(99.9)=24.96ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.22ms  min=783.45µs med=41.21ms max=291.11ms p(90)=105.31ms p(95)=130.18ms p(99.9)=180.35ms
     http_reqs......................: 280404  4595.582613/s
     iteration_duration.............: avg=50.98ms  min=1.26ms   med=42.13ms max=326.3ms  p(90)=109.28ms p(95)=134.87ms p(99.9)=206.36ms
     iterations.....................: 279404  4579.193465/s
     success_rate...................: 100.00% ✓ 279404      ✗ 0     
     vus............................: 58      min=0         max=498 
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

     checks.........................: 100.00% ✓ 833958      ✗ 0     
     data_received..................: 24 GB   400 MB/s
     data_sent......................: 335 MB  5.5 MB/s
     http_req_blocked...............: avg=61.94µs  min=781ns    med=2.02µs  max=133.14ms p(90)=3.71µs   p(95)=4.91µs   p(99.9)=21.19ms 
     http_req_connecting............: avg=57.74µs  min=0s       med=0s      max=132.87ms p(90)=0s       p(95)=0s       p(99.9)=20.38ms 
     http_req_duration..............: avg=49.74ms  min=910.31µs med=41.91ms max=276.73ms p(90)=105.68ms p(95)=130.55ms p(99.9)=183.07ms
       { expected_response:true }...: avg=49.74ms  min=910.31µs med=41.91ms max=276.73ms p(90)=105.68ms p(95)=130.55ms p(99.9)=183.07ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 278986
     http_req_receiving.............: avg=325.47µs min=24.01µs  med=53.27µs max=146.7ms  p(90)=216.49µs p(95)=378.62µs p(99.9)=45.23ms 
     http_req_sending...............: avg=143.36µs min=4.21µs   med=8.48µs  max=100.33ms p(90)=18.05µs  p(95)=121.4µs  p(99.9)=25.15ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.27ms  min=855.58µs med=41.6ms  max=274.3ms  p(90)=104.61ms p(95)=129.28ms p(99.9)=176.62ms
     http_reqs......................: 278986  4565.761779/s
     iteration_duration.............: avg=51.24ms  min=1.45ms   med=42.64ms max=360.56ms p(90)=108.85ms p(95)=134.66ms p(99.9)=206.49ms
     iterations.....................: 277986  4549.39622/s
     success_rate...................: 100.00% ✓ 277986      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 831717      ✗ 0     
     data_received..................: 24 GB   399 MB/s
     data_sent......................: 334 MB  5.5 MB/s
     http_req_blocked...............: avg=53.79µs  min=771ns    med=2.05µs  max=130.59ms p(90)=3.61µs   p(95)=4.69µs   p(99.9)=18.52ms 
     http_req_connecting............: avg=50.48µs  min=0s       med=0s      max=130.33ms p(90)=0s       p(95)=0s       p(99.9)=17.74ms 
     http_req_duration..............: avg=49.88ms  min=847.34µs med=42.23ms max=258.4ms  p(90)=105.62ms p(95)=130.77ms p(99.9)=180.83ms
       { expected_response:true }...: avg=49.88ms  min=847.34µs med=42.23ms max=258.4ms  p(90)=105.62ms p(95)=130.77ms p(99.9)=180.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 278239
     http_req_receiving.............: avg=288.68µs min=24.2µs   med=49.9µs  max=98.39ms  p(90)=215.27µs p(95)=377.32µs p(99.9)=38.97ms 
     http_req_sending...............: avg=131.07µs min=4.06µs   med=8.72µs  max=105.15ms p(90)=17.56µs  p(95)=121.58µs p(99.9)=23.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.46ms  min=801.79µs med=41.97ms max=255.8ms  p(90)=104.66ms p(95)=129.61ms p(99.9)=176.78ms
     http_reqs......................: 278239  4557.322557/s
     iteration_duration.............: avg=51.38ms  min=1.31ms   med=42.89ms max=313.66ms p(90)=108.87ms p(95)=135.16ms p(99.9)=206.98ms
     iterations.....................: 277239  4540.943392/s
     success_rate...................: 100.00% ✓ 277239      ✗ 0     
     vus............................: 59      min=0         max=497 
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

     checks.........................: 100.00% ✓ 825498      ✗ 0     
     data_received..................: 24 GB   396 MB/s
     data_sent......................: 332 MB  5.4 MB/s
     http_req_blocked...............: avg=67.3µs   min=822ns    med=2.49µs  max=145.43ms p(90)=4.21µs   p(95)=5.44µs   p(99.9)=24.74ms 
     http_req_connecting............: avg=63.47µs  min=0s       med=0s      max=145.37ms p(90)=0s       p(95)=0s       p(99.9)=24.39ms 
     http_req_duration..............: avg=49.84ms  min=919.78µs med=40.96ms max=324.15ms p(90)=106.11ms p(95)=132.78ms p(99.9)=187.45ms
       { expected_response:true }...: avg=49.84ms  min=919.78µs med=40.96ms max=324.15ms p(90)=106.11ms p(95)=132.78ms p(99.9)=187.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 276166
     http_req_receiving.............: avg=340.65µs min=22.43µs  med=53.98µs max=206.94ms p(90)=218.99µs p(95)=382.54µs p(99.9)=46.23ms 
     http_req_sending...............: avg=156.53µs min=4.17µs   med=8.89µs  max=206.92ms p(90)=18.67µs  p(95)=124.76µs p(99.9)=27.85ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.34ms  min=869.58µs med=40.64ms max=304.89ms p(90)=104.79ms p(95)=131.56ms p(99.9)=183.15ms
     http_reqs......................: 276166  4519.590044/s
     iteration_duration.............: avg=51.76ms  min=1.41ms   med=42.24ms max=357.68ms p(90)=110.18ms p(95)=138.89ms p(99.9)=220.75ms
     iterations.....................: 275166  4503.224561/s
     success_rate...................: 100.00% ✓ 275166      ✗ 0     
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

     checks.........................: 100.00% ✓ 806334      ✗ 0     
     data_received..................: 24 GB   386 MB/s
     data_sent......................: 324 MB  5.3 MB/s
     http_req_blocked...............: avg=51.83µs  min=822ns    med=2.09µs  max=107.72ms p(90)=3.74µs   p(95)=4.94µs   p(99.9)=18.58ms 
     http_req_connecting............: avg=48.18µs  min=0s       med=0s      max=107.54ms p(90)=0s       p(95)=0s       p(99.9)=18.09ms 
     http_req_duration..............: avg=51.67ms  min=988.23µs med=43.55ms max=371.95ms p(90)=109.79ms p(95)=134.98ms p(99.9)=191.84ms
       { expected_response:true }...: avg=51.67ms  min=988.23µs med=43.55ms max=371.95ms p(90)=109.79ms p(95)=134.98ms p(99.9)=191.84ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 269778
     http_req_receiving.............: avg=303.5µs  min=26.54µs  med=50.44µs max=261.9ms  p(90)=218.05µs p(95)=378.37µs p(99.9)=42.87ms 
     http_req_sending...............: avg=125.53µs min=4.26µs   med=8.64µs  max=93.73ms  p(90)=18.55µs  p(95)=124.37µs p(99.9)=21.86ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.24ms  min=938.87µs med=43.3ms  max=260.32ms p(90)=108.97ms p(95)=133.93ms p(99.9)=184.38ms
     http_reqs......................: 269778  4409.175799/s
     iteration_duration.............: avg=53ms     min=1.58ms   med=44.35ms max=380.53ms p(90)=112.56ms p(95)=138ms    p(99.9)=216.44ms
     iterations.....................: 268778  4392.83208/s
     success_rate...................: 100.00% ✓ 268778      ✗ 0     
     vus............................: 65      min=0         max=496 
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

     checks.........................: 100.00% ✓ 801582      ✗ 0     
     data_received..................: 24 GB   384 MB/s
     data_sent......................: 322 MB  5.3 MB/s
     http_req_blocked...............: avg=46.83µs  min=782ns    med=2.08µs  max=104.95ms p(90)=3.85µs   p(95)=5.1µs    p(99.9)=15.44ms 
     http_req_connecting............: avg=43.16µs  min=0s       med=0s      max=104.77ms p(90)=0s       p(95)=0s       p(99.9)=14.96ms 
     http_req_duration..............: avg=51.87ms  min=965.01µs med=43.5ms  max=323.38ms p(90)=110.58ms p(95)=136.32ms p(99.9)=191.47ms
       { expected_response:true }...: avg=51.87ms  min=965.01µs med=43.5ms  max=323.38ms p(90)=110.58ms p(95)=136.32ms p(99.9)=191.47ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 268194
     http_req_receiving.............: avg=284.13µs min=22.55µs  med=50.13µs max=193.3ms  p(90)=224.25µs p(95)=381.91µs p(99.9)=38.06ms 
     http_req_sending...............: avg=124.89µs min=4.1µs    med=8.5µs   max=168.66ms p(90)=19.1µs   p(95)=126.17µs p(99.9)=21.91ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.46ms  min=918.21µs med=43.24ms max=293.46ms p(90)=109.76ms p(95)=135.3ms  p(99.9)=186.93ms
     http_reqs......................: 268194  4382.801608/s
     iteration_duration.............: avg=53.31ms  min=1.4ms    med=44.39ms max=326.54ms p(90)=113.25ms p(95)=139.53ms p(99.9)=224.02ms
     iterations.....................: 267194  4366.4597/s
     success_rate...................: 100.00% ✓ 267194      ✗ 0     
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

     checks.........................: 100.00% ✓ 764556      ✗ 0     
     data_received..................: 22 GB   367 MB/s
     data_sent......................: 307 MB  5.0 MB/s
     http_req_blocked...............: avg=54.49µs  min=831ns    med=2.64µs  max=127.32ms p(90)=4.45µs   p(95)=5.68µs   p(99.9)=15.68ms 
     http_req_connecting............: avg=49.55µs  min=0s       med=0s      max=110.79ms p(90)=0s       p(95)=0s       p(99.9)=15.01ms 
     http_req_duration..............: avg=54.12ms  min=697.64µs med=45.19ms max=330.54ms p(90)=116.14ms p(95)=145.65ms p(99.9)=213.65ms
       { expected_response:true }...: avg=54.12ms  min=697.64µs med=45.19ms max=330.54ms p(90)=116.14ms p(95)=145.65ms p(99.9)=213.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 255852
     http_req_receiving.............: avg=324.97µs min=24.85µs  med=53.14µs max=162.05ms p(90)=227.06µs p(95)=409.05µs p(99.9)=46.13ms 
     http_req_sending...............: avg=134.25µs min=4.19µs   med=9.42µs  max=106.79ms p(90)=19.34µs  p(95)=135.93µs p(99.9)=24.83ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.66ms  min=657.94µs med=44.89ms max=329.69ms p(90)=115.1ms  p(95)=144.42ms p(99.9)=209.65ms
     http_reqs......................: 255852  4197.327218/s
     iteration_duration.............: avg=55.9ms   min=1.34ms   med=46.26ms max=342.88ms p(90)=120.19ms p(95)=150.84ms p(99.9)=234.9ms 
     iterations.....................: 254852  4180.921924/s
     success_rate...................: 100.00% ✓ 254852      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 510963      ✗ 0     
     data_received..................: 15 GB   243 MB/s
     data_sent......................: 206 MB  3.3 MB/s
     http_req_blocked...............: avg=15.81µs  min=922ns   med=2.34µs  max=43.5ms   p(90)=4.16µs   p(95)=5.48µs   p(99.9)=715.82µs
     http_req_connecting............: avg=12.58µs  min=0s      med=0s      max=43.31ms  p(90)=0s       p(95)=0s       p(99.9)=621µs   
     http_req_duration..............: avg=82.96ms  min=1.29ms  med=77.73ms max=305.94ms p(90)=162.23ms p(95)=176.86ms p(99.9)=224.4ms 
       { expected_response:true }...: avg=82.96ms  min=1.29ms  med=77.73ms max=305.94ms p(90)=162.23ms p(95)=176.86ms p(99.9)=224.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 171321
     http_req_receiving.............: avg=138.62µs min=25.42µs med=55.51µs max=192.37ms p(90)=175.04µs p(95)=355.99µs p(99.9)=12.9ms  
     http_req_sending...............: avg=70.42µs  min=4.43µs  med=10.09µs max=249.44ms p(90)=20.17µs  p(95)=126.69µs p(99.9)=8.94ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.75ms  min=1.24ms  med=77.48ms max=305.79ms p(90)=161.93ms p(95)=176.57ms p(99.9)=223.7ms 
     http_reqs......................: 171321  2783.070132/s
     iteration_duration.............: avg=83.7ms   min=3.81ms  med=78.59ms max=324.33ms p(90)=162.69ms p(95)=177.26ms p(99.9)=225.33ms
     iterations.....................: 170321  2766.825362/s
     success_rate...................: 100.00% ✓ 170321      ✗ 0     
     vus............................: 83      min=0         max=492 
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

     checks.........................: 100.00% ✓ 261804      ✗ 0    
     data_received..................: 7.7 GB  124 MB/s
     data_sent......................: 106 MB  1.7 MB/s
     http_req_blocked...............: avg=6.31µs   min=1.06µs  med=3.13µs   max=12.71ms  p(90)=5.15µs   p(95)=6.3µs    p(99.9)=549.4µs 
     http_req_connecting............: avg=2.39µs   min=0s      med=0s       max=12.6ms   p(90)=0s       p(95)=0s       p(99.9)=479.28µs
     http_req_duration..............: avg=161.62ms min=1.98ms  med=130.37ms max=1.06s    p(90)=343.5ms  p(95)=404.52ms p(99.9)=680.91ms
       { expected_response:true }...: avg=161.62ms min=1.98ms  med=130.37ms max=1.06s    p(90)=343.5ms  p(95)=404.52ms p(99.9)=680.91ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 88268
     http_req_receiving.............: avg=83.45µs  min=28.84µs med=65.8µs   max=46.62ms  p(90)=106.3µs  p(95)=125.5µs  p(99.9)=2.27ms  
     http_req_sending...............: avg=36.39µs  min=4.93µs  med=13.64µs  max=137.03ms p(90)=21.08µs  p(95)=25.37µs  p(99.9)=4.09ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=161.5ms  min=1.94ms  med=130.22ms max=1.06s    p(90)=343.4ms  p(95)=404.37ms p(99.9)=680.81ms
     http_reqs......................: 88268   1413.791265/s
     iteration_duration.............: avg=163.72ms min=6.83ms  med=132.69ms max=1.06s    p(90)=344.88ms p(95)=405.72ms p(99.9)=681.83ms
     iterations.....................: 87268   1397.774234/s
     success_rate...................: 100.00% ✓ 87268       ✗ 0    
     vus............................: 78      min=0         max=493
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

     checks.........................: 100.00% ✓ 240060      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 97 MB   1.6 MB/s
     http_req_blocked...............: avg=6.5µs    min=1.11µs  med=2.76µs   max=21.55ms  p(90)=4.45µs   p(95)=5.42µs   p(99.9)=563.36µs
     http_req_connecting............: avg=3.06µs   min=0s      med=0s       max=21.48ms  p(90)=0s       p(95)=0s       p(99.9)=515.73µs
     http_req_duration..............: avg=176.01ms min=2.02ms  med=174.13ms max=453.34ms p(90)=334.65ms p(95)=356.72ms p(99.9)=417.67ms
       { expected_response:true }...: avg=176.01ms min=2.02ms  med=174.13ms max=453.34ms p(90)=334.65ms p(95)=356.72ms p(99.9)=417.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 81020
     http_req_receiving.............: avg=81.43µs  min=28.45µs med=64.36µs  max=175.63ms p(90)=102.56µs p(95)=118.92µs p(99.9)=1.44ms  
     http_req_sending...............: avg=33.63µs  min=4.78µs  med=11.52µs  max=166.29ms p(90)=18.01µs  p(95)=21.62µs  p(99.9)=3.48ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=175.89ms min=1.97ms  med=174ms    max=453.26ms p(90)=334.54ms p(95)=356.61ms p(99.9)=417.58ms
     http_reqs......................: 81020   1296.202621/s
     iteration_duration.............: avg=178.45ms min=5.28ms  med=176.93ms max=453.56ms p(90)=335.34ms p(95)=357.23ms p(99.9)=418.1ms 
     iterations.....................: 80020   1280.20407/s
     success_rate...................: 100.00% ✓ 80020       ✗ 0    
     vus............................: 81      min=0         max=493
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

     checks.........................: 100.00% ✓ 93237      ✗ 0    
     data_received..................: 2.8 GB  43 MB/s
     data_sent......................: 39 MB   596 kB/s
     http_req_blocked...............: avg=8.22µs   min=972ns   med=2.64µs   max=4.07ms  p(90)=4.34µs   p(95)=5.27µs   p(99.9)=1.48ms 
     http_req_connecting............: avg=4.58µs   min=0s      med=0s       max=3.86ms  p(90)=0s       p(95)=0s       p(99.9)=1.43ms 
     http_req_duration..............: avg=447.49ms min=3.78ms  med=415.85ms max=1.87s   p(90)=893.45ms p(95)=975.96ms p(99.9)=1.39s  
       { expected_response:true }...: avg=447.49ms min=3.78ms  med=415.85ms max=1.87s   p(90)=893.45ms p(95)=975.96ms p(99.9)=1.39s  
     http_req_failed................: 0.00%   ✓ 0          ✗ 32079
     http_req_receiving.............: avg=78.8µs   min=28.33µs med=68.83µs  max=16.95ms p(90)=107.05µs p(95)=121.15µs p(99.9)=979.3µs
     http_req_sending...............: avg=34.99µs  min=4.98µs  med=12.81µs  max=142ms   p(90)=19.32µs  p(95)=21.73µs  p(99.9)=2.78ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=447.38ms min=3.73ms  med=415.74ms max=1.87s   p(90)=893.37ms p(95)=975.57ms p(99.9)=1.39s  
     http_reqs......................: 32079   496.178129/s
     iteration_duration.............: avg=462.09ms min=26.29ms med=433.77ms max=1.87s   p(90)=897ms    p(95)=979.21ms p(99.9)=1.4s   
     iterations.....................: 31079   480.710748/s
     success_rate...................: 100.00% ✓ 31079      ✗ 0    
     vus............................: 87      min=0        max=500
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

     checks.........................: 100.00% ✓ 46290      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   288 kB/s
     http_req_blocked...............: avg=14.53µs  min=1.26µs  med=3.5µs    max=9.95ms   p(90)=5.25µs   p(95)=6.96µs   p(99.9)=2.21ms
     http_req_connecting............: avg=9.35µs   min=0s      med=0s       max=9.89ms   p(90)=0s       p(95)=0s       p(99.9)=2.19ms
     http_req_duration..............: avg=883.43ms min=7.61ms  med=814.66ms max=3s       p(90)=1.8s     p(95)=1.91s    p(99.9)=2.64s 
       { expected_response:true }...: avg=883.43ms min=7.61ms  med=814.66ms max=3s       p(90)=1.8s     p(95)=1.91s    p(99.9)=2.64s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16430
     http_req_receiving.............: avg=100.15µs min=32.7µs  med=88.23µs  max=95.07ms  p(90)=125.83µs p(95)=141.25µs p(99.9)=1.04ms
     http_req_sending...............: avg=35.4µs   min=5.58µs  med=17.21µs  max=150.52ms p(90)=22.59µs  p(95)=25.92µs  p(99.9)=2.55ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=883.29ms min=7.53ms  med=814.56ms max=3s       p(90)=1.8s     p(95)=1.91s    p(99.9)=2.64s 
     http_reqs......................: 16430   239.844787/s
     iteration_duration.............: avg=940.66ms min=23.92ms med=871.18ms max=3s       p(90)=1.81s    p(95)=1.92s    p(99.9)=2.65s 
     iterations.....................: 15430   225.246808/s
     success_rate...................: 100.00% ✓ 15430      ✗ 0    
     vus............................: 82      min=0        max=499
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

     checks.........................: 100.00% ✓ 45726      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   288 kB/s
     http_req_blocked...............: avg=14.35µs  min=1.14µs  med=3.15µs   max=13.44ms p(90)=4.86µs   p(95)=6.38µs   p(99.9)=2.25ms
     http_req_connecting............: avg=9.58µs   min=0s      med=0s       max=13.37ms p(90)=0s       p(95)=0s       p(99.9)=2.23ms
     http_req_duration..............: avg=896.88ms min=5.79ms  med=824.86ms max=4.73s   p(90)=1.77s    p(95)=2.02s    p(99.9)=4.25s 
       { expected_response:true }...: avg=896.88ms min=5.79ms  med=824.86ms max=4.73s   p(90)=1.77s    p(95)=2.02s    p(99.9)=4.25s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16242
     http_req_receiving.............: avg=94.77µs  min=28.71µs med=84.92µs  max=32.89ms p(90)=121.63µs p(95)=137.08µs p(99.9)=1.2ms 
     http_req_sending...............: avg=23.42µs  min=5.55µs  med=16.1µs   max=26.43ms p(90)=21.32µs  p(95)=24.55µs  p(99.9)=1.11ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=896.76ms min=5.68ms  med=824.74ms max=4.73s   p(90)=1.77s    p(95)=2.02s    p(99.9)=4.25s 
     http_reqs......................: 16242   239.999075/s
     iteration_duration.............: avg=955.7ms  min=66.35ms med=910.58ms max=4.74s   p(90)=1.8s     p(95)=2.03s    p(99.9)=4.26s 
     iterations.....................: 15242   225.222626/s
     success_rate...................: 100.00% ✓ 15242      ✗ 0    
     vus............................: 81      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

