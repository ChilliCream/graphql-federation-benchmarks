## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-fed-net-11 | 16.7.6 | 4,821 | 4,837 | 4,817 | 0.2% | 432 MB | 91.7 KB |  |
| fusion-net-11 | 16.7.6 | 4,818 | 4,825 | 4,678 | 1.4% | 394 MB | 83.8 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.15 | 4,701 | 4,718 | 4,681 | 0.3% | 399 MB | 86.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.15 | 4,695 | 4,781 | 4,679 | 1.0% | 151 MB | 32.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.15 | 4,683 | 4,786 | 4,657 | 1.2% | 140 MB | 30.7 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.15 | 4,681 | 4,794 | 4,670 | 1.2% | 402 MB | 87.9 KB |  |
| fusion-aot-11 | 16.7.6 | 4,659 | 4,680 | 4,645 | 0.3% | 151 MB | 33.2 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 4,640 | 4,681 | 4,548 | 1.4% | 158 MB | 34.9 KB |  |
| feddi-gateway | 2026-11-03-0517 | 4,481 | 4,563 | 4,450 | 1.1% | 2,295 MB | 524.4 KB |  |
| hive-router | v0.3.13 | 2,793 | 2,802 | 2,790 | 0.2% | 177 MB | 65.0 KB |  |
| caliban | 3.2.1 | 1,512 | 1,515 | 1,512 | 0.1% | 11,603 MB | 7,857.9 KB |  |
| cosmo | 0.372.0 | 1,362 | 1,366 | 1,358 | 0.2% | 631 MB | 474.5 KB |  |
| hive-gateway-router-runtime | 2.15.8 | 554 | 555 | 549 | 0.5% | 3,026 MB | 5,594.1 KB |  |
| hive-gateway | 2.15.8 | 274 | 275 | 272 | 0.5% | 3,608 MB | 13,484.3 KB |  |
| apollo-gateway | 2.14.4 | 232 | 232 | 232 | 0.0% | 2,462 MB | 10,865.3 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (7166 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (9679 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (142775 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 878097      ✗ 0     
     data_received..................: 26 GB   422 MB/s
     data_sent......................: 353 MB  5.8 MB/s
     http_req_blocked...............: avg=70.23µs  min=762ns    med=2.14µs  max=150.19ms p(90)=3.74µs   p(95)=4.85µs   p(99.9)=24.77ms 
     http_req_connecting............: avg=66.94µs  min=0s       med=0s      max=150.14ms p(90)=0s       p(95)=0s       p(99.9)=24.25ms 
     http_req_duration..............: avg=46.46ms  min=731.88µs med=39.35ms max=310.04ms p(90)=97.36ms  p(95)=120.6ms  p(99.9)=177.11ms
       { expected_response:true }...: avg=46.46ms  min=731.88µs med=39.35ms max=310.04ms p(90)=97.36ms  p(95)=120.6ms  p(99.9)=177.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 293699
     http_req_receiving.............: avg=349.9µs  min=25.22µs  med=52.61µs max=118.09ms p(90)=201.79µs p(95)=349.11µs p(99.9)=47.02ms 
     http_req_sending...............: avg=158.04µs min=3.88µs   med=8.76µs  max=206.74ms p(90)=16.48µs  p(95)=111.66µs p(99.9)=27.33ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=45.96ms  min=694.51µs med=38.98ms max=302.49ms p(90)=96.21ms  p(95)=119.4ms  p(99.9)=171.22ms
     http_reqs......................: 293699  4821.344378/s
     iteration_duration.............: avg=48.66ms  min=1.22ms   med=40.31ms max=330.77ms p(90)=103.39ms p(95)=128.72ms p(99.9)=201.65ms
     iterations.....................: 292699  4804.92844/s
     success_rate...................: 100.00% ✓ 292699      ✗ 0     
     vus............................: 53      min=0         max=499 
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

     checks.........................: 100.00% ✓ 877491      ✗ 0     
     data_received..................: 26 GB   422 MB/s
     data_sent......................: 353 MB  5.8 MB/s
     http_req_blocked...............: avg=65.43µs  min=821ns   med=2.03µs  max=134.34ms p(90)=3.57µs   p(95)=4.61µs   p(99.9)=24.58ms 
     http_req_connecting............: avg=62µs     min=0s      med=0s      max=122.04ms p(90)=0s       p(95)=0s       p(99.9)=24.4ms  
     http_req_duration..............: avg=46.79ms  min=727.1µs med=39.24ms max=294.63ms p(90)=99.77ms  p(95)=123.45ms p(99.9)=178.33ms
       { expected_response:true }...: avg=46.79ms  min=727.1µs med=39.24ms max=294.63ms p(90)=99.77ms  p(95)=123.45ms p(99.9)=178.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 293497
     http_req_receiving.............: avg=348.77µs min=25.33µs med=51.87µs max=168.47ms p(90)=205.87µs p(95)=359.42µs p(99.9)=47.72ms 
     http_req_sending...............: avg=147.31µs min=3.94µs  med=8.49µs  max=116.03ms p(90)=16µs     p(95)=113.79µs p(99.9)=27.18ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.29ms  min=693.5µs med=38.91ms max=294.25ms p(90)=98.46ms  p(95)=122.07ms p(99.9)=174.32ms
     http_reqs......................: 293497  4818.414134/s
     iteration_duration.............: avg=48.69ms  min=1.17ms  med=40.22ms max=356.07ms p(90)=104.13ms p(95)=129.86ms p(99.9)=208.98ms
     iterations.....................: 292497  4801.996882/s
     success_rate...................: 100.00% ✓ 292497      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 856617      ✗ 0     
     data_received..................: 25 GB   411 MB/s
     data_sent......................: 344 MB  5.6 MB/s
     http_req_blocked...............: avg=73.42µs  min=952ns    med=2.61µs  max=149.75ms p(90)=4.07µs   p(95)=5.2µs    p(99.9)=28.19ms 
     http_req_connecting............: avg=68.58µs  min=0s       med=0s      max=149.65ms p(90)=0s       p(95)=0s       p(99.9)=26.99ms 
     http_req_duration..............: avg=47.24ms  min=746.61µs med=39.75ms max=276.94ms p(90)=99.56ms  p(95)=124.47ms p(99.9)=183.8ms 
       { expected_response:true }...: avg=47.24ms  min=746.61µs med=39.75ms max=276.94ms p(90)=99.56ms  p(95)=124.47ms p(99.9)=183.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 286539
     http_req_receiving.............: avg=369.24µs min=26.6µs   med=53.18µs max=139.27ms p(90)=211.13µs p(95)=368.92µs p(99.9)=48.98ms 
     http_req_sending...............: avg=165.05µs min=4.09µs   med=9.15µs  max=229.7ms  p(90)=17.12µs  p(95)=117.74µs p(99.9)=29.4ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.71ms  min=703.64µs med=39.4ms  max=276.16ms p(90)=98.24ms  p(95)=123.05ms p(99.9)=177.43ms
     http_reqs......................: 286539  4701.150219/s
     iteration_duration.............: avg=49.88ms  min=1.2ms    med=41.04ms max=367.59ms p(90)=106.4ms  p(95)=133.07ms p(99.9)=217.75ms
     iterations.....................: 285539  4684.743551/s
     success_rate...................: 100.00% ✓ 285539      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 855717      ✗ 0     
     data_received..................: 25 GB   411 MB/s
     data_sent......................: 344 MB  5.6 MB/s
     http_req_blocked...............: avg=69.69µs  min=781ns    med=2.38µs  max=138.53ms p(90)=3.97µs   p(95)=5.1µs    p(99.9)=27.7ms  
     http_req_connecting............: avg=65.88µs  min=0s       med=0s      max=138.33ms p(90)=0s       p(95)=0s       p(99.9)=26.79ms 
     http_req_duration..............: avg=48.03ms  min=795.19µs med=40.71ms max=314.66ms p(90)=101.61ms p(95)=127.66ms p(99.9)=184.07ms
       { expected_response:true }...: avg=48.03ms  min=795.19µs med=40.71ms max=314.66ms p(90)=101.61ms p(95)=127.66ms p(99.9)=184.07ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 286239
     http_req_receiving.............: avg=340.55µs min=26.51µs  med=52.25µs max=127.32ms p(90)=212.94µs p(95)=373.44µs p(99.9)=47.9ms  
     http_req_sending...............: avg=153.89µs min=4.16µs   med=8.85µs  max=217.68ms p(90)=17.32µs  p(95)=121.37µs p(99.9)=27.13ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.53ms  min=735.22µs med=40.38ms max=286.73ms p(90)=100.4ms  p(95)=126.46ms p(99.9)=179.5ms 
     http_reqs......................: 286239  4695.054446/s
     iteration_duration.............: avg=49.93ms  min=1.19ms   med=41.47ms max=371.36ms p(90)=106.75ms p(95)=133.77ms p(99.9)=207.83ms
     iterations.....................: 285239  4678.651879/s
     success_rate...................: 100.00% ✓ 285239      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 853446      ✗ 0     
     data_received..................: 25 GB   410 MB/s
     data_sent......................: 343 MB  5.6 MB/s
     http_req_blocked...............: avg=67.01µs  min=892ns    med=2.5µs   max=155.34ms p(90)=4.08µs   p(95)=5.28µs   p(99.9)=26.05ms 
     http_req_connecting............: avg=62.88µs  min=0s       med=0s      max=155.17ms p(90)=0s       p(95)=0s       p(99.9)=25.7ms  
     http_req_duration..............: avg=48.28ms  min=793.11µs med=40.35ms max=404.01ms p(90)=103.38ms p(95)=128.82ms p(99.9)=185.57ms
       { expected_response:true }...: avg=48.28ms  min=793.11µs med=40.35ms max=404.01ms p(90)=103.38ms p(95)=128.82ms p(99.9)=185.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 285482
     http_req_receiving.............: avg=363.74µs min=22.1µs   med=51.98µs max=277.16ms p(90)=215.76µs p(95)=377.95µs p(99.9)=50.74ms 
     http_req_sending...............: avg=153.31µs min=4.05µs   med=8.9µs   max=117.01ms p(90)=17.59µs  p(95)=123.02µs p(99.9)=27.42ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.77ms  min=744.04µs med=40.01ms max=258.03ms p(90)=102.14ms p(95)=127.38ms p(99.9)=180.58ms
     http_reqs......................: 285482  4683.131009/s
     iteration_duration.............: avg=50.07ms  min=1.21ms   med=41.23ms max=418.44ms p(90)=107.57ms p(95)=134.28ms p(99.9)=205.5ms 
     iterations.....................: 284482  4666.726714/s
     success_rate...................: 100.00% ✓ 284482      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.15)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 852774      ✗ 0     
     data_received..................: 25 GB   410 MB/s
     data_sent......................: 343 MB  5.6 MB/s
     http_req_blocked...............: avg=78.44µs  min=951ns    med=2.65µs  max=144.43ms p(90)=4.2µs    p(95)=5.41µs   p(99.9)=30.78ms 
     http_req_connecting............: avg=74.94µs  min=0s       med=0s      max=144.37ms p(90)=0s       p(95)=0s       p(99.9)=30.65ms 
     http_req_duration..............: avg=47.64ms  min=744.17µs med=40.35ms max=314.9ms  p(90)=99.7ms   p(95)=123.12ms p(99.9)=181.57ms
       { expected_response:true }...: avg=47.64ms  min=744.17µs med=40.35ms max=314.9ms  p(90)=99.7ms   p(95)=123.12ms p(99.9)=181.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 285258
     http_req_receiving.............: avg=377.92µs min=23.99µs  med=55.27µs max=138.84ms p(90)=216.05µs p(95)=365.21µs p(99.9)=53.31ms 
     http_req_sending...............: avg=171.09µs min=3.86µs   med=9.37µs  max=175.76ms p(90)=17.87µs  p(95)=119.58µs p(99.9)=31.04ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.09ms  min=704.06µs med=39.95ms max=303.69ms p(90)=98.46ms  p(95)=121.65ms p(99.9)=176.3ms 
     http_reqs......................: 285258  4681.889012/s
     iteration_duration.............: avg=50.11ms  min=1.18ms   med=41.55ms max=332.38ms p(90)=106.42ms p(95)=131.16ms p(99.9)=205.84ms
     iterations.....................: 284258  4665.476189/s
     success_rate...................: 100.00% ✓ 284258      ✗ 0     
     vus............................: 54      min=0         max=499 
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

     checks.........................: 100.00% ✓ 849285      ✗ 0     
     data_received..................: 25 GB   408 MB/s
     data_sent......................: 341 MB  5.6 MB/s
     http_req_blocked...............: avg=68.93µs  min=812ns    med=2.57µs  max=162.93ms p(90)=4.21µs   p(95)=5.41µs   p(99.9)=26.5ms  
     http_req_connecting............: avg=64.95µs  min=0s       med=0s      max=139.76ms p(90)=0s       p(95)=0s       p(99.9)=26.3ms  
     http_req_duration..............: avg=48.49ms  min=787.02µs med=40.27ms max=310.37ms p(90)=104.09ms p(95)=129.45ms p(99.9)=184.13ms
       { expected_response:true }...: avg=48.49ms  min=787.02µs med=40.27ms max=310.37ms p(90)=104.09ms p(95)=129.45ms p(99.9)=184.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 284095
     http_req_receiving.............: avg=329.15µs min=24.98µs  med=52.23µs max=152.97ms p(90)=220.61µs p(95)=385.19µs p(99.9)=44.21ms 
     http_req_sending...............: avg=154.68µs min=4.1µs    med=9.06µs  max=287.34ms p(90)=17.62µs  p(95)=124.32µs p(99.9)=28.29ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.01ms  min=748.98µs med=39.94ms max=309.8ms  p(90)=102.96ms p(95)=128.22ms p(99.9)=180.12ms
     http_reqs......................: 284095  4659.102934/s
     iteration_duration.............: avg=50.32ms  min=1.24ms   med=41.35ms max=341.16ms p(90)=107.91ms p(95)=135.68ms p(99.9)=205.9ms 
     iterations.....................: 283095  4642.703128/s
     success_rate...................: 100.00% ✓ 283095      ✗ 0     
     vus............................: 56      min=0         max=498 
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

     checks.........................: 100.00% ✓ 846102      ✗ 0     
     data_received..................: 25 GB   406 MB/s
     data_sent......................: 340 MB  5.6 MB/s
     http_req_blocked...............: avg=64.29µs  min=822ns    med=2.33µs  max=134.12ms p(90)=3.94µs   p(95)=5.06µs   p(99.9)=22.57ms 
     http_req_connecting............: avg=60.96µs  min=0s       med=0s      max=134.07ms p(90)=0s       p(95)=0s       p(99.9)=22.22ms 
     http_req_duration..............: avg=48.64ms  min=790.23µs med=40.61ms max=302.5ms  p(90)=104.55ms p(95)=131.13ms p(99.9)=186.15ms
       { expected_response:true }...: avg=48.64ms  min=790.23µs med=40.61ms max=302.5ms  p(90)=104.55ms p(95)=131.13ms p(99.9)=186.15ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 283034
     http_req_receiving.............: avg=339.68µs min=22.72µs  med=52.22µs max=126.94ms p(90)=219.02µs p(95)=384.58µs p(99.9)=44.92ms 
     http_req_sending...............: avg=147.3µs  min=4.01µs   med=8.81µs  max=149.16ms p(90)=17.15µs  p(95)=124.06µs p(99.9)=26.16ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.15ms  min=749.53µs med=40.29ms max=263.57ms p(90)=103.31ms p(95)=129.86ms p(99.9)=181.78ms
     http_reqs......................: 283034  4640.942961/s
     iteration_duration.............: avg=50.5ms   min=1.32ms   med=41.47ms max=318.27ms p(90)=108.97ms p(95)=137.06ms p(99.9)=209.78ms
     iterations.....................: 282034  4624.545839/s
     success_rate...................: 100.00% ✓ 282034      ✗ 0     
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

     checks.........................: 100.00% ✓ 815547      ✗ 0     
     data_received..................: 24 GB   392 MB/s
     data_sent......................: 328 MB  5.4 MB/s
     http_req_blocked...............: avg=60.28µs  min=811ns    med=2.5µs   max=138.49ms p(90)=4.27µs   p(95)=5.4µs    p(99.9)=20.1ms  
     http_req_connecting............: avg=56.22µs  min=0s       med=0s      max=138.24ms p(90)=0s       p(95)=0s       p(99.9)=19.38ms 
     http_req_duration..............: avg=50.93ms  min=646.31µs med=41.84ms max=292.64ms p(90)=110.27ms p(95)=136.88ms p(99.9)=202.18ms
       { expected_response:true }...: avg=50.93ms  min=646.31µs med=41.84ms max=292.64ms p(90)=110.27ms p(95)=136.88ms p(99.9)=202.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 272849
     http_req_receiving.............: avg=293.28µs min=23.7µs   med=52.16µs max=101.48ms p(90)=209.75µs p(95)=388.8µs  p(99.9)=38.63ms 
     http_req_sending...............: avg=143.91µs min=3.88µs   med=9.22µs  max=190.68ms p(90)=18.32µs  p(95)=129.25µs p(99.9)=25.99ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.49ms  min=612.01µs med=41.53ms max=284.41ms p(90)=109.22ms p(95)=135.81ms p(99.9)=199.06ms
     http_reqs......................: 272849  4481.823851/s
     iteration_duration.............: avg=52.4ms   min=1.24ms   med=42.58ms max=385.82ms p(90)=113.09ms p(95)=141.43ms p(99.9)=221.56ms
     iterations.....................: 271849  4465.397828/s
     success_rate...................: 100.00% ✓ 271849      ✗ 0     
     vus............................: 51      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.13)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 511551      ✗ 0     
     data_received..................: 15 GB   244 MB/s
     data_sent......................: 206 MB  3.4 MB/s
     http_req_blocked...............: avg=19.64µs  min=892ns   med=2.35µs  max=53.62ms  p(90)=4.19µs   p(95)=5.48µs   p(99.9)=1.15ms  
     http_req_connecting............: avg=16.39µs  min=0s      med=0s      max=53.42ms  p(90)=0s       p(95)=0s       p(99.9)=1.06ms  
     http_req_duration..............: avg=82.85ms  min=1.16ms  med=77.23ms max=290.34ms p(90)=159.61ms p(95)=174.16ms p(99.9)=223.17ms
       { expected_response:true }...: avg=82.85ms  min=1.16ms  med=77.23ms max=290.34ms p(90)=159.61ms p(95)=174.16ms p(99.9)=223.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 171517
     http_req_receiving.............: avg=158.18µs min=24.16µs med=53.9µs  max=225.88ms p(90)=168.22µs p(95)=362.41µs p(99.9)=16.08ms 
     http_req_sending...............: avg=74µs     min=4.38µs  med=9.85µs  max=236.25ms p(90)=21.26µs  p(95)=127.83µs p(99.9)=9.97ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=82.62ms  min=1.1ms   med=77.01ms max=254.8ms  p(90)=159.3ms  p(95)=173.85ms p(99.9)=222.11ms
     http_reqs......................: 171517  2793.810236/s
     iteration_duration.............: avg=83.59ms  min=2.22ms  med=78.07ms max=300.82ms p(90)=160.02ms p(95)=174.55ms p(99.9)=224.79ms
     iterations.....................: 170517  2777.521412/s
     success_rate...................: 100.00% ✓ 170517      ✗ 0     
     vus............................: 74      min=0         max=494 
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

     checks.........................: 100.00% ✓ 279417      ✗ 0    
     data_received..................: 8.2 GB  132 MB/s
     data_sent......................: 113 MB  1.8 MB/s
     http_req_blocked...............: avg=6.36µs   min=902ns   med=2.72µs   max=16.32ms  p(90)=4.73µs   p(95)=5.83µs   p(99.9)=470.38µs
     http_req_connecting............: avg=2.95µs   min=0s      med=0s       max=16.11ms  p(90)=0s       p(95)=0s       p(99.9)=353.19µs
     http_req_duration..............: avg=151.38ms min=1.89ms  med=124.6ms  max=829.65ms p(90)=318.68ms p(95)=372.02ms p(99.9)=615.6ms 
       { expected_response:true }...: avg=151.38ms min=1.89ms  med=124.6ms  max=829.65ms p(90)=318.68ms p(95)=372.02ms p(99.9)=615.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 94139
     http_req_receiving.............: avg=82.15µs  min=28.67µs med=61.33µs  max=80.65ms  p(90)=103.26µs p(95)=124.91µs p(99.9)=2.3ms   
     http_req_sending...............: avg=34.01µs  min=5.07µs  med=12.43µs  max=36.57ms  p(90)=20.86µs  p(95)=25.23µs  p(99.9)=4.25ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=151.26ms min=1.84ms  med=124.48ms max=829.6ms  p(90)=318.56ms p(95)=371.91ms p(99.9)=615.53ms
     http_reqs......................: 94139   1512.05741/s
     iteration_duration.............: avg=153.27ms min=7.46ms  med=126.76ms max=829.87ms p(90)=319.92ms p(95)=372.96ms p(99.9)=617.31ms
     iterations.....................: 93139   1495.995444/s
     success_rate...................: 100.00% ✓ 93139       ✗ 0    
     vus............................: 69      min=0         max=495
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.372.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 252081      ✗ 0    
     data_received..................: 7.4 GB  119 MB/s
     data_sent......................: 102 MB  1.6 MB/s
     http_req_blocked...............: avg=5.09µs   min=952ns   med=2.23µs   max=17.44ms  p(90)=3.89µs   p(95)=4.86µs   p(99.9)=325.28µs
     http_req_connecting............: avg=2.24µs   min=0s      med=0s       max=17.31ms  p(90)=0s       p(95)=0s       p(99.9)=252.44µs
     http_req_duration..............: avg=167.73ms min=1.96ms  med=167.21ms max=452.64ms p(90)=317.21ms p(95)=340.38ms p(99.9)=401.68ms
       { expected_response:true }...: avg=167.73ms min=1.96ms  med=167.21ms max=452.64ms p(90)=317.21ms p(95)=340.38ms p(99.9)=401.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 85027
     http_req_receiving.............: avg=72µs     min=26.52µs med=58.81µs  max=22.7ms   p(90)=96.03µs  p(95)=110.99µs p(99.9)=1.16ms  
     http_req_sending...............: avg=28.09µs  min=4.59µs  med=10.24µs  max=114.27ms p(90)=16.95µs  p(95)=20.57µs  p(99.9)=3.34ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=167.63ms min=1.88ms  med=167.11ms max=452.57ms p(90)=317.13ms p(95)=340.29ms p(99.9)=401.64ms
     http_reqs......................: 85027   1362.761878/s
     iteration_duration.............: avg=169.96ms min=5.42ms  med=169.65ms max=452.83ms p(90)=318.03ms p(95)=340.92ms p(99.9)=402.19ms
     iterations.....................: 84027   1346.734476/s
     success_rate...................: 100.00% ✓ 84027       ✗ 0    
     vus............................: 75      min=0         max=494
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 103845     ✗ 0    
     data_received..................: 3.1 GB  49 MB/s
     data_sent......................: 43 MB   665 kB/s
     http_req_blocked...............: avg=9.47µs   min=1.32µs  med=3.34µs   max=21.8ms   p(90)=5.15µs   p(95)=6.18µs   p(99.9)=1.24ms
     http_req_connecting............: avg=5.19µs   min=0s      med=0s       max=21.75ms  p(90)=0s       p(95)=0s       p(99.9)=1.22ms
     http_req_duration..............: avg=402.7ms  min=3.44ms  med=376.97ms max=1.57s    p(90)=798.72ms p(95)=868.3ms  p(99.9)=1.27s 
       { expected_response:true }...: avg=402.7ms  min=3.44ms  med=376.97ms max=1.57s    p(90)=798.72ms p(95)=868.3ms  p(99.9)=1.27s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 35615
     http_req_receiving.............: avg=87.65µs  min=30.41µs med=75.67µs  max=47.54ms  p(90)=111.91µs p(95)=126.46µs p(99.9)=1.02ms
     http_req_sending...............: avg=35.25µs  min=5.64µs  med=15.18µs  max=132.65ms p(90)=21.61µs  p(95)=24.43µs  p(99.9)=2.63ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=402.58ms min=3.39ms  med=376.89ms max=1.57s    p(90)=798.63ms p(95)=868.1ms  p(99.9)=1.27s 
     http_reqs......................: 35615   554.290501/s
     iteration_duration.............: avg=414.57ms min=21.4ms  med=391.13ms max=1.57s    p(90)=803.14ms p(95)=871.1ms  p(99.9)=1.28s 
     iterations.....................: 34615   538.727101/s
     success_rate...................: 100.00% ✓ 34615      ✗ 0    
     vus............................: 67      min=0        max=496
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 51747      ✗ 0    
     data_received..................: 1.6 GB  24 MB/s
     data_sent......................: 22 MB   329 kB/s
     http_req_blocked...............: avg=11.18µs  min=1.28µs  med=3.61µs   max=19.22ms p(90)=5.49µs   p(95)=7.16µs   p(99.9)=874.19µs
     http_req_connecting............: avg=5.98µs   min=0s      med=0s       max=19.15ms p(90)=0s       p(95)=0s       p(99.9)=850.37µs
     http_req_duration..............: avg=794.65ms min=5.22ms  med=713.97ms max=3.74s   p(90)=1.57s    p(95)=1.88s    p(99.9)=3.17s   
       { expected_response:true }...: avg=794.65ms min=5.22ms  med=713.97ms max=3.74s   p(90)=1.57s    p(95)=1.88s    p(99.9)=3.17s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 18249
     http_req_receiving.............: avg=98.11µs  min=35.37µs med=90.27µs  max=17.72ms p(90)=127.64µs p(95)=144.34µs p(99.9)=1.18ms  
     http_req_sending...............: avg=35.89µs  min=5.71µs  med=17.31µs  max=95.39ms p(90)=22.9µs   p(95)=26.28µs  p(99.9)=2.83ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=794.52ms min=5.11ms  med=713.87ms max=3.74s   p(90)=1.57s    p(95)=1.88s    p(99.9)=3.17s   
     http_reqs......................: 18249   274.075141/s
     iteration_duration.............: avg=840.84ms min=25.23ms med=775.25ms max=3.75s   p(90)=1.6s     p(95)=1.9s     p(99.9)=3.2s    
     iterations.....................: 17249   259.056502/s
     success_rate...................: 100.00% ✓ 17249      ✗ 0    
     vus............................: 86      min=0        max=500
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

     checks.........................: 100.00% ✓ 44970      ✗ 0    
     data_received..................: 1.4 GB  20 MB/s
     data_sent......................: 19 MB   280 kB/s
     http_req_blocked...............: avg=10.91µs  min=1.15µs  med=3.04µs   max=6.63ms  p(90)=4.73µs   p(95)=6.16µs   p(99.9)=1.08ms
     http_req_connecting............: avg=6.23µs   min=0s      med=0s       max=6.57ms  p(90)=0s       p(95)=0s       p(99.9)=1.06ms
     http_req_duration..............: avg=908.07ms min=7.64ms  med=827.17ms max=3.12s   p(90)=1.83s    p(95)=1.97s    p(99.9)=2.81s 
       { expected_response:true }...: avg=908.07ms min=7.64ms  med=827.17ms max=3.12s   p(90)=1.83s    p(95)=1.97s    p(99.9)=2.81s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 15990
     http_req_receiving.............: avg=96.95µs  min=32.38µs med=84.08µs  max=85.49ms p(90)=122.35µs p(95)=137.16µs p(99.9)=1.35ms
     http_req_sending...............: avg=41.27µs  min=5.15µs  med=15.68µs  max=96.9ms  p(90)=20.43µs  p(95)=24.11µs  p(99.9)=3.1ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=907.93ms min=7.56ms  med=827.08ms max=3.12s   p(90)=1.83s    p(95)=1.97s    p(99.9)=2.81s 
     http_reqs......................: 15990   232.887082/s
     iteration_duration.............: avg=968.59ms min=41.65ms med=893.4ms  max=3.12s   p(90)=1.86s    p(95)=1.98s    p(99.9)=2.84s 
     iterations.....................: 14990   218.322537/s
     success_rate...................: 100.00% ✓ 14990      ✗ 0    
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

