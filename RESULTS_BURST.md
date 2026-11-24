## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.20 | 4,856 | 4,869 | 4,848 | 0.2% | 399 MB | 84.2 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.20 | 4,808 | 4,823 | 4,682 | 1.3% | 160 MB | 34.2 KB |  |
| fusion-net-11 | 16.7.7 | 4,719 | 4,819 | 4,688 | 1.3% | 388 MB | 84.3 KB |  |
| fusion-fed-net-11 | 16.7.7 | 4,710 | 4,735 | 4,705 | 0.3% | 413 MB | 89.8 KB |  |
| fusion-aot-11 | 16.7.7 | 4,672 | 4,681 | 4,657 | 0.2% | 149 MB | 32.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.20 | 4,658 | 4,676 | 4,644 | 0.3% | 408 MB | 89.7 KB |  |
| feddi-gateway | 2026-11-03-0517 | 4,630 | 4,651 | 4,523 | 1.2% | 2,296 MB | 507.8 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.20 | 4,594 | 4,615 | 4,582 | 0.3% | 150 MB | 33.4 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 4,530 | 4,626 | 4,512 | 1.0% | 150 MB | 33.9 KB |  |
| hive-router-nightly | v0.3.19-nightly.e7e70652 | 4,039 | 4,059 | 4,020 | 0.4% | 181 MB | 45.8 KB |  |
| hive-router | v0.3.17 | 3,969 | 3,973 | 3,956 | 0.2% | 196 MB | 50.6 KB |  |
| caliban | 3.2.1 | 1,364 | 1,367 | 1,362 | 0.1% | 11,364 MB | 8,531.0 KB |  |
| cosmo | 0.373.0 | 1,355 | 1,364 | 1,348 | 0.4% | 582 MB | 439.6 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 561 | 563 | 555 | 0.6% | 3,025 MB | 5,520.7 KB |  |
| hive-gateway | 2.15.10 | 269 | 271 | 265 | 0.8% | 3,669 MB | 13,967.4 KB |  |
| apollo-gateway | 2.14.4 | 239 | 241 | 238 | 0.5% | 2,467 MB | 10,571.4 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (9907 across 5/5 runs) |
| apollo-router-nightly | v3.0.0-preview.0-nightly.fbceee06 | — | — | — | — | — | — | non-compatible response (4147 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (2596 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (170981 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 884412      ✗ 0     
     data_received..................: 26 GB   425 MB/s
     data_sent......................: 355 MB  5.8 MB/s
     http_req_blocked...............: avg=68.51µs  min=801ns    med=2.06µs  max=142.09ms p(90)=3.61µs   p(95)=4.7µs    p(99.9)=26.99ms 
     http_req_connecting............: avg=65.44µs  min=0s       med=0s      max=141.89ms p(90)=0s       p(95)=0s       p(99.9)=26.71ms 
     http_req_duration..............: avg=46.14ms  min=710.94µs med=39.58ms max=268.03ms p(90)=95.92ms  p(95)=118.64ms p(99.9)=172.39ms
       { expected_response:true }...: avg=46.14ms  min=710.94µs med=39.58ms max=268.03ms p(90)=95.92ms  p(95)=118.64ms p(99.9)=172.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 295804
     http_req_receiving.............: avg=343.74µs min=25.63µs  med=52.75µs max=144.81ms p(90)=201.38µs p(95)=348.27µs p(99.9)=47.11ms 
     http_req_sending...............: avg=152.57µs min=3.94µs   med=8.52µs  max=158.85ms p(90)=15.92µs  p(95)=111.39µs p(99.9)=28.43ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.64ms  min=671.99µs med=39.24ms max=240.64ms p(90)=94.84ms  p(95)=117.3ms  p(99.9)=167.58ms
     http_reqs......................: 295804  4856.466497/s
     iteration_duration.............: avg=48.31ms  min=1.18ms   med=40.42ms max=331.75ms p(90)=101.84ms p(95)=126.91ms p(99.9)=215.24ms
     iterations.....................: 294804  4840.048644/s
     success_rate...................: 100.00% ✓ 294804      ✗ 0     
     vus............................: 52      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 876123      ✗ 0     
     data_received..................: 26 GB   421 MB/s
     data_sent......................: 352 MB  5.8 MB/s
     http_req_blocked...............: avg=59.08µs  min=801ns    med=1.99µs  max=122.49ms p(90)=3.59µs   p(95)=4.72µs   p(99.9)=20.83ms 
     http_req_connecting............: avg=56.03µs  min=0s       med=0s      max=122.42ms p(90)=0s       p(95)=0s       p(99.9)=20.69ms 
     http_req_duration..............: avg=47.02ms  min=769.51µs med=39.5ms  max=296.74ms p(90)=100.14ms p(95)=124.6ms  p(99.9)=182.27ms
       { expected_response:true }...: avg=47.02ms  min=769.51µs med=39.5ms  max=296.74ms p(90)=100.14ms p(95)=124.6ms  p(99.9)=182.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 293041
     http_req_receiving.............: avg=347.98µs min=24.44µs  med=51.06µs max=137.66ms p(90)=207.52µs p(95)=365.18µs p(99.9)=49.41ms 
     http_req_sending...............: avg=147.91µs min=3.86µs   med=8.3µs   max=250.51ms p(90)=16.29µs  p(95)=116.26µs p(99.9)=25.92ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.52ms  min=731.2µs  med=39.22ms max=296.31ms p(90)=98.87ms  p(95)=123.18ms p(99.9)=175.18ms
     http_reqs......................: 293041  4808.653342/s
     iteration_duration.............: avg=48.77ms  min=1.19ms   med=40.23ms max=416.94ms p(90)=104.41ms p(95)=130.42ms p(99.9)=209.26ms
     iterations.....................: 292041  4792.243852/s
     success_rate...................: 100.00% ✓ 292041      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 859329      ✗ 0     
     data_received..................: 25 GB   413 MB/s
     data_sent......................: 345 MB  5.7 MB/s
     http_req_blocked...............: avg=70.25µs  min=842ns    med=2.54µs  max=159.91ms p(90)=4.08µs   p(95)=5.2µs    p(99.9)=25.77ms 
     http_req_connecting............: avg=66.56µs  min=0s       med=0s      max=139.11ms p(90)=0s       p(95)=0s       p(99.9)=25.7ms  
     http_req_duration..............: avg=47.38ms  min=725.51µs med=39.44ms max=294.86ms p(90)=100.21ms p(95)=125.47ms p(99.9)=183.3ms 
       { expected_response:true }...: avg=47.38ms  min=725.51µs med=39.44ms max=294.86ms p(90)=100.21ms p(95)=125.47ms p(99.9)=183.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 287443
     http_req_receiving.............: avg=359.65µs min=24.64µs  med=52.97µs max=156.91ms p(90)=214.64µs p(95)=372.71µs p(99.9)=48.25ms 
     http_req_sending...............: avg=155.54µs min=4.02µs   med=9.04µs  max=105.53ms p(90)=16.83µs  p(95)=119.94µs p(99.9)=27.86ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.87ms  min=686.02µs med=39.09ms max=293.82ms p(90)=99.02ms  p(95)=124.23ms p(99.9)=177.72ms
     http_reqs......................: 287443  4719.636345/s
     iteration_duration.............: avg=49.73ms  min=1.19ms   med=40.49ms max=342.86ms p(90)=106.18ms p(95)=133.44ms p(99.9)=214.78ms
     iterations.....................: 286443  4703.216963/s
     success_rate...................: 100.00% ✓ 286443      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 858084      ✗ 0     
     data_received..................: 25 GB   412 MB/s
     data_sent......................: 345 MB  5.7 MB/s
     http_req_blocked...............: avg=75.03µs  min=942ns    med=2.71µs  max=139.73ms p(90)=4.22µs   p(95)=5.4µs    p(99.9)=28.35ms 
     http_req_connecting............: avg=70.54µs  min=0s       med=0s      max=139.67ms p(90)=0s       p(95)=0s       p(99.9)=27.93ms 
     http_req_duration..............: avg=47.43ms  min=750.35µs med=40.01ms max=339.31ms p(90)=98.78ms  p(95)=122.99ms p(99.9)=181.51ms
       { expected_response:true }...: avg=47.43ms  min=750.35µs med=40.01ms max=339.31ms p(90)=98.78ms  p(95)=122.99ms p(99.9)=181.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 287028
     http_req_receiving.............: avg=386.26µs min=25.74µs  med=54.09µs max=131.23ms p(90)=215.28µs p(95)=367.57µs p(99.9)=52.67ms 
     http_req_sending...............: avg=168.06µs min=4.01µs   med=9.47µs  max=145.03ms p(90)=17.78µs  p(95)=119.57µs p(99.9)=29.82ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.88ms  min=702.13µs med=39.65ms max=330.26ms p(90)=97.46ms  p(95)=121.55ms p(99.9)=176.85ms
     http_reqs......................: 287028  4710.602167/s
     iteration_duration.............: avg=49.8ms   min=1.12ms   med=41.17ms max=351.97ms p(90)=105.37ms p(95)=131.56ms p(99.9)=204.32ms
     iterations.....................: 286028  4694.19052/s
     success_rate...................: 100.00% ✓ 286028      ✗ 0     
     vus............................: 55      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 851514      ✗ 0     
     data_received..................: 25 GB   409 MB/s
     data_sent......................: 342 MB  5.6 MB/s
     http_req_blocked...............: avg=71.91µs  min=942ns    med=2.58µs  max=169.24ms p(90)=4.16µs   p(95)=5.31µs   p(99.9)=26.31ms 
     http_req_connecting............: avg=67.28µs  min=0s       med=0s      max=140.09ms p(90)=0s       p(95)=0s       p(99.9)=25.07ms 
     http_req_duration..............: avg=48.4ms   min=787.66µs med=40.43ms max=307.04ms p(90)=102.92ms p(95)=128.78ms p(99.9)=186.96ms
       { expected_response:true }...: avg=48.4ms   min=787.66µs med=40.43ms max=307.04ms p(90)=102.92ms p(95)=128.78ms p(99.9)=186.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 284838
     http_req_receiving.............: avg=354.3µs  min=25.05µs  med=53.34µs max=138.71ms p(90)=219.13µs p(95)=379.56µs p(99.9)=51.25ms 
     http_req_sending...............: avg=161.69µs min=3.88µs   med=9.19µs  max=164.84ms p(90)=18.01µs  p(95)=122.72µs p(99.9)=30.52ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.88ms  min=744.72µs med=40.06ms max=298.52ms p(90)=101.71ms p(95)=127.34ms p(99.9)=181.69ms
     http_reqs......................: 284838  4672.32054/s
     iteration_duration.............: avg=50.18ms  min=1.25ms   med=41.4ms  max=343.47ms p(90)=106.95ms p(95)=134.62ms p(99.9)=203.45ms
     iterations.....................: 283838  4655.917109/s
     success_rate...................: 100.00% ✓ 283838      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 848313      ✗ 0     
     data_received..................: 25 GB   408 MB/s
     data_sent......................: 341 MB  5.6 MB/s
     http_req_blocked...............: avg=77.16µs  min=962ns    med=2.69µs  max=158.28ms p(90)=4.25µs   p(95)=5.44µs   p(99.9)=29.43ms 
     http_req_connecting............: avg=72.95µs  min=0s       med=0s      max=141.97ms p(90)=0s       p(95)=0s       p(99.9)=28.68ms 
     http_req_duration..............: avg=47.94ms  min=743.95µs med=40.5ms  max=251.7ms  p(90)=99.83ms  p(95)=124.2ms  p(99.9)=199.04ms
       { expected_response:true }...: avg=47.94ms  min=743.95µs med=40.5ms  max=251.7ms  p(90)=99.83ms  p(95)=124.2ms  p(99.9)=199.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 283771
     http_req_receiving.............: avg=436.57µs min=26.67µs  med=55.13µs max=134.01ms p(90)=217.82µs p(95)=373.23µs p(99.9)=60.78ms 
     http_req_sending...............: avg=165.51µs min=3.92µs   med=9.41µs  max=156.32ms p(90)=17.39µs  p(95)=118.99µs p(99.9)=28.99ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.34ms  min=703.42µs med=40.12ms max=251.65ms p(90)=98.49ms  p(95)=122.67ms p(99.9)=175.48ms
     http_reqs......................: 283771  4658.214693/s
     iteration_duration.............: avg=50.37ms  min=1.25ms   med=41.66ms max=383.65ms p(90)=106.37ms p(95)=132.93ms p(99.9)=217.4ms 
     iterations.....................: 282771  4641.799292/s
     success_rate...................: 100.00% ✓ 282771      ✗ 0     
     vus............................: 53      min=0         max=499 
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

     checks.........................: 100.00% ✓ 842643      ✗ 0     
     data_received..................: 25 GB   405 MB/s
     data_sent......................: 339 MB  5.6 MB/s
     http_req_blocked...............: avg=57.6µs   min=831ns    med=2.16µs  max=120.47ms p(90)=3.81µs   p(95)=4.9µs    p(99.9)=19.23ms 
     http_req_connecting............: avg=54.16µs  min=0s       med=0s      max=111.55ms p(90)=0s       p(95)=0s       p(99.9)=18.9ms  
     http_req_duration..............: avg=49.16ms  min=655.04µs med=41.13ms max=264.84ms p(90)=105.28ms p(95)=131.23ms p(99.9)=190.87ms
       { expected_response:true }...: avg=49.16ms  min=655.04µs med=41.13ms max=264.84ms p(90)=105.28ms p(95)=131.23ms p(99.9)=190.87ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281881
     http_req_receiving.............: avg=295.82µs min=25.02µs  med=51.02µs max=107.3ms  p(90)=203.5µs  p(95)=372.41µs p(99.9)=40.25ms 
     http_req_sending...............: avg=137µs    min=4.02µs   med=8.97µs  max=129.53ms p(90)=17.75µs  p(95)=120.92µs p(99.9)=24.73ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.73ms  min=618.73µs med=40.83ms max=264.73ms p(90)=104.3ms  p(95)=130.18ms p(99.9)=187.6ms 
     http_reqs......................: 281881  4630.289604/s
     iteration_duration.............: avg=50.71ms  min=1.14ms   med=42.07ms max=336.82ms p(90)=108.58ms p(95)=135.67ms p(99.9)=213.66ms
     iterations.....................: 280881  4613.863206/s
     success_rate...................: 100.00% ✓ 280881      ✗ 0     
     vus............................: 51      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 837402      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=69.23µs  min=942ns    med=2.56µs  max=136.4ms  p(90)=4.14µs   p(95)=5.28µs   p(99.9)=25.67ms 
     http_req_connecting............: avg=65.6µs   min=0s       med=0s      max=136.17ms p(90)=0s       p(95)=0s       p(99.9)=25ms    
     http_req_duration..............: avg=48.88ms  min=767.75µs med=41.05ms max=268.64ms p(90)=104.47ms p(95)=130.76ms p(99.9)=183.01ms
       { expected_response:true }...: avg=48.88ms  min=767.75µs med=41.05ms max=268.64ms p(90)=104.47ms p(95)=130.76ms p(99.9)=183.01ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280134
     http_req_receiving.............: avg=340.26µs min=24.91µs  med=54.34µs max=127.1ms  p(90)=218.19µs p(95)=383.24µs p(99.9)=45.53ms 
     http_req_sending...............: avg=156.78µs min=4.12µs   med=9.16µs  max=109.76ms p(90)=17.5µs   p(95)=123.37µs p(99.9)=27.24ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.39ms  min=722.87µs med=40.73ms max=258.99ms p(90)=103.27ms p(95)=129.58ms p(99.9)=178.99ms
     http_reqs......................: 280134  4594.539521/s
     iteration_duration.............: avg=51.03ms  min=1.28ms   med=41.96ms max=321.82ms p(90)=109.38ms p(95)=137.6ms  p(99.9)=221.79ms
     iterations.....................: 279134  4578.1383/s
     success_rate...................: 100.00% ✓ 279134      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 825531      ✗ 0     
     data_received..................: 24 GB   396 MB/s
     data_sent......................: 332 MB  5.4 MB/s
     http_req_blocked...............: avg=68.67µs  min=812ns    med=2.51µs  max=182.2ms  p(90)=4.24µs   p(95)=5.45µs   p(99.9)=24.4ms  
     http_req_connecting............: avg=64.03µs  min=0s       med=0s      max=130.34ms p(90)=0s       p(95)=0s       p(99.9)=23.56ms 
     http_req_duration..............: avg=50.09ms  min=779.81µs med=42.09ms max=304.99ms p(90)=107.48ms p(95)=134.16ms p(99.9)=188.98ms
       { expected_response:true }...: avg=50.09ms  min=779.81µs med=42.09ms max=304.99ms p(90)=107.48ms p(95)=134.16ms p(99.9)=188.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 276177
     http_req_receiving.............: avg=342.47µs min=24.63µs  med=53.34µs max=228.61ms p(90)=221.84µs p(95)=390.22µs p(99.9)=46.14ms 
     http_req_sending...............: avg=153.88µs min=4.1µs    med=9.19µs  max=101.3ms  p(90)=18.03µs  p(95)=126.71µs p(99.9)=27.01ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.6ms   min=734.46µs med=41.75ms max=304.53ms p(90)=106.31ms p(95)=132.97ms p(99.9)=184.13ms
     http_reqs......................: 276177  4530.497654/s
     iteration_duration.............: avg=51.77ms  min=1.34ms   med=42.74ms max=365.81ms p(90)=110.98ms p(95)=140.12ms p(99.9)=209.56ms
     iterations.....................: 275177  4514.093328/s
     success_rate...................: 100.00% ✓ 275177      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.e7e70652)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 737286      ✗ 0     
     data_received..................: 22 GB   353 MB/s
     data_sent......................: 296 MB  4.9 MB/s
     http_req_blocked...............: avg=53.62µs  min=1µs      med=2.82µs  max=126.43ms p(90)=4.53µs   p(95)=5.78µs   p(99.9)=13.63ms 
     http_req_connecting............: avg=48.55µs  min=0s       med=0s      max=104.7ms  p(90)=0s       p(95)=0s       p(99.9)=12.6ms  
     http_req_duration..............: avg=56.68ms  min=861.31µs med=48.71ms max=308.7ms  p(90)=120.75ms p(95)=150.48ms p(99.9)=213.3ms 
       { expected_response:true }...: avg=56.68ms  min=861.31µs med=48.71ms max=308.7ms  p(90)=120.75ms p(95)=150.48ms p(99.9)=213.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 246762
     http_req_receiving.............: avg=297.84µs min=26.12µs  med=55.85µs max=105.62ms p(90)=222.69µs p(95)=406.73µs p(99.9)=44.84ms 
     http_req_sending...............: avg=135.97µs min=4.18µs   med=9.81µs  max=228.6ms  p(90)=18.88µs  p(95)=134.31µs p(99.9)=24.51ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=56.24ms  min=822.63µs med=48.4ms  max=308.64ms p(90)=119.81ms p(95)=149.64ms p(99.9)=210.16ms
     http_reqs......................: 246762  4039.774134/s
     iteration_duration.............: avg=57.97ms  min=1.39ms   med=49.44ms max=362.04ms p(90)=123.78ms p(95)=154.58ms p(99.9)=227.27ms
     iterations.....................: 245762  4023.402999/s
     success_rate...................: 100.00% ✓ 245762      ✗ 0     
     vus............................: 61      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 724497      ✗ 0     
     data_received..................: 21 GB   347 MB/s
     data_sent......................: 291 MB  4.8 MB/s
     http_req_blocked...............: avg=39.65µs  min=811ns    med=2.11µs  max=129.87ms p(90)=3.76µs   p(95)=4.95µs   p(99.9)=7.41ms  
     http_req_connecting............: avg=36.26µs  min=0s       med=0s      max=101.83ms p(90)=0s       p(95)=0s       p(99.9)=6.72ms  
     http_req_duration..............: avg=57.74ms  min=879.25µs med=48.41ms max=311.63ms p(90)=120.19ms p(95)=146.23ms p(99.9)=206ms   
       { expected_response:true }...: avg=57.74ms  min=879.25µs med=48.41ms max=311.63ms p(90)=120.19ms p(95)=146.23ms p(99.9)=206ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 242499
     http_req_receiving.............: avg=284.13µs min=24.88µs  med=53µs    max=109.13ms p(90)=219.27µs p(95)=381µs    p(99.9)=41.24ms 
     http_req_sending...............: avg=112.77µs min=4.12µs   med=8.99µs  max=117.44ms p(90)=17.97µs  p(95)=126.28µs p(99.9)=21.07ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=57.34ms  min=830.51µs med=48.17ms max=311.2ms  p(90)=119.38ms p(95)=145.22ms p(99.9)=201.8ms 
     http_reqs......................: 242499  3969.735357/s
     iteration_duration.............: avg=59ms     min=1.68ms   med=49.36ms max=332.69ms p(90)=122.5ms  p(95)=149.05ms p(99.9)=225.91ms
     iterations.....................: 241499  3953.365246/s
     success_rate...................: 100.00% ✓ 241499      ✗ 0     
     vus............................: 61      min=0         max=497 
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

     checks.........................: 100.00% ✓ 252999      ✗ 0    
     data_received..................: 7.5 GB  119 MB/s
     data_sent......................: 103 MB  1.6 MB/s
     http_req_blocked...............: avg=4.81µs   min=932ns   med=2.2µs    max=6.66ms   p(90)=3.79µs   p(95)=4.7µs    p(99.9)=305.52µs
     http_req_connecting............: avg=2.02µs   min=0s      med=0s       max=6.59ms   p(90)=0s       p(95)=0s       p(99.9)=196.68µs
     http_req_duration..............: avg=167.14ms min=2.14ms  med=134.08ms max=871.55ms p(90)=356.44ms p(95)=416.02ms p(99.9)=668.94ms
       { expected_response:true }...: avg=167.14ms min=2.14ms  med=134.08ms max=871.55ms p(90)=356.44ms p(95)=416.02ms p(99.9)=668.94ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 85333
     http_req_receiving.............: avg=70.61µs  min=27.65µs med=56.82µs  max=152.41ms p(90)=89.59µs  p(95)=103.16µs p(99.9)=1.38ms  
     http_req_sending...............: avg=28.33µs  min=4.61µs  med=10.1µs   max=132.15ms p(90)=15.01µs  p(95)=18.13µs  p(99.9)=3.45ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.04ms min=2.08ms  med=133.97ms max=871.48ms p(90)=356.36ms p(95)=415.91ms p(99.9)=668.88ms
     http_reqs......................: 85333   1364.156578/s
     iteration_duration.............: avg=169.34ms min=6.79ms  med=136.55ms max=871.74ms p(90)=357.64ms p(95)=417.33ms p(99.9)=670.56ms
     iterations.....................: 84333   1348.170306/s
     success_rate...................: 100.00% ✓ 84333       ✗ 0    
     vus............................: 81      min=0         max=495
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

     checks.........................: 100.00% ✓ 250866      ✗ 0    
     data_received..................: 7.4 GB  119 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=5.68µs   min=891ns   med=2.27µs   max=18.05ms  p(90)=3.95µs   p(95)=4.87µs   p(99.9)=342.21µs
     http_req_connecting............: avg=2.75µs   min=0s      med=0s       max=17.98ms  p(90)=0s       p(95)=0s       p(99.9)=223.85µs
     http_req_duration..............: avg=168.54ms min=1.96ms  med=165.36ms max=458.49ms p(90)=320.68ms p(95)=343.04ms p(99.9)=408.25ms
       { expected_response:true }...: avg=168.54ms min=1.96ms  med=165.36ms max=458.49ms p(90)=320.68ms p(95)=343.04ms p(99.9)=408.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 84622
     http_req_receiving.............: avg=70.91µs  min=26.33µs med=57.8µs   max=26.75ms  p(90)=94.73µs  p(95)=109.16µs p(99.9)=1.19ms  
     http_req_sending...............: avg=30.15µs  min=4.69µs  med=10.46µs  max=121.98ms p(90)=17.06µs  p(95)=20.37µs  p(99.9)=3.34ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=168.44ms min=1.91ms  med=165.27ms max=458.39ms p(90)=320.6ms  p(95)=342.95ms p(99.9)=408.18ms
     http_reqs......................: 84622   1355.528338/s
     iteration_duration.............: avg=170.77ms min=4.82ms  med=168.06ms max=458.67ms p(90)=321.4ms  p(95)=343.59ms p(99.9)=408.6ms 
     iterations.....................: 83622   1339.50971/s
     success_rate...................: 100.00% ✓ 83622       ✗ 0    
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

     checks.........................: 100.00% ✓ 105012     ✗ 0    
     data_received..................: 3.2 GB  49 MB/s
     data_sent......................: 43 MB   674 kB/s
     http_req_blocked...............: avg=9.76µs   min=1.04µs  med=2.5µs    max=6.29ms  p(90)=4.18µs   p(95)=5.18µs   p(99.9)=2.18ms 
     http_req_connecting............: avg=6.06µs   min=0s      med=0s       max=6.13ms  p(90)=0s       p(95)=0s       p(99.9)=1.8ms  
     http_req_duration..............: avg=398.34ms min=3.33ms  med=368.11ms max=1.51s   p(90)=792.52ms p(95)=860.69ms p(99.9)=1.28s  
       { expected_response:true }...: avg=398.34ms min=3.33ms  med=368.11ms max=1.51s   p(90)=792.52ms p(95)=860.69ms p(99.9)=1.28s  
     http_req_failed................: 0.00%   ✓ 0          ✗ 36004
     http_req_receiving.............: avg=80.61µs  min=27.64µs med=67.93µs  max=67.49ms p(90)=106.32µs p(95)=121.43µs p(99.9)=881.1µs
     http_req_sending...............: avg=27.54µs  min=4.9µs   med=12.74µs  max=92.65ms p(90)=19.51µs  p(95)=22.05µs  p(99.9)=2.67ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=398.23ms min=3.26ms  med=368.02ms max=1.51s   p(90)=792.44ms p(95)=860.59ms p(99.9)=1.28s  
     http_reqs......................: 36004   561.57278/s
     iteration_duration.............: avg=409.94ms min=16.31ms med=382.3ms  max=1.51s   p(90)=795.66ms p(95)=862.56ms p(99.9)=1.29s  
     iterations.....................: 35004   545.975269/s
     success_rate...................: 100.00% ✓ 35004      ✗ 0    
     vus............................: 60      min=0        max=498
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

     checks.........................: 100.00% ✓ 51444      ✗ 0    
     data_received..................: 1.6 GB  24 MB/s
     data_sent......................: 22 MB   323 kB/s
     http_req_blocked...............: avg=13.24µs  min=1.35µs  med=3.49µs   max=9.66ms  p(90)=5.27µs   p(95)=6.69µs   p(99.9)=2.22ms
     http_req_connecting............: avg=8.06µs   min=0s      med=0s       max=9.59ms  p(90)=0s       p(95)=0s       p(99.9)=2.2ms 
     http_req_duration..............: avg=799.11ms min=5.45ms  med=694.34ms max=3.69s   p(90)=1.58s    p(95)=1.84s    p(99.9)=3.29s 
       { expected_response:true }...: avg=799.11ms min=5.45ms  med=694.34ms max=3.69s   p(90)=1.58s    p(95)=1.84s    p(99.9)=3.29s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 18148
     http_req_receiving.............: avg=98.23µs  min=35.26µs med=86.4µs   max=61.83ms p(90)=124.62µs p(95)=141.53µs p(99.9)=1.2ms 
     http_req_sending...............: avg=36.14µs  min=6.38µs  med=16.84µs  max=69.51ms p(90)=22.7µs   p(95)=25.67µs  p(99.9)=3.52ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=798.98ms min=5.38ms  med=694.24ms max=3.69s   p(90)=1.58s    p(95)=1.84s    p(99.9)=3.29s 
     http_reqs......................: 18148   269.001309/s
     iteration_duration.............: avg=845.8ms  min=21.4ms  med=764.7ms  max=3.69s   p(90)=1.6s     p(95)=1.88s    p(99.9)=3.31s 
     iterations.....................: 17148   254.178666/s
     success_rate...................: 100.00% ✓ 17148      ✗ 0    
     vus............................: 66      min=0        max=500
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

     checks.........................: 100.00% ✓ 46347      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   288 kB/s
     http_req_blocked...............: avg=14.26µs  min=1.14µs  med=2.83µs   max=6.6ms    p(90)=4.46µs   p(95)=5.9µs    p(99.9)=2.63ms
     http_req_connecting............: avg=9.69µs   min=0s      med=0s       max=6.54ms   p(90)=0s       p(95)=0s       p(99.9)=2.58ms
     http_req_duration..............: avg=883.04ms min=7.54ms  med=799.94ms max=3.02s    p(90)=1.83s    p(95)=1.93s    p(99.9)=2.64s 
       { expected_response:true }...: avg=883.04ms min=7.54ms  med=799.94ms max=3.02s    p(90)=1.83s    p(95)=1.93s    p(99.9)=2.64s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16449
     http_req_receiving.............: avg=93.01µs  min=33.26µs med=83.66µs  max=32.26ms  p(90)=119.83µs p(95)=134.56µs p(99.9)=1.18ms
     http_req_sending...............: avg=56.44µs  min=5.15µs  med=15.48µs  max=187.02ms p(90)=20.33µs  p(95)=23.72µs  p(99.9)=5.35ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=882.89ms min=7.46ms  med=799.89ms max=3.02s    p(90)=1.83s    p(95)=1.93s    p(99.9)=2.64s 
     http_reqs......................: 16449   239.717747/s
     iteration_duration.............: avg=940.19ms min=29.3ms  med=864.64ms max=3.03s    p(90)=1.84s    p(95)=1.94s    p(99.9)=2.66s 
     iterations.....................: 15449   225.144354/s
     success_rate...................: 100.00% ✓ 15449      ✗ 0    
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

