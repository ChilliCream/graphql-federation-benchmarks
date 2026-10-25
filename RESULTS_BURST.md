## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-fed-net-11 | 16.7.0-p.39 | 3,800 | 4,022 | 3,762 | 2.2% |  |
| fusion-nightly-net-11 | 16.7.0-p.39 | 3,773 | 3,994 | 3,698 | 2.4% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.39 | 3,754 | 3,962 | 3,725 | 2.0% |  |
| fusion-nightly-fed-aot-11 | 16.7.0-p.39 | 3,624 | 3,812 | 3,612 | 1.9% |  |
| fusion-nightly-net-10 | 16.7.0-p.39 | 3,622 | 3,838 | 3,580 | 2.3% |  |
| fusion-nightly-aot-11 | 16.7.0-p.39 | 3,556 | 3,715 | 3,495 | 2.0% |  |
| feddi-gateway | 3c75a7db8876 | 3,056 | 3,176 | 3,021 | 1.6% |  |
| fusion-net-10 | 16.6.9 | 2,454 | 2,547 | 2,446 | 1.5% |  |
| fusion-net-11 | 16.6.9 | 2,442 | 2,511 | 2,420 | 1.3% |  |
| fusion-fed-net-10 | 16.6.9 | 2,321 | 2,403 | 2,307 | 1.4% |  |
| hive-router | v0.3.5 | 2,315 | 2,510 | 2,294 | 3.3% |  |
| fusion-fed-net-11 | 16.6.9 | 2,211 | 2,281 | 2,191 | 1.4% |  |
| fusion-aot-11 | 16.6.9 | 2,097 | 2,177 | 2,084 | 1.6% |  |
| fusion-fed-aot-11 | 16.6.9 | 1,890 | 1,977 | 1,881 | 1.8% |  |
| caliban | 3.2.0 | 1,344 | 1,385 | 1,332 | 1.3% |  |
| cosmo | 0.361.0 | 1,255 | 1,314 | 1,250 | 1.8% |  |
| hive-gateway-router-runtime | 2.15.2 | 481 | 492 | 478 | 1.1% |  |
| hive-gateway | 2.15.2 | 238 | 248 | 236 | 1.6% |  |
| apollo-gateway | 2.14.4 | 232 | 238 | 231 | 0.9% |  |
| apollo-router | v2.18.0 | — | — | — | — | non-compatible response (21780 across 9/9 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | non-compatible response (12370 across 9/9 runs) |
| grafbase | 0.53.5 | — | — | — | — | non-compatible response (338128 across 9/9 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 697689      ✗ 0     
     data_received..................: 21 GB   333 MB/s
     data_sent......................: 281 MB  4.6 MB/s
     http_req_blocked...............: avg=84.21µs  min=782ns   med=2.17µs  max=134.7ms  p(90)=4.02µs   p(95)=5.28µs   p(99.9)=34.87ms 
     http_req_connecting............: avg=80.67µs  min=0s      med=0s      max=134.61ms p(90)=0s       p(95)=0s       p(99.9)=34.5ms  
     http_req_duration..............: avg=59.11ms  min=1.19ms  med=51.24ms max=321.94ms p(90)=122.28ms p(95)=149.39ms p(99.9)=206.76ms
       { expected_response:true }...: avg=59.11ms  min=1.19ms  med=51.24ms max=321.94ms p(90)=122.28ms p(95)=149.39ms p(99.9)=206.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 233563
     http_req_receiving.............: avg=1.09ms   min=52.87µs med=88.08µs max=140.92ms p(90)=2.79ms   p(95)=5.65ms   p(99.9)=57.6ms  
     http_req_sending...............: avg=157.13µs min=4.34µs  med=9.01µs  max=169.75ms p(90)=18.92µs  p(95)=121.99µs p(99.9)=29.43ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=57.85ms  min=1.09ms  med=50.02ms max=305.24ms p(90)=120.96ms p(95)=147.98ms p(99.9)=201.35ms
     http_reqs......................: 233563  3800.889801/s
     iteration_duration.............: avg=61.26ms  min=1.94ms  med=52.39ms max=390.07ms p(90)=127.67ms p(95)=155.94ms p(99.9)=237.5ms 
     iterations.....................: 232563  3784.616291/s
     success_rate...................: 100.00% ✓ 232563      ✗ 0     
     vus............................: 77      min=0         max=493 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 689574      ✗ 0     
     data_received..................: 20 GB   331 MB/s
     data_sent......................: 277 MB  4.5 MB/s
     http_req_blocked...............: avg=78.47µs  min=781ns    med=2.09µs  max=149.27ms p(90)=3.74µs   p(95)=4.91µs   p(99.9)=32.6ms  
     http_req_connecting............: avg=74.92µs  min=0s       med=0s      max=149.21ms p(90)=0s       p(95)=0s       p(99.9)=32.39ms 
     http_req_duration..............: avg=59.78ms  min=913.69µs med=52.04ms max=290.06ms p(90)=121.09ms p(95)=147.77ms p(99.9)=210.3ms 
       { expected_response:true }...: avg=59.78ms  min=913.69µs med=52.04ms max=290.06ms p(90)=121.09ms p(95)=147.77ms p(99.9)=210.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 230858
     http_req_receiving.............: avg=1.48ms   min=54.2µs   med=87.5µs  max=277.26ms p(90)=4.31ms   p(95)=8.13ms   p(99.9)=61.93ms 
     http_req_sending...............: avg=146.67µs min=4.51µs   med=8.79µs  max=190ms    p(90)=18.13µs  p(95)=118.4µs  p(99.9)=27.74ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=58.15ms  min=808.68µs med=50.12ms max=284.41ms p(90)=119.81ms p(95)=146.47ms p(99.9)=200.75ms
     http_reqs......................: 230858  3773.938547/s
     iteration_duration.............: avg=61.99ms  min=1.68ms   med=53.2ms  max=380.13ms p(90)=126.24ms p(95)=154.07ms p(99.9)=255.42ms
     iterations.....................: 229858  3757.591102/s
     success_rate...................: 100.00% ✓ 229858      ✗ 0     
     vus............................: 65      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 690438      ✗ 0     
     data_received..................: 20 GB   329 MB/s
     data_sent......................: 278 MB  4.5 MB/s
     http_req_blocked...............: avg=86.12µs  min=821ns   med=2.12µs  max=146.73ms p(90)=3.92µs   p(95)=5.12µs   p(99.9)=34.67ms 
     http_req_connecting............: avg=82.47µs  min=0s      med=0s      max=146.68ms p(90)=0s       p(95)=0s       p(99.9)=34.46ms 
     http_req_duration..............: avg=59.5ms   min=1.2ms   med=51.07ms max=317.7ms  p(90)=122.8ms  p(95)=150.52ms p(99.9)=212.97ms
       { expected_response:true }...: avg=59.5ms   min=1.2ms   med=51.07ms max=317.7ms  p(90)=122.8ms  p(95)=150.52ms p(99.9)=212.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 231146
     http_req_receiving.............: avg=815.34µs min=52.31µs med=86.65µs max=137.75ms p(90)=1.29ms   p(95)=3.76ms   p(99.9)=53.43ms 
     http_req_sending...............: avg=147.48µs min=4.45µs  med=8.76µs  max=103.78ms p(90)=18.66µs  p(95)=120.92µs p(99.9)=27.84ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=58.54ms  min=1.1ms   med=50.33ms max=317.44ms p(90)=121.59ms p(95)=149.04ms p(99.9)=208.47ms
     http_reqs......................: 231146  3754.189127/s
     iteration_duration.............: avg=61.91ms  min=1.98ms  med=52.42ms max=374.59ms p(90)=128.47ms p(95)=156.26ms p(99.9)=243.32ms
     iterations.....................: 230146  3737.947491/s
     success_rate...................: 100.00% ✓ 230146      ✗ 0     
     vus............................: 82      min=0         max=492 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 666666      ✗ 0     
     data_received..................: 20 GB   318 MB/s
     data_sent......................: 268 MB  4.4 MB/s
     http_req_blocked...............: avg=76.31µs  min=841ns  med=2.17µs  max=199.93ms p(90)=4.03µs   p(95)=5.32µs   p(99.9)=31ms    
     http_req_connecting............: avg=73.25µs  min=0s     med=0s      max=199.85ms p(90)=0s       p(95)=0s       p(99.9)=30.94ms 
     http_req_duration..............: avg=62.26ms  min=1.3ms  med=53.68ms max=327.88ms p(90)=129.5ms  p(95)=156.95ms p(99.9)=223.23ms
       { expected_response:true }...: avg=62.26ms  min=1.3ms  med=53.68ms max=327.88ms p(90)=129.5ms  p(95)=156.95ms p(99.9)=223.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 223222
     http_req_receiving.............: avg=1.48ms   min=53.8µs med=90.54µs max=205.17ms p(90)=4.48ms   p(95)=7.22ms   p(99.9)=58.2ms  
     http_req_sending...............: avg=142.03µs min=4.65µs med=8.97µs  max=182.79ms p(90)=19.79µs  p(95)=124.9µs  p(99.9)=27.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=60.62ms  min=1.21ms med=51.77ms max=303.28ms p(90)=128.21ms p(95)=155.65ms p(99.9)=212.35ms
     http_reqs......................: 223222  3624.73161/s
     iteration_duration.............: avg=64.12ms  min=2.02ms med=54.86ms max=434.04ms p(90)=133.25ms p(95)=161.17ms p(99.9)=255.23ms
     iterations.....................: 222222  3608.493373/s
     success_rate...................: 100.00% ✓ 222222      ✗ 0     
     vus............................: 83      min=0         max=494 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 662211      ✗ 0     
     data_received..................: 19 GB   318 MB/s
     data_sent......................: 266 MB  4.4 MB/s
     http_req_blocked...............: avg=89.66µs  min=1.05µs   med=2.82µs  max=165.98ms p(90)=4.52µs   p(95)=5.72µs   p(99.9)=37.68ms 
     http_req_connecting............: avg=85.31µs  min=0s       med=0s      max=165.92ms p(90)=0s       p(95)=0s       p(99.9)=37.21ms 
     http_req_duration..............: avg=61.67ms  min=919.85µs med=52.95ms max=370.16ms p(90)=128.54ms p(95)=155.9ms  p(99.9)=219.07ms
       { expected_response:true }...: avg=61.67ms  min=919.85µs med=52.95ms max=370.16ms p(90)=128.54ms p(95)=155.9ms  p(99.9)=219.07ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 221737
     http_req_receiving.............: avg=1.05ms   min=53.32µs  med=89.18µs max=141.22ms p(90)=2.36ms   p(95)=5.18ms   p(99.9)=55.92ms 
     http_req_sending...............: avg=167.29µs min=4.3µs    med=9.63µs  max=113.87ms p(90)=19.41µs  p(95)=134.57µs p(99.9)=31.3ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=60.45ms  min=832.83µs med=51.85ms max=369.65ms p(90)=127.29ms p(95)=154.59ms p(99.9)=212.39ms
     http_reqs......................: 221737  3622.76758/s
     iteration_duration.............: avg=64.55ms  min=1.52ms   med=54.76ms max=395.26ms p(90)=134.74ms p(95)=163.81ms p(99.9)=263.98ms
     iterations.....................: 220737  3606.429452/s
     success_rate...................: 100.00% ✓ 220737      ✗ 0     
     vus............................: 67      min=0         max=496 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 650646      ✗ 0     
     data_received..................: 19 GB   312 MB/s
     data_sent......................: 262 MB  4.3 MB/s
     http_req_blocked...............: avg=58.6µs   min=821ns    med=2.14µs  max=106.09ms p(90)=3.84µs   p(95)=5.09µs   p(99.9)=22.71ms 
     http_req_connecting............: avg=54.87µs  min=0s       med=0s      max=106ms    p(90)=0s       p(95)=0s       p(99.9)=21.85ms 
     http_req_duration..............: avg=64.41ms  min=962.27µs med=56.52ms max=304.13ms p(90)=127.72ms p(95)=154.42ms p(99.9)=216.79ms
       { expected_response:true }...: avg=64.41ms  min=962.27µs med=56.52ms max=304.13ms p(90)=127.72ms p(95)=154.42ms p(99.9)=216.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 217882
     http_req_receiving.............: avg=2.65ms   min=51.58µs  med=95.74µs max=130.38ms p(90)=8.33ms   p(95)=12.35ms  p(99.9)=61.58ms 
     http_req_sending...............: avg=128.92µs min=4.53µs   med=8.96µs  max=233.9ms  p(90)=19.28µs  p(95)=119.67µs p(99.9)=24.95ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=61.62ms  min=875.85µs med=53ms    max=287.38ms p(90)=125.11ms p(95)=153.03ms p(99.9)=213.69ms
     http_reqs......................: 217882  3556.236393/s
     iteration_duration.............: avg=65.7ms   min=1.66ms   med=57.54ms max=352.29ms p(90)=130.58ms p(95)=157.62ms p(99.9)=230.22ms
     iterations.....................: 216882  3539.914547/s
     success_rate...................: 100.00% ✓ 216882      ✗ 0     
     vus............................: 69      min=0         max=495 
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

     checks.........................: 100.00% ✓ 558555      ✗ 0     
     data_received..................: 16 GB   267 MB/s
     data_sent......................: 225 MB  3.7 MB/s
     http_req_blocked...............: avg=47.6µs   min=982ns    med=2.9µs   max=99.26ms  p(90)=4.96µs   p(95)=6.25µs   p(99.9)=14.47ms 
     http_req_connecting............: avg=43.44µs  min=0s       med=0s      max=99.15ms  p(90)=0s       p(95)=0s       p(99.9)=14.17ms 
     http_req_duration..............: avg=75ms     min=903.38µs med=65.61ms max=359.21ms p(90)=151.7ms  p(95)=179.4ms  p(99.9)=270.03ms
       { expected_response:true }...: avg=75ms     min=903.38µs med=65.61ms max=359.21ms p(90)=151.7ms  p(95)=179.4ms  p(99.9)=270.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 187185
     http_req_receiving.............: avg=279.9µs  min=26.68µs  med=55.66µs max=149.31ms p(90)=209.98µs p(95)=423.27µs p(99.9)=43.63ms 
     http_req_sending...............: avg=122.29µs min=4.85µs   med=10.71µs max=90.5ms   p(90)=22.76µs  p(95)=148.98µs p(99.9)=22.35ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=74.59ms  min=837.06µs med=65.3ms  max=359.16ms p(90)=150.96ms p(95)=178.31ms p(99.9)=267.47ms
     http_reqs......................: 187185  3056.626245/s
     iteration_duration.............: avg=76.56ms  min=1.48ms   med=67.1ms  max=447.1ms  p(90)=153.91ms p(95)=182.49ms p(99.9)=290.46ms
     iterations.....................: 186185  3040.296805/s
     success_rate...................: 100.00% ✓ 186185      ✗ 0     
     vus............................: 67      min=0         max=495 
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

     checks.........................: 100.00% ✓ 452406      ✗ 0     
     data_received..................: 13 GB   215 MB/s
     data_sent......................: 182 MB  2.9 MB/s
     http_req_blocked...............: avg=17.99µs min=832ns   med=2.29µs  max=60.58ms  p(90)=4.5µs    p(95)=5.71µs   p(99.9)=1.82ms  
     http_req_connecting............: avg=14.81µs min=0s      med=0s      max=60.51ms  p(90)=0s       p(95)=0s       p(99.9)=1.76ms  
     http_req_duration..............: avg=93.68ms min=1.48ms  med=89.49ms max=292.54ms p(90)=177.24ms p(95)=190.58ms p(99.9)=239.81ms
       { expected_response:true }...: avg=93.68ms min=1.48ms  med=89.49ms max=292.54ms p(90)=177.24ms p(95)=190.58ms p(99.9)=239.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 151802
     http_req_receiving.............: avg=2.11ms  min=52.96µs med=1.53ms  max=202.68ms p(90)=4.69ms   p(95)=5.99ms   p(99.9)=31.3ms  
     http_req_sending...............: avg=68.93µs min=4.91µs  med=9.36µs  max=101.27ms p(90)=23.43µs  p(95)=118.29µs p(99.9)=9.03ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.49ms min=1.42ms  med=87.06ms max=291.81ms p(90)=174.98ms p(95)=188.38ms p(99.9)=238.52ms
     http_reqs......................: 151802  2454.426505/s
     iteration_duration.............: avg=94.56ms min=4.32ms  med=90.51ms max=333.55ms p(90)=177.67ms p(95)=191ms    p(99.9)=240.63ms
     iterations.....................: 150802  2438.257901/s
     success_rate...................: 100.00% ✓ 150802      ✗ 0     
     vus............................: 96      min=0         max=500 
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

     checks.........................: 100.00% ✓ 449478      ✗ 0     
     data_received..................: 13 GB   214 MB/s
     data_sent......................: 181 MB  2.9 MB/s
     http_req_blocked...............: avg=21.09µs min=862ns   med=2.29µs  max=58.02ms  p(90)=4.52µs   p(95)=5.8µs    p(99.9)=2.18ms  
     http_req_connecting............: avg=17.38µs min=0s      med=0s      max=57.67ms  p(90)=0s       p(95)=0s       p(99.9)=1.98ms  
     http_req_duration..............: avg=94.25ms min=1.45ms  med=89.48ms max=345.2ms  p(90)=179.43ms p(95)=195.5ms  p(99.9)=245.59ms
       { expected_response:true }...: avg=94.25ms min=1.45ms  med=89.48ms max=345.2ms  p(90)=179.43ms p(95)=195.5ms  p(99.9)=245.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 150826
     http_req_receiving.............: avg=4.39ms  min=52.49µs med=4.51ms  max=170.52ms p(90)=7.79ms   p(95)=9.86ms   p(99.9)=39.75ms 
     http_req_sending...............: avg=71.54µs min=4.63µs  med=9.47µs  max=143.42ms p(90)=25.38µs  p(95)=118.32µs p(99.9)=8.86ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=89.78ms min=1.35ms  med=83.95ms max=336.5ms  p(90)=174.51ms p(95)=190.62ms p(99.9)=244.46ms
     http_reqs......................: 150826  2442.740952/s
     iteration_duration.............: avg=95.16ms min=4.02ms  med=90.45ms max=353.68ms p(90)=179.98ms p(95)=195.99ms p(99.9)=247.18ms
     iterations.....................: 149826  2426.545196/s
     success_rate...................: 100.00% ✓ 149826      ✗ 0     
     vus............................: 90      min=0         max=499 
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

     checks.........................: 100.00% ✓ 429912      ✗ 0     
     data_received..................: 13 GB   204 MB/s
     data_sent......................: 173 MB  2.8 MB/s
     http_req_blocked...............: avg=17.06µs min=821ns   med=2.25µs  max=50.59ms  p(90)=4.5µs    p(95)=5.76µs   p(99.9)=1.67ms  
     http_req_connecting............: avg=13.82µs min=0s      med=0s      max=50.54ms  p(90)=0s       p(95)=0s       p(99.9)=1.52ms  
     http_req_duration..............: avg=98.56ms min=1.78ms  med=94.96ms max=365.61ms p(90)=186.64ms p(95)=200.85ms p(99.9)=249.98ms
       { expected_response:true }...: avg=98.56ms min=1.78ms  med=94.96ms max=365.61ms p(90)=186.64ms p(95)=200.85ms p(99.9)=249.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 144304
     http_req_receiving.............: avg=2.2ms   min=53.34µs med=1.62ms  max=269.51ms p(90)=4.8ms    p(95)=6.03ms   p(99.9)=30.12ms 
     http_req_sending...............: avg=63.47µs min=4.35µs  med=9.19µs  max=38.82ms  p(90)=23.65µs  p(95)=117.66µs p(99.9)=8.43ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.3ms  min=1.69ms  med=92.35ms max=280.02ms p(90)=184.23ms p(95)=198.49ms p(99.9)=247.47ms
     http_reqs......................: 144304  2321.420903/s
     iteration_duration.............: avg=99.51ms min=3.34ms  med=96.02ms max=376.28ms p(90)=187.14ms p(95)=201.3ms  p(99.9)=250.89ms
     iterations.....................: 143304  2305.333886/s
     success_rate...................: 100.00% ✓ 143304      ✗ 0     
     vus............................: 65      min=0         max=496 
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

     checks.........................: 100.00% ✓ 427887      ✗ 0     
     data_received..................: 13 GB   203 MB/s
     data_sent......................: 173 MB  2.8 MB/s
     http_req_blocked...............: avg=19.72µs  min=1.1µs   med=3.01µs  max=62.83ms  p(90)=4.92µs   p(95)=6.29µs   p(99.9)=1.09ms  
     http_req_connecting............: avg=15.71µs  min=0s      med=0s      max=57.04ms  p(90)=0s       p(95)=0s       p(99.9)=1.07ms  
     http_req_duration..............: avg=99.02ms  min=1.53ms  med=93.59ms max=340.51ms p(90)=191.38ms p(95)=209.21ms p(99.9)=263.25ms
       { expected_response:true }...: avg=99.02ms  min=1.53ms  med=93.59ms max=340.51ms p(90)=191.38ms p(95)=209.21ms p(99.9)=263.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 143629
     http_req_receiving.............: avg=160.58µs min=28.93µs med=59.69µs max=272.64ms p(90)=160.23µs p(95)=392.55µs p(99.9)=16.12ms 
     http_req_sending...............: avg=75.19µs  min=5.19µs  med=11.47µs max=226.35ms p(90)=22.11µs  p(95)=139.26µs p(99.9)=9.31ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=98.78ms  min=1.44ms  med=93.34ms max=319.1ms  p(90)=191.02ms p(95)=208.86ms p(99.9)=261.97ms
     http_reqs......................: 143629  2315.078588/s
     iteration_duration.............: avg=99.98ms  min=4.75ms  med=94.75ms max=353.01ms p(90)=191.88ms p(95)=209.71ms p(99.9)=264.63ms
     iterations.....................: 142629  2298.960126/s
     success_rate...................: 100.00% ✓ 142629      ✗ 0     
     vus............................: 59      min=0         max=498 
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

     checks.........................: 100.00% ✓ 408249      ✗ 0     
     data_received..................: 12 GB   194 MB/s
     data_sent......................: 165 MB  2.7 MB/s
     http_req_blocked...............: avg=15.06µs  min=861ns   med=2.29µs   max=49.01ms  p(90)=4.57µs   p(95)=5.8µs    p(99.9)=1.83ms  
     http_req_connecting............: avg=11.96µs  min=0s      med=0s       max=48.96ms  p(90)=0s       p(95)=0s       p(99.9)=1.76ms  
     http_req_duration..............: avg=103.77ms min=1.63ms  med=98.94ms  max=306.31ms p(90)=197.56ms p(95)=210.9ms  p(99.9)=252.55ms
       { expected_response:true }...: avg=103.77ms min=1.63ms  med=98.94ms  max=306.31ms p(90)=197.56ms p(95)=210.9ms  p(99.9)=252.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 137083
     http_req_receiving.............: avg=4.98ms   min=55.08µs med=5.23ms   max=269.08ms p(90)=8.06ms   p(95)=10.2ms   p(99.9)=37ms    
     http_req_sending...............: avg=63.64µs  min=4.6µs   med=9.54µs   max=186.1ms  p(90)=24.76µs  p(95)=113.92µs p(99.9)=7.88ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=98.72ms  min=1.52ms  med=93.04ms  max=305.56ms p(90)=191.96ms p(95)=205.23ms p(99.9)=251.05ms
     http_reqs......................: 137083  2211.220555/s
     iteration_duration.............: avg=104.8ms  min=3.4ms   med=100.11ms max=354.1ms  p(90)=198.08ms p(95)=211.32ms p(99.9)=253.58ms
     iterations.....................: 136083  2195.090031/s
     success_rate...................: 100.00% ✓ 136083      ✗ 0     
     vus............................: 57      min=0         max=498 
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

     checks.........................: 100.00% ✓ 386733      ✗ 0     
     data_received..................: 11 GB   184 MB/s
     data_sent......................: 156 MB  2.5 MB/s
     http_req_blocked...............: avg=13.86µs  min=842ns   med=2.37µs   max=39.18ms  p(90)=4.76µs   p(95)=5.85µs   p(99.9)=1.44ms  
     http_req_connecting............: avg=10.65µs  min=0s      med=0s       max=39.04ms  p(90)=0s       p(95)=0s       p(99.9)=1.35ms  
     http_req_duration..............: avg=109.52ms min=1.51ms  med=104.97ms max=338.93ms p(90)=208.35ms p(95)=223.01ms p(99.9)=252.27ms
       { expected_response:true }...: avg=109.52ms min=1.51ms  med=104.97ms max=338.93ms p(90)=208.35ms p(95)=223.01ms p(99.9)=252.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 129911
     http_req_receiving.............: avg=5.7ms    min=51.77µs med=6.03ms   max=314.52ms p(90)=8.81ms   p(95)=10.8ms   p(99.9)=35.76ms 
     http_req_sending...............: avg=61.28µs  min=4.5µs   med=9.54µs   max=191.25ms p(90)=24.19µs  p(95)=107.87µs p(99.9)=7.4ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=103.75ms min=1.44ms  med=98.04ms  max=269.59ms p(90)=202.02ms p(95)=216.62ms p(99.9)=248.86ms
     http_reqs......................: 129911  2097.780923/s
     iteration_duration.............: avg=110.63ms min=4.61ms  med=106.22ms max=356.63ms p(90)=208.93ms p(95)=223.4ms  p(99.9)=253.51ms
     iterations.....................: 128911  2081.633091/s
     success_rate...................: 100.00% ✓ 128911      ✗ 0     
     vus............................: 55      min=0         max=499 
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

     checks.........................: 100.00% ✓ 350205      ✗ 0     
     data_received..................: 10 GB   166 MB/s
     data_sent......................: 141 MB  2.3 MB/s
     http_req_blocked...............: avg=12.37µs  min=1.06µs  med=2.96µs   max=35.81ms  p(90)=5.08µs   p(95)=6.24µs   p(99.9)=1.49ms  
     http_req_connecting............: avg=8.63µs   min=0s      med=0s       max=35.65ms  p(90)=0s       p(95)=0s       p(99.9)=1.39ms  
     http_req_duration..............: avg=120.9ms  min=1.78ms  med=116.2ms  max=336.8ms  p(90)=230.47ms p(95)=245.24ms p(99.9)=277.58ms
       { expected_response:true }...: avg=120.9ms  min=1.78ms  med=116.2ms  max=336.8ms  p(90)=230.47ms p(95)=245.24ms p(99.9)=277.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 117735
     http_req_receiving.............: avg=6.24ms   min=54.86µs med=6.65ms   max=105.8ms  p(90)=9.27ms   p(95)=11.49ms  p(99.9)=34.01ms 
     http_req_sending...............: avg=58.56µs  min=4.56µs  med=11.26µs  max=129.68ms p(90)=23.46µs  p(95)=111.15µs p(99.9)=7.8ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=114.6ms  min=1.66ms  med=108.89ms max=336.5ms  p(90)=223.11ms p(95)=237.7ms  p(99.9)=274.13ms
     http_reqs......................: 117735  1890.573382/s
     iteration_duration.............: avg=122.21ms min=6.53ms  med=117.76ms max=348.33ms p(90)=231.04ms p(95)=245.62ms p(99.9)=279.04ms
     iterations.....................: 116735  1874.515512/s
     success_rate...................: 100.00% ✓ 116735      ✗ 0     
     vus............................: 70      min=0         max=495 
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

     checks.........................: 100.00% ✓ 250530      ✗ 0    
     data_received..................: 7.4 GB  118 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=7.01µs   min=982ns   med=2.82µs   max=20.69ms  p(90)=5.13µs   p(95)=6.23µs   p(99.9)=717.36µs
     http_req_connecting............: avg=3.26µs   min=0s      med=0s       max=20.51ms  p(90)=0s       p(95)=0s       p(99.9)=589.28µs
     http_req_duration..............: avg=168.78ms min=2.41ms  med=136.31ms max=983.57ms p(90)=359.33ms p(95)=438.12ms p(99.9)=763.24ms
       { expected_response:true }...: avg=168.78ms min=2.41ms  med=136.31ms max=983.57ms p(90)=359.33ms p(95)=438.12ms p(99.9)=763.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 84510
     http_req_receiving.............: avg=88.36µs  min=28.51µs med=66.05µs  max=147.41ms p(90)=109.43µs p(95)=131.35µs p(99.9)=2.33ms  
     http_req_sending...............: avg=39.61µs  min=5.23µs  med=12.51µs  max=152.71ms p(90)=20.82µs  p(95)=25.42µs  p(99.9)=5ms     
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=168.65ms min=2.35ms  med=136.18ms max=983.46ms p(90)=359.18ms p(95)=437.91ms p(99.9)=763.15ms
     http_reqs......................: 84510   1344.145212/s
     iteration_duration.............: avg=171.05ms min=7.08ms  med=138.5ms  max=983.75ms p(90)=361.14ms p(95)=439.61ms p(99.9)=766.28ms
     iterations.....................: 83510   1328.24005/s
     success_rate...................: 100.00% ✓ 83510       ✗ 0    
     vus............................: 52      min=0         max=499
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

     checks.........................: 100.00% ✓ 233709      ✗ 0    
     data_received..................: 6.9 GB  110 MB/s
     data_sent......................: 95 MB   1.5 MB/s
     http_req_blocked...............: avg=6.97µs   min=992ns   med=2.9µs    max=22.96ms  p(90)=4.83µs   p(95)=5.87µs   p(99.9)=542.85µs
     http_req_connecting............: avg=3.4µs    min=0s      med=0s       max=22.92ms  p(90)=0s       p(95)=0s       p(99.9)=499.27µs
     http_req_duration..............: avg=180.76ms min=2.32ms  med=179.5ms  max=499.73ms p(90)=343.9ms  p(95)=369.21ms p(99.9)=443.9ms 
       { expected_response:true }...: avg=180.76ms min=2.32ms  med=179.5ms  max=499.73ms p(90)=343.9ms  p(95)=369.21ms p(99.9)=443.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 78903
     http_req_receiving.............: avg=89.82µs  min=28.98µs med=67.84µs  max=221.36ms p(90)=111.17µs p(95)=130.71µs p(99.9)=2ms     
     http_req_sending...............: avg=39.08µs  min=5.04µs  med=12.1µs   max=172.45ms p(90)=19.18µs  p(95)=23.36µs  p(99.9)=4ms     
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=180.63ms min=2.25ms  med=179.36ms max=499.55ms p(90)=343.75ms p(95)=369.03ms p(99.9)=443.78ms
     http_reqs......................: 78903   1255.447834/s
     iteration_duration.............: avg=183.34ms min=5.71ms  med=182.51ms max=499.94ms p(90)=344.71ms p(95)=369.96ms p(99.9)=444.39ms
     iterations.....................: 77903   1239.536553/s
     success_rate...................: 100.00% ✓ 77903       ✗ 0    
     vus............................: 5       min=0         max=500
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

     checks.........................: 100.00% ✓ 91116      ✗ 0    
     data_received..................: 2.7 GB  42 MB/s
     data_sent......................: 38 MB   578 kB/s
     http_req_blocked...............: avg=9.51µs   min=1.02µs  med=2.99µs   max=7.75ms   p(90)=4.84µs   p(95)=5.9µs    p(99.9)=1.77ms
     http_req_connecting............: avg=5.31µs   min=0s      med=0s       max=7.68ms   p(90)=0s       p(95)=0s       p(99.9)=1.68ms
     http_req_duration..............: avg=457.79ms min=4.22ms  med=421.31ms max=1.75s    p(90)=910.95ms p(95)=984.71ms p(99.9)=1.4s  
       { expected_response:true }...: avg=457.79ms min=4.22ms  med=421.31ms max=1.75s    p(90)=910.95ms p(95)=984.71ms p(99.9)=1.4s  
     http_req_failed................: 0.00%   ✓ 0          ✗ 31372
     http_req_receiving.............: avg=93.49µs  min=30.7µs  med=75.73µs  max=127.22ms p(90)=114.85µs p(95)=130.42µs p(99.9)=1.13ms
     http_req_sending...............: avg=26.53µs  min=5.05µs  med=14.49µs  max=71.98ms  p(90)=21.2µs   p(95)=23.96µs  p(99.9)=1.95ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=457.67ms min=4.15ms  med=421.23ms max=1.75s    p(90)=910.85ms p(95)=984.61ms p(99.9)=1.4s  
     http_reqs......................: 31372   481.197276/s
     iteration_duration.............: avg=473.07ms min=27.47ms med=441.93ms max=1.75s    p(90)=915.02ms p(95)=988.18ms p(99.9)=1.41s 
     iterations.....................: 30372   465.858845/s
     success_rate...................: 100.00% ✓ 30372      ✗ 0    
     vus............................: 65      min=0        max=497
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

     checks.........................: 100.00% ✓ 45348      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 19 MB   286 kB/s
     http_req_blocked...............: avg=17.57µs  min=1.4µs   med=3.83µs   max=21.93ms p(90)=5.81µs   p(95)=7.47µs  p(99.9)=2.3ms 
     http_req_connecting............: avg=10.84µs  min=0s      med=0s       max=21.86ms p(90)=0s       p(95)=0s      p(99.9)=2.26ms
     http_req_duration..............: avg=903.21ms min=5.8ms   med=810.14ms max=4.69s   p(90)=1.8s     p(95)=2.09s   p(99.9)=4.19s 
       { expected_response:true }...: avg=903.21ms min=5.8ms   med=810.14ms max=4.69s   p(90)=1.8s     p(95)=2.09s   p(99.9)=4.19s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16116
     http_req_receiving.............: avg=103.3µs  min=36.97µs med=93.83µs  max=25.24ms p(90)=131.59µs p(95)=148.8µs p(99.9)=1.47ms
     http_req_sending...............: avg=35.36µs  min=5.83µs  med=18.36µs  max=40.23ms p(90)=23.94µs  p(95)=27.82µs p(99.9)=3.64ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s      p(99.9)=0s    
     http_req_waiting...............: avg=903.07ms min=5.67ms  med=810.02ms max=4.69s   p(90)=1.8s     p(95)=2.09s   p(99.9)=4.19s 
     http_reqs......................: 16116   238.090357/s
     iteration_duration.............: avg=962.99ms min=42.51ms med=883.63ms max=4.7s    p(90)=1.82s    p(95)=2.12s   p(99.9)=4.21s 
     iterations.....................: 15116   223.316818/s
     success_rate...................: 100.00% ✓ 15116      ✗ 0    
     vus............................: 90      min=0        max=500
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

     checks.........................: 100.00% ✓ 44973      ✗ 0    
     data_received..................: 1.4 GB  20 MB/s
     data_sent......................: 19 MB   279 kB/s
     http_req_blocked...............: avg=15.57µs  min=1.16µs  med=3.77µs   max=9.07ms   p(90)=5.69µs   p(95)=7.39µs   p(99.9)=2.28ms
     http_req_connecting............: avg=10.03µs  min=0s      med=0s       max=9.01ms   p(90)=0s       p(95)=0s       p(99.9)=2.25ms
     http_req_duration..............: avg=908.82ms min=7.89ms  med=828.49ms max=3.54s    p(90)=1.83s    p(95)=1.99s    p(99.9)=2.89s 
       { expected_response:true }...: avg=908.82ms min=7.89ms  med=828.49ms max=3.54s    p(90)=1.83s    p(95)=1.99s    p(99.9)=2.89s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 15991
     http_req_receiving.............: avg=114.86µs min=37.68µs med=93.01µs  max=196.15ms p(90)=133.21µs p(95)=149.69µs p(99.9)=1.07ms
     http_req_sending...............: avg=40.35µs  min=5.58µs  med=18.06µs  max=122.36ms p(90)=23.91µs  p(95)=27.92µs  p(99.9)=4.58ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=908.66ms min=7.77ms  med=828.36ms max=3.54s    p(90)=1.83s    p(95)=1.99s    p(99.9)=2.88s 
     http_reqs......................: 15991   232.092235/s
     iteration_duration.............: avg=969.48ms min=40.9ms  med=909.94ms max=3.54s    p(90)=1.85s    p(95)=2s       p(99.9)=2.9s  
     iterations.....................: 14991   217.578306/s
     success_rate...................: 100.00% ✓ 14991      ✗ 0    
     vus............................: 21      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

