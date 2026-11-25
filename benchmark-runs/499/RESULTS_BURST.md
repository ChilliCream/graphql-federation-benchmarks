## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-fed-aot-11 | 16.7.7 | 4,780 | 4,783 | 4,763 | 0.2% | 147 MB | 31.6 KB |  |
| fusion-fed-net-11 | 16.7.7 | 4,770 | 4,785 | 4,769 | 0.2% | 395 MB | 84.7 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.21 | 4,763 | 4,897 | 4,757 | 1.2% | 389 MB | 83.5 KB |  |
| fusion-net-11 | 16.7.7 | 4,739 | 4,748 | 4,726 | 0.2% | 387 MB | 83.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.21 | 4,730 | 4,825 | 4,723 | 0.9% | 139 MB | 30.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.21 | 4,721 | 4,797 | 4,700 | 1.0% | 391 MB | 84.7 KB |  |
| fusion-aot-11 | 16.7.7 | 4,694 | 4,706 | 4,685 | 0.2% | 158 MB | 34.6 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.21 | 4,640 | 4,672 | 4,607 | 0.6% | 138 MB | 30.4 KB |  |
| feddi-gateway | 2026-11-22-1912 | 4,617 | 4,646 | 4,604 | 0.4% | 2,327 MB | 516.2 KB |  |
| hive-router-nightly | v0.3.19-nightly.be76f6cb | 3,991 | 4,070 | 3,976 | 1.0% | 188 MB | 48.1 KB |  |
| hive-router | v0.3.17 | 3,958 | 3,972 | 3,948 | 0.2% | 194 MB | 50.3 KB |  |
| caliban | 3.2.1 | 1,538 | 1,539 | 1,532 | 0.2% | 11,281 MB | 7,511.0 KB |  |
| cosmo | 0.373.0 | 1,317 | 1,323 | 1,314 | 0.3% | 620 MB | 481.9 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 559 | 560 | 551 | 0.7% | 3,030 MB | 5,550.7 KB |  |
| hive-gateway | 2.15.10 | 278 | 279 | 276 | 0.4% | 3,588 MB | 13,216.4 KB |  |
| apollo-gateway | 2.14.4 | 239 | 239 | 235 | 0.7% | 2,431 MB | 10,414.5 KB |  |
| apollo-router | v2.19.1 | — | — | — | — | — | — | non-compatible response (4545 across 5/5 runs) |
| apollo-router-nightly | v3.0.0-preview.0-nightly.0e21b2b0 | — | — | — | — | — | — | non-compatible response (5454 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (8431 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (110992 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 871245      ✗ 0     
     data_received..................: 26 GB   418 MB/s
     data_sent......................: 350 MB  5.7 MB/s
     http_req_blocked...............: avg=62.11µs  min=771ns    med=2.01µs  max=123.04ms p(90)=3.66µs   p(95)=4.84µs   p(99.9)=20.49ms 
     http_req_connecting............: avg=59.22µs  min=0s       med=0s      max=122.94ms p(90)=0s       p(95)=0s       p(99.9)=20.05ms 
     http_req_duration..............: avg=47.25ms  min=775.81µs med=39.31ms max=321.52ms p(90)=101.45ms p(95)=126.25ms p(99.9)=178.19ms
       { expected_response:true }...: avg=47.25ms  min=775.81µs med=39.31ms max=321.52ms p(90)=101.45ms p(95)=126.25ms p(99.9)=178.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 291415
     http_req_receiving.............: avg=327.8µs  min=21.94µs  med=51.37µs max=129.13ms p(90)=203.76µs p(95)=365.73µs p(99.9)=46.14ms 
     http_req_sending...............: avg=145.27µs min=4.08µs   med=8.33µs  max=218.69ms p(90)=16.42µs  p(95)=117.67µs p(99.9)=25.41ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.77ms  min=739.28µs med=39ms    max=292.22ms p(90)=100.3ms  p(95)=125.1ms  p(99.9)=173.57ms
     http_reqs......................: 291415  4780.955838/s
     iteration_duration.............: avg=49.04ms  min=1.36ms   med=40.3ms  max=331.79ms p(90)=105.21ms p(95)=131.1ms  p(99.9)=209.38ms
     iterations.....................: 290415  4764.549834/s
     success_rate...................: 100.00% ✓ 290415      ✗ 0     
     vus............................: 55      min=0         max=498 
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

     checks.........................: 100.00% ✓ 869004      ✗ 0     
     data_received..................: 25 GB   417 MB/s
     data_sent......................: 349 MB  5.7 MB/s
     http_req_blocked...............: avg=72.88µs  min=832ns    med=2.57µs  max=135.78ms p(90)=4.07µs   p(95)=5.24µs   p(99.9)=27.86ms 
     http_req_connecting............: avg=69.17µs  min=0s       med=0s      max=135.68ms p(90)=0s       p(95)=0s       p(99.9)=27.43ms 
     http_req_duration..............: avg=46.61ms  min=743µs    med=39.47ms max=314.33ms p(90)=96.83ms  p(95)=120.61ms p(99.9)=177.39ms
       { expected_response:true }...: avg=46.61ms  min=743µs    med=39.47ms max=314.33ms p(90)=96.83ms  p(95)=120.61ms p(99.9)=177.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290668
     http_req_receiving.............: avg=384.99µs min=22.19µs  med=54.19µs max=200.94ms p(90)=212.71µs p(95)=358.56µs p(99.9)=52.18ms 
     http_req_sending...............: avg=170.45µs min=4.19µs   med=9.23µs  max=108.9ms  p(90)=17.33µs  p(95)=117.05µs p(99.9)=31.94ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.05ms  min=704.19µs med=39.1ms  max=303.81ms p(90)=95.54ms  p(95)=119.15ms p(99.9)=171.17ms
     http_reqs......................: 290668  4770.787856/s
     iteration_duration.............: avg=49.17ms  min=1.15ms   med=40.64ms max=341.38ms p(90)=103.48ms p(95)=130.13ms p(99.9)=216.07ms
     iterations.....................: 289668  4754.37467/s
     success_rate...................: 100.00% ✓ 289668      ✗ 0     
     vus............................: 53      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 867360      ✗ 0     
     data_received..................: 25 GB   417 MB/s
     data_sent......................: 349 MB  5.7 MB/s
     http_req_blocked...............: avg=75.25µs  min=911ns    med=2.63µs  max=146.75ms p(90)=4.14µs   p(95)=5.34µs   p(99.9)=29.87ms 
     http_req_connecting............: avg=71.37µs  min=0s       med=0s      max=146.66ms p(90)=0s       p(95)=0s       p(99.9)=29.37ms 
     http_req_duration..............: avg=46.8ms   min=740.01µs med=39.94ms max=307.96ms p(90)=96.81ms  p(95)=120.37ms p(99.9)=175.78ms
       { expected_response:true }...: avg=46.8ms   min=740.01µs med=39.94ms max=307.96ms p(90)=96.81ms  p(95)=120.37ms p(99.9)=175.78ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 290120
     http_req_receiving.............: avg=360.52µs min=24.99µs  med=54.35µs max=195.14ms p(90)=204.81µs p(95)=355.76µs p(99.9)=47.25ms 
     http_req_sending...............: avg=168.67µs min=4.01µs   med=9.4µs   max=254.29ms p(90)=17.16µs  p(95)=114.46µs p(99.9)=29.79ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.27ms  min=700.51µs med=39.54ms max=302.3ms  p(90)=95.58ms  p(95)=118.99ms p(99.9)=171.86ms
     http_reqs......................: 290120  4763.170624/s
     iteration_duration.............: avg=49.26ms  min=1.2ms    med=40.83ms max=386.26ms p(90)=103.96ms p(95)=130.42ms p(99.9)=212.66ms
     iterations.....................: 289120  4746.752691/s
     success_rate...................: 100.00% ✓ 289120      ✗ 0     
     vus............................: 53      min=0         max=499 
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

     checks.........................: 100.00% ✓ 862950      ✗ 0     
     data_received..................: 25 GB   415 MB/s
     data_sent......................: 347 MB  5.7 MB/s
     http_req_blocked...............: avg=79.35µs  min=942ns    med=2.65µs  max=153.04ms p(90)=4.13µs   p(95)=5.33µs   p(99.9)=32.47ms 
     http_req_connecting............: avg=75.32µs  min=0s       med=0s      max=153ms    p(90)=0s       p(95)=0s       p(99.9)=31.6ms  
     http_req_duration..............: avg=47.32ms  min=726.14µs med=40.46ms max=337.62ms p(90)=98.76ms  p(95)=121.07ms p(99.9)=178.49ms
       { expected_response:true }...: avg=47.32ms  min=726.14µs med=40.46ms max=337.62ms p(90)=98.76ms  p(95)=121.07ms p(99.9)=178.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288650
     http_req_receiving.............: avg=378.09µs min=26.68µs  med=54.86µs max=139.42ms p(90)=213.54µs p(95)=363.48µs p(99.9)=49.62ms 
     http_req_sending...............: avg=171.37µs min=3.97µs   med=9.34µs  max=179.33ms p(90)=17.06µs  p(95)=117.77µs p(99.9)=30.99ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.77ms  min=689.42µs med=40.07ms max=328.15ms p(90)=97.35ms  p(95)=119.62ms p(99.9)=174.2ms 
     http_reqs......................: 288650  4739.89801/s
     iteration_duration.............: avg=49.51ms  min=1.07ms   med=41.28ms max=364.31ms p(90)=104.32ms p(95)=130.05ms p(99.9)=207.16ms
     iterations.....................: 287650  4723.477092/s
     success_rate...................: 100.00% ✓ 287650      ✗ 0     
     vus............................: 52      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 861990      ✗ 0     
     data_received..................: 25 GB   414 MB/s
     data_sent......................: 346 MB  5.7 MB/s
     http_req_blocked...............: avg=71.03µs  min=821ns    med=2.4µs   max=200.62ms p(90)=4µs      p(95)=5.18µs   p(99.9)=25.94ms 
     http_req_connecting............: avg=67.56µs  min=0s       med=0s      max=200.21ms p(90)=0s       p(95)=0s       p(99.9)=25.65ms 
     http_req_duration..............: avg=47.14ms  min=761.05µs med=39.6ms  max=296.79ms p(90)=99.1ms   p(95)=123.61ms p(99.9)=183.93ms
       { expected_response:true }...: avg=47.14ms  min=761.05µs med=39.6ms  max=296.79ms p(90)=99.1ms   p(95)=123.61ms p(99.9)=183.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288330
     http_req_receiving.............: avg=359.64µs min=25.5µs   med=52.96µs max=145.64ms p(90)=208.26µs p(95)=366.65µs p(99.9)=49.7ms  
     http_req_sending...............: avg=162.74µs min=4.05µs   med=9.06µs  max=217.31ms p(90)=16.93µs  p(95)=116.94µs p(99.9)=28.66ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.62ms  min=717.79µs med=39.26ms max=296.23ms p(90)=97.88ms  p(95)=122.11ms p(99.9)=178.29ms
     http_reqs......................: 288330  4730.944904/s
     iteration_duration.............: avg=49.57ms  min=1.23ms   med=40.53ms max=331.22ms p(90)=106.05ms p(95)=133.35ms p(99.9)=220.34ms
     iterations.....................: 287330  4714.536813/s
     success_rate...................: 100.00% ✓ 287330      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 859710      ✗ 0     
     data_received..................: 25 GB   413 MB/s
     data_sent......................: 346 MB  5.7 MB/s
     http_req_blocked...............: avg=74.53µs  min=972ns    med=2.65µs  max=149.23ms p(90)=4.11µs   p(95)=5.23µs   p(99.9)=28.4ms  
     http_req_connecting............: avg=70.02µs  min=0s       med=0s      max=149.12ms p(90)=0s       p(95)=0s       p(99.9)=27.53ms 
     http_req_duration..............: avg=47.36ms  min=734.1µs  med=40.14ms max=323.94ms p(90)=98.62ms  p(95)=121.46ms p(99.9)=177.32ms
       { expected_response:true }...: avg=47.36ms  min=734.1µs  med=40.14ms max=323.94ms p(90)=98.62ms  p(95)=121.46ms p(99.9)=177.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 287570
     http_req_receiving.............: avg=359.91µs min=26.47µs  med=55.36µs max=119.38ms p(90)=214.89µs p(95)=363.79µs p(99.9)=48.71ms 
     http_req_sending...............: avg=160.09µs min=3.96µs   med=9.36µs  max=219.97ms p(90)=16.71µs  p(95)=115.97µs p(99.9)=28.77ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.84ms  min=697.73µs med=39.78ms max=314.56ms p(90)=97.36ms  p(95)=120.1ms  p(99.9)=172.74ms
     http_reqs......................: 287570  4721.246852/s
     iteration_duration.............: avg=49.7ms   min=1.2ms    med=41.13ms max=351.53ms p(90)=104.83ms p(95)=129.88ms p(99.9)=211.77ms
     iterations.....................: 286570  4704.829121/s
     success_rate...................: 100.00% ✓ 286570      ✗ 0     
     vus............................: 54      min=0         max=499 
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

     checks.........................: 100.00% ✓ 855735      ✗ 0     
     data_received..................: 25 GB   411 MB/s
     data_sent......................: 344 MB  5.6 MB/s
     http_req_blocked...............: avg=55.88µs  min=781ns    med=2.04µs  max=117.07ms p(90)=3.6µs    p(95)=4.69µs   p(99.9)=18.19ms 
     http_req_connecting............: avg=52.59µs  min=0s       med=0s      max=117.01ms p(90)=0s       p(95)=0s       p(99.9)=18.04ms 
     http_req_duration..............: avg=48.22ms  min=784.37µs med=40.45ms max=316.19ms p(90)=103.9ms  p(95)=129.13ms p(99.9)=181.54ms
       { expected_response:true }...: avg=48.22ms  min=784.37µs med=40.45ms max=316.19ms p(90)=103.9ms  p(95)=129.13ms p(99.9)=181.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 286245
     http_req_receiving.............: avg=313.81µs min=23.98µs  med=50.79µs max=103.19ms p(90)=214µs    p(95)=379.91µs p(99.9)=41.27ms 
     http_req_sending...............: avg=137.78µs min=4µs      med=8.48µs  max=254ms    p(90)=16.51µs  p(95)=120.75µs p(99.9)=25.27ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.77ms  min=739.56µs med=40.16ms max=301.31ms p(90)=102.77ms p(95)=127.89ms p(99.9)=177.54ms
     http_reqs......................: 286245  4694.635472/s
     iteration_duration.............: avg=49.94ms  min=1.25ms   med=41.24ms max=326.22ms p(90)=107.53ms p(95)=133.81ms p(99.9)=218.8ms 
     iterations.....................: 285245  4678.234712/s
     success_rate...................: 100.00% ✓ 285245      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.21)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 845688      ✗ 0     
     data_received..................: 25 GB   406 MB/s
     data_sent......................: 340 MB  5.6 MB/s
     http_req_blocked...............: avg=67.34µs  min=852ns    med=2.53µs  max=146.33ms p(90)=4.12µs   p(95)=5.29µs   p(99.9)=23.84ms 
     http_req_connecting............: avg=63.39µs  min=0s       med=0s      max=146.26ms p(90)=0s       p(95)=0s       p(99.9)=23.54ms 
     http_req_duration..............: avg=48.49ms  min=756µs    med=39.94ms max=268.76ms p(90)=104.22ms p(95)=130.24ms p(99.9)=186.42ms
       { expected_response:true }...: avg=48.49ms  min=756µs    med=39.94ms max=268.76ms p(90)=104.22ms p(95)=130.24ms p(99.9)=186.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 282896
     http_req_receiving.............: avg=348.54µs min=24.45µs  med=52.79µs max=209.87ms p(90)=218.88µs p(95)=381.42µs p(99.9)=45.57ms 
     http_req_sending...............: avg=159.07µs min=3.94µs   med=9.14µs  max=163.63ms p(90)=17.81µs  p(95)=123.65µs p(99.9)=28.81ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.98ms  min=716.47µs med=39.61ms max=268.46ms p(90)=103.02ms p(95)=128.91ms p(99.9)=179.82ms
     http_reqs......................: 282896  4640.476499/s
     iteration_duration.............: avg=50.52ms  min=1.23ms   med=41.06ms max=324.44ms p(90)=108.69ms p(95)=136.83ms p(99.9)=210.09ms
     iterations.....................: 281896  4624.073028/s
     success_rate...................: 100.00% ✓ 281896      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-22-1912)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 841152      ✗ 0     
     data_received..................: 25 GB   404 MB/s
     data_sent......................: 338 MB  5.5 MB/s
     http_req_blocked...............: avg=72.07µs  min=811ns    med=2.4µs   max=155.97ms p(90)=4.11µs   p(95)=5.2µs    p(99.9)=29.21ms 
     http_req_connecting............: avg=68.02µs  min=0s       med=0s      max=155.86ms p(90)=0s       p(95)=0s       p(99.9)=28.66ms 
     http_req_duration..............: avg=48.38ms  min=746.49µs med=40.56ms max=326.82ms p(90)=101.71ms p(95)=126.07ms p(99.9)=194.88ms
       { expected_response:true }...: avg=48.38ms  min=746.49µs med=40.56ms max=326.82ms p(90)=101.71ms p(95)=126.07ms p(99.9)=194.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281384
     http_req_receiving.............: avg=357.43µs min=21.44µs  med=54.51µs max=172.93ms p(90)=215.06µs p(95)=374.26µs p(99.9)=50.92ms 
     http_req_sending...............: avg=162.99µs min=3.97µs   med=9.41µs  max=153.15ms p(90)=17.36µs  p(95)=119.12µs p(99.9)=29.3ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.86ms  min=707.01µs med=40.19ms max=297.53ms p(90)=100.59ms p(95)=124.78ms p(99.9)=186.74ms
     http_reqs......................: 281384  4617.297757/s
     iteration_duration.............: avg=50.8ms   min=1.23ms   med=41.73ms max=336.77ms p(90)=107.83ms p(95)=135.15ms p(99.9)=226.91ms
     iterations.....................: 280384  4600.888516/s
     success_rate...................: 100.00% ✓ 280384      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.be76f6cb)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 728352      ✗ 0     
     data_received..................: 21 GB   349 MB/s
     data_sent......................: 293 MB  4.8 MB/s
     http_req_blocked...............: avg=50.81µs  min=932ns    med=2.77µs  max=114.03ms p(90)=4.55µs   p(95)=5.86µs   p(99.9)=10.18ms 
     http_req_connecting............: avg=46.77µs  min=0s       med=0s      max=113.79ms p(90)=0s       p(95)=0s       p(99.9)=9.42ms  
     http_req_duration..............: avg=57.41ms  min=866.16µs med=48.59ms max=302.39ms p(90)=122.53ms p(95)=154.02ms p(99.9)=218.9ms 
       { expected_response:true }...: avg=57.41ms  min=866.16µs med=48.59ms max=302.39ms p(90)=122.53ms p(95)=154.02ms p(99.9)=218.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 243784
     http_req_receiving.............: avg=298.39µs min=26.39µs  med=55.48µs max=175.79ms p(90)=224.43µs p(95)=405.45µs p(99.9)=44.28ms 
     http_req_sending...............: avg=130.98µs min=4.26µs   med=9.69µs  max=194.25ms p(90)=18.84µs  p(95)=133.84µs p(99.9)=25.1ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=56.98ms  min=812.23µs med=48.32ms max=298.37ms p(90)=121.49ms p(95)=152.77ms p(99.9)=214.96ms
     http_reqs......................: 243784  3991.116167/s
     iteration_duration.............: avg=58.68ms  min=1.55ms   med=49.33ms max=335.03ms p(90)=125.65ms p(95)=157.31ms p(99.9)=235.46ms
     iterations.....................: 242784  3974.74464/s
     success_rate...................: 100.00% ✓ 242784      ✗ 0     
     vus............................: 60      min=0         max=497 
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

     checks.........................: 100.00% ✓ 722586      ✗ 0     
     data_received..................: 21 GB   346 MB/s
     data_sent......................: 291 MB  4.8 MB/s
     http_req_blocked...............: avg=52.38µs  min=942ns    med=2.84µs  max=119.67ms p(90)=4.62µs   p(95)=5.9µs    p(99.9)=12.12ms 
     http_req_connecting............: avg=47.77µs  min=0s       med=0s      max=119.56ms p(90)=0s       p(95)=0s       p(99.9)=11.45ms 
     http_req_duration..............: avg=57.7ms   min=888.93µs med=48.91ms max=327.39ms p(90)=122.85ms p(95)=152.65ms p(99.9)=213.42ms
       { expected_response:true }...: avg=57.7ms   min=888.93µs med=48.91ms max=327.39ms p(90)=122.85ms p(95)=152.65ms p(99.9)=213.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 241862
     http_req_receiving.............: avg=292.59µs min=24µs     med=55.7µs  max=99.71ms  p(90)=226.17µs p(95)=404.62µs p(99.9)=43.14ms 
     http_req_sending...............: avg=129µs    min=4.04µs   med=9.94µs  max=241.36ms p(90)=19.18µs  p(95)=134.57µs p(99.9)=23.18ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=57.28ms  min=836.77µs med=48.65ms max=294.08ms p(90)=121.98ms p(95)=151.66ms p(99.9)=209.29ms
     http_reqs......................: 241862  3958.83457/s
     iteration_duration.............: avg=59.15ms  min=1.47ms   med=49.82ms max=338.11ms p(90)=125.99ms p(95)=156.14ms p(99.9)=241.81ms
     iterations.....................: 240862  3942.466416/s
     success_rate...................: 100.00% ✓ 240862      ✗ 0     
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

     checks.........................: 100.00% ✓ 284517      ✗ 0    
     data_received..................: 8.4 GB  135 MB/s
     data_sent......................: 115 MB  1.8 MB/s
     http_req_blocked...............: avg=6.32µs   min=971ns   med=2.79µs   max=24.88ms  p(90)=4.89µs   p(95)=5.95µs   p(99.9)=313.11µs
     http_req_connecting............: avg=2.86µs   min=0s      med=0s       max=24.77ms  p(90)=0s       p(95)=0s       p(99.9)=255.83µs
     http_req_duration..............: avg=148.73ms min=1.9ms   med=125.25ms max=936.26ms p(90)=308.82ms p(95)=365.71ms p(99.9)=667.85ms
       { expected_response:true }...: avg=148.73ms min=1.9ms   med=125.25ms max=936.26ms p(90)=308.82ms p(95)=365.71ms p(99.9)=667.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 95839
     http_req_receiving.............: avg=81.47µs  min=26.81µs med=60.36µs  max=151.59ms p(90)=102.74µs p(95)=124.63µs p(99.9)=2.26ms  
     http_req_sending...............: avg=39.08µs  min=4.83µs  med=12.05µs  max=159.24ms p(90)=20.5µs   p(95)=25.32µs  p(99.9)=4.64ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=148.61ms min=1.85ms  med=125.13ms max=935.96ms p(90)=308.71ms p(95)=365.6ms  p(99.9)=667.79ms
     http_reqs......................: 95839   1538.293928/s
     iteration_duration.............: avg=150.54ms min=7.23ms  med=127.25ms max=936.43ms p(90)=310.07ms p(95)=366.8ms  p(99.9)=669.25ms
     iterations.....................: 94839   1522.243114/s
     success_rate...................: 100.00% ✓ 94839       ✗ 0    
     vus............................: 70      min=0         max=495
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

     checks.........................: 100.00% ✓ 243807      ✗ 0    
     data_received..................: 7.2 GB  115 MB/s
     data_sent......................: 99 MB   1.6 MB/s
     http_req_blocked...............: avg=5.79µs   min=932ns   med=2.35µs   max=29.76ms  p(90)=4µs      p(95)=4.91µs   p(99.9)=259.09µs
     http_req_connecting............: avg=2.48µs   min=0s      med=0s       max=29.6ms   p(90)=0s       p(95)=0s       p(99.9)=194.82µs
     http_req_duration..............: avg=173.39ms min=1.99ms  med=171.5ms  max=464.39ms p(90)=327.58ms p(95)=351.75ms p(99.9)=422.63ms
       { expected_response:true }...: avg=173.39ms min=1.99ms  med=171.5ms  max=464.39ms p(90)=327.58ms p(95)=351.75ms p(99.9)=422.63ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 82269
     http_req_receiving.............: avg=73.87µs  min=26.49µs med=58.78µs  max=102.63ms p(90)=96.78µs  p(95)=114.14µs p(99.9)=1.15ms  
     http_req_sending...............: avg=30.35µs  min=4.66µs  med=10.37µs  max=112.03ms p(90)=16.99µs  p(95)=20.74µs  p(99.9)=3.47ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=173.28ms min=1.93ms  med=171.39ms max=464.34ms p(90)=327.47ms p(95)=351.65ms p(99.9)=422.54ms
     http_reqs......................: 82269   1317.399489/s
     iteration_duration.............: avg=175.75ms min=4.95ms  med=174.3ms  max=464.58ms p(90)=328.3ms  p(95)=352.3ms  p(99.9)=423.04ms
     iterations.....................: 81269   1301.386173/s
     success_rate...................: 100.00% ✓ 81269       ✗ 0    
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

     checks.........................: 100.00% ✓ 104775     ✗ 0    
     data_received..................: 3.1 GB  49 MB/s
     data_sent......................: 43 MB   672 kB/s
     http_req_blocked...............: avg=8.56µs   min=1.04µs  med=3.13µs   max=8.34ms   p(90)=4.9µs    p(95)=5.93µs   p(99.9)=1.47ms
     http_req_connecting............: avg=4.49µs   min=0s      med=0s       max=8.27ms   p(90)=0s       p(95)=0s       p(99.9)=1.41ms
     http_req_duration..............: avg=399.37ms min=3.4ms   med=369.19ms max=1.59s    p(90)=793.72ms p(95)=864.78ms p(99.9)=1.25s 
       { expected_response:true }...: avg=399.37ms min=3.4ms   med=369.19ms max=1.59s    p(90)=793.72ms p(95)=864.78ms p(99.9)=1.25s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 35925
     http_req_receiving.............: avg=84.53µs  min=30.22µs med=72.44µs  max=87.88ms  p(90)=109.82µs p(95)=124.81µs p(99.9)=1.32ms
     http_req_sending...............: avg=37.68µs  min=5.18µs  med=14.3µs   max=164.62ms p(90)=20.99µs  p(95)=23.71µs  p(99.9)=2.38ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=399.24ms min=3.34ms  med=369.07ms max=1.59s    p(90)=793.63ms p(95)=864.68ms p(99.9)=1.25s 
     http_reqs......................: 35925   559.765537/s
     iteration_duration.............: avg=411.07ms min=21.94ms med=383.7ms  max=1.6s     p(90)=797.46ms p(95)=868.47ms p(99.9)=1.25s 
     iterations.....................: 34925   544.184033/s
     success_rate...................: 100.00% ✓ 34925      ✗ 0    
     vus............................: 64      min=0        max=497
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

     checks.........................: 100.00% ✓ 52800      ✗ 0    
     data_received..................: 1.6 GB  24 MB/s
     data_sent......................: 22 MB   334 kB/s
     http_req_blocked...............: avg=14.73µs  min=1.54µs  med=3.75µs   max=11.5ms  p(90)=5.62µs   p(95)=7.16µs  p(99.9)=2.12ms
     http_req_connecting............: avg=9.35µs   min=0s      med=0s       max=11.44ms p(90)=0s       p(95)=0s      p(99.9)=2.09ms
     http_req_duration..............: avg=779.71ms min=5.15ms  med=687.35ms max=3.85s   p(90)=1.55s    p(95)=1.87s   p(99.9)=3.22s 
       { expected_response:true }...: avg=779.71ms min=5.15ms  med=687.35ms max=3.85s   p(90)=1.55s    p(95)=1.87s   p(99.9)=3.22s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 18600
     http_req_receiving.............: avg=100.7µs  min=35.4µs  med=90.99µs  max=9.07ms  p(90)=130.27µs p(95)=148.3µs p(99.9)=1.26ms
     http_req_sending...............: avg=30.11µs  min=6.13µs  med=18.26µs  max=22.14ms p(90)=24.03µs  p(95)=27.64µs p(99.9)=2.98ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s      p(99.9)=0s    
     http_req_waiting...............: avg=779.58ms min=5.05ms  med=687.21ms max=3.85s   p(90)=1.55s    p(95)=1.87s   p(99.9)=3.22s 
     http_reqs......................: 18600   278.150803/s
     iteration_duration.............: avg=824.12ms min=43.63ms med=741.6ms  max=3.85s   p(90)=1.58s    p(95)=1.88s   p(99.9)=3.23s 
     iterations.....................: 17600   263.196459/s
     success_rate...................: 100.00% ✓ 17600      ✗ 0    
     vus............................: 3       min=0        max=500
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

     checks.........................: 100.00% ✓ 46095      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   288 kB/s
     http_req_blocked...............: avg=14.26µs  min=1.1µs   med=3.11µs   max=6.21ms   p(90)=4.67µs   p(95)=6.04µs   p(99.9)=2.26ms
     http_req_connecting............: avg=9.51µs   min=0s      med=0s       max=6.15ms   p(90)=0s       p(95)=0s       p(99.9)=2.22ms
     http_req_duration..............: avg=887.77ms min=7.41ms  med=824.97ms max=2.96s    p(90)=1.81s    p(95)=1.95s    p(99.9)=2.69s 
       { expected_response:true }...: avg=887.77ms min=7.41ms  med=824.97ms max=2.96s    p(90)=1.81s    p(95)=1.95s    p(99.9)=2.69s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16365
     http_req_receiving.............: avg=97.68µs  min=32.44µs med=85.55µs  max=96.93ms  p(90)=124.24µs p(95)=139.43µs p(99.9)=1.15ms
     http_req_sending...............: avg=33.54µs  min=5.31µs  med=15.77µs  max=133.48ms p(90)=20.44µs  p(95)=23.92µs  p(99.9)=2.79ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=887.64ms min=7.33ms  med=824.86ms max=2.96s    p(90)=1.81s    p(95)=1.95s    p(99.9)=2.69s 
     http_reqs......................: 16365   239.564604/s
     iteration_duration.............: avg=945.57ms min=21.55ms med=881.48ms max=2.97s    p(90)=1.83s    p(95)=1.96s    p(99.9)=2.71s 
     iterations.....................: 15365   224.925765/s
     success_rate...................: 100.00% ✓ 15365      ✗ 0    
     vus............................: 71      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

