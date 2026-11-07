## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,676 | 4,703 | 4,635 | 0.7% | 419 MB | 91.8 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,603 | 4,612 | 4,510 | 0.9% | 432 MB | 96.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,593 | 4,600 | 4,571 | 0.2% | 412 MB | 91.8 KB |  |
| fusion-net-11 | 16.7.3 | 4,587 | 4,676 | 4,577 | 0.9% | 421 MB | 94.0 KB |  |
| fusion-aot-11 | 16.7.3 | 4,455 | 4,529 | 4,404 | 1.2% | 155 MB | 35.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,369 | 4,408 | 4,357 | 0.4% | 160 MB | 37.5 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,236 | 4,244 | 4,223 | 0.2% | 193 MB | 46.7 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,209 | 4,228 | 4,131 | 0.9% | 2,306 MB | 560.9 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,203 | 4,233 | 4,174 | 0.6% | 177 MB | 43.1 KB |  |
| hive-router | v0.3.10 | 2,657 | 2,664 | 2,652 | 0.2% | 168 MB | 64.8 KB |  |
| caliban | 3.2.0 | 1,353 | 1,355 | 1,353 | 0.1% | 10,874 MB | 8,229.8 KB |  |
| cosmo | 0.365.2 | 1,345 | 1,346 | 1,343 | 0.1% | 595 MB | 453.3 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 499 | 499 | 494 | 0.4% | 3,175 MB | 6,515.0 KB |  |
| hive-gateway | 2.15.6 | 241 | 241 | 239 | 0.5% | 3,907 MB | 16,599.2 KB |  |
| apollo-gateway | 2.14.4 | 235 | 236 | 235 | 0.2% | 2,451 MB | 10,679.1 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (7751 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (6788 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (158788 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 852060      ✗ 0     
     data_received..................: 25 GB   409 MB/s
     data_sent......................: 342 MB  5.6 MB/s
     http_req_blocked...............: avg=70.04µs  min=792ns    med=2.3µs   max=146.52ms p(90)=3.9µs    p(95)=5.05µs   p(99.9)=26.62ms 
     http_req_connecting............: avg=65.11µs  min=0s       med=0s      max=137.31ms p(90)=0s       p(95)=0s       p(99.9)=25.68ms 
     http_req_duration..............: avg=48.27ms  min=760.35µs med=40.79ms max=255.62ms p(90)=100.56ms p(95)=124.85ms p(99.9)=184.51ms
       { expected_response:true }...: avg=48.27ms  min=760.35µs med=40.79ms max=255.62ms p(90)=100.56ms p(95)=124.85ms p(99.9)=184.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 285020
     http_req_receiving.............: avg=356.46µs min=24.41µs  med=52.72µs max=185.07ms p(90)=211.55µs p(95)=363.19µs p(99.9)=49.77ms 
     http_req_sending...............: avg=155.06µs min=3.97µs   med=8.64µs  max=106.88ms p(90)=16.71µs  p(95)=117.1µs  p(99.9)=27.96ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.76ms  min=713.29µs med=40.47ms max=255.56ms p(90)=99.48ms  p(95)=123.47ms p(99.9)=174.73ms
     http_reqs......................: 285020  4676.553815/s
     iteration_duration.............: avg=50.15ms  min=1.21ms   med=41.42ms max=391.52ms p(90)=105.48ms p(95)=132.61ms p(99.9)=211.58ms
     iterations.....................: 284020  4660.146006/s
     success_rate...................: 100.00% ✓ 284020      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 841347      ✗ 0     
     data_received..................: 25 GB   403 MB/s
     data_sent......................: 338 MB  5.5 MB/s
     http_req_blocked...............: avg=58.93µs  min=812ns    med=2.11µs  max=140.8ms  p(90)=3.83µs   p(95)=5.06µs   p(99.9)=20.26ms 
     http_req_connecting............: avg=55.34µs  min=0s       med=0s      max=115.27ms p(90)=0s       p(95)=0s       p(99.9)=19.75ms 
     http_req_duration..............: avg=49.15ms  min=904.93µs med=41.46ms max=300.67ms p(90)=104.17ms p(95)=129.73ms p(99.9)=180.35ms
       { expected_response:true }...: avg=49.15ms  min=904.93µs med=41.46ms max=300.67ms p(90)=104.17ms p(95)=129.73ms p(99.9)=180.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281449
     http_req_receiving.............: avg=326.97µs min=26.03µs  med=52.56µs max=111.87ms p(90)=212.7µs  p(95)=374.58µs p(99.9)=42.1ms  
     http_req_sending...............: avg=139.13µs min=4.21µs   med=8.58µs  max=96.76ms  p(90)=17.91µs  p(95)=119.79µs p(99.9)=24.48ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.69ms  min=860.8µs  med=41.13ms max=256.25ms p(90)=103.04ms p(95)=128.64ms p(99.9)=176.66ms
     http_reqs......................: 281449  4603.923376/s
     iteration_duration.............: avg=50.79ms  min=1.44ms   med=42.32ms max=323.76ms p(90)=107.42ms p(95)=134.67ms p(99.9)=208.67ms
     iterations.....................: 280449  4587.565445/s
     success_rate...................: 100.00% ✓ 280449      ✗ 0     
     vus............................: 62      min=0         max=497 
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

     checks.........................: 100.00% ✓ 839028      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=61.83µs  min=822ns    med=2.13µs  max=125.68ms p(90)=3.89µs   p(95)=5.12µs   p(99.9)=21.52ms 
     http_req_connecting............: avg=58.19µs  min=0s       med=0s      max=125.58ms p(90)=0s       p(95)=0s       p(99.9)=21.45ms 
     http_req_duration..............: avg=49.22ms  min=890.17µs med=41.58ms max=288.85ms p(90)=103.63ms p(95)=128.67ms p(99.9)=181.1ms 
       { expected_response:true }...: avg=49.22ms  min=890.17µs med=41.58ms max=288.85ms p(90)=103.63ms p(95)=128.67ms p(99.9)=181.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 280676
     http_req_receiving.............: avg=322.86µs min=26.12µs  med=52.78µs max=147.43ms p(90)=203.23µs p(95)=365.45µs p(99.9)=46.33ms 
     http_req_sending...............: avg=145.23µs min=4.03µs   med=8.8µs   max=156.89ms p(90)=18.12µs  p(95)=119.02µs p(99.9)=25.41ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.75ms  min=851.76µs med=41.27ms max=267.67ms p(90)=102.5ms  p(95)=127.42ms p(99.9)=177.17ms
     http_reqs......................: 280676  4593.202979/s
     iteration_duration.............: avg=50.92ms  min=1.44ms   med=42.34ms max=346.36ms p(90)=107.38ms p(95)=133.67ms p(99.9)=206.83ms
     iterations.....................: 279676  4576.838192/s
     success_rate...................: 100.00% ✓ 279676      ✗ 0     
     vus............................: 61      min=0         max=497 
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

     checks.........................: 100.00% ✓ 835683      ✗ 0     
     data_received..................: 25 GB   401 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=68.85µs  min=812ns    med=2.49µs  max=148.34ms p(90)=4.06µs   p(95)=5.2µs    p(99.9)=25.97ms 
     http_req_connecting............: avg=64.77µs  min=0s       med=0s      max=147.98ms p(90)=0s       p(95)=0s       p(99.9)=25.03ms 
     http_req_duration..............: avg=49.24ms  min=763.14µs med=41.4ms  max=299.44ms p(90)=104.42ms p(95)=129.44ms p(99.9)=186.52ms
       { expected_response:true }...: avg=49.24ms  min=763.14µs med=41.4ms  max=299.44ms p(90)=104.42ms p(95)=129.44ms p(99.9)=186.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279561
     http_req_receiving.............: avg=398.47µs min=25.34µs  med=53.26µs max=179.85ms p(90)=221.91µs p(95)=377.01µs p(99.9)=57.34ms 
     http_req_sending...............: avg=158.26µs min=4.07µs   med=8.9µs   max=127.69ms p(90)=17.21µs  p(95)=121.33µs p(99.9)=28.1ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.68ms  min=719.27µs med=41.06ms max=255.41ms p(90)=103.07ms p(95)=128.02ms p(99.9)=176.65ms
     http_reqs......................: 279561  4587.422677/s
     iteration_duration.............: avg=51.14ms  min=1.23ms   med=42.27ms max=382.63ms p(90)=109.02ms p(95)=136.26ms p(99.9)=209.78ms
     iterations.....................: 278561  4571.013297/s
     success_rate...................: 100.00% ✓ 278561      ✗ 0     
     vus............................: 54      min=0         max=499 
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

     checks.........................: 100.00% ✓ 812808      ✗ 0     
     data_received..................: 24 GB   390 MB/s
     data_sent......................: 327 MB  5.4 MB/s
     http_req_blocked...............: avg=57.74µs  min=821ns    med=2.41µs  max=162.94ms p(90)=4.14µs   p(95)=5.36µs   p(99.9)=19.47ms 
     http_req_connecting............: avg=54.11µs  min=0s       med=0s      max=162.84ms p(90)=0s       p(95)=0s       p(99.9)=18.78ms 
     http_req_duration..............: avg=51.22ms  min=833.82µs med=42.51ms max=315.97ms p(90)=110.7ms  p(95)=138.33ms p(99.9)=190.95ms
       { expected_response:true }...: avg=51.22ms  min=833.82µs med=42.51ms max=315.97ms p(90)=110.7ms  p(95)=138.33ms p(99.9)=190.95ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 271936
     http_req_receiving.............: avg=335.5µs  min=21.41µs  med=51.28µs max=99.02ms  p(90)=223.1µs  p(95)=401.23µs p(99.9)=44.3ms  
     http_req_sending...............: avg=140.12µs min=3.91µs   med=8.85µs  max=80.51ms  p(90)=18.34µs  p(95)=129.46µs p(99.9)=25.81ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.74ms  min=792.7µs  med=42.23ms max=315.44ms p(90)=109.62ms p(95)=137.14ms p(99.9)=186.95ms
     http_reqs......................: 271936  4455.059656/s
     iteration_duration.............: avg=52.58ms  min=1.4ms    med=43.22ms max=390.83ms p(90)=113.67ms p(95)=142.19ms p(99.9)=210.1ms 
     iterations.....................: 270936  4438.676905/s
     success_rate...................: 100.00% ✓ 270936      ✗ 0     
     vus............................: 59      min=0         max=497 
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

     checks.........................: 100.00% ✓ 797394      ✗ 0     
     data_received..................: 23 GB   382 MB/s
     data_sent......................: 321 MB  5.2 MB/s
     http_req_blocked...............: avg=57.2µs   min=932ns   med=2.48µs  max=183.81ms p(90)=4.1µs    p(95)=5.25µs   p(99.9)=19.99ms 
     http_req_connecting............: avg=52.65µs  min=0s      med=0s      max=119.59ms p(90)=0s       p(95)=0s       p(99.9)=19.28ms 
     http_req_duration..............: avg=52.2ms   min=844.9µs med=43.38ms max=286.6ms  p(90)=112.62ms p(95)=139.81ms p(99.9)=200.12ms
       { expected_response:true }...: avg=52.2ms   min=844.9µs med=43.38ms max=286.6ms  p(90)=112.62ms p(95)=139.81ms p(99.9)=200.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 266798
     http_req_receiving.............: avg=353.52µs min=24.84µs med=51.98µs max=163.26ms p(90)=235.46µs p(95)=411.13µs p(99.9)=48.58ms 
     http_req_sending...............: avg=133.51µs min=4.06µs  med=8.99µs  max=98.1ms   p(90)=18.74µs  p(95)=134.21µs p(99.9)=23.9ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.71ms  min=797.3µs med=43.1ms  max=268.5ms  p(90)=111.6ms  p(95)=138.47ms p(99.9)=188.86ms
     http_reqs......................: 266798  4369.861363/s
     iteration_duration.............: avg=53.6ms   min=1.34ms  med=44.16ms max=355.23ms p(90)=115.17ms p(95)=142.93ms p(99.9)=221.94ms
     iterations.....................: 265798  4353.48245/s
     success_rate...................: 100.00% ✓ 265798      ✗ 0     
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

     checks.........................: 100.00% ✓ 774792      ✗ 0     
     data_received..................: 23 GB   371 MB/s
     data_sent......................: 312 MB  5.1 MB/s
     http_req_blocked...............: avg=51.56µs  min=851ns    med=2.54µs  max=126.77ms p(90)=4.25µs   p(95)=5.47µs   p(99.9)=14.83ms 
     http_req_connecting............: avg=47.59µs  min=0s       med=0s      max=124.28ms p(90)=0s       p(95)=0s       p(99.9)=14.63ms 
     http_req_duration..............: avg=53.79ms  min=995.51µs med=45.36ms max=286.13ms p(90)=115.1ms  p(95)=144.09ms p(99.9)=198.97ms
       { expected_response:true }...: avg=53.79ms  min=995.51µs med=45.36ms max=286.13ms p(90)=115.1ms  p(95)=144.09ms p(99.9)=198.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 259264
     http_req_receiving.............: avg=293.25µs min=24.06µs  med=52.03µs max=131.47ms p(90)=234.46µs p(95)=411.52µs p(99.9)=36.98ms 
     http_req_sending...............: avg=127.04µs min=4.2µs    med=9.08µs  max=67.79ms  p(90)=19.92µs  p(95)=135.69µs p(99.9)=22.49ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.37ms  min=941.6µs  med=45.08ms max=285.89ms p(90)=114.29ms p(95)=143.03ms p(99.9)=194.4ms 
     http_reqs......................: 259264  4236.910912/s
     iteration_duration.............: avg=55.16ms  min=1.61ms   med=46.13ms max=361.45ms p(90)=117.88ms p(95)=147ms    p(99.9)=231.43ms
     iterations.....................: 258264  4220.56884/s
     success_rate...................: 100.00% ✓ 258264      ✗ 0     
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

     checks.........................: 100.00% ✓ 766767      ✗ 0     
     data_received..................: 22 GB   368 MB/s
     data_sent......................: 308 MB  5.1 MB/s
     http_req_blocked...............: avg=45.21µs  min=761ns    med=2.26µs  max=102.89ms p(90)=3.92µs   p(95)=5.03µs   p(99.9)=9.19ms  
     http_req_connecting............: avg=42.21µs  min=0s       med=0s      max=102.81ms p(90)=0s       p(95)=0s       p(99.9)=9.05ms  
     http_req_duration..............: avg=54.56ms  min=687.69µs med=45.76ms max=308.52ms p(90)=115.63ms p(95)=144.73ms p(99.9)=214.71ms
       { expected_response:true }...: avg=54.56ms  min=687.69µs med=45.76ms max=308.52ms p(90)=115.63ms p(95)=144.73ms p(99.9)=214.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 256589
     http_req_receiving.............: avg=276.17µs min=24.19µs  med=51µs    max=108.22ms p(90)=213.85µs p(95)=377.13µs p(99.9)=39.01ms 
     http_req_sending...............: avg=124.37µs min=3.9µs    med=9.08µs  max=184.29ms p(90)=17.96µs  p(95)=126.83µs p(99.9)=22.8ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.16ms  min=645.9µs  med=45.47ms max=308.46ms p(90)=114.72ms p(95)=143.61ms p(99.9)=209.94ms
     http_reqs......................: 256589  4209.89336/s
     iteration_duration.............: avg=55.74ms  min=1.43ms   med=46.57ms max=308.71ms p(90)=118.01ms p(95)=147.73ms p(99.9)=229.02ms
     iterations.....................: 255589  4193.486213/s
     success_rate...................: 100.00% ✓ 255589      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 768828      ✗ 0     
     data_received..................: 23 GB   368 MB/s
     data_sent......................: 309 MB  5.1 MB/s
     http_req_blocked...............: avg=49.42µs  min=822ns    med=2.46µs  max=105.32ms p(90)=4.22µs   p(95)=5.38µs   p(99.9)=16.15ms 
     http_req_connecting............: avg=45.32µs  min=0s       med=0s      max=105.27ms p(90)=0s       p(95)=0s       p(99.9)=15.12ms 
     http_req_duration..............: avg=54.39ms  min=987.7µs  med=45.57ms max=322.01ms p(90)=117ms    p(95)=145.43ms p(99.9)=201.45ms
       { expected_response:true }...: avg=54.39ms  min=987.7µs  med=45.57ms max=322.01ms p(90)=117ms    p(95)=145.43ms p(99.9)=201.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 257276
     http_req_receiving.............: avg=282.98µs min=26.63µs  med=51.78µs max=184.88ms p(90)=234.33µs p(95)=410.24µs p(99.9)=39.6ms  
     http_req_sending...............: avg=127.48µs min=4.11µs   med=9.04µs  max=155.09ms p(90)=19.43µs  p(95)=136.71µs p(99.9)=22.46ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.98ms  min=932.34µs med=45.29ms max=302.01ms p(90)=116.2ms  p(95)=144.49ms p(99.9)=197.08ms
     http_reqs......................: 257276  4203.658922/s
     iteration_duration.............: avg=55.59ms  min=1.56ms   med=46.25ms max=332.66ms p(90)=119.39ms p(95)=147.84ms p(99.9)=223.15ms
     iterations.....................: 256276  4187.31982/s
     success_rate...................: 100.00% ✓ 256276      ✗ 0     
     vus............................: 66      min=0         max=496 
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

     checks.........................: 100.00% ✓ 486981      ✗ 0     
     data_received..................: 14 GB   233 MB/s
     data_sent......................: 196 MB  3.2 MB/s
     http_req_blocked...............: avg=17.89µs  min=1.09µs  med=2.94µs  max=59.88ms  p(90)=4.72µs   p(95)=6µs      p(99.9)=1.22ms  
     http_req_connecting............: avg=14.16µs  min=0s      med=0s      max=59.65ms  p(90)=0s       p(95)=0s       p(99.9)=1.1ms   
     http_req_duration..............: avg=87.04ms  min=1.21ms  med=81.55ms max=297.52ms p(90)=169.96ms p(95)=185.02ms p(99.9)=234.85ms
       { expected_response:true }...: avg=87.04ms  min=1.21ms  med=81.55ms max=297.52ms p(90)=169.96ms p(95)=185.02ms p(99.9)=234.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 163327
     http_req_receiving.............: avg=145.64µs min=26.83µs med=58.11µs max=73.33ms  p(90)=185µs    p(95)=382.04µs p(99.9)=13.33ms 
     http_req_sending...............: avg=71.9µs   min=4.27µs  med=10.92µs max=180.32ms p(90)=20.8µs   p(95)=133.8µs  p(99.9)=9ms     
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=86.82ms  min=1.15ms  med=81.34ms max=297.25ms p(90)=169.66ms p(95)=184.71ms p(99.9)=234.16ms
     http_reqs......................: 163327  2657.834021/s
     iteration_duration.............: avg=87.83ms  min=3.38ms  med=82.55ms max=325.71ms p(90)=170.43ms p(95)=185.48ms p(99.9)=235.94ms
     iterations.....................: 162327  2641.560937/s
     success_rate...................: 100.00% ✓ 162327      ✗ 0     
     vus............................: 78      min=0         max=493 
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

     checks.........................: 100.00% ✓ 250425      ✗ 0    
     data_received..................: 7.4 GB  118 MB/s
     data_sent......................: 101 MB  1.6 MB/s
     http_req_blocked...............: avg=6.24µs   min=1.14µs  med=3.05µs   max=7.84ms   p(90)=4.85µs   p(95)=5.84µs   p(99.9)=551.32µs
     http_req_connecting............: avg=2.52µs   min=0s      med=0s       max=7.77ms   p(90)=0s       p(95)=0s       p(99.9)=484.96µs
     http_req_duration..............: avg=168.9ms  min=1.96ms  med=142.67ms max=907.51ms p(90)=347.94ms p(95)=409.22ms p(99.9)=678.48ms
       { expected_response:true }...: avg=168.9ms  min=1.96ms  med=142.67ms max=907.51ms p(90)=347.94ms p(95)=409.22ms p(99.9)=678.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 84475
     http_req_receiving.............: avg=75.66µs  min=28.23µs med=61.17µs  max=45.71ms  p(90)=97.44µs  p(95)=112.02µs p(99.9)=1.8ms   
     http_req_sending...............: avg=34.5µs   min=4.71µs  med=12.22µs  max=119ms    p(90)=18.21µs  p(95)=21.69µs  p(99.9)=4ms     
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=168.79ms min=1.91ms  med=142.57ms max=907.4ms  p(90)=347.85ms p(95)=409.08ms p(99.9)=678.41ms
     http_reqs......................: 84475   1353.937419/s
     iteration_duration.............: avg=171.16ms min=7.4ms   med=145.37ms max=907.7ms  p(90)=349.57ms p(95)=410.63ms p(99.9)=679.36ms
     iterations.....................: 83475   1337.909749/s
     success_rate...................: 100.00% ✓ 83475       ✗ 0    
     vus............................: 74      min=0         max=494
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

     checks.........................: 100.00% ✓ 248799      ✗ 0    
     data_received..................: 7.3 GB  118 MB/s
     data_sent......................: 101 MB  1.6 MB/s
     http_req_blocked...............: avg=6.29µs   min=1.13µs  med=2.85µs   max=14.23ms  p(90)=4.61µs   p(95)=5.6µs    p(99.9)=456.04µs
     http_req_connecting............: avg=2.8µs    min=0s      med=0s       max=13.95ms  p(90)=0s       p(95)=0s       p(99.9)=341.31µs
     http_req_duration..............: avg=169.9ms  min=1.97ms  med=167.74ms max=464.07ms p(90)=323.07ms p(95)=346.18ms p(99.9)=415.11ms
       { expected_response:true }...: avg=169.9ms  min=1.97ms  med=167.74ms max=464.07ms p(90)=323.07ms p(95)=346.18ms p(99.9)=415.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 83933
     http_req_receiving.............: avg=79.35µs  min=27.51µs med=62.38µs  max=23.57ms  p(90)=100.06µs p(95)=116.82µs p(99.9)=1.83ms  
     http_req_sending...............: avg=38.99µs  min=5.14µs  med=11.9µs   max=193.44ms p(90)=18.49µs  p(95)=22.64µs  p(99.9)=3.98ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=169.78ms min=1.91ms  med=167.62ms max=463.99ms p(90)=322.97ms p(95)=346.06ms p(99.9)=414.99ms
     http_reqs......................: 83933   1345.019427/s
     iteration_duration.............: avg=172.21ms min=4.12ms  med=170.51ms max=464.31ms p(90)=323.78ms p(95)=346.82ms p(99.9)=415.89ms
     iterations.....................: 82933   1328.99451/s
     success_rate...................: 100.00% ✓ 82933       ✗ 0    
     vus............................: 76      min=0         max=494
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

     checks.........................: 100.00% ✓ 93774      ✗ 0    
     data_received..................: 2.8 GB  44 MB/s
     data_sent......................: 39 MB   600 kB/s
     http_req_blocked...............: avg=9.77µs   min=1.2µs   med=3.24µs   max=9.33ms   p(90)=4.98µs   p(95)=6.05µs   p(99.9)=1.91ms
     http_req_connecting............: avg=5.44µs   min=0s      med=0s       max=9.27ms   p(90)=0s       p(95)=0s       p(99.9)=1.84ms
     http_req_duration..............: avg=445.09ms min=3.69ms  med=410.84ms max=1.7s     p(90)=885.26ms p(95)=974.45ms p(99.9)=1.42s 
       { expected_response:true }...: avg=445.09ms min=3.69ms  med=410.84ms max=1.7s     p(90)=885.26ms p(95)=974.45ms p(99.9)=1.42s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 32258
     http_req_receiving.............: avg=92.23µs  min=29.98µs med=73.91µs  max=136.19ms p(90)=111.77µs p(95)=126.69µs p(99.9)=1.02ms
     http_req_sending...............: avg=28.59µs  min=5.41µs  med=14.73µs  max=68.15ms  p(90)=21.38µs  p(95)=23.94µs  p(99.9)=2.61ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=444.96ms min=3.63ms  med=410.75ms max=1.7s     p(90)=885.14ms p(95)=974.37ms p(99.9)=1.42s 
     http_reqs......................: 32258   499.56141/s
     iteration_duration.............: avg=459.55ms min=20.66ms med=428.5ms  max=1.7s     p(90)=889.92ms p(95)=977.93ms p(99.9)=1.42s 
     iterations.....................: 31258   484.074976/s
     success_rate...................: 100.00% ✓ 31258      ✗ 0    
     vus............................: 84      min=0        max=499
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

     checks.........................: 100.00% ✓ 46032      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   290 kB/s
     http_req_blocked...............: avg=11.57µs  min=1.27µs  med=3.44µs   max=17.11ms p(90)=5.16µs   p(95)=6.93µs   p(99.9)=932.45µs
     http_req_connecting............: avg=6.37µs   min=0s      med=0s       max=17.05ms p(90)=0s       p(95)=0s       p(99.9)=908.94µs
     http_req_duration..............: avg=891.04ms min=5.6ms   med=815.4ms  max=4.73s   p(90)=1.76s    p(95)=2.07s    p(99.9)=4.36s   
       { expected_response:true }...: avg=891.04ms min=5.6ms   med=815.4ms  max=4.73s   p(90)=1.76s    p(95)=2.07s    p(99.9)=4.36s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16344
     http_req_receiving.............: avg=105.01µs min=32.67µs med=87.68µs  max=62.88ms p(90)=124.44µs p(95)=139.85µs p(99.9)=1.26ms  
     http_req_sending...............: avg=39.78µs  min=5.5µs   med=16.8µs   max=60.28ms p(90)=22.29µs  p(95)=25.92µs  p(99.9)=3.58ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=890.89ms min=5.52ms  med=815.27ms max=4.73s   p(90)=1.76s    p(95)=2.07s    p(99.9)=4.36s   
     http_reqs......................: 16344   241.453715/s
     iteration_duration.............: avg=949.12ms min=22.21ms med=869.08ms max=4.74s   p(90)=1.78s    p(95)=2.09s    p(99.9)=4.38s   
     iterations.....................: 15344   226.680482/s
     success_rate...................: 100.00% ✓ 15344      ✗ 0    
     vus............................: 93      min=0        max=500
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

     checks.........................: 100.00% ✓ 45477      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 19 MB   283 kB/s
     http_req_blocked...............: avg=14.01µs  min=1.18µs  med=3.01µs   max=13.87ms  p(90)=4.59µs   p(95)=5.95µs   p(99.9)=2.23ms
     http_req_connecting............: avg=9.46µs   min=0s      med=0s       max=13.81ms  p(90)=0s       p(95)=0s       p(99.9)=2.21ms
     http_req_duration..............: avg=898.47ms min=7.65ms  med=816.84ms max=2.97s    p(90)=1.82s    p(95)=1.95s    p(99.9)=2.69s 
       { expected_response:true }...: avg=898.47ms min=7.65ms  med=816.84ms max=2.97s    p(90)=1.82s    p(95)=1.95s    p(99.9)=2.69s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16159
     http_req_receiving.............: avg=107.98µs min=32.79µs med=83.83µs  max=144.31ms p(90)=121.72µs p(95)=137.01µs p(99.9)=1.37ms
     http_req_sending...............: avg=36.44µs  min=5.08µs  med=15.18µs  max=133.48ms p(90)=20.19µs  p(95)=23.65µs  p(99.9)=2.29ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=898.32ms min=7.52ms  med=816.74ms max=2.97s    p(90)=1.82s    p(95)=1.95s    p(99.9)=2.69s 
     http_reqs......................: 16159   235.541206/s
     iteration_duration.............: avg=957.68ms min=33.14ms med=917.97ms max=2.98s    p(90)=1.84s    p(95)=1.96s    p(99.9)=2.7s  
     iterations.....................: 15159   220.964735/s
     success_rate...................: 100.00% ✓ 15159      ✗ 0    
     vus............................: 88      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

