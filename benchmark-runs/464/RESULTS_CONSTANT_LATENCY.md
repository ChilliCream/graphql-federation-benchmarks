## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 3,434 | 3,447 | 3,425 | 0.2% | 407 MB | 121.4 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,392 | 3,401 | 3,387 | 0.2% | 388 MB | 117.2 KB |  |
| fusion-aot-11 | 16.7.3 | 3,388 | 3,403 | 3,385 | 0.2% | 129 MB | 38.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,376 | 3,390 | 3,368 | 0.3% | 128 MB | 38.8 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,289 | 3,306 | 3,273 | 0.4% | 2,307 MB | 718.2 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,808 | 2,816 | 2,775 | 0.6% | 390 MB | 142.0 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,787 | 2,790 | 2,780 | 0.2% | 390 MB | 143.3 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,743 | 2,748 | 2,732 | 0.2% | 136 MB | 50.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,741 | 2,751 | 2,701 | 0.7% | 136 MB | 50.8 KB |  |
| hive-router | v0.3.6 | 2,044 | 2,047 | 2,034 | 0.3% | 90 MB | 44.8 KB |  |
| grafbase | 0.53.5 | 1,453 | 1,464 | 1,446 | 0.5% | 99 MB | 70.0 KB |  |
| cosmo | 0.363.0 | 1,418 | 1,420 | 1,417 | 0.1% | 148 MB | 106.8 KB |  |
| caliban | 3.2.0 | 1,382 | 1,383 | 1,379 | 0.1% | 4,618 MB | 3,421.8 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 517 | 518 | 516 | 0.1% | 2,755 MB | 5,455.9 KB |  |
| apollo-router | v2.19.0 | 504 | 508 | 486 | 1.7% | 179 MB | 364.5 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 399 | 402 | 388 | 1.4% | 206 MB | 528.5 KB |  |
| hive-gateway | 2.15.3 | 264 | 264 | 263 | 0.2% | 3,673 MB | 14,245.5 KB |  |
| apollo-gateway | 2.14.4 | 263 | 264 | 262 | 0.3% | 2,150 MB | 8,369.2 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1245984     ✗ 0     
     data_received..................: 36 GB   301 MB/s
     data_sent......................: 499 MB  4.1 MB/s
     http_req_blocked...............: avg=2.48µs  min=792ns   med=1.84µs  max=4ms      p(90)=3.09µs  p(95)=3.9µs    p(99.9)=25.5µs 
     http_req_connecting............: avg=249ns   min=0s      med=0s      max=3.94ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.24ms min=8.18ms  med=13.81ms max=275.75ms p(90)=17.66ms p(95)=19ms     p(99.9)=26.66ms
       { expected_response:true }...: avg=14.24ms min=8.18ms  med=13.81ms max=275.75ms p(90)=17.66ms p(95)=19ms     p(99.9)=26.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 415428
     http_req_receiving.............: avg=69.81µs min=24.17µs med=42.5µs  max=178.11ms p(90)=92.2µs  p(95)=170.53µs p(99.9)=2.13ms 
     http_req_sending...............: avg=31.63µs min=4.4µs   med=7.91µs  max=195.36ms p(90)=17.26µs p(95)=91.25µs  p(99.9)=1.98ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.13ms min=8.13ms  med=13.72ms max=275.5ms  p(90)=17.55ms p(95)=18.88ms  p(99.9)=26.43ms
     http_reqs......................: 415428  3434.617408/s
     iteration_duration.............: avg=14.43ms min=8.39ms  med=14.01ms max=284.83ms p(90)=17.85ms p(95)=19.19ms  p(99.9)=26.87ms
     iterations.....................: 415328  3433.790642/s
     success_rate...................: 100.00% ✓ 415328      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1230588     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 493 MB  4.1 MB/s
     http_req_blocked...............: avg=2.44µs  min=801ns   med=1.84µs  max=4.64ms   p(90)=3.04µs  p(95)=3.75µs   p(99.9)=23.41µs
     http_req_connecting............: avg=233ns   min=0s      med=0s      max=3.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.42ms min=8.19ms  med=14ms    max=279.65ms p(90)=17.93ms p(95)=19.27ms  p(99.9)=27.68ms
       { expected_response:true }...: avg=14.42ms min=8.19ms  med=14ms    max=279.65ms p(90)=17.93ms p(95)=19.27ms  p(99.9)=27.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 410296
     http_req_receiving.............: avg=68.18µs min=24.54µs med=43.02µs max=48.23ms  p(90)=90.16µs p(95)=168.02µs p(99.9)=1.96ms 
     http_req_sending...............: avg=30.69µs min=4.45µs  med=7.81µs  max=238.74ms p(90)=15.63µs p(95)=89.87µs  p(99.9)=1.87ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.32ms min=8.13ms  med=13.91ms max=279.35ms p(90)=17.82ms p(95)=19.16ms  p(99.9)=27.45ms
     http_reqs......................: 410296  3392.09769/s
     iteration_duration.............: avg=14.61ms min=8.32ms  med=14.2ms  max=313.6ms  p(90)=18.12ms p(95)=19.46ms  p(99.9)=27.93ms
     iterations.....................: 410196  3391.270946/s
     success_rate...................: 100.00% ✓ 410196      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1229334     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 493 MB  4.1 MB/s
     http_req_blocked...............: avg=2.45µs  min=802ns   med=1.85µs  max=3.75ms   p(90)=3.1µs   p(95)=3.84µs  p(99.9)=24.66µs
     http_req_connecting............: avg=241ns   min=0s      med=0s      max=3.7ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.43ms min=8.32ms  med=14.02ms max=282.41ms p(90)=17.8ms  p(95)=19.14ms p(99.9)=27.19ms
       { expected_response:true }...: avg=14.43ms min=8.32ms  med=14.02ms max=282.41ms p(90)=17.8ms  p(95)=19.14ms p(99.9)=27.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 409878
     http_req_receiving.............: avg=66.95µs min=23.32µs med=42.15µs max=161.36ms p(90)=89.64µs p(95)=165.7µs p(99.9)=1.79ms 
     http_req_sending...............: avg=30.49µs min=4.51µs  med=7.96µs  max=165.62ms p(90)=16.45µs p(95)=92.09µs p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=14.34ms min=8.27ms  med=13.92ms max=272.48ms p(90)=17.7ms  p(95)=19.03ms p(99.9)=27ms   
     http_reqs......................: 409878  3388.399237/s
     iteration_duration.............: avg=14.63ms min=8.48ms  med=14.21ms max=295.13ms p(90)=17.99ms p(95)=19.33ms p(99.9)=27.43ms
     iterations.....................: 409778  3387.572552/s
     success_rate...................: 100.00% ✓ 409778      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1224876     ✗ 0     
     data_received..................: 36 GB   295 MB/s
     data_sent......................: 491 MB  4.1 MB/s
     http_req_blocked...............: avg=3.17µs  min=882ns   med=2.2µs   max=10.11ms  p(90)=3.48µs  p(95)=4.17µs   p(99.9)=28.64µs
     http_req_connecting............: avg=622ns   min=0s      med=0s      max=10.05ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.49ms min=7.5ms   med=14.04ms max=308.65ms p(90)=17.93ms p(95)=19.31ms  p(99.9)=28.07ms
       { expected_response:true }...: avg=14.49ms min=7.5ms   med=14.04ms max=308.65ms p(90)=17.93ms p(95)=19.31ms  p(99.9)=28.07ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 408392
     http_req_receiving.............: avg=86.58µs min=25.18µs med=46.21µs max=266.2ms  p(90)=93.37µs p(95)=185.53µs p(99.9)=2.14ms 
     http_req_sending...............: avg=32µs    min=4.26µs  med=8.3µs   max=27.33ms  p(90)=16.61µs p(95)=98.27µs  p(99.9)=1.99ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.37ms min=7.45ms  med=13.94ms max=101.42ms p(90)=17.82ms p(95)=19.18ms  p(99.9)=27.68ms
     http_reqs......................: 408392  3376.270406/s
     iteration_duration.............: avg=14.68ms min=7.65ms  med=14.24ms max=318.32ms p(90)=18.12ms p(95)=19.5ms   p(99.9)=28.35ms
     iterations.....................: 408292  3375.443683/s
     success_rate...................: 100.00% ✓ 408292      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1193415     ✗ 0     
     data_received..................: 35 GB   288 MB/s
     data_sent......................: 478 MB  4.0 MB/s
     http_req_blocked...............: avg=2.5µs   min=812ns   med=1.95µs  max=4.06ms   p(90)=3.1µs   p(95)=3.75µs   p(99.9)=24.97µs
     http_req_connecting............: avg=233ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.88ms min=8.64ms  med=14.54ms max=294.26ms p(90)=17.94ms p(95)=19.15ms  p(99.9)=26.65ms
       { expected_response:true }...: avg=14.88ms min=8.64ms  med=14.54ms max=294.26ms p(90)=17.94ms p(95)=19.15ms  p(99.9)=26.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 397905
     http_req_receiving.............: avg=66.77µs min=23.82µs med=45µs    max=9.29ms   p(90)=88.36µs p(95)=161.55µs p(99.9)=1.47ms 
     http_req_sending...............: avg=30.56µs min=4.4µs   med=8.25µs  max=188.16ms p(90)=15.25µs p(95)=92.32µs  p(99.9)=1.53ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.78ms min=8.58ms  med=14.45ms max=293.57ms p(90)=17.84ms p(95)=19.03ms  p(99.9)=26.44ms
     http_reqs......................: 397905  3289.661357/s
     iteration_duration.............: avg=15.07ms min=8.78ms  med=14.73ms max=305.17ms p(90)=18.13ms p(95)=19.34ms  p(99.9)=26.92ms
     iterations.....................: 397805  3288.834611/s
     success_rate...................: 100.00% ✓ 397805      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1022487     ✗ 0     
     data_received..................: 30 GB   246 MB/s
     data_sent......................: 410 MB  3.4 MB/s
     http_req_blocked...............: avg=2.5µs   min=791ns   med=1.84µs  max=3.47ms   p(90)=3.13µs  p(95)=3.91µs   p(99.9)=25.7µs 
     http_req_connecting............: avg=274ns   min=0s      med=0s      max=3.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.39ms min=11.73ms med=16.97ms max=301.69ms p(90)=20.37ms p(95)=21.57ms  p(99.9)=28.36ms
       { expected_response:true }...: avg=17.39ms min=11.73ms med=16.97ms max=301.69ms p(90)=20.37ms p(95)=21.57ms  p(99.9)=28.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 340929
     http_req_receiving.............: avg=65.79µs min=23.79µs med=43.7µs  max=99.34ms  p(90)=91.27µs p(95)=144.14µs p(99.9)=1.38ms 
     http_req_sending...............: avg=28.29µs min=4.18µs  med=7.9µs   max=223.79ms p(90)=16.22µs p(95)=79.53µs  p(99.9)=1.44ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.3ms  min=11.67ms med=16.88ms max=301.27ms p(90)=20.27ms p(95)=21.46ms  p(99.9)=28.14ms
     http_reqs......................: 340929  2808.299242/s
     iteration_duration.............: avg=17.59ms min=11.94ms med=17.16ms max=311.72ms p(90)=20.56ms p(95)=21.77ms  p(99.9)=28.6ms 
     iterations.....................: 340829  2807.475522/s
     success_rate...................: 100.00% ✓ 340829      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1014690     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 407 MB  3.3 MB/s
     http_req_blocked...............: avg=2.43µs  min=801ns   med=1.8µs   max=3.37ms   p(90)=3.17µs  p(95)=4µs      p(99.9)=23.41µs
     http_req_connecting............: avg=251ns   min=0s      med=0s      max=3.34ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.52ms min=11.78ms med=17.08ms max=295.88ms p(90)=20.64ms p(95)=21.9ms   p(99.9)=28.67ms
       { expected_response:true }...: avg=17.52ms min=11.78ms med=17.08ms max=295.88ms p(90)=20.64ms p(95)=21.9ms   p(99.9)=28.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 338330
     http_req_receiving.............: avg=63.85µs min=23.49µs med=42.72µs max=10.11ms  p(90)=90.21µs p(95)=141.46µs p(99.9)=1.39ms 
     http_req_sending...............: avg=27.1µs  min=4.05µs  med=7.59µs  max=179.66ms p(90)=16.31µs p(95)=79.22µs  p(99.9)=1.43ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.43ms min=11.7ms  med=17ms    max=295.2ms  p(90)=20.54ms p(95)=21.79ms  p(99.9)=28.5ms 
     http_reqs......................: 338330  2787.144879/s
     iteration_duration.............: avg=17.73ms min=12.02ms med=17.28ms max=312.14ms p(90)=20.84ms p(95)=22.09ms  p(99.9)=28.89ms
     iterations.....................: 338230  2786.321084/s
     success_rate...................: 100.00% ✓ 338230      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 999018      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=2.46µs  min=802ns   med=1.85µs  max=3.51ms   p(90)=3.17µs  p(95)=3.93µs   p(99.9)=23.64µs
     http_req_connecting............: avg=255ns   min=0s      med=0s      max=3.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.8ms  min=11.96ms med=17.4ms  max=290.68ms p(90)=20.81ms p(95)=22.04ms  p(99.9)=29.42ms
       { expected_response:true }...: avg=17.8ms  min=11.96ms med=17.4ms  max=290.68ms p(90)=20.81ms p(95)=22.04ms  p(99.9)=29.42ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 333106
     http_req_receiving.............: avg=64.43µs min=23.77µs med=44.12µs max=18.36ms  p(90)=90.15µs p(95)=138.96µs p(99.9)=1.2ms  
     http_req_sending...............: avg=26.96µs min=4.16µs  med=7.74µs  max=161.33ms p(90)=16.16µs p(95)=79.69µs  p(99.9)=1.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.71ms min=11.91ms med=17.31ms max=290.09ms p(90)=20.7ms  p(95)=21.93ms  p(99.9)=29.17ms
     http_reqs......................: 333106  2743.762582/s
     iteration_duration.............: avg=18.01ms min=12.2ms  med=17.59ms max=299.53ms p(90)=21ms    p(95)=22.24ms  p(99.9)=29.68ms
     iterations.....................: 333006  2742.938892/s
     success_rate...................: 100.00% ✓ 333006      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 998184      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=2.91µs  min=872ns   med=2.25µs  max=3.46ms   p(90)=3.74µs  p(95)=4.53µs   p(99.9)=31.54µs
     http_req_connecting............: avg=281ns   min=0s      med=0s      max=3.42ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.81ms min=11.98ms med=17.37ms max=287.7ms  p(90)=20.9ms  p(95)=22.2ms   p(99.9)=29.24ms
       { expected_response:true }...: avg=17.81ms min=11.98ms med=17.37ms max=287.7ms  p(90)=20.9ms  p(95)=22.2ms   p(99.9)=29.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 332828
     http_req_receiving.............: avg=71.67µs min=23.23µs med=44.75µs max=251.59ms p(90)=92.58µs p(95)=149.13µs p(99.9)=1.34ms 
     http_req_sending...............: avg=30.79µs min=4.26µs  med=8.53µs  max=229.99ms p(90)=17.55µs p(95)=88.19µs  p(99.9)=1.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.71ms min=11.91ms med=17.28ms max=240.94ms p(90)=20.8ms  p(95)=22.08ms  p(99.9)=28.94ms
     http_reqs......................: 332828  2741.480892/s
     iteration_duration.............: avg=18.02ms min=12.18ms med=17.57ms max=296.56ms p(90)=21.1ms  p(95)=22.4ms   p(99.9)=29.45ms
     iterations.....................: 332728  2740.657199/s
     success_rate...................: 100.00% ✓ 332728      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 747135      ✗ 0     
     data_received..................: 22 GB   179 MB/s
     data_sent......................: 299 MB  2.5 MB/s
     http_req_blocked...............: avg=2.89µs  min=811ns   med=2.13µs  max=4.21ms   p(90)=3.81µs  p(95)=4.51µs   p(99.9)=33.07µs 
     http_req_connecting............: avg=389ns   min=0s      med=0s      max=4.16ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.87ms min=17.46ms med=23.52ms max=300.98ms p(90)=26.91ms p(95)=28ms     p(99.9)=33.49ms 
       { expected_response:true }...: avg=23.87ms min=17.46ms med=23.52ms max=300.98ms p(90)=26.91ms p(95)=28ms     p(99.9)=33.49ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 249145
     http_req_receiving.............: avg=67.4µs  min=25.36µs med=50.13µs max=239.81ms p(90)=93.84µs p(95)=118.03µs p(99.9)=915.41µs
     http_req_sending...............: avg=25.9µs  min=4.22µs  med=9.1µs   max=154.24ms p(90)=17.22µs p(95)=23.33µs  p(99.9)=904.95µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.77ms min=17.37ms med=23.43ms max=278.89ms p(90)=26.82ms p(95)=27.91ms  p(99.9)=33.26ms 
     http_reqs......................: 249145  2044.317402/s
     iteration_duration.............: avg=24.08ms min=17.66ms med=23.72ms max=310.82ms p(90)=27.11ms p(95)=28.2ms   p(99.9)=33.7ms  
     iterations.....................: 249045  2043.496869/s
     success_rate...................: 100.00% ✓ 249045      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: grafbase (HotChocolate subgraphs) (0.53.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 531501      ✗ 0     
     data_received..................: 16 GB   127 MB/s
     data_sent......................: 213 MB  1.7 MB/s
     http_req_blocked...............: avg=3.3µs   min=852ns   med=2.19µs  max=4.12ms   p(90)=4.52µs   p(95)=5.42µs   p(99.9)=37.44µs
     http_req_connecting............: avg=551ns   min=0s      med=0s      max=4.07ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.6ms  min=17.49ms med=33.33ms max=316.23ms p(90)=39.34ms  p(95)=41.04ms  p(99.9)=49.5ms 
       { expected_response:true }...: avg=33.6ms  min=17.49ms med=33.33ms max=316.23ms p(90)=39.34ms  p(95)=41.04ms  p(99.9)=49.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 177267
     http_req_receiving.............: avg=78.5µs  min=26.36µs med=53.92µs max=121.76ms p(90)=117.09µs p(95)=157.41µs p(99.9)=1.31ms 
     http_req_sending...............: avg=25.92µs min=4.69µs  med=9.19µs  max=9.3ms    p(90)=21.76µs  p(95)=35.57µs  p(99.9)=1.15ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.5ms  min=17.43ms med=33.23ms max=315.93ms p(90)=39.24ms  p(95)=40.94ms  p(99.9)=49.18ms
     http_reqs......................: 177267  1453.786332/s
     iteration_duration.............: avg=33.85ms min=20.05ms med=33.57ms max=324.44ms p(90)=39.56ms  p(95)=41.25ms  p(99.9)=49.77ms
     iterations.....................: 177167  1452.966221/s
     success_rate...................: 100.00% ✓ 177167      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 518826      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=3.07µs  min=951ns   med=2.19µs  max=3.87ms   p(90)=3.77µs  p(95)=4.48µs   p(99.9)=25.85µs 
     http_req_connecting............: avg=556ns   min=0s      med=0s      max=3.83ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.47ms min=18.64ms med=33.92ms max=305.4ms  p(90)=41.1ms  p(95)=43.38ms  p(99.9)=55.16ms 
       { expected_response:true }...: avg=34.47ms min=18.64ms med=33.92ms max=305.4ms  p(90)=41.1ms  p(95)=43.38ms  p(99.9)=55.16ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173042
     http_req_receiving.............: avg=71.86µs min=26.37µs med=60.03µs max=83ms     p(90)=99.03µs p(95)=116.21µs p(99.9)=722.66µs
     http_req_sending...............: avg=21.75µs min=4.57µs  med=10.16µs max=241.25ms p(90)=17.02µs p(95)=20.89µs  p(99.9)=746.44µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.38ms min=18.5ms  med=33.83ms max=305.2ms  p(90)=41.01ms p(95)=43.29ms  p(99.9)=55.03ms 
     http_reqs......................: 173042  1418.873528/s
     iteration_duration.............: avg=34.68ms min=21.06ms med=34.12ms max=322.62ms p(90)=41.29ms p(95)=43.58ms  p(99.9)=55.4ms  
     iterations.....................: 172942  1418.053569/s
     success_rate...................: 100.00% ✓ 172942      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 505485      ✗ 0     
     data_received..................: 15 GB   121 MB/s
     data_sent......................: 203 MB  1.7 MB/s
     http_req_blocked...............: avg=4.64µs  min=1.02µs  med=3.13µs  max=7.88ms   p(90)=4.79µs   p(95)=5.56µs   p(99.9)=34.02µs 
     http_req_connecting............: avg=1.15µs  min=0s      med=0s      max=7.17ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.36ms min=18.93ms med=34.84ms max=292.08ms p(90)=41.76ms  p(95)=44.08ms  p(99.9)=60.25ms 
       { expected_response:true }...: avg=35.36ms min=18.93ms med=34.84ms max=292.08ms p(90)=41.76ms  p(95)=44.08ms  p(99.9)=60.25ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 168595
     http_req_receiving.............: avg=76.96µs min=27.59µs med=63.8µs  max=130.83ms p(90)=101.09µs p(95)=118.23µs p(99.9)=861.27µs
     http_req_sending...............: avg=23.93µs min=4.93µs  med=12.5µs  max=102.91ms p(90)=18.75µs  p(95)=22.69µs  p(99.9)=795.05µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.26ms min=18.87ms med=34.74ms max=291.93ms p(90)=41.67ms  p(95)=43.97ms  p(99.9)=59.99ms 
     http_reqs......................: 168595  1382.077855/s
     iteration_duration.............: avg=35.6ms  min=20.13ms med=35.06ms max=312.76ms p(90)=41.98ms  p(95)=44.3ms   p(99.9)=60.71ms 
     iterations.....................: 168495  1381.258093/s
     success_rate...................: 100.00% ✓ 168495      ✗ 0     
     vus............................: 1       min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 189615     ✗ 0    
     data_received..................: 5.5 GB  45 MB/s
     data_sent......................: 76 MB   622 kB/s
     http_req_blocked...............: avg=4.8µs   min=1.19µs  med=3µs     max=4.14ms   p(90)=4.53µs   p(95)=5.17µs   p(99.9)=48.93µs 
     http_req_connecting............: avg=1.53µs  min=0s      med=0s      max=4.09ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.59ms min=20.83ms med=82.52ms max=342.85ms p(90)=151.86ms p(95)=167.31ms p(99.9)=271.36ms
       { expected_response:true }...: avg=94.59ms min=20.83ms med=82.52ms max=342.85ms p(90)=151.86ms p(95)=167.31ms p(99.9)=271.36ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63305
     http_req_receiving.............: avg=81.43µs min=31.18µs med=73.98µs max=61.89ms  p(90)=106.74µs p(95)=119.12µs p(99.9)=563.04µs
     http_req_sending...............: avg=21.99µs min=5.45µs  med=13.77µs max=119.26ms p(90)=19.5µs   p(95)=21.67µs  p(99.9)=549.47µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.48ms min=20.71ms med=82.41ms max=342.72ms p(90)=151.74ms p(95)=167.2ms  p(99.9)=270.51ms
     http_reqs......................: 63305   517.706741/s
     iteration_duration.............: avg=94.95ms min=32.47ms med=82.77ms max=345.26ms p(90)=152.13ms p(95)=167.59ms p(99.9)=274.17ms
     iterations.....................: 63205   516.888944/s
     success_rate...................: 100.00% ✓ 63205      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 184779     ✗ 0    
     data_received..................: 5.4 GB  44 MB/s
     data_sent......................: 74 MB   606 kB/s
     http_req_blocked...............: avg=4.38µs  min=1.03µs  med=2.75µs  max=3.26ms   p(90)=4.15µs   p(95)=4.7µs    p(99.9)=46.4µs  
     http_req_connecting............: avg=1.43µs  min=0s      med=0s      max=3.22ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=97.06ms min=19.78ms med=95.29ms max=313.08ms p(90)=122.7ms  p(95)=131.59ms p(99.9)=170.23ms
       { expected_response:true }...: avg=97.06ms min=19.78ms med=95.29ms max=313.08ms p(90)=122.7ms  p(95)=131.59ms p(99.9)=170.23ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61693
     http_req_receiving.............: avg=78.61µs min=28.42µs med=71.73µs max=69.23ms  p(90)=103.3µs  p(95)=115.75µs p(99.9)=481.76µs
     http_req_sending...............: avg=26.26µs min=4.82µs  med=13.83µs max=180.08ms p(90)=18.91µs  p(95)=20.76µs  p(99.9)=471.45µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.96ms min=19.7ms  med=95.19ms max=312.58ms p(90)=122.6ms  p(95)=131.5ms  p(99.9)=169.36ms
     http_reqs......................: 61693   504.79172/s
     iteration_duration.............: avg=97.43ms min=32.42ms med=95.56ms max=342.71ms p(90)=122.95ms p(95)=131.87ms p(99.9)=171ms   
     iterations.....................: 61593   503.973488/s
     success_rate...................: 100.00% ✓ 61593      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-v3 (HotChocolate subgraphs) (v3.0.0-preview.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 146181     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   479 kB/s
     http_req_blocked...............: avg=5.24µs   min=1.08µs  med=3.25µs   max=3.58ms   p(90)=4.75µs   p(95)=5.36µs   p(99.9)=131.43µs
     http_req_connecting............: avg=1.79µs   min=0s      med=0s       max=3.55ms   p(90)=0s       p(95)=0s       p(99.9)=75.88µs 
     http_req_duration..............: avg=122.7ms  min=20.88ms med=121.03ms max=345.66ms p(90)=151.99ms p(95)=161.99ms p(99.9)=206.92ms
       { expected_response:true }...: avg=122.7ms  min=20.88ms med=121.03ms max=345.66ms p(90)=151.99ms p(95)=161.99ms p(99.9)=206.92ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48827
     http_req_receiving.............: avg=80.61µs  min=28.48µs med=76.03µs  max=12.41ms  p(90)=107.74µs p(95)=119.43µs p(99.9)=561.51µs
     http_req_sending...............: avg=26.03µs  min=5.17µs  med=15.2µs   max=145.5ms  p(90)=20.6µs   p(95)=22.65µs  p(99.9)=541µs   
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=122.59ms min=20.78ms med=120.94ms max=345.06ms p(90)=151.87ms p(95)=161.88ms p(99.9)=206.66ms
     http_reqs......................: 48827   399.116461/s
     iteration_duration.............: avg=123.17ms min=34.72ms med=121.31ms max=355.2ms  p(90)=152.27ms p(95)=162.25ms p(99.9)=208.96ms
     iterations.....................: 48727   398.299051/s
     success_rate...................: 100.00% ✓ 48727      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 96648      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=6.12µs   min=1.08µs  med=3.21µs   max=3.5ms    p(90)=4.58µs   p(95)=5.14µs   p(99.9)=1.27ms  
     http_req_connecting............: avg=2.71µs   min=0s      med=0s       max=3.47ms   p(90)=0s       p(95)=0s       p(99.9)=1.25ms  
     http_req_duration..............: avg=185.53ms min=17.39ms med=170.84ms max=752.63ms p(90)=225.15ms p(95)=249.92ms p(99.9)=696.05ms
       { expected_response:true }...: avg=185.53ms min=17.39ms med=170.84ms max=752.63ms p(90)=225.15ms p(95)=249.92ms p(99.9)=696.05ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32316
     http_req_receiving.............: avg=92.73µs  min=33.03µs med=88.22µs  max=63.01ms  p(90)=118.3µs  p(95)=129.77µs p(99.9)=504.72µs
     http_req_sending...............: avg=27µs     min=5.16µs  med=16.26µs  max=78.87ms  p(90)=20.51µs  p(95)=22.28µs  p(99.9)=566.22µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.41ms min=17.25ms med=170.74ms max=752.51ms p(90)=225.06ms p(95)=249.83ms p(99.9)=695.95ms
     http_reqs......................: 32316   264.815774/s
     iteration_duration.............: avg=186.33ms min=30.64ms med=171.22ms max=752.89ms p(90)=225.48ms p(95)=250.51ms p(99.9)=696.34ms
     iterations.....................: 32216   263.996317/s
     success_rate...................: 100.00% ✓ 32216      ✗ 0    
     vus............................: 20      min=0        max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 96699      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   317 kB/s
     http_req_blocked...............: avg=4.65µs   min=1.18µs  med=2.96µs   max=2.85ms   p(90)=4.19µs   p(95)=4.71µs   p(99.9)=487.82µs
     http_req_connecting............: avg=1.53µs   min=0s      med=0s       max=2.83ms   p(90)=0s       p(95)=0s       p(99.9)=469.66µs
     http_req_duration..............: avg=185.46ms min=22.18ms med=185.77ms max=353.91ms p(90)=197.49ms p(95)=202.15ms p(99.9)=273.23ms
       { expected_response:true }...: avg=185.46ms min=22.18ms med=185.77ms max=353.91ms p(90)=197.49ms p(95)=202.15ms p(99.9)=273.23ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32333
     http_req_receiving.............: avg=88.89µs  min=29.38µs med=82.41µs  max=121.19ms p(90)=111.07µs p(95)=120.73µs p(99.9)=404.7µs 
     http_req_sending...............: avg=32.92µs  min=4.86µs  med=15.87µs  max=102.66ms p(90)=20.02µs  p(95)=21.74µs  p(99.9)=437.72µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.34ms min=22.05ms med=185.65ms max=353.79ms p(90)=197.38ms p(95)=202.03ms p(99.9)=273.02ms
     http_reqs......................: 32333   263.772058/s
     iteration_duration.............: avg=186.25ms min=50.21ms med=186.12ms max=359.55ms p(90)=197.75ms p(95)=202.43ms p(99.9)=273.93ms
     iterations.....................: 32233   262.95626/s
     success_rate...................: 100.00% ✓ 32233      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

