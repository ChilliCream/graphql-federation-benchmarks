## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.18 | 5,565 | 5,603 | 5,531 | 0.5% | 364 MB | 67.1 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.18 | 5,484 | 5,518 | 5,458 | 0.4% | 373 MB | 69.7 KB |  |
| fusion-net-11 | 16.7.7 | 5,460 | 5,515 | 5,435 | 0.6% | 367 MB | 68.9 KB |  |
| fusion-fed-net-11 | 16.7.7 | 5,414 | 5,460 | 5,391 | 0.5% | 370 MB | 70.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.18 | 5,292 | 5,310 | 5,287 | 0.2% | 109 MB | 21.2 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.18 | 5,259 | 5,262 | 5,221 | 0.4% | 120 MB | 23.4 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 5,221 | 5,250 | 5,179 | 0.5% | 125 MB | 24.5 KB |  |
| fusion-aot-11 | 16.7.7 | 5,185 | 5,197 | 5,172 | 0.2% | 114 MB | 22.5 KB | non-compatible response (6 across 1/5 runs) |
| feddi-gateway | 2026-11-03-0517 | 5,011 | 5,034 | 4,969 | 0.6% | 2,284 MB | 466.6 KB |  |
| hive-router-nightly | v0.3.19-nightly.9fc3d405 | 4,575 | 4,601 | 4,551 | 0.4% | 97 MB | 21.7 KB |  |
| hive-router | v0.3.17 | 4,559 | 4,597 | 4,536 | 0.5% | 94 MB | 21.1 KB |  |
| grafbase | 0.53.5 | 1,866 | 1,872 | 1,861 | 0.2% | 113 MB | 62.0 KB |  |
| cosmo | 0.373.0 | 1,505 | 1,506 | 1,504 | 0.1% | 163 MB | 111.2 KB |  |
| caliban | 3.2.1 | 1,475 | 1,477 | 1,470 | 0.2% | 5,264 MB | 3,654.4 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 617 | 618 | 617 | 0.1% | 2,614 MB | 4,337.8 KB |  |
| apollo-router | v2.19.1 | 534 | 535 | 532 | 0.2% | 182 MB | 349.6 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.e028e66f | 474 | 474 | 473 | 0.1% | 197 MB | 426.4 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 430 | 431 | 424 | 0.6% | 204 MB | 484.9 KB |  |
| hive-gateway | 2.15.10 | 299 | 299 | 297 | 0.3% | 3,411 MB | 11,682.8 KB |  |
| apollo-gateway | 2.14.4 | 270 | 270 | 269 | 0.2% | 2,157 MB | 8,182.0 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.18)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 2005128     ✗ 0     
     data_received..................: 59 GB   487 MB/s
     data_sent......................: 804 MB  6.7 MB/s
     http_req_blocked...............: avg=2.4µs   min=762ns    med=1.83µs  max=6.71ms   p(90)=2.91µs  p(95)=3.5µs    p(99.9)=27.33µs
     http_req_connecting............: avg=138ns   min=0s       med=0s      max=3.91ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.77ms  min=773.8µs  med=7.85ms  max=262.02ms p(90)=14.1ms  p(95)=17.29ms  p(99.9)=29.37ms
       { expected_response:true }...: avg=8.77ms  min=773.8µs  med=7.85ms  max=262.02ms p(90)=14.1ms  p(95)=17.29ms  p(99.9)=29.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 668476
     http_req_receiving.............: avg=89.72µs min=23.95µs  med=45.13µs max=73.27ms  p(90)=84.97µs p(95)=185.46µs p(99.9)=5.76ms 
     http_req_sending...............: avg=40.97µs min=4.3µs    med=7.87µs  max=58.3ms   p(90)=13.27µs p(95)=96.8µs   p(99.9)=4.78ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.64ms  min=722.73µs med=7.75ms  max=261.85ms p(90)=13.87ms p(95)=17.01ms  p(99.9)=29.01ms
     http_reqs......................: 668476  5565.879453/s
     iteration_duration.............: avg=8.96ms  min=1.13ms   med=8.03ms  max=281.14ms p(90)=14.3ms  p(95)=17.5ms   p(99.9)=29.64ms
     iterations.....................: 668376  5565.046831/s
     success_rate...................: 100.00% ✓ 668376      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.18)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1975929     ✗ 0     
     data_received..................: 58 GB   480 MB/s
     data_sent......................: 792 MB  6.6 MB/s
     http_req_blocked...............: avg=2.46µs  min=782ns    med=1.9µs   max=6.41ms   p(90)=2.99µs  p(95)=3.6µs    p(99.9)=27.32µs
     http_req_connecting............: avg=142ns   min=0s       med=0s      max=3.89ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.9ms   min=764.23µs med=7.96ms  max=256.98ms p(90)=14.29ms p(95)=17.48ms  p(99.9)=30.19ms
       { expected_response:true }...: avg=8.9ms   min=764.23µs med=7.96ms  max=256.98ms p(90)=14.29ms p(95)=17.48ms  p(99.9)=30.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 658743
     http_req_receiving.............: avg=94.87µs min=25.51µs  med=46.37µs max=23.73ms  p(90)=87.95µs p(95)=189.85µs p(99.9)=6.36ms 
     http_req_sending...............: avg=42.2µs  min=4.34µs   med=8µs     max=121.98ms p(90)=13.61µs p(95)=98.84µs  p(99.9)=4.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.76ms  min=707.42µs med=7.86ms  max=256.85ms p(90)=14.06ms p(95)=17.21ms  p(99.9)=29.64ms
     http_reqs......................: 658743  5484.741938/s
     iteration_duration.............: avg=9.1ms   min=919.9µs  med=8.15ms  max=293.52ms p(90)=14.5ms  p(95)=17.7ms   p(99.9)=30.46ms
     iterations.....................: 658643  5483.909331/s
     success_rate...................: 100.00% ✓ 658643      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1967211     ✗ 0     
     data_received..................: 57 GB   478 MB/s
     data_sent......................: 788 MB  6.6 MB/s
     http_req_blocked...............: avg=2.91µs  min=821ns    med=2.36µs  max=7.11ms   p(90)=3.6µs   p(95)=4.27µs   p(99.9)=32.26µs
     http_req_connecting............: avg=130ns   min=0s       med=0s      max=3.38ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.93ms  min=779.74µs med=7.92ms  max=300.2ms  p(90)=14.55ms p(95)=18.03ms  p(99.9)=31.49ms
       { expected_response:true }...: avg=8.93ms  min=779.74µs med=7.92ms  max=300.2ms  p(90)=14.55ms p(95)=18.03ms  p(99.9)=31.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 655837
     http_req_receiving.............: avg=99.25µs min=25.03µs  med=47.01µs max=62.96ms  p(90)=89.52µs p(95)=195.87µs p(99.9)=6.88ms 
     http_req_sending...............: avg=44.33µs min=4.4µs    med=8.96µs  max=203.08ms p(90)=15.03µs p(95)=103.8µs  p(99.9)=5ms    
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.79ms  min=719.11µs med=7.81ms  max=299.67ms p(90)=14.29ms p(95)=17.72ms  p(99.9)=30.99ms
     http_reqs......................: 655837  5460.510747/s
     iteration_duration.............: avg=9.14ms  min=1.06ms   med=8.11ms  max=314.69ms p(90)=14.77ms p(95)=18.26ms  p(99.9)=31.84ms
     iterations.....................: 655737  5459.678145/s
     success_rate...................: 100.00% ✓ 655737      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1950735     ✗ 0     
     data_received..................: 57 GB   474 MB/s
     data_sent......................: 782 MB  6.5 MB/s
     http_req_blocked...............: avg=3.12µs  min=811ns    med=2.23µs  max=8.97ms   p(90)=3.5µs   p(95)=4.17µs   p(99.9)=31.66µs
     http_req_connecting............: avg=391ns   min=0s       med=0s      max=8.38ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.01ms  min=802.62µs med=8.03ms  max=267.13ms p(90)=14.59ms p(95)=17.98ms  p(99.9)=30.74ms
       { expected_response:true }...: avg=9.01ms  min=802.62µs med=8.03ms  max=267.13ms p(90)=14.59ms p(95)=17.98ms  p(99.9)=30.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 650345
     http_req_receiving.............: avg=98.97µs min=25.5µs   med=47.31µs max=127.02ms p(90)=90.59µs p(95)=195.82µs p(99.9)=6.83ms 
     http_req_sending...............: avg=44.33µs min=4.07µs   med=8.45µs  max=186.02ms p(90)=14.49µs p(95)=102.25µs p(99.9)=5.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.87ms  min=731.2µs  med=7.92ms  max=266.08ms p(90)=14.34ms p(95)=17.69ms  p(99.9)=30.15ms
     http_reqs......................: 650345  5414.768547/s
     iteration_duration.............: avg=9.21ms  min=993.92µs med=8.22ms  max=282.71ms p(90)=14.8ms  p(95)=18.2ms   p(99.9)=31.01ms
     iterations.....................: 650245  5413.935948/s
     success_rate...................: 100.00% ✓ 650245      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.18)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1906755     ✗ 0     
     data_received..................: 56 GB   463 MB/s
     data_sent......................: 764 MB  6.4 MB/s
     http_req_blocked...............: avg=2.46µs   min=811ns    med=1.92µs  max=7.03ms   p(90)=2.99µs  p(95)=3.55µs   p(99.9)=26.17µs
     http_req_connecting............: avg=133ns    min=0s       med=0s      max=3.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.23ms   min=833.59µs med=8.35ms  max=290.65ms p(90)=14.74ms p(95)=17.76ms  p(99.9)=30.32ms
       { expected_response:true }...: avg=9.23ms   min=833.59µs med=8.35ms  max=290.65ms p(90)=14.74ms p(95)=17.76ms  p(99.9)=30.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 635685
     http_req_receiving.............: avg=100.33µs min=25.07µs  med=45.62µs max=262.36ms p(90)=84.94µs p(95)=191.84µs p(99.9)=5.98ms 
     http_req_sending...............: avg=40.99µs  min=4.22µs   med=8.2µs   max=152.94ms p(90)=13.74µs p(95)=98.38µs  p(99.9)=4.63ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.09ms   min=764.03µs med=8.24ms  max=126.16ms p(90)=14.52ms p(95)=17.5ms   p(99.9)=29.57ms
     http_reqs......................: 635685  5292.479559/s
     iteration_duration.............: avg=9.43ms   min=1.17ms   med=8.53ms  max=304.39ms p(90)=14.95ms p(95)=17.97ms  p(99.9)=30.61ms
     iterations.....................: 635585  5291.646996/s
     success_rate...................: 100.00% ✓ 635585      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.18)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1894995     ✗ 0     
     data_received..................: 55 GB   460 MB/s
     data_sent......................: 759 MB  6.3 MB/s
     http_req_blocked...............: avg=2.48µs  min=851ns    med=1.96µs  max=5.4ms    p(90)=3.02µs  p(95)=3.57µs   p(99.9)=27.21µs
     http_req_connecting............: avg=160ns   min=0s       med=0s      max=4.31ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.29ms  min=848.27µs med=8.43ms  max=232.87ms p(90)=14.8ms  p(95)=17.82ms  p(99.9)=29.99ms
       { expected_response:true }...: avg=9.29ms  min=848.27µs med=8.43ms  max=232.87ms p(90)=14.8ms  p(95)=17.82ms  p(99.9)=29.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 631765
     http_req_receiving.............: avg=93.88µs min=25.4µs   med=46.13µs max=76.9ms   p(90)=85.76µs p(95)=193.01µs p(99.9)=6.17ms 
     http_req_sending...............: avg=40.27µs min=4.33µs   med=8.21µs  max=171.89ms p(90)=13.7µs  p(95)=99.71µs  p(99.9)=4.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.16ms  min=800.47µs med=8.32ms  max=232.51ms p(90)=14.58ms p(95)=17.55ms  p(99.9)=29.51ms
     http_reqs......................: 631765  5259.677724/s
     iteration_duration.............: avg=9.48ms  min=1.11ms   med=8.61ms  max=348.48ms p(90)=15.01ms p(95)=18.03ms  p(99.9)=30.24ms
     iterations.....................: 631665  5258.845187/s
     success_rate...................: 100.00% ✓ 631665      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1881246     ✗ 0     
     data_received..................: 55 GB   457 MB/s
     data_sent......................: 754 MB  6.3 MB/s
     http_req_blocked...............: avg=2.67µs  min=761ns    med=2.13µs  max=7.33ms   p(90)=3.34µs  p(95)=3.97µs   p(99.9)=31.46µs
     http_req_connecting............: avg=145ns   min=0s       med=0s      max=3.53ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.36ms  min=842.27µs med=8.44ms  max=272.44ms p(90)=14.98ms p(95)=18.13ms  p(99.9)=30.81ms
       { expected_response:true }...: avg=9.36ms  min=842.27µs med=8.44ms  max=272.44ms p(90)=14.98ms p(95)=18.13ms  p(99.9)=30.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 627182
     http_req_receiving.............: avg=93.44µs min=24.64µs  med=46.29µs max=108.37ms p(90)=88.34µs p(95)=197.31µs p(99.9)=6.05ms 
     http_req_sending...............: avg=42.06µs min=4.24µs   med=8.43µs  max=207.66ms p(90)=14.16µs p(95)=102.63µs p(99.9)=4.47ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.22ms  min=772.07µs med=8.33ms  max=271.56ms p(90)=14.77ms p(95)=17.86ms  p(99.9)=30.39ms
     http_reqs......................: 627182  5221.608435/s
     iteration_duration.............: avg=9.55ms  min=1.22ms   med=8.63ms  max=328.66ms p(90)=15.19ms p(95)=18.35ms  p(99.9)=31.09ms
     iterations.....................: 627082  5220.775884/s
     success_rate...................: 100.00% ✓ 627082      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1868220     ✗ 0     
     data_received..................: 55 GB   454 MB/s
     data_sent......................: 749 MB  6.2 MB/s
     http_req_blocked...............: avg=2.91µs  min=882ns    med=2.3µs   max=5.9ms    p(90)=3.56µs  p(95)=4.19µs   p(99.9)=34.78µs
     http_req_connecting............: avg=159ns   min=0s       med=0s      max=3.72ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.42ms  min=822.48µs med=8.46ms  max=273.79ms p(90)=15.27ms p(95)=18.59ms  p(99.9)=31.5ms 
       { expected_response:true }...: avg=9.42ms  min=822.48µs med=8.46ms  max=273.79ms p(90)=15.27ms p(95)=18.59ms  p(99.9)=31.5ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 622840
     http_req_receiving.............: avg=97.17µs min=25.11µs  med=46.68µs max=55.44ms  p(90)=90.2µs  p(95)=204.81µs p(99.9)=6.28ms 
     http_req_sending...............: avg=43.66µs min=4.56µs   med=8.45µs  max=102.82ms p(90)=14.42µs p(95)=107.51µs p(99.9)=4.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.28ms  min=768.77µs med=8.34ms  max=273.66ms p(90)=15.03ms p(95)=18.31ms  p(99.9)=31.12ms
     http_reqs......................: 622840  5185.392282/s
     iteration_duration.............: avg=9.62ms  min=1.22ms   med=8.64ms  max=285.29ms p(90)=15.48ms p(95)=18.81ms  p(99.9)=31.81ms
     iterations.....................: 622740  5184.559742/s
     success_rate...................: 100.00% ✓ 622740      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1805334     ✗ 0     
     data_received..................: 53 GB   438 MB/s
     data_sent......................: 723 MB  6.0 MB/s
     http_req_blocked...............: avg=3.19µs  min=862ns    med=2.48µs  max=8.63ms   p(90)=3.85µs  p(95)=4.56µs   p(99.9)=35.55µs
     http_req_connecting............: avg=170ns   min=0s       med=0s      max=3.84ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.75ms  min=677.86µs med=8.81ms  max=284.69ms p(90)=15.15ms p(95)=18.75ms  p(99.9)=30.99ms
       { expected_response:true }...: avg=9.75ms  min=677.86µs med=8.81ms  max=284.69ms p(90)=15.15ms p(95)=18.75ms  p(99.9)=30.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 601878
     http_req_receiving.............: avg=99.8µs  min=23.95µs  med=48.13µs max=161.09ms p(90)=93.81µs p(95)=209.47µs p(99.9)=6.62ms 
     http_req_sending...............: avg=46.17µs min=4.3µs    med=9.11µs  max=116.61ms p(90)=16.01µs p(95)=113.24µs p(99.9)=5.19ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.6ms   min=633.13µs med=8.72ms  max=278.75ms p(90)=14.87ms p(95)=18.46ms  p(99.9)=30.38ms
     http_reqs......................: 601878  5011.500016/s
     iteration_duration.............: avg=9.96ms  min=1.06ms   med=9.01ms  max=296.78ms p(90)=15.38ms p(95)=18.98ms  p(99.9)=31.29ms
     iterations.....................: 601778  5010.667373/s
     success_rate...................: 100.00% ✓ 601778      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.9fc3d405)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1648551     ✗ 0     
     data_received..................: 48 GB   400 MB/s
     data_sent......................: 661 MB  5.5 MB/s
     http_req_blocked...............: avg=3.21µs   min=862ns    med=2.58µs  max=6.27ms   p(90)=4.04µs   p(95)=4.79µs   p(99.9)=34.32µs
     http_req_connecting............: avg=164ns    min=0s       med=0s      max=3.51ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.7ms   min=941.05µs med=10.02ms max=296.9ms  p(90)=15.32ms  p(95)=19.03ms  p(99.9)=30.66ms
       { expected_response:true }...: avg=10.7ms   min=941.05µs med=10.02ms max=296.9ms  p(90)=15.32ms  p(95)=19.03ms  p(99.9)=30.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 549617
     http_req_receiving.............: avg=101.03µs min=25.45µs  med=52.33µs max=134.04ms p(90)=102.52µs p(95)=220.53µs p(99.9)=5.97ms 
     http_req_sending...............: avg=46.36µs  min=4.63µs   med=9.39µs  max=96.02ms  p(90)=16.62µs  p(95)=117.84µs p(99.9)=4.8ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.55ms  min=880.68µs med=9.92ms  max=296.08ms p(90)=15.02ms  p(95)=18.72ms  p(99.9)=30.06ms
     http_reqs......................: 549617  4575.296601/s
     iteration_duration.............: avg=10.9ms   min=1.53ms   med=10.21ms max=319.64ms p(90)=15.54ms  p(95)=19.26ms  p(99.9)=30.96ms
     iterations.....................: 549517  4574.464149/s
     success_rate...................: 100.00% ✓ 549517      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1642716     ✗ 0     
     data_received..................: 48 GB   399 MB/s
     data_sent......................: 658 MB  5.5 MB/s
     http_req_blocked...............: avg=2.66µs   min=762ns    med=2.07µs  max=5.98ms   p(90)=3.3µs   p(95)=3.96µs   p(99.9)=29.43µs
     http_req_connecting............: avg=166ns    min=0s       med=0s      max=3.31ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.75ms  min=941.1µs  med=10.25ms max=286.04ms p(90)=14.8ms  p(95)=17.99ms  p(99.9)=28.66ms
       { expected_response:true }...: avg=10.75ms  min=941.1µs  med=10.25ms max=286.04ms p(90)=14.8ms  p(95)=17.99ms  p(99.9)=28.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 547672
     http_req_receiving.............: avg=106.13µs min=25.95µs  med=49.96µs max=239.09ms p(90)=95.34µs p(95)=204.49µs p(99.9)=6.26ms 
     http_req_sending...............: avg=42.59µs  min=4.68µs   med=8.87µs  max=258.9ms  p(90)=15.58µs p(95)=108.43µs p(99.9)=4.5ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.6ms   min=862.58µs med=10.16ms max=124.9ms  p(90)=14.54ms p(95)=17.7ms   p(99.9)=28.07ms
     http_reqs......................: 547672  4559.073203/s
     iteration_duration.............: avg=10.94ms  min=1.54ms   med=10.43ms max=293.55ms p(90)=15.01ms p(95)=18.21ms  p(99.9)=28.91ms
     iterations.....................: 547572  4558.240757/s
     success_rate...................: 100.00% ✓ 547572      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 672990      ✗ 0     
     data_received..................: 20 GB   164 MB/s
     data_sent......................: 270 MB  2.2 MB/s
     http_req_blocked...............: avg=3.87µs  min=822ns   med=2.25µs  max=8.68ms   p(90)=4.37µs   p(95)=5.4µs    p(99.9)=38.14µs
     http_req_connecting............: avg=1.03µs  min=0s      med=0s      max=8.54ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.5ms  min=1.85ms  med=26.01ms max=319.73ms p(90)=34.48ms  p(95)=37.28ms  p(99.9)=50.9ms 
       { expected_response:true }...: avg=26.5ms  min=1.85ms  med=26.01ms max=319.73ms p(90)=34.48ms  p(95)=37.28ms  p(99.9)=50.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 224430
     http_req_receiving.............: avg=83.23µs min=25.62µs med=54.2µs  max=194.05ms p(90)=117.66µs p(95)=195.22µs p(99.9)=1.64ms 
     http_req_sending...............: avg=34.86µs min=4.34µs  med=9.59µs  max=234.93ms p(90)=22.62µs  p(95)=104.55µs p(99.9)=1.62ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.38ms min=1.79ms  med=25.9ms  max=318.59ms p(90)=34.36ms  p(95)=37.15ms  p(99.9)=50.66ms
     http_reqs......................: 224430  1866.188981/s
     iteration_duration.............: avg=26.73ms min=5.13ms  med=26.23ms max=334.32ms p(90)=34.7ms   p(95)=37.5ms   p(99.9)=51.22ms
     iterations.....................: 224330  1865.357458/s
     success_rate...................: 100.00% ✓ 224330      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 543099      ✗ 0     
     data_received..................: 16 GB   132 MB/s
     data_sent......................: 218 MB  1.8 MB/s
     http_req_blocked...............: avg=3.59µs  min=922ns   med=2.11µs  max=8.96ms   p(90)=3.49µs  p(95)=4.17µs   p(99.9)=27.77µs 
     http_req_connecting............: avg=1.12µs  min=0s      med=0s      max=8.93ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.92ms min=2.03ms  med=32.02ms max=277.97ms p(90)=47.5ms  p(95)=52.29ms  p(99.9)=75.41ms 
       { expected_response:true }...: avg=32.92ms min=2.03ms  med=32.02ms max=277.97ms p(90)=47.5ms  p(95)=52.29ms  p(99.9)=75.41ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 181133
     http_req_receiving.............: avg=69.02µs min=25.72µs med=57.36µs max=177.03ms p(90)=92.01µs p(95)=106.37µs p(99.9)=681.12µs
     http_req_sending...............: avg=19.84µs min=4.77µs  med=9.79µs  max=85.41ms  p(90)=15.43µs p(95)=19.09µs  p(99.9)=750.6µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.83ms min=1.97ms  med=31.94ms max=275.58ms p(90)=47.42ms p(95)=52.2ms   p(99.9)=75.16ms 
     http_reqs......................: 181133  1505.979247/s
     iteration_duration.............: avg=33.13ms min=3.91ms  med=32.22ms max=291.35ms p(90)=47.7ms  p(95)=52.48ms  p(99.9)=75.75ms 
     iterations.....................: 181033  1505.147826/s
     success_rate...................: 100.00% ✓ 181033      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 532122      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 213 MB  1.8 MB/s
     http_req_blocked...............: avg=3.11µs  min=891ns   med=2.33µs  max=3.46ms   p(90)=3.93µs  p(95)=4.63µs  p(99.9)=27.68µs 
     http_req_connecting............: avg=482ns   min=0s      med=0s      max=3.42ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=33.59ms min=2.06ms  med=32.64ms max=308.74ms p(90)=47.97ms p(95)=53.15ms p(99.9)=80.21ms 
       { expected_response:true }...: avg=33.59ms min=2.06ms  med=32.64ms max=308.74ms p(90)=47.97ms p(95)=53.15ms p(99.9)=80.21ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 177474
     http_req_receiving.............: avg=91.9µs  min=27.35µs med=59.58µs max=202.06ms p(90)=94.53µs p(95)=109.7µs p(99.9)=893.47µs
     http_req_sending...............: avg=18.91µs min=4.82µs  med=10.9µs  max=34.47ms  p(90)=17.51µs p(95)=21.02µs p(99.9)=693.68µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=33.48ms min=1.96ms  med=32.55ms max=108.67ms p(90)=47.88ms p(95)=53.04ms p(99.9)=79.82ms 
     http_reqs......................: 177474  1475.618395/s
     iteration_duration.............: avg=33.81ms min=4.24ms  med=32.85ms max=323.62ms p(90)=48.19ms p(95)=53.35ms p(99.9)=80.61ms 
     iterations.....................: 177374  1474.786939/s
     success_rate...................: 100.00% ✓ 177374      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 222990     ✗ 0    
     data_received..................: 6.5 GB  54 MB/s
     data_sent......................: 89 MB   742 kB/s
     http_req_blocked...............: avg=4.22µs  min=1.03µs  med=2.55µs  max=4.02ms   p(90)=3.97µs   p(95)=4.56µs   p(99.9)=47.24µs 
     http_req_connecting............: avg=1.41µs  min=0s      med=0s      max=3.94ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=80.38ms min=3.45ms  med=77.59ms max=322.9ms  p(90)=98.91ms  p(95)=110.57ms p(99.9)=202.02ms
       { expected_response:true }...: avg=80.38ms min=3.45ms  med=77.59ms max=322.9ms  p(90)=98.91ms  p(95)=110.57ms p(99.9)=202.02ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 74430
     http_req_receiving.............: avg=78.85µs min=27.98µs med=70.24µs max=79.51ms  p(90)=104.28µs p(95)=116.99µs p(99.9)=553.25µs
     http_req_sending...............: avg=22.05µs min=4.91µs  med=12.74µs max=115.01ms p(90)=18.51µs  p(95)=20.48µs  p(99.9)=559.53µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=80.28ms min=3.38ms  med=77.5ms  max=322.51ms p(90)=98.8ms   p(95)=110.45ms p(99.9)=201.82ms
     http_reqs......................: 74430   617.772915/s
     iteration_duration.............: avg=80.72ms min=12.17ms med=77.83ms max=332.17ms p(90)=99.17ms  p(95)=110.86ms p(99.9)=204.02ms
     iterations.....................: 74330   616.94291/s
     success_rate...................: 100.00% ✓ 74330      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 193032     ✗ 0    
     data_received..................: 5.6 GB  47 MB/s
     data_sent......................: 77 MB   642 kB/s
     http_req_blocked...............: avg=4.44µs  min=992ns   med=2.82µs  max=7.93ms   p(90)=4.24µs   p(95)=4.8µs    p(99.9)=45.5µs  
     http_req_connecting............: avg=1.38µs  min=0s      med=0s      max=7.91ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.87ms min=4.37ms  med=90.94ms max=285.33ms p(90)=125.03ms p(95)=134.91ms p(99.9)=174.64ms
       { expected_response:true }...: avg=92.87ms min=4.37ms  med=90.94ms max=285.33ms p(90)=125.03ms p(95)=134.91ms p(99.9)=174.64ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64444
     http_req_receiving.............: avg=79.74µs min=27.5µs  med=72.72µs max=124.46ms p(90)=102.57µs p(95)=114.54µs p(99.9)=507.27µs
     http_req_sending...............: avg=23.9µs  min=4.95µs  med=14.43µs max=112.99ms p(90)=19.57µs  p(95)=21.47µs  p(99.9)=575.56µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.77ms min=4.29ms  med=90.84ms max=284.71ms p(90)=124.92ms p(95)=134.8ms  p(99.9)=174.41ms
     http_reqs......................: 64444   534.501685/s
     iteration_duration.............: avg=93.25ms min=19.41ms med=91.23ms max=306.56ms p(90)=125.29ms p(95)=135.17ms p(99.9)=175.29ms
     iterations.....................: 64344   533.67228/s
     success_rate...................: 100.00% ✓ 64344      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.e028e66f)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 171324    ✗ 0    
     data_received..................: 5.0 GB  42 MB/s
     data_sent......................: 69 MB   570 kB/s
     http_req_blocked...............: avg=8.48µs   min=1.29µs  med=3.19µs   max=9.13ms   p(90)=4.56µs   p(95)=5.1µs    p(99.9)=57.26µs 
     http_req_connecting............: avg=4.91µs   min=0s      med=0s       max=9.09ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=104.66ms min=4.64ms  med=102.61ms max=313.13ms p(90)=139.16ms p(95)=150.28ms p(99.9)=198.17ms
       { expected_response:true }...: avg=104.66ms min=4.64ms  med=102.61ms max=313.13ms p(90)=139.16ms p(95)=150.28ms p(99.9)=198.17ms
     http_req_failed................: 0.00%   ✓ 0         ✗ 57208
     http_req_receiving.............: avg=122.4µs  min=30.25µs med=70.98µs  max=137.95ms p(90)=101.59µs p(95)=113.94µs p(99.9)=754.19µs
     http_req_sending...............: avg=19.04µs  min=5.19µs  med=14.88µs  max=16.82ms  p(90)=20.25µs  p(95)=22.1µs   p(99.9)=606.1µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=104.51ms min=4.52ms  med=102.51ms max=231.33ms p(90)=139.06ms p(95)=150.17ms p(99.9)=192.86ms
     http_reqs......................: 57208   474.26586/s
     iteration_duration.............: avg=105.08ms min=8.66ms  med=102.91ms max=347.53ms p(90)=139.44ms p(95)=150.56ms p(99.9)=200ms   
     iterations.....................: 57108   473.43684/s
     success_rate...................: 100.00% ✓ 57108     ✗ 0    
     vus............................: 50      min=50      max=50 
     vus_max........................: 50      min=50      max=50
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

     checks.........................: 100.00% ✓ 155511     ✗ 0    
     data_received..................: 4.5 GB  38 MB/s
     data_sent......................: 62 MB   517 kB/s
     http_req_blocked...............: avg=5.33µs   min=1.31µs  med=3.41µs   max=3.79ms   p(90)=4.78µs   p(95)=5.36µs   p(99.9)=71.84µs 
     http_req_connecting............: avg=1.71µs   min=0s      med=0s       max=3.76ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=115.29ms min=5.31ms  med=113.08ms max=351.34ms p(90)=150.45ms p(95)=162.11ms p(99.9)=209.73ms
       { expected_response:true }...: avg=115.29ms min=5.31ms  med=113.08ms max=351.34ms p(90)=150.45ms p(95)=162.11ms p(99.9)=209.73ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51937
     http_req_receiving.............: avg=87.12µs  min=31.73µs med=80.51µs  max=99.02ms  p(90)=110.51µs p(95)=121.7µs  p(99.9)=461.62µs
     http_req_sending...............: avg=22.95µs  min=5.74µs  med=16.29µs  max=86.32ms  p(90)=21.12µs  p(95)=22.91µs  p(99.9)=545.56µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=115.18ms min=5.24ms  med=112.98ms max=350.81ms p(90)=150.35ms p(95)=162.02ms p(99.9)=209ms   
     http_reqs......................: 51937   430.362246/s
     iteration_duration.............: avg=115.77ms min=24.22ms med=113.4ms  max=360.97ms p(90)=150.76ms p(95)=162.41ms p(99.9)=211.52ms
     iterations.....................: 51837   429.533623/s
     success_rate...................: 100.00% ✓ 51837      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 108402     ✗ 0    
     data_received..................: 3.2 GB  26 MB/s
     data_sent......................: 44 MB   360 kB/s
     http_req_blocked...............: avg=6.87µs   min=1.44µs  med=3.66µs   max=4.3ms    p(90)=5.12µs   p(95)=5.73µs   p(99.9)=1.43ms  
     http_req_connecting............: avg=2.9µs    min=0s      med=0s       max=4.25ms   p(90)=0s       p(95)=0s       p(99.9)=1.39ms  
     http_req_duration..............: avg=165.41ms min=5.38ms  med=149.37ms max=744.21ms p(90)=190.39ms p(95)=215.29ms p(99.9)=672.14ms
       { expected_response:true }...: avg=165.41ms min=5.38ms  med=149.37ms max=744.21ms p(90)=190.39ms p(95)=215.29ms p(99.9)=672.14ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 36234
     http_req_receiving.............: avg=95.4µs   min=34.98µs med=89.57µs  max=53.62ms  p(90)=119.64µs p(95)=131.35µs p(99.9)=738.64µs
     http_req_sending...............: avg=31.58µs  min=6.58µs  med=18.05µs  max=132.42ms p(90)=22.76µs  p(95)=24.66µs  p(99.9)=560.15µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=165.28ms min=5.29ms  med=149.25ms max=744.08ms p(90)=190.26ms p(95)=215.12ms p(99.9)=672.03ms
     http_reqs......................: 36234   299.694928/s
     iteration_duration.............: avg=166.12ms min=23.22ms med=149.7ms  max=744.44ms p(90)=190.73ms p(95)=215.88ms p(99.9)=672.42ms
     iterations.....................: 36134   298.867818/s
     success_rate...................: 100.00% ✓ 36134      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 97968      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   325 kB/s
     http_req_blocked...............: avg=8.99µs   min=1.04µs  med=2.87µs   max=9.73ms   p(90)=4.09µs   p(95)=4.58µs   p(99.9)=3.02ms  
     http_req_connecting............: avg=5.52µs   min=0s      med=0s       max=9.52ms   p(90)=0s       p(95)=0s       p(99.9)=2.6ms   
     http_req_duration..............: avg=183.01ms min=7.54ms  med=181.73ms max=349.86ms p(90)=196.31ms p(95)=201.19ms p(99.9)=282.03ms
       { expected_response:true }...: avg=183.01ms min=7.54ms  med=181.73ms max=349.86ms p(90)=196.31ms p(95)=201.19ms p(99.9)=282.03ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32756
     http_req_receiving.............: avg=85.39µs  min=27.51µs med=81.3µs   max=56.76ms  p(90)=110.55µs p(95)=121.03µs p(99.9)=419.35µs
     http_req_sending...............: avg=22.53µs  min=4.76µs  med=15.21µs  max=52.21ms  p(90)=19.13µs  p(95)=20.67µs  p(99.9)=651.09µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.9ms  min=7.43ms  med=181.63ms max=349.64ms p(90)=196.2ms  p(95)=201.08ms p(99.9)=281.95ms
     http_reqs......................: 32756   270.846863/s
     iteration_duration.............: avg=183.82ms min=31.9ms  med=182.07ms max=366.08ms p(90)=196.58ms p(95)=201.48ms p(99.9)=282.82ms
     iterations.....................: 32656   270.020001/s
     success_rate...................: 100.00% ✓ 32656      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

