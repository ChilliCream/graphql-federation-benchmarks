## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.16 | 4,867 | 4,884 | 4,859 | 0.2% | 410 MB | 86.2 KB |  |
| fusion-fed-net-11 | 16.7.6 | 4,809 | 4,818 | 4,802 | 0.1% | 414 MB | 88.2 KB |  |
| fusion-net-11 | 16.7.6 | 4,800 | 4,810 | 4,676 | 1.2% | 407 MB | 86.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.16 | 4,650 | 4,671 | 4,638 | 0.3% | 151 MB | 33.2 KB |  |
| feddi-gateway | 2026-11-03-0517 | 4,631 | 4,639 | 4,615 | 0.2% | 2,311 MB | 511.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.16 | 4,587 | 4,598 | 4,568 | 0.2% | 156 MB | 34.8 KB |  |
| fusion-aot-11 | 16.7.6 | 4,585 | 4,612 | 4,573 | 0.3% | 158 MB | 35.3 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.16 | 4,568 | 4,594 | 4,546 | 0.4% | 417 MB | 93.6 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 4,559 | 4,690 | 4,556 | 1.3% | 168 MB | 37.8 KB |  |
| hive-router | v0.3.16 | 3,922 | 3,979 | 3,912 | 0.8% | 195 MB | 50.9 KB |  |
| caliban | 3.2.1 | 1,393 | 1,402 | 1,386 | 0.5% | 11,183 MB | 8,220.9 KB |  |
| cosmo | 0.373.0 | 1,291 | 1,295 | 1,290 | 0.2% | 610 MB | 483.5 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 554 | 555 | 552 | 0.2% | 3,017 MB | 5,576.6 KB |  |
| hive-gateway | 2.15.10 | 278 | 278 | 277 | 0.2% | 3,583 MB | 13,197.5 KB |  |
| apollo-gateway | 2.14.4 | 236 | 237 | 235 | 0.4% | 2,438 MB | 10,578.6 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (6952 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (4433 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (157060 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 886482      ✗ 0     
     data_received..................: 26 GB   426 MB/s
     data_sent......................: 356 MB  5.8 MB/s
     http_req_blocked...............: avg=67.8µs   min=792ns    med=2.11µs  max=130.26ms p(90)=3.68µs   p(95)=4.75µs   p(99.9)=25.75ms 
     http_req_connecting............: avg=64.52µs  min=0s       med=0s      max=130.16ms p(90)=0s       p(95)=0s       p(99.9)=25.36ms 
     http_req_duration..............: avg=45.9ms   min=722.49µs med=38.81ms max=286.69ms p(90)=95.98ms  p(95)=119.26ms p(99.9)=174.62ms
       { expected_response:true }...: avg=45.9ms   min=722.49µs med=38.81ms max=286.69ms p(90)=95.98ms  p(95)=119.26ms p(99.9)=174.62ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 296494
     http_req_receiving.............: avg=347.12µs min=21.4µs   med=52.42µs max=131.05ms p(90)=205.03µs p(95)=349.09µs p(99.9)=47.06ms 
     http_req_sending...............: avg=153.7µs  min=3.86µs   med=8.61µs  max=113.47ms p(90)=16.09µs  p(95)=110.85µs p(99.9)=27.58ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.4ms   min=687.49µs med=38.47ms max=286.18ms p(90)=94.87ms  p(95)=117.95ms p(99.9)=169.45ms
     http_reqs......................: 296494  4867.920355/s
     iteration_duration.............: avg=48.2ms   min=1.22ms   med=39.83ms max=329.12ms p(90)=102.77ms p(95)=127.75ms p(99.9)=197.14ms
     iterations.....................: 295494  4851.502079/s
     success_rate...................: 100.00% ✓ 295494      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 876249      ✗ 0     
     data_received..................: 26 GB   421 MB/s
     data_sent......................: 352 MB  5.8 MB/s
     http_req_blocked...............: avg=70.01µs  min=812ns    med=2.1µs   max=171.38ms p(90)=3.74µs   p(95)=4.89µs   p(99.9)=24.86ms 
     http_req_connecting............: avg=66.11µs  min=0s       med=0s      max=155.47ms p(90)=0s       p(95)=0s       p(99.9)=24.72ms 
     http_req_duration..............: avg=46.66ms  min=758.66µs med=39.72ms max=296.85ms p(90)=97.15ms  p(95)=120.61ms p(99.9)=174.66ms
       { expected_response:true }...: avg=46.66ms  min=758.66µs med=39.72ms max=296.85ms p(90)=97.15ms  p(95)=120.61ms p(99.9)=174.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 293083
     http_req_receiving.............: avg=342.85µs min=25.49µs  med=52.56µs max=127.24ms p(90)=204.52µs p(95)=357.08µs p(99.9)=48.19ms 
     http_req_sending...............: avg=157.45µs min=3.84µs   med=8.63µs  max=160.02ms p(90)=16.45µs  p(95)=114.16µs p(99.9)=28.75ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.16ms  min=712.55µs med=39.38ms max=296.71ms p(90)=95.93ms  p(95)=119.37ms p(99.9)=169.81ms
     http_reqs......................: 293083  4809.643727/s
     iteration_duration.............: avg=48.76ms  min=1.28ms   med=40.54ms max=372.11ms p(90)=102.68ms p(95)=127.57ms p(99.9)=204.73ms
     iterations.....................: 292083  4793.233209/s
     success_rate...................: 100.00% ✓ 292083      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 874794      ✗ 0     
     data_received..................: 26 GB   420 MB/s
     data_sent......................: 352 MB  5.8 MB/s
     http_req_blocked...............: avg=70.67µs  min=831ns    med=2.09µs  max=153.6ms  p(90)=3.66µs   p(95)=4.75µs   p(99.9)=26.61ms 
     http_req_connecting............: avg=66.91µs  min=0s       med=0s      max=150.75ms p(90)=0s       p(95)=0s       p(99.9)=26.2ms  
     http_req_duration..............: avg=46.86ms  min=749.48µs med=39.63ms max=247.84ms p(90)=97.94ms  p(95)=122.14ms p(99.9)=175.41ms
       { expected_response:true }...: avg=46.86ms  min=749.48µs med=39.63ms max=247.84ms p(90)=97.94ms  p(95)=122.14ms p(99.9)=175.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 292598
     http_req_receiving.............: avg=345.99µs min=25.16µs  med=52.36µs max=111.82ms p(90)=208.06µs p(95)=357.09µs p(99.9)=46.59ms 
     http_req_sending...............: avg=161.21µs min=4.02µs   med=8.57µs  max=148.94ms p(90)=15.85µs  p(95)=113.19µs p(99.9)=29.19ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.35ms  min=701.35µs med=39.28ms max=247.79ms p(90)=96.61ms  p(95)=120.75ms p(99.9)=170.9ms 
     http_reqs......................: 292598  4800.994003/s
     iteration_duration.............: avg=48.85ms  min=1.18ms   med=40.62ms max=324.78ms p(90)=103.12ms p(95)=128.92ms p(99.9)=200.13ms
     iterations.....................: 291598  4784.585846/s
     success_rate...................: 100.00% ✓ 291598      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 847668      ✗ 0     
     data_received..................: 25 GB   407 MB/s
     data_sent......................: 341 MB  5.6 MB/s
     http_req_blocked...............: avg=71.43µs  min=962ns    med=2.56µs  max=143.69ms p(90)=4.18µs   p(95)=5.41µs   p(99.9)=26.84ms 
     http_req_connecting............: avg=67.18µs  min=0s       med=0s      max=143.39ms p(90)=0s       p(95)=0s       p(99.9)=26.56ms 
     http_req_duration..............: avg=48.59ms  min=788.13µs med=40.3ms  max=304.34ms p(90)=104.17ms p(95)=130.12ms p(99.9)=188.74ms
       { expected_response:true }...: avg=48.59ms  min=788.13µs med=40.3ms  max=304.34ms p(90)=104.17ms p(95)=130.12ms p(99.9)=188.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 283556
     http_req_receiving.............: avg=356.23µs min=25.71µs  med=53µs    max=123.57ms p(90)=221.86µs p(95)=379.98µs p(99.9)=49.44ms 
     http_req_sending...............: avg=160.86µs min=4.15µs   med=8.97µs  max=243.74ms p(90)=17.79µs  p(95)=123.51µs p(99.9)=29.69ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.07ms  min=750.5µs  med=39.96ms max=303.57ms p(90)=102.95ms p(95)=128.71ms p(99.9)=182.78ms
     http_reqs......................: 283556  4650.506232/s
     iteration_duration.............: avg=50.41ms  min=1.22ms   med=41.37ms max=326.14ms p(90)=108.58ms p(95)=135.59ms p(99.9)=208.14ms
     iterations.....................: 282556  4634.105569/s
     success_rate...................: 100.00% ✓ 282556      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-03-0517)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 842853      ✗ 0     
     data_received..................: 25 GB   405 MB/s
     data_sent......................: 339 MB  5.6 MB/s
     http_req_blocked...............: avg=57.9µs   min=801ns    med=2.1µs   max=131.31ms p(90)=3.77µs   p(95)=4.86µs   p(99.9)=19.83ms 
     http_req_connecting............: avg=54.19µs  min=0s       med=0s      max=113.18ms p(90)=0s       p(95)=0s       p(99.9)=19.66ms 
     http_req_duration..............: avg=49.22ms  min=650.62µs med=41.45ms max=321.68ms p(90)=104.79ms p(95)=130.35ms p(99.9)=191.81ms
       { expected_response:true }...: avg=49.22ms  min=650.62µs med=41.45ms max=321.68ms p(90)=104.79ms p(95)=130.35ms p(99.9)=191.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281951
     http_req_receiving.............: avg=332.62µs min=21.59µs  med=51.89µs max=104.04ms p(90)=210.62µs p(95)=375.59µs p(99.9)=47.94ms 
     http_req_sending...............: avg=140.39µs min=4.05µs   med=8.64µs  max=152.07ms p(90)=16.98µs  p(95)=120.06µs p(99.9)=25.97ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.74ms  min=614.34µs med=41.16ms max=321.47ms p(90)=103.68ms p(95)=129.11ms p(99.9)=183.13ms
     http_reqs......................: 281951  4631.852562/s
     iteration_duration.............: avg=50.7ms   min=1.17ms   med=42.11ms max=336.72ms p(90)=107.91ms p(95)=134.98ms p(99.9)=207.57ms
     iterations.....................: 280951  4615.424698/s
     success_rate...................: 100.00% ✓ 280951      ✗ 0     
     vus............................: 51      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 836274      ✗ 0     
     data_received..................: 25 GB   401 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=67.67µs  min=981ns    med=2.61µs  max=127.28ms p(90)=4.18µs   p(95)=5.31µs   p(99.9)=25.36ms 
     http_req_connecting............: avg=63.81µs  min=0s       med=0s      max=127.24ms p(90)=0s       p(95)=0s       p(99.9)=24.91ms 
     http_req_duration..............: avg=49.26ms  min=787.92µs med=41.05ms max=258.63ms p(90)=105.72ms p(95)=132.89ms p(99.9)=185.14ms
       { expected_response:true }...: avg=49.26ms  min=787.92µs med=41.05ms max=258.63ms p(90)=105.72ms p(95)=132.89ms p(99.9)=185.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279758
     http_req_receiving.............: avg=332.07µs min=26.46µs  med=53.02µs max=239.14ms p(90)=223.42µs p(95)=391.13µs p(99.9)=45.51ms 
     http_req_sending...............: avg=154.24µs min=4.32µs   med=9.18µs  max=134.22ms p(90)=17.91µs  p(95)=126.66µs p(99.9)=26.71ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.77ms  min=748.43µs med=40.72ms max=250.53ms p(90)=104.59ms p(95)=131.63ms p(99.9)=179.61ms
     http_reqs......................: 279758  4587.181536/s
     iteration_duration.............: avg=51.09ms  min=1.26ms   med=41.99ms max=388.6ms  p(90)=110.1ms  p(95)=138.78ms p(99.9)=212.62ms
     iterations.....................: 278758  4570.784573/s
     success_rate...................: 100.00% ✓ 278758      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 835665      ✗ 0     
     data_received..................: 25 GB   401 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=64.47µs  min=942ns    med=2.58µs  max=140.22ms p(90)=4.11µs   p(95)=5.23µs   p(99.9)=22.66ms 
     http_req_connecting............: avg=60.42µs  min=0s       med=0s      max=139.99ms p(90)=0s       p(95)=0s       p(99.9)=21.77ms 
     http_req_duration..............: avg=49.08ms  min=783.43µs med=40.89ms max=322.7ms  p(90)=105.65ms p(95)=131.78ms p(99.9)=189.68ms
       { expected_response:true }...: avg=49.08ms  min=783.43µs med=40.89ms max=322.7ms  p(90)=105.65ms p(95)=131.78ms p(99.9)=189.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279555
     http_req_receiving.............: avg=345.47µs min=26.26µs  med=53.09µs max=139.49ms p(90)=220.01µs p(95)=387.46µs p(99.9)=50.7ms  
     http_req_sending...............: avg=155.95µs min=3.99µs   med=8.98µs  max=276.03ms p(90)=17.38µs  p(95)=125.01µs p(99.9)=27.46ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.58ms  min=744.15µs med=40.59ms max=322.15ms p(90)=104.46ms p(95)=130.63ms p(99.9)=181.02ms
     http_reqs......................: 279555  4585.616154/s
     iteration_duration.............: avg=51.14ms  min=1.22ms   med=41.97ms max=332.93ms p(90)=110.17ms p(95)=138.01ms p(99.9)=231.56ms
     iterations.....................: 278555  4569.212884/s
     success_rate...................: 100.00% ✓ 278555      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 832377      ✗ 0     
     data_received..................: 24 GB   400 MB/s
     data_sent......................: 335 MB  5.5 MB/s
     http_req_blocked...............: avg=75.82µs  min=932ns    med=2.69µs  max=139.05ms p(90)=4.27µs   p(95)=5.42µs   p(99.9)=28.3ms  
     http_req_connecting............: avg=70.94µs  min=0s       med=0s      max=138.97ms p(90)=0s       p(95)=0s       p(99.9)=27.44ms 
     http_req_duration..............: avg=49.19ms  min=758.34µs med=41.17ms max=263.36ms p(90)=104.27ms p(95)=129.81ms p(99.9)=187.21ms
       { expected_response:true }...: avg=49.19ms  min=758.34µs med=41.17ms max=263.36ms p(90)=104.27ms p(95)=129.81ms p(99.9)=187.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 278459
     http_req_receiving.............: avg=380.14µs min=25.03µs  med=55.98µs max=134.54ms p(90)=226.01µs p(95)=387.64µs p(99.9)=53.12ms 
     http_req_sending...............: avg=167.31µs min=4µs      med=9.41µs  max=157.38ms p(90)=17.74µs  p(95)=124.88µs p(99.9)=30.57ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.65ms  min=711.19µs med=40.8ms  max=262.02ms p(90)=103.13ms p(95)=128.4ms  p(99.9)=181.29ms
     http_reqs......................: 278459  4568.727848/s
     iteration_duration.............: avg=51.34ms  min=1.3ms    med=42.17ms max=362.14ms p(90)=109.69ms p(95)=136.37ms p(99.9)=214.96ms
     iterations.....................: 277459  4552.320665/s
     success_rate...................: 100.00% ✓ 277459      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 831054      ✗ 0     
     data_received..................: 24 GB   399 MB/s
     data_sent......................: 334 MB  5.5 MB/s
     http_req_blocked...............: avg=73.09µs  min=1.02µs   med=2.67µs  max=155.46ms p(90)=4.23µs   p(95)=5.35µs   p(99.9)=28.62ms 
     http_req_connecting............: avg=68.99µs  min=0s       med=0s      max=155.22ms p(90)=0s       p(95)=0s       p(99.9)=27.96ms 
     http_req_duration..............: avg=49.61ms  min=810.48µs med=41.59ms max=281.27ms p(90)=105.69ms p(95)=132.59ms p(99.9)=187.25ms
       { expected_response:true }...: avg=49.61ms  min=810.48µs med=41.59ms max=281.27ms p(90)=105.69ms p(95)=132.59ms p(99.9)=187.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 278018
     http_req_receiving.............: avg=356.49µs min=22.86µs  med=54.49µs max=134.74ms p(90)=224.65µs p(95)=388.23µs p(99.9)=48.85ms 
     http_req_sending...............: avg=161.67µs min=4.07µs   med=9.32µs  max=256.16ms p(90)=17.41µs  p(95)=125.12µs p(99.9)=29.03ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.09ms  min=757.08µs med=41.27ms max=260.14ms p(90)=104.58ms p(95)=131.13ms p(99.9)=181.98ms
     http_reqs......................: 278018  4559.01776/s
     iteration_duration.............: avg=51.42ms  min=1.24ms   med=42.49ms max=372.91ms p(90)=109.88ms p(95)=138.14ms p(99.9)=214.35ms
     iterations.....................: 277018  4542.619478/s
     success_rate...................: 100.00% ✓ 277018      ✗ 0     
     vus............................: 57      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.16)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 715680      ✗ 0     
     data_received..................: 21 GB   343 MB/s
     data_sent......................: 288 MB  4.7 MB/s
     http_req_blocked...............: avg=52.02µs  min=861ns    med=2.62µs  max=109.91ms p(90)=4.38µs   p(95)=5.68µs   p(99.9)=11.7ms  
     http_req_connecting............: avg=48.22µs  min=0s       med=0s      max=109.79ms p(90)=0s       p(95)=0s       p(99.9)=10.77ms 
     http_req_duration..............: avg=58.3ms   min=880.95µs med=49.35ms max=332.22ms p(90)=124.01ms p(95)=152.37ms p(99.9)=214.46ms
       { expected_response:true }...: avg=58.3ms   min=880.95µs med=49.35ms max=332.22ms p(90)=124.01ms p(95)=152.37ms p(99.9)=214.46ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 239560
     http_req_receiving.............: avg=288.54µs min=22.68µs  med=54.5µs  max=125.63ms p(90)=225.91µs p(95)=404.85µs p(99.9)=44.82ms 
     http_req_sending...............: avg=127.71µs min=4.32µs   med=9.73µs  max=161.37ms p(90)=19.75µs  p(95)=135.9µs  p(99.9)=23.3ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=57.88ms  min=827.64µs med=49.07ms max=331.97ms p(90)=123.15ms p(95)=151.14ms p(99.9)=209.23ms
     http_reqs......................: 239560  3922.394643/s
     iteration_duration.............: avg=59.72ms  min=1.48ms   med=50.41ms max=351.85ms p(90)=126.55ms p(95)=155.72ms p(99.9)=237.78ms
     iterations.....................: 238560  3906.021314/s
     success_rate...................: 100.00% ✓ 238560      ✗ 0     
     vus............................: 60      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 257724      ✗ 0    
     data_received..................: 7.6 GB  122 MB/s
     data_sent......................: 104 MB  1.7 MB/s
     http_req_blocked...............: avg=5.98µs   min=1.15µs  med=2.92µs   max=9.76ms   p(90)=4.61µs   p(95)=5.57µs   p(99.9)=386.23µs
     http_req_connecting............: avg=2.39µs   min=0s      med=0s       max=9.69ms   p(90)=0s       p(95)=0s       p(99.9)=324.24µs
     http_req_duration..............: avg=164.13ms min=1.93ms  med=137.53ms max=947.57ms p(90)=338.26ms p(95)=400.46ms p(99.9)=698.64ms
       { expected_response:true }...: avg=164.13ms min=1.93ms  med=137.53ms max=947.57ms p(90)=338.26ms p(95)=400.46ms p(99.9)=698.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 86908
     http_req_receiving.............: avg=77.35µs  min=27.93µs med=61.3µs   max=84.12ms  p(90)=96.56µs  p(95)=111.72µs p(99.9)=2.06ms  
     http_req_sending...............: avg=34.51µs  min=5.17µs  med=12.3µs   max=165.46ms p(90)=18.02µs  p(95)=21.31µs  p(99.9)=3.7ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=164.02ms min=1.88ms  med=137.42ms max=947.5ms  p(90)=338.13ms p(95)=400.36ms p(99.9)=698.57ms
     http_reqs......................: 86908   1393.106176/s
     iteration_duration.............: avg=166.29ms min=5.48ms  med=140.1ms  max=947.74ms p(90)=339.65ms p(95)=401.66ms p(99.9)=699.11ms
     iterations.....................: 85908   1377.076511/s
     success_rate...................: 100.00% ✓ 85908       ✗ 0    
     vus............................: 75      min=0         max=494
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.373.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 238818      ✗ 0    
     data_received..................: 7.1 GB  113 MB/s
     data_sent......................: 97 MB   1.6 MB/s
     http_req_blocked...............: avg=5.28µs   min=1µs     med=2.63µs   max=5.29ms   p(90)=4.19µs   p(95)=5.05µs   p(99.9)=271.42µs
     http_req_connecting............: avg=2.01µs   min=0s      med=0s       max=5.23ms   p(90)=0s       p(95)=0s       p(99.9)=179.18µs
     http_req_duration..............: avg=176.97ms min=1.98ms  med=174.65ms max=543.9ms  p(90)=335.35ms p(95)=360.13ms p(99.9)=447ms   
       { expected_response:true }...: avg=176.97ms min=1.98ms  med=174.65ms max=543.9ms  p(90)=335.35ms p(95)=360.13ms p(99.9)=447ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 80606
     http_req_receiving.............: avg=79.04µs  min=26.18µs med=62.43µs  max=219.02ms p(90)=99.15µs  p(95)=114.35µs p(99.9)=1.22ms  
     http_req_sending...............: avg=28.48µs  min=4.63µs  med=11.36µs  max=103.22ms p(90)=17.21µs  p(95)=20.44µs  p(99.9)=3.14ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=176.87ms min=1.92ms  med=174.52ms max=543.77ms p(90)=335.24ms p(95)=360.02ms p(99.9)=446.72ms
     http_reqs......................: 80606   1291.004336/s
     iteration_duration.............: avg=179.44ms min=4.15ms  med=177.38ms max=544.19ms p(90)=336.16ms p(95)=360.75ms p(99.9)=448.11ms
     iterations.....................: 79606   1274.988105/s
     success_rate...................: 100.00% ✓ 79606       ✗ 0    
     vus............................: 77      min=0         max=493
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 103857     ✗ 0    
     data_received..................: 3.1 GB  49 MB/s
     data_sent......................: 43 MB   666 kB/s
     http_req_blocked...............: avg=7.47µs   min=1.06µs  med=2.45µs   max=3.88ms   p(90)=4.12µs   p(95)=5.02µs   p(99.9)=1.19ms
     http_req_connecting............: avg=4.06µs   min=0s      med=0s       max=3.84ms   p(90)=0s       p(95)=0s       p(99.9)=1.17ms
     http_req_duration..............: avg=402.7ms  min=3.43ms  med=370.77ms max=1.84s    p(90)=800.85ms p(95)=872.28ms p(99.9)=1.31s 
       { expected_response:true }...: avg=402.7ms  min=3.43ms  med=370.77ms max=1.84s    p(90)=800.85ms p(95)=872.28ms p(99.9)=1.31s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 35619
     http_req_receiving.............: avg=78.39µs  min=27.98µs med=67.53µs  max=46.93ms  p(90)=104.87µs p(95)=119.28µs p(99.9)=1ms   
     http_req_sending...............: avg=29.67µs  min=4.9µs   med=12.76µs  max=115.65ms p(90)=19.38µs  p(95)=21.84µs  p(99.9)=2.37ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=402.59ms min=3.38ms  med=370.66ms max=1.84s    p(90)=800.77ms p(95)=872.16ms p(99.9)=1.31s 
     http_reqs......................: 35619   554.577755/s
     iteration_duration.............: avg=414.55ms min=28.19ms med=386ms    max=1.84s    p(90)=805.02ms p(95)=875.38ms p(99.9)=1.32s 
     iterations.....................: 34619   539.008037/s
     success_rate...................: 100.00% ✓ 34619      ✗ 0    
     vus............................: 66      min=0        max=496
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 52752      ✗ 0    
     data_received..................: 1.6 GB  24 MB/s
     data_sent......................: 22 MB   334 kB/s
     http_req_blocked...............: avg=13.62µs  min=1.5µs   med=3.73µs   max=11.79ms p(90)=5.57µs  p(95)=7.02µs  p(99.9)=1.96ms
     http_req_connecting............: avg=8.32µs   min=0s      med=0s       max=11.72ms p(90)=0s      p(95)=0s      p(99.9)=1.94ms
     http_req_duration..............: avg=779.21ms min=5.18ms  med=705.51ms max=3.5s    p(90)=1.55s   p(95)=1.84s   p(99.9)=2.92s 
       { expected_response:true }...: avg=779.21ms min=5.18ms  med=705.51ms max=3.5s    p(90)=1.55s   p(95)=1.84s   p(99.9)=2.92s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 18584
     http_req_receiving.............: avg=99.6µs   min=38.46µs med=90.87µs  max=10.04ms p(90)=129.3µs p(95)=146µs   p(99.9)=1.24ms
     http_req_sending...............: avg=27.94µs  min=6.33µs  med=18.02µs  max=25.14ms p(90)=23.47µs p(95)=26.78µs p(99.9)=2.88ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s      p(95)=0s      p(99.9)=0s    
     http_req_waiting...............: avg=779.08ms min=5.1ms   med=705.32ms max=3.5s    p(90)=1.55s   p(95)=1.84s   p(99.9)=2.92s 
     http_reqs......................: 18584   278.381125/s
     iteration_duration.............: avg=823.62ms min=30.35ms med=752.43ms max=3.51s   p(90)=1.57s   p(95)=1.85s   p(99.9)=2.93s 
     iterations.....................: 17584   263.401512/s
     success_rate...................: 100.00% ✓ 17584      ✗ 0    
     vus............................: 95      min=0        max=500
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

     checks.........................: 100.00% ✓ 45630      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   283 kB/s
     http_req_blocked...............: avg=14.11µs  min=1.15µs  med=3.05µs   max=5.7ms   p(90)=4.65µs   p(95)=6.07µs   p(99.9)=2.21ms  
     http_req_connecting............: avg=9.38µs   min=0s      med=0s       max=5.64ms  p(90)=0s       p(95)=0s       p(99.9)=2.1ms   
     http_req_duration..............: avg=896.43ms min=7.76ms  med=812.23ms max=3.21s   p(90)=1.81s    p(95)=1.94s    p(99.9)=2.72s   
       { expected_response:true }...: avg=896.43ms min=7.76ms  med=812.23ms max=3.21s   p(90)=1.81s    p(95)=1.94s    p(99.9)=2.72s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16210
     http_req_receiving.............: avg=90.65µs  min=31.2µs  med=83.04µs  max=42.35ms p(90)=120.45µs p(95)=135.11µs p(99.9)=799.17µs
     http_req_sending...............: avg=39.97µs  min=5.2µs   med=15.74µs  max=55.46ms p(90)=20.58µs  p(95)=24.06µs  p(99.9)=5.36ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=896.3ms  min=7.68ms  med=812.14ms max=3.21s   p(90)=1.81s    p(95)=1.94s    p(99.9)=2.72s   
     http_reqs......................: 16210   236.11365/s
     iteration_duration.............: avg=955.38ms min=35.78ms med=886.02ms max=3.22s   p(90)=1.83s    p(95)=1.95s    p(99.9)=2.73s   
     iterations.....................: 15210   221.547725/s
     success_rate...................: 100.00% ✓ 15210      ✗ 0    
     vus............................: 85      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

