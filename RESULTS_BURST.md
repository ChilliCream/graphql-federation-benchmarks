## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.10 | 4,775 | 4,781 | 4,769 | 0.1% | 411 MB | 88.1 KB |  |
| fusion-net-11 | 16.7.5 | 4,592 | 4,718 | 4,565 | 1.5% | 423 MB | 94.3 KB |  |
| fusion-aot-11 | 16.7.5 | 4,568 | 4,583 | 4,549 | 0.3% | 160 MB | 35.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.10 | 4,516 | 4,607 | 4,461 | 1.2% | 419 MB | 94.9 KB |  |
| fusion-fed-net-11 | 16.7.5 | 4,511 | 4,538 | 4,508 | 0.3% | 422 MB | 95.8 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.10 | 4,424 | 4,488 | 4,404 | 0.7% | 153 MB | 35.5 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 4,408 | 4,416 | 4,334 | 0.8% | 185 MB | 42.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.10 | 4,290 | 4,305 | 4,284 | 0.2% | 191 MB | 45.7 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,163 | 4,201 | 4,133 | 0.6% | 2,308 MB | 567.7 KB |  |
| hive-router | v0.3.10 | 2,631 | 2,635 | 2,629 | 0.1% | 166 MB | 64.6 KB |  |
| cosmo | 0.365.2 | 1,346 | 1,349 | 1,343 | 0.2% | 554 MB | 421.5 KB |  |
| caliban | 3.2.0 | 1,333 | 1,335 | 1,331 | 0.1% | 10,808 MB | 8,302.7 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 504 | 506 | 496 | 0.8% | 3,164 MB | 6,428.8 KB |  |
| hive-gateway | 2.15.6 | 244 | 245 | 242 | 0.5% | 3,972 MB | 16,670.2 KB |  |
| apollo-gateway | 2.14.4 | 239 | 240 | 237 | 0.5% | 2,481 MB | 10,629.6 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (7245 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (10120 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (118247 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 870744      ✗ 0     
     data_received..................: 26 GB   418 MB/s
     data_sent......................: 350 MB  5.7 MB/s
     http_req_blocked...............: avg=64.56µs  min=792ns    med=2.09µs  max=132.37ms p(90)=3.73µs   p(95)=4.87µs   p(99.9)=24.27ms 
     http_req_connecting............: avg=61.57µs  min=0s       med=0s      max=132.29ms p(90)=0s       p(95)=0s       p(99.9)=24.19ms 
     http_req_duration..............: avg=47.12ms  min=781.86µs med=39.91ms max=256.73ms p(90)=98.33ms  p(95)=122.03ms p(99.9)=173.29ms
       { expected_response:true }...: avg=47.12ms  min=781.86µs med=39.91ms max=256.73ms p(90)=98.33ms  p(95)=122.03ms p(99.9)=173.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 291248
     http_req_receiving.............: avg=331.54µs min=25.7µs   med=51.41µs max=107.15ms p(90)=201.97µs p(95)=355.92µs p(99.9)=42.92ms 
     http_req_sending...............: avg=146.37µs min=4.06µs   med=8.62µs  max=103.2ms  p(90)=16.72µs  p(95)=114.01µs p(99.9)=26.56ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=46.64ms  min=731.16µs med=39.57ms max=252.96ms p(90)=97.16ms  p(95)=120.95ms p(99.9)=168.43ms
     http_reqs......................: 291248  4775.388287/s
     iteration_duration.............: avg=49.07ms  min=1.31ms   med=40.69ms max=319.57ms p(90)=103.2ms  p(95)=128.91ms p(99.9)=219.5ms 
     iterations.....................: 290248  4758.991992/s
     success_rate...................: 100.00% ✓ 290248      ✗ 0     
     vus............................: 56      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 836817      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 336 MB  5.5 MB/s
     http_req_blocked...............: avg=70.94µs  min=811ns    med=2.46µs  max=154.07ms p(90)=4.09µs   p(95)=5.27µs   p(99.9)=24.85ms 
     http_req_connecting............: avg=66.69µs  min=0s       med=0s      max=147.1ms  p(90)=0s       p(95)=0s       p(99.9)=24.22ms 
     http_req_duration..............: avg=48.92ms  min=766.11µs med=40.88ms max=346.13ms p(90)=103.06ms p(95)=128.13ms p(99.9)=186.05ms
       { expected_response:true }...: avg=48.92ms  min=766.11µs med=40.88ms max=346.13ms p(90)=103.06ms p(95)=128.13ms p(99.9)=186.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 279939
     http_req_receiving.............: avg=339.02µs min=22.06µs  med=54.04µs max=173.09ms p(90)=216.2µs  p(95)=373.68µs p(99.9)=44.85ms 
     http_req_sending...............: avg=163.87µs min=4.04µs   med=8.92µs  max=164.16ms p(90)=17.49µs  p(95)=120.93µs p(99.9)=29.49ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.42ms  min=717.22µs med=40.56ms max=336.55ms p(90)=101.77ms p(95)=126.71ms p(99.9)=182.33ms
     http_reqs......................: 279939  4592.829673/s
     iteration_duration.............: avg=51.06ms  min=1.17ms   med=41.91ms max=356.38ms p(90)=108.69ms p(95)=135.84ms p(99.9)=221.06ms
     iterations.....................: 278939  4576.423136/s
     success_rate...................: 100.00% ✓ 278939      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 833277      ✗ 0     
     data_received..................: 24 GB   400 MB/s
     data_sent......................: 335 MB  5.5 MB/s
     http_req_blocked...............: avg=54.72µs  min=781ns    med=2.05µs  max=125.07ms p(90)=3.58µs   p(95)=4.65µs   p(99.9)=18.83ms 
     http_req_connecting............: avg=51.66µs  min=0s       med=0s      max=124.82ms p(90)=0s       p(95)=0s       p(99.9)=18.72ms 
     http_req_duration..............: avg=49.78ms  min=834.96µs med=41.85ms max=312.48ms p(90)=106.22ms p(95)=131.83ms p(99.9)=182.23ms
       { expected_response:true }...: avg=49.78ms  min=834.96µs med=41.85ms max=312.48ms p(90)=106.22ms p(95)=131.83ms p(99.9)=182.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 278759
     http_req_receiving.............: avg=291.66µs min=23.38µs  med=50.2µs  max=112.35ms p(90)=213.87µs p(95)=375.85µs p(99.9)=39.48ms 
     http_req_sending...............: avg=137.95µs min=4.18µs   med=8.52µs  max=220.84ms p(90)=16.9µs   p(95)=121.26µs p(99.9)=25.24ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.35ms  min=791.46µs med=41.56ms max=311.88ms p(90)=105.29ms p(95)=130.79ms p(99.9)=179.2ms 
     http_reqs......................: 278759  4568.735278/s
     iteration_duration.............: avg=51.28ms  min=1.42ms   med=42.73ms max=321.8ms  p(90)=109.36ms p(95)=135.73ms p(99.9)=206.28ms
     iterations.....................: 277759  4552.345726/s
     success_rate...................: 100.00% ✓ 277759      ✗ 0     
     vus............................: 57      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 825297      ✗ 0     
     data_received..................: 24 GB   395 MB/s
     data_sent......................: 332 MB  5.4 MB/s
     http_req_blocked...............: avg=70.59µs  min=832ns    med=2.45µs  max=134.51ms p(90)=4.15µs   p(95)=5.37µs   p(99.9)=25.84ms 
     http_req_connecting............: avg=66.78µs  min=0s       med=0s      max=134.43ms p(90)=0s       p(95)=0s       p(99.9)=25.59ms 
     http_req_duration..............: avg=49.95ms  min=917.15µs med=41.66ms max=319.82ms p(90)=105.8ms  p(95)=132.12ms p(99.9)=189.15ms
       { expected_response:true }...: avg=49.95ms  min=917.15µs med=41.66ms max=319.82ms p(90)=105.8ms  p(95)=132.12ms p(99.9)=189.15ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 276099
     http_req_receiving.............: avg=381.86µs min=26.08µs  med=54.36µs max=122.38ms p(90)=218.47µs p(95)=377.36µs p(99.9)=58.53ms 
     http_req_sending...............: avg=165.47µs min=4.32µs   med=9.27µs  max=233.86ms p(90)=18.44µs  p(95)=122.87µs p(99.9)=30.94ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.4ms   min=871.63µs med=41.31ms max=319.59ms p(90)=104.46ms p(95)=130.54ms p(99.9)=182.26ms
     http_reqs......................: 276099  4516.837099/s
     iteration_duration.............: avg=51.78ms  min=1.5ms    med=42.48ms max=353.16ms p(90)=110.09ms p(95)=138.36ms p(99.9)=215.25ms
     iterations.....................: 275099  4500.477616/s
     success_rate...................: 100.00% ✓ 275099      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 824097      ✗ 0     
     data_received..................: 24 GB   395 MB/s
     data_sent......................: 331 MB  5.4 MB/s
     http_req_blocked...............: avg=55.78µs  min=811ns    med=2.06µs  max=125.78ms p(90)=3.64µs   p(95)=4.72µs   p(99.9)=21.04ms 
     http_req_connecting............: avg=52.53µs  min=0s       med=0s      max=125.64ms p(90)=0s       p(95)=0s       p(99.9)=20.59ms 
     http_req_duration..............: avg=50.2ms   min=898.1µs  med=42.8ms  max=322.52ms p(90)=106.06ms p(95)=130.29ms p(99.9)=185ms   
       { expected_response:true }...: avg=50.2ms   min=898.1µs  med=42.8ms  max=322.52ms p(90)=106.06ms p(95)=130.29ms p(99.9)=185ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 275699
     http_req_receiving.............: avg=310.84µs min=25.4µs   med=52.2µs  max=117.57ms p(90)=214.4µs  p(95)=380.28µs p(99.9)=45.57ms 
     http_req_sending...............: avg=135.27µs min=4.15µs   med=8.6µs   max=92.98ms  p(90)=17.45µs  p(95)=121.66µs p(99.9)=23.99ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.75ms  min=853.32µs med=42.53ms max=318.22ms p(90)=105.09ms p(95)=129.27ms p(99.9)=177.75ms
     http_reqs......................: 275699  4511.041604/s
     iteration_duration.............: avg=51.85ms  min=1.57ms   med=43.57ms max=332.9ms  p(90)=109.61ms p(95)=135.04ms p(99.9)=224.52ms
     iterations.....................: 274699  4494.679406/s
     success_rate...................: 100.00% ✓ 274699      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 807228      ✗ 0     
     data_received..................: 24 GB   387 MB/s
     data_sent......................: 325 MB  5.3 MB/s
     http_req_blocked...............: avg=60.13µs  min=912ns    med=2.51µs  max=129.16ms p(90)=4.16µs   p(95)=5.35µs   p(99.9)=22.27ms 
     http_req_connecting............: avg=55.6µs   min=0s       med=0s      max=129.1ms  p(90)=0s       p(95)=0s       p(99.9)=21.7ms  
     http_req_duration..............: avg=51.62ms  min=843.43µs med=43.15ms max=309.36ms p(90)=111.22ms p(95)=137.87ms p(99.9)=195.39ms
       { expected_response:true }...: avg=51.62ms  min=843.43µs med=43.15ms max=309.36ms p(90)=111.22ms p(95)=137.87ms p(99.9)=195.39ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 270076
     http_req_receiving.............: avg=322.75µs min=25.33µs  med=51.72µs max=115.32ms p(90)=231.12µs p(95)=404.65µs p(99.9)=44.84ms 
     http_req_sending...............: avg=139.49µs min=4.17µs   med=9.08µs  max=162.77ms p(90)=18.48µs  p(95)=131.64µs p(99.9)=25.35ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.16ms  min=804.13µs med=42.85ms max=309.21ms p(90)=110.12ms p(95)=136.69ms p(99.9)=188.7ms 
     http_reqs......................: 270076  4424.152101/s
     iteration_duration.............: avg=52.94ms  min=1.34ms   med=43.85ms max=320.22ms p(90)=113.81ms p(95)=141.77ms p(99.9)=212.68ms
     iterations.....................: 269076  4407.770964/s
     success_rate...................: 100.00% ✓ 269076      ✗ 0     
     vus............................: 58      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 806679      ✗ 0     
     data_received..................: 24 GB   386 MB/s
     data_sent......................: 324 MB  5.3 MB/s
     http_req_blocked...............: avg=45.28µs  min=801ns    med=2.08µs  max=169.68ms p(90)=3.76µs   p(95)=4.95µs   p(99.9)=12.39ms 
     http_req_connecting............: avg=41.74µs  min=0s       med=0s      max=113.37ms p(90)=0s       p(95)=0s       p(99.9)=11.79ms 
     http_req_duration..............: avg=51.66ms  min=1ms      med=43.4ms  max=326.78ms p(90)=110.32ms p(95)=135.77ms p(99.9)=189.19ms
       { expected_response:true }...: avg=51.66ms  min=1ms      med=43.4ms  max=326.78ms p(90)=110.32ms p(95)=135.77ms p(99.9)=189.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 269893
     http_req_receiving.............: avg=290.92µs min=25.42µs  med=49.88µs max=108.33ms p(90)=218.43µs p(95)=377.57µs p(99.9)=40.92ms 
     http_req_sending...............: avg=123.65µs min=4.31µs   med=8.55µs  max=156.22ms p(90)=18.86µs  p(95)=125.06µs p(99.9)=22.33ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.25ms  min=958.26µs med=43.13ms max=320.79ms p(90)=109.52ms p(95)=134.75ms p(99.9)=183.96ms
     http_reqs......................: 269893  4408.582157/s
     iteration_duration.............: avg=52.98ms  min=1.65ms   med=44.24ms max=339.79ms p(90)=113.04ms p(95)=138.87ms p(99.9)=212.35ms
     iterations.....................: 268893  4392.247602/s
     success_rate...................: 100.00% ✓ 268893      ✗ 0     
     vus............................: 67      min=0         max=495 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 784683      ✗ 0     
     data_received..................: 23 GB   375 MB/s
     data_sent......................: 315 MB  5.2 MB/s
     http_req_blocked...............: avg=39.3µs   min=822ns    med=2.13µs  max=99.5ms   p(90)=3.77µs   p(95)=4.94µs   p(99.9)=9.91ms  
     http_req_connecting............: avg=35.6µs   min=0s       med=0s      max=99.42ms  p(90)=0s       p(95)=0s       p(99.9)=9.41ms  
     http_req_duration..............: avg=53.55ms  min=994.97µs med=45.34ms max=271.92ms p(90)=112.87ms p(95)=139.64ms p(99.9)=196.24ms
       { expected_response:true }...: avg=53.55ms  min=994.97µs med=45.34ms max=271.92ms p(90)=112.87ms p(95)=139.64ms p(99.9)=196.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 262561
     http_req_receiving.............: avg=271.45µs min=24.84µs  med=49.64µs max=161.16ms p(90)=218.94µs p(95)=376.43µs p(99.9)=38.43ms 
     http_req_sending...............: avg=105.2µs  min=4.3µs    med=8.52µs  max=235.03ms p(90)=17.83µs  p(95)=123.4µs  p(99.9)=18.73ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.17ms  min=957.47µs med=45.08ms max=248.92ms p(90)=112.08ms p(95)=138.6ms  p(99.9)=193.28ms
     http_reqs......................: 262561  4290.059472/s
     iteration_duration.............: avg=54.47ms  min=1.61ms   med=45.92ms max=336.04ms p(90)=114.66ms p(95)=141.66ms p(99.9)=205.99ms
     iterations.....................: 261561  4273.720185/s
     success_rate...................: 100.00% ✓ 261561      ✗ 0     
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

     checks.........................: 100.00% ✓ 758388      ✗ 0     
     data_received..................: 22 GB   364 MB/s
     data_sent......................: 305 MB  5.0 MB/s
     http_req_blocked...............: avg=50.06µs  min=841ns    med=2.45µs  max=111.84ms p(90)=4.3µs    p(95)=5.53µs   p(99.9)=12.04ms 
     http_req_connecting............: avg=46.24µs  min=0s       med=0s      max=111.56ms p(90)=0s       p(95)=0s       p(99.9)=11.72ms 
     http_req_duration..............: avg=55.1ms   min=722.19µs med=45.25ms max=324.42ms p(90)=117.8ms  p(95)=149.71ms p(99.9)=229.09ms
       { expected_response:true }...: avg=55.1ms   min=722.19µs med=45.25ms max=324.42ms p(90)=117.8ms  p(95)=149.71ms p(99.9)=229.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 253796
     http_req_receiving.............: avg=272.15µs min=21.41µs  med=52.25µs max=96.81ms  p(90)=216.33µs p(95)=388.64µs p(99.9)=39.17ms 
     http_req_sending...............: avg=128.86µs min=4.34µs   med=9.32µs  max=157.4ms  p(90)=19.25µs  p(95)=131.97µs p(99.9)=22.49ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.69ms  min=659.75µs med=44.97ms max=320.4ms  p(90)=116.91ms p(95)=148.74ms p(99.9)=225.01ms
     http_reqs......................: 253796  4163.734967/s
     iteration_duration.............: avg=56.35ms  min=1.46ms   med=45.99ms max=392.22ms p(90)=120.29ms p(95)=153.48ms p(99.9)=246.1ms 
     iterations.....................: 252796  4147.329133/s
     success_rate...................: 100.00% ✓ 252796      ✗ 0     
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

     checks.........................: 100.00% ✓ 482112      ✗ 0     
     data_received..................: 14 GB   230 MB/s
     data_sent......................: 194 MB  3.2 MB/s
     http_req_blocked...............: avg=18.36µs  min=1.13µs  med=3.07µs  max=45.92ms  p(90)=4.95µs   p(95)=6.25µs   p(99.9)=1.69ms  
     http_req_connecting............: avg=14.5µs   min=0s      med=0s      max=45.87ms  p(90)=0s       p(95)=0s       p(99.9)=1.52ms  
     http_req_duration..............: avg=87.91ms  min=1.19ms  med=81.87ms max=355.26ms p(90)=172.66ms p(95)=187.59ms p(99.9)=237.19ms
       { expected_response:true }...: avg=87.91ms  min=1.19ms  med=81.87ms max=355.26ms p(90)=172.66ms p(95)=187.59ms p(99.9)=237.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 161704
     http_req_receiving.............: avg=148.84µs min=22.55µs med=58.89µs max=39ms     p(90)=188.47µs p(95)=385.84µs p(99.9)=13.01ms 
     http_req_sending...............: avg=73.62µs  min=4.54µs  med=11.66µs max=134.71ms p(90)=21.64µs  p(95)=136.11µs p(99.9)=9.32ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=87.69ms  min=1.15ms  med=81.66ms max=355.01ms p(90)=172.35ms p(95)=187.29ms p(99.9)=236.11ms
     http_reqs......................: 161704  2631.759201/s
     iteration_duration.............: avg=88.71ms  min=3.11ms  med=82.76ms max=365.89ms p(90)=173.13ms p(95)=188ms    p(99.9)=238.13ms
     iterations.....................: 160704  2615.484036/s
     success_rate...................: 100.00% ✓ 160704      ✗ 0     
     vus............................: 77      min=0         max=493 
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

     checks.........................: 100.00% ✓ 249336      ✗ 0    
     data_received..................: 7.4 GB  118 MB/s
     data_sent......................: 101 MB  1.6 MB/s
     http_req_blocked...............: avg=4.95µs   min=941ns   med=2.23µs   max=12.6ms   p(90)=3.88µs   p(95)=4.79µs   p(99.9)=401.99µs
     http_req_connecting............: avg=2.11µs   min=0s      med=0s       max=12.53ms  p(90)=0s       p(95)=0s       p(99.9)=331.07µs
     http_req_duration..............: avg=169.57ms min=1.98ms  med=167.18ms max=468.9ms  p(90)=323.79ms p(95)=346.32ms p(99.9)=410.15ms
       { expected_response:true }...: avg=169.57ms min=1.98ms  med=167.18ms max=468.9ms  p(90)=323.79ms p(95)=346.32ms p(99.9)=410.15ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 84112
     http_req_receiving.............: avg=71.87µs  min=26.36µs med=57.97µs  max=78.25ms  p(90)=94.31µs  p(95)=108.22µs p(99.9)=1.24ms  
     http_req_sending...............: avg=25.63µs  min=4.79µs  med=10.6µs   max=30.82ms  p(90)=17.23µs  p(95)=20.55µs  p(99.9)=3.16ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=169.47ms min=1.92ms  med=167.11ms max=468.83ms p(90)=323.64ms p(95)=346.23ms p(99.9)=410.08ms
     http_reqs......................: 84112   1346.920511/s
     iteration_duration.............: avg=171.83ms min=4.91ms  med=169.68ms max=469.04ms p(90)=324.46ms p(95)=346.91ms p(99.9)=410.76ms
     iterations.....................: 83112   1330.907095/s
     success_rate...................: 100.00% ✓ 83112       ✗ 0    
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

     checks.........................: 100.00% ✓ 247140      ✗ 0    
     data_received..................: 7.3 GB  117 MB/s
     data_sent......................: 100 MB  1.6 MB/s
     http_req_blocked...............: avg=5.93µs   min=1.09µs  med=2.92µs   max=9.03ms   p(90)=4.75µs   p(95)=5.75µs   p(99.9)=450.52µs
     http_req_connecting............: avg=2.36µs   min=0s      med=0s       max=8.96ms   p(90)=0s       p(95)=0s       p(99.9)=390.41µs
     http_req_duration..............: avg=171.08ms min=2.16ms  med=145.42ms max=974.7ms  p(90)=351.26ms p(95)=421.76ms p(99.9)=736.45ms
       { expected_response:true }...: avg=171.08ms min=2.16ms  med=145.42ms max=974.7ms  p(90)=351.26ms p(95)=421.76ms p(99.9)=736.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 83380
     http_req_receiving.............: avg=76.96µs  min=28.79µs med=61.04µs  max=155.92ms p(90)=97.34µs  p(95)=112.31µs p(99.9)=1.52ms  
     http_req_sending...............: avg=32.92µs  min=5.24µs  med=12.83µs  max=111.64ms p(90)=19.48µs  p(95)=22.98µs  p(99.9)=3.66ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=170.97ms min=2.12ms  med=145.28ms max=974.64ms p(90)=351.18ms p(95)=421.64ms p(99.9)=736.38ms
     http_reqs......................: 83380   1333.36572/s
     iteration_duration.............: avg=173.4ms  min=7.08ms  med=148.08ms max=974.92ms p(90)=352.63ms p(95)=423.53ms p(99.9)=736.77ms
     iterations.....................: 82380   1317.374286/s
     success_rate...................: 100.00% ✓ 82380       ✗ 0    
     vus............................: 81      min=0         max=492
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

     checks.........................: 100.00% ✓ 94593      ✗ 0    
     data_received..................: 2.8 GB  44 MB/s
     data_sent......................: 39 MB   606 kB/s
     http_req_blocked...............: avg=8.12µs   min=1.28µs  med=3.12µs   max=15.16ms p(90)=4.85µs   p(95)=5.86µs   p(99.9)=718µs   
     http_req_connecting............: avg=3.86µs   min=0s      med=0s       max=15ms    p(90)=0s       p(95)=0s       p(99.9)=665.84µs
     http_req_duration..............: avg=441.38ms min=3.68ms  med=409.68ms max=1.83s   p(90)=871.98ms p(95)=958.05ms p(99.9)=1.41s   
       { expected_response:true }...: avg=441.38ms min=3.68ms  med=409.68ms max=1.83s   p(90)=871.98ms p(95)=958.05ms p(99.9)=1.41s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 32531
     http_req_receiving.............: avg=82.07µs  min=29.81µs med=71.67µs  max=11.83ms p(90)=110.8µs  p(95)=125.85µs p(99.9)=996.28µs
     http_req_sending...............: avg=30.06µs  min=5.65µs  med=14.58µs  max=91.96ms p(90)=21.23µs  p(95)=23.77µs  p(99.9)=2.6ms   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=441.27ms min=3.62ms  med=409.59ms max=1.83s   p(90)=871.76ms p(95)=957.95ms p(99.9)=1.41s   
     http_reqs......................: 32531   504.472973/s
     iteration_duration.............: avg=455.63ms min=18.24ms med=430.65ms max=1.84s   p(90)=877.34ms p(95)=961.73ms p(99.9)=1.42s   
     iterations.....................: 31531   488.965519/s
     success_rate...................: 100.00% ✓ 31531      ✗ 0    
     vus............................: 80      min=0        max=499
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

     checks.........................: 100.00% ✓ 46629      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   294 kB/s
     http_req_blocked...............: avg=15.32µs  min=1.32µs  med=3.84µs   max=12.76ms p(90)=5.68µs   p(95)=7.53µs   p(99.9)=2.22ms
     http_req_connecting............: avg=9.5µs    min=0s      med=0s       max=12.7ms  p(90)=0s       p(95)=0s       p(99.9)=2.12ms
     http_req_duration..............: avg=881.05ms min=5.74ms  med=809.63ms max=4.92s   p(90)=1.74s    p(95)=1.99s    p(99.9)=3.88s 
       { expected_response:true }...: avg=881.05ms min=5.74ms  med=809.63ms max=4.92s   p(90)=1.74s    p(95)=1.99s    p(99.9)=3.88s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16543
     http_req_receiving.............: avg=98.16µs  min=35.83µs med=90.96µs  max=6.07ms  p(90)=128.67µs p(95)=145.97µs p(99.9)=1.13ms
     http_req_sending...............: avg=25.97µs  min=6.33µs  med=18.11µs  max=11.64ms p(90)=23.53µs  p(95)=27.03µs  p(99.9)=1.97ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=880.93ms min=5.65ms  med=809.51ms max=4.92s   p(90)=1.74s    p(95)=1.99s    p(99.9)=3.88s 
     http_reqs......................: 16543   244.683327/s
     iteration_duration.............: avg=937.76ms min=54.71ms med=883.41ms max=4.92s   p(90)=1.77s    p(95)=2.01s    p(99.9)=3.92s 
     iterations.....................: 15543   229.89258/s
     success_rate...................: 100.00% ✓ 15543      ✗ 0    
     vus............................: 85      min=0        max=500
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
     http_req_blocked...............: avg=15.7µs   min=1.43µs  med=3.59µs   max=15.96ms  p(90)=5.41µs   p(95)=7µs      p(99.9)=2.21ms
     http_req_connecting............: avg=10.38µs  min=0s      med=0s       max=15.89ms  p(90)=0s       p(95)=0s       p(99.9)=2.19ms
     http_req_duration..............: avg=883.24ms min=7.7ms   med=805.36ms max=3.1s     p(90)=1.81s    p(95)=1.92s    p(99.9)=2.7s  
       { expected_response:true }...: avg=883.24ms min=7.7ms   med=805.36ms max=3.1s     p(90)=1.81s    p(95)=1.92s    p(99.9)=2.7s  
     http_req_failed................: 0.00%   ✓ 0          ✗ 16449
     http_req_receiving.............: avg=109.57µs min=33.14µs med=88.29µs  max=139.91ms p(90)=127.13µs p(95)=144.25µs p(99.9)=1.22ms
     http_req_sending...............: avg=60.56µs  min=5.66µs  med=17.12µs  max=151.31ms p(90)=22.77µs  p(95)=26.52µs  p(99.9)=4.69ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=883.07ms min=7.61ms  med=805.29ms max=3.1s     p(90)=1.81s    p(95)=1.92s    p(99.9)=2.7s  
     http_reqs......................: 16449   239.701846/s
     iteration_duration.............: avg=940.4ms  min=43.2ms  med=880.51ms max=3.11s    p(90)=1.83s    p(95)=1.93s    p(99.9)=2.72s 
     iterations.....................: 15449   225.129419/s
     success_rate...................: 100.00% ✓ 15449      ✗ 0    
     vus............................: 90      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

