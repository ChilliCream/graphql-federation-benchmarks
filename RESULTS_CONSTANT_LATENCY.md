## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.10 | 3,502 | 3,518 | 3,499 | 0.2% | 388 MB | 113.5 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.10 | 3,451 | 3,485 | 3,441 | 0.5% | 124 MB | 36.7 KB |  |
| fusion-net-11 | 16.7.5 | 3,389 | 3,416 | 3,377 | 0.5% | 379 MB | 114.4 KB |  |
| fusion-aot-11 | 16.7.5 | 3,342 | 3,350 | 3,324 | 0.3% | 136 MB | 41.8 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,300 | 3,309 | 3,262 | 0.6% | 2,302 MB | 714.2 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.10 | 2,828 | 2,832 | 2,810 | 0.3% | 403 MB | 145.8 KB |  |
| fusion-fed-net-11 | 16.7.5 | 2,792 | 2,794 | 2,779 | 0.2% | 379 MB | 139.0 KB |  |
| fusion-fed-aot-11 | 16.7.5 | 2,759 | 2,771 | 2,740 | 0.5% | 159 MB | 59.2 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.10 | 2,757 | 2,781 | 2,753 | 0.5% | 133 MB | 49.4 KB |  |
| hive-router | v0.3.10 | 2,037 | 2,052 | 2,030 | 0.4% | 92 MB | 46.4 KB |  |
| grafbase | 0.53.5 | 1,425 | 1,442 | 1,423 | 0.6% | 100 MB | 72.0 KB |  |
| cosmo | 0.365.2 | 1,417 | 1,419 | 1,416 | 0.1% | 150 MB | 108.3 KB |  |
| caliban | 3.2.0 | 1,347 | 1,349 | 1,344 | 0.2% | 4,614 MB | 3,507.9 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 529 | 530 | 527 | 0.2% | 2,775 MB | 5,371.9 KB |  |
| apollo-router | v2.19.0 | 527 | 528 | 527 | 0.1% | 177 MB | 344.7 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 413 | 413 | 410 | 0.3% | 205 MB | 507.6 KB |  |
| apollo-gateway | 2.14.4 | 268 | 269 | 267 | 0.3% | 2,160 MB | 8,254.5 KB |  |
| hive-gateway | 2.15.6 | 254 | 254 | 253 | 0.2% | 3,515 MB | 14,169.9 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1270728     ✗ 0     
     data_received..................: 37 GB   307 MB/s
     data_sent......................: 509 MB  4.2 MB/s
     http_req_blocked...............: avg=2.82µs  min=931ns  med=2.23µs  max=4.05ms   p(90)=3.56µs  p(95)=4.28µs   p(99.9)=28.99µs
     http_req_connecting............: avg=245ns   min=0s     med=0s      max=4.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.95ms min=8.19ms med=13.51ms max=313.5ms  p(90)=17.29ms p(95)=18.66ms  p(99.9)=27.06ms
       { expected_response:true }...: avg=13.95ms min=8.19ms med=13.51ms max=313.5ms  p(90)=17.29ms p(95)=18.66ms  p(99.9)=27.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 423676
     http_req_receiving.............: avg=71.64µs min=25.2µs med=45.3µs  max=55.33ms  p(90)=92.63µs p(95)=185.21µs p(99.9)=1.93ms 
     http_req_sending...............: avg=33.91µs min=4.43µs med=8.45µs  max=137.97ms p(90)=16.73µs p(95)=100.03µs p(99.9)=1.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.85ms min=8.14ms med=13.4ms  max=313.12ms p(90)=17.17ms p(95)=18.53ms  p(99.9)=26.72ms
     http_reqs......................: 423676  3502.763278/s
     iteration_duration.............: avg=14.15ms min=8.38ms med=13.7ms  max=323.2ms  p(90)=17.48ms p(95)=18.86ms  p(99.9)=27.29ms
     iterations.....................: 423576  3501.936523/s
     success_rate...................: 100.00% ✓ 423576      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1252086     ✗ 0     
     data_received..................: 37 GB   302 MB/s
     data_sent......................: 502 MB  4.1 MB/s
     http_req_blocked...............: avg=2.32µs  min=781ns   med=1.8µs   max=3.4ms    p(90)=2.94µs  p(95)=3.6µs    p(99.9)=24.95µs
     http_req_connecting............: avg=198ns   min=0s      med=0s      max=3.36ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.17ms min=8.33ms  med=13.78ms max=281.98ms p(90)=17.29ms p(95)=18.54ms  p(99.9)=25.69ms
       { expected_response:true }...: avg=14.17ms min=8.33ms  med=13.78ms max=281.98ms p(90)=17.29ms p(95)=18.54ms  p(99.9)=25.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 417462
     http_req_receiving.............: avg=66.61µs min=24.22µs med=43.56µs max=124.34ms p(90)=87.37µs p(95)=167.31µs p(99.9)=1.53ms 
     http_req_sending...............: avg=30.37µs min=4.09µs  med=7.76µs  max=166.11ms p(90)=15.42µs p(95)=93.3µs   p(99.9)=1.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.08ms min=8.27ms  med=13.68ms max=281.5ms  p(90)=17.18ms p(95)=18.43ms  p(99.9)=25.53ms
     http_reqs......................: 417462  3451.152722/s
     iteration_duration.............: avg=14.36ms min=8.47ms  med=13.96ms max=298.57ms p(90)=17.47ms p(95)=18.72ms  p(99.9)=25.91ms
     iterations.....................: 417362  3450.326024/s
     success_rate...................: 100.00% ✓ 417362      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1229571     ✗ 0     
     data_received..................: 36 GB   297 MB/s
     data_sent......................: 493 MB  4.1 MB/s
     http_req_blocked...............: avg=2.41µs  min=791ns  med=1.82µs  max=7.14ms   p(90)=3.03µs  p(95)=3.79µs   p(99.9)=24.71µs
     http_req_connecting............: avg=205ns   min=0s     med=0s      max=3.39ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.43ms min=8.14ms med=14.01ms max=273.96ms p(90)=17.96ms p(95)=19.35ms  p(99.9)=27.85ms
       { expected_response:true }...: avg=14.43ms min=8.14ms med=14.01ms max=273.96ms p(90)=17.96ms p(95)=19.35ms  p(99.9)=27.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 409957
     http_req_receiving.............: avg=68.7µs  min=23.5µs med=41.98µs max=160.87ms p(90)=90.21µs p(95)=170.25µs p(99.9)=2.04ms 
     http_req_sending...............: avg=30.91µs min=4.08µs med=7.68µs  max=178.74ms p(90)=16.35µs p(95)=91.03µs  p(99.9)=1.96ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.33ms min=8.05ms med=13.91ms max=273.45ms p(90)=17.86ms p(95)=19.24ms  p(99.9)=27.62ms
     http_reqs......................: 409957  3389.275983/s
     iteration_duration.............: avg=14.63ms min=8.32ms med=14.2ms  max=284.57ms p(90)=18.15ms p(95)=19.54ms  p(99.9)=28.06ms
     iterations.....................: 409857  3388.449244/s
     success_rate...................: 100.00% ✓ 409857      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1212726     ✗ 0     
     data_received..................: 35 GB   293 MB/s
     data_sent......................: 486 MB  4.0 MB/s
     http_req_blocked...............: avg=2.83µs  min=912ns  med=2.26µs  max=23.62ms  p(90)=3.61µs  p(95)=4.33µs   p(99.9)=30.63µs
     http_req_connecting............: avg=166ns   min=0s     med=0s      max=3.07ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.63ms min=8.44ms med=14.19ms max=287.31ms p(90)=18.13ms p(95)=19.53ms  p(99.9)=28.05ms
       { expected_response:true }...: avg=14.63ms min=8.44ms med=14.19ms max=287.31ms p(90)=18.13ms p(95)=19.53ms  p(99.9)=28.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 404342
     http_req_receiving.............: avg=71.8µs  min=24.5µs med=45.82µs max=59.62ms  p(90)=93.29µs p(95)=180.69µs p(99.9)=1.89ms 
     http_req_sending...............: avg=32.25µs min=4.37µs med=8.48µs  max=84.68ms  p(90)=16.82µs p(95)=98.9µs   p(99.9)=1.78ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.53ms min=8.4ms  med=14.09ms max=287ms    p(90)=18.02ms p(95)=19.41ms  p(99.9)=27.82ms
     http_reqs......................: 404342  3342.570066/s
     iteration_duration.............: avg=14.83ms min=8.64ms med=14.38ms max=297.73ms p(90)=18.32ms p(95)=19.72ms  p(99.9)=28.27ms
     iterations.....................: 404242  3341.743397/s
     success_rate...................: 100.00% ✓ 404242      ✗ 0     
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

     checks.........................: 100.00% ✓ 1197360     ✗ 0     
     data_received..................: 35 GB   288 MB/s
     data_sent......................: 480 MB  4.0 MB/s
     http_req_blocked...............: avg=2.97µs  min=802ns   med=2.34µs  max=3.88ms   p(90)=3.85µs  p(95)=4.69µs   p(99.9)=30.69µs
     http_req_connecting............: avg=247ns   min=0s      med=0s      max=3.85ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.82ms min=8.52ms  med=14.45ms max=298.14ms p(90)=17.95ms p(95)=19.21ms  p(99.9)=26.9ms 
       { expected_response:true }...: avg=14.82ms min=8.52ms  med=14.45ms max=298.14ms p(90)=17.95ms p(95)=19.21ms  p(99.9)=26.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 399220
     http_req_receiving.............: avg=74.84µs min=24.16µs med=47.23µs max=218.57ms p(90)=98.02µs p(95)=184.91µs p(99.9)=1.93ms 
     http_req_sending...............: avg=34.27µs min=4.51µs  med=8.87µs  max=100.15ms p(90)=18.57µs p(95)=102.84µs p(99.9)=1.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.71ms min=8.47ms  med=14.35ms max=277.95ms p(90)=17.83ms p(95)=19.08ms  p(99.9)=26.64ms
     http_reqs......................: 399220  3300.224272/s
     iteration_duration.............: avg=15.02ms min=8.65ms  med=14.65ms max=310.16ms p(90)=18.15ms p(95)=19.41ms  p(99.9)=27.11ms
     iterations.....................: 399120  3299.397604/s
     success_rate...................: 100.00% ✓ 399120      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1029666     ✗ 0     
     data_received..................: 30 GB   248 MB/s
     data_sent......................: 413 MB  3.4 MB/s
     http_req_blocked...............: avg=2.48µs  min=781ns   med=1.82µs  max=3.92ms   p(90)=3.18µs  p(95)=3.99µs   p(99.9)=24.93µs
     http_req_connecting............: avg=285ns   min=0s      med=0s      max=3.87ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.27ms min=11.76ms med=16.87ms max=281.74ms p(90)=20.12ms p(95)=21.3ms   p(99.9)=27.35ms
       { expected_response:true }...: avg=17.27ms min=11.76ms med=16.87ms max=281.74ms p(90)=20.12ms p(95)=21.3ms   p(99.9)=27.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 343322
     http_req_receiving.............: avg=68.67µs min=24.32µs med=44.86µs max=200.49ms p(90)=90.87µs p(95)=140.32µs p(99.9)=1.33ms 
     http_req_sending...............: avg=28.5µs  min=4.11µs  med=7.68µs  max=160.8ms  p(90)=15.62µs p(95)=79.49µs  p(99.9)=1.32ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.17ms min=11.66ms med=16.78ms max=281.29ms p(90)=20.02ms p(95)=21.19ms  p(99.9)=27.11ms
     http_reqs......................: 343322  2828.124628/s
     iteration_duration.............: avg=17.47ms min=11.95ms med=17.07ms max=290.93ms p(90)=20.32ms p(95)=21.49ms  p(99.9)=27.55ms
     iterations.....................: 343222  2827.300875/s
     success_rate...................: 100.00% ✓ 343222      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1016715     ✗ 0     
     data_received..................: 30 GB   244 MB/s
     data_sent......................: 407 MB  3.4 MB/s
     http_req_blocked...............: avg=2.83µs  min=911ns   med=2.21µs  max=3.52ms   p(90)=3.63µs  p(95)=4.39µs   p(99.9)=29.32µs
     http_req_connecting............: avg=257ns   min=0s      med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.48ms min=11.85ms med=17.03ms max=271.89ms p(90)=20.58ms p(95)=21.85ms  p(99.9)=28.89ms
       { expected_response:true }...: avg=17.48ms min=11.85ms med=17.03ms max=271.89ms p(90)=20.58ms p(95)=21.85ms  p(99.9)=28.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 339005
     http_req_receiving.............: avg=69.01µs min=23.81µs med=45.14µs max=80.49ms  p(90)=93.97µs p(95)=156.45µs p(99.9)=1.52ms 
     http_req_sending...............: avg=30.05µs min=4.16µs  med=8.43µs  max=202.6ms  p(90)=17.36µs p(95)=88.55µs  p(99.9)=1.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.38ms min=11.79ms med=16.94ms max=271.38ms p(90)=20.46ms p(95)=21.73ms  p(99.9)=28.6ms 
     http_reqs......................: 339005  2792.627413/s
     iteration_duration.............: avg=17.69ms min=12.03ms med=17.23ms max=307.82ms p(90)=20.77ms p(95)=22.05ms  p(99.9)=29.14ms
     iterations.....................: 338905  2791.803641/s
     success_rate...................: 100.00% ✓ 338905      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1004847     ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 403 MB  3.3 MB/s
     http_req_blocked...............: avg=2.93µs  min=871ns   med=2.27µs  max=4.12ms   p(90)=3.77µs  p(95)=4.56µs   p(99.9)=31.43µs
     http_req_connecting............: avg=280ns   min=0s      med=0s      max=4.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.69ms min=11.64ms med=17.27ms max=312.78ms p(90)=20.66ms p(95)=21.92ms  p(99.9)=29.16ms
       { expected_response:true }...: avg=17.69ms min=11.64ms med=17.27ms max=312.78ms p(90)=20.66ms p(95)=21.92ms  p(99.9)=29.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 335049
     http_req_receiving.............: avg=93.26µs min=23.85µs med=45.81µs max=266.14ms p(90)=94.77µs p(95)=153.68µs p(99.9)=1.58ms 
     http_req_sending...............: avg=30.33µs min=4.51µs  med=8.75µs  max=94.06ms  p(90)=17.89µs p(95)=88.94µs  p(99.9)=1.73ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.57ms min=11.58ms med=17.18ms max=71.98ms  p(90)=20.55ms p(95)=21.79ms  p(99.9)=28.88ms
     http_reqs......................: 335049  2759.597963/s
     iteration_duration.............: avg=17.9ms  min=11.84ms med=17.48ms max=321.22ms p(90)=20.86ms p(95)=22.12ms  p(99.9)=29.37ms
     iterations.....................: 334949  2758.774323/s
     success_rate...................: 100.00% ✓ 334949      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1003890     ✗ 0     
     data_received..................: 29 GB   241 MB/s
     data_sent......................: 402 MB  3.3 MB/s
     http_req_blocked...............: avg=2.47µs  min=822ns   med=1.86µs  max=3.59ms   p(90)=3.15µs  p(95)=3.91µs   p(99.9)=24.81µs
     http_req_connecting............: avg=265ns   min=0s      med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.72ms min=12.07ms med=17.3ms  max=280.87ms p(90)=20.7ms  p(95)=21.96ms  p(99.9)=28.64ms
       { expected_response:true }...: avg=17.72ms min=12.07ms med=17.3ms  max=280.87ms p(90)=20.7ms  p(95)=21.96ms  p(99.9)=28.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 334730
     http_req_receiving.............: avg=64µs    min=24.13µs med=43.15µs max=13.63ms  p(90)=88.88µs p(95)=140.11µs p(99.9)=1.28ms 
     http_req_sending...............: avg=28.19µs min=4.44µs  med=8.06µs  max=214.56ms p(90)=16.58µs p(95)=82.04µs  p(99.9)=1.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.62ms min=12ms    med=17.21ms max=280.31ms p(90)=20.6ms  p(95)=21.86ms  p(99.9)=28.44ms
     http_reqs......................: 334730  2757.091/s
     iteration_duration.............: avg=17.92ms min=12.22ms med=17.5ms  max=296ms    p(90)=20.9ms  p(95)=22.16ms  p(99.9)=28.89ms
     iterations.....................: 334630  2756.267323/s
     success_rate...................: 100.00% ✓ 334630      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 744633      ✗ 0     
     data_received..................: 22 GB   178 MB/s
     data_sent......................: 298 MB  2.4 MB/s
     http_req_blocked...............: avg=2.86µs  min=841ns   med=2.08µs  max=4.32ms   p(90)=3.73µs  p(95)=4.45µs   p(99.9)=30.59µs 
     http_req_connecting............: avg=413ns   min=0s      med=0s      max=4.28ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.95ms min=17.18ms med=23.62ms max=288.45ms p(90)=26.94ms p(95)=28.03ms  p(99.9)=33.47ms 
       { expected_response:true }...: avg=23.95ms min=17.18ms med=23.62ms max=288.45ms p(90)=26.94ms p(95)=28.03ms  p(99.9)=33.47ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 248311
     http_req_receiving.............: avg=64.5µs  min=23.5µs  med=49.25µs max=69.31ms  p(90)=91.1µs  p(95)=113.32µs p(99.9)=845.93µs
     http_req_sending...............: avg=23.62µs min=4.45µs  med=9.16µs  max=169.54ms p(90)=17.01µs p(95)=22.67µs  p(99.9)=888.52µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.87ms min=17.13ms med=23.53ms max=287.98ms p(90)=26.85ms p(95)=27.93ms  p(99.9)=33.31ms 
     http_reqs......................: 248311  2037.395992/s
     iteration_duration.............: avg=24.16ms min=17.41ms med=23.82ms max=304.49ms p(90)=27.14ms p(95)=28.23ms  p(99.9)=33.69ms 
     iterations.....................: 248211  2036.57549/s
     success_rate...................: 100.00% ✓ 248211      ✗ 0     
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

     checks.........................: 100.00% ✓ 521295      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.34µs  min=882ns   med=2.31µs  max=3.86ms   p(90)=4.54µs   p(95)=5.43µs   p(99.9)=41.31µs
     http_req_connecting............: avg=510ns   min=0s      med=0s      max=3.83ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.27ms min=17.65ms med=33.99ms max=297.17ms p(90)=40.04ms  p(95)=41.73ms  p(99.9)=50.56ms
       { expected_response:true }...: avg=34.27ms min=17.65ms med=33.99ms max=297.17ms p(90)=40.04ms  p(95)=41.73ms  p(99.9)=50.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 173865
     http_req_receiving.............: avg=81.8µs  min=26.66µs med=55.35µs max=189.15ms p(90)=118.85µs p(95)=165.17µs p(99.9)=1.41ms 
     http_req_sending...............: avg=30.35µs min=4.53µs  med=9.65µs  max=142.47ms p(90)=22.23µs  p(95)=56.21µs  p(99.9)=1.32ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.16ms min=17.57ms med=33.89ms max=296.8ms  p(90)=39.93ms  p(95)=41.63ms  p(99.9)=50.33ms
     http_reqs......................: 173865  1425.850355/s
     iteration_duration.............: avg=34.52ms min=21.21ms med=34.23ms max=313.87ms p(90)=40.26ms  p(95)=41.95ms  p(99.9)=50.98ms
     iterations.....................: 173765  1425.030264/s
     success_rate...................: 100.00% ✓ 173765      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 518538      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=3.66µs  min=1.08µs  med=2.72µs  max=4.18ms   p(90)=4.36µs   p(95)=5.1µs    p(99.9)=37.09µs 
     http_req_connecting............: avg=593ns   min=0s      med=0s      max=4.14ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.48ms min=18.07ms med=33.92ms max=307.51ms p(90)=41.16ms  p(95)=43.45ms  p(99.9)=55.6ms  
       { expected_response:true }...: avg=34.48ms min=18.07ms med=33.92ms max=307.51ms p(90)=41.16ms  p(95)=43.45ms  p(99.9)=55.6ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 172946
     http_req_receiving.............: avg=75.65µs min=25.59µs med=61.86µs max=179.25ms p(90)=100.44µs p(95)=117.57µs p(99.9)=795.28µs
     http_req_sending...............: avg=22.76µs min=4.89µs  med=11.56µs max=46.23ms  p(90)=18.49µs  p(95)=22.56µs  p(99.9)=809.85µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.38ms min=17.99ms med=33.82ms max=307.28ms p(90)=41.06ms  p(95)=43.35ms  p(99.9)=55.39ms 
     http_reqs......................: 172946  1417.958478/s
     iteration_duration.............: avg=34.7ms  min=20.89ms med=34.12ms max=317.4ms  p(90)=41.36ms  p(95)=43.65ms  p(99.9)=55.9ms  
     iterations.....................: 172846  1417.138593/s
     success_rate...................: 100.00% ✓ 172846      ✗ 0     
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

     checks.........................: 100.00% ✓ 492645      ✗ 0     
     data_received..................: 14 GB   118 MB/s
     data_sent......................: 197 MB  1.6 MB/s
     http_req_blocked...............: avg=3.62µs  min=992ns   med=2.66µs  max=4.22ms   p(90)=4.17µs  p(95)=4.84µs  p(99.9)=34.27µs 
     http_req_connecting............: avg=658ns   min=0s      med=0s      max=4.19ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=36.31ms min=18.24ms med=35.77ms max=302.79ms p(90)=43.24ms p(95)=45.68ms p(99.9)=59.3ms  
       { expected_response:true }...: avg=36.31ms min=18.24ms med=35.77ms max=302.79ms p(90)=43.24ms p(95)=45.68ms p(99.9)=59.3ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 164315
     http_req_receiving.............: avg=70.91µs min=28.23µs med=59.35µs max=90.06ms  p(90)=93.02µs p(95)=108µs   p(99.9)=770.81µs
     http_req_sending...............: avg=22µs    min=5.03µs  med=11.23µs max=126.2ms  p(90)=16.76µs p(95)=20.13µs p(99.9)=722.06µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=36.21ms min=18.17ms med=35.68ms max=293.48ms p(90)=43.15ms p(95)=45.59ms p(99.9)=59.19ms 
     http_reqs......................: 164315  1347.110609/s
     iteration_duration.............: avg=36.53ms min=20.63ms med=35.97ms max=314.54ms p(90)=43.45ms p(95)=45.88ms p(99.9)=59.69ms 
     iterations.....................: 164215  1346.290774/s
     success_rate...................: 100.00% ✓ 164215      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 193737     ✗ 0    
     data_received..................: 5.7 GB  46 MB/s
     data_sent......................: 78 MB   636 kB/s
     http_req_blocked...............: avg=4.52µs  min=1.05µs  med=2.56µs  max=4.03ms   p(90)=3.97µs   p(95)=4.56µs   p(99.9)=49.29µs 
     http_req_connecting............: avg=1.7µs   min=0s      med=0s      max=3.99ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.58ms min=20.75ms med=90.67ms max=341.89ms p(90)=110.69ms p(95)=120.01ms p(99.9)=212.9ms 
       { expected_response:true }...: avg=92.58ms min=20.75ms med=90.67ms max=341.89ms p(90)=110.69ms p(95)=120.01ms p(99.9)=212.9ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 64679
     http_req_receiving.............: avg=79.69µs min=28.02µs med=71.6µs  max=52.92ms  p(90)=105.14µs p(95)=117.44µs p(99.9)=585.73µs
     http_req_sending...............: avg=22.2µs  min=5.13µs  med=13.26µs max=90.74ms  p(90)=18.75µs  p(95)=20.73µs  p(99.9)=523.93µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.48ms min=20.69ms med=90.57ms max=341.59ms p(90)=110.59ms p(95)=119.92ms p(99.9)=212.72ms
     http_reqs......................: 64679   529.215322/s
     iteration_duration.............: avg=92.92ms min=32.29ms med=90.92ms max=350.34ms p(90)=110.92ms p(95)=120.3ms  p(99.9)=213.86ms
     iterations.....................: 64579   528.397103/s
     success_rate...................: 100.00% ✓ 64579      ✗ 0    
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

     checks.........................: 100.00% ✓ 192939     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   633 kB/s
     http_req_blocked...............: avg=4.66µs  min=1.08µs  med=2.98µs  max=3.64ms   p(90)=4.47µs   p(95)=5.03µs   p(99.9)=44.57µs 
     http_req_connecting............: avg=1.47µs  min=0s      med=0s      max=3.61ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.95ms min=19.79ms med=91.15ms max=322.54ms p(90)=117.04ms p(95)=125.32ms p(99.9)=160.23ms
       { expected_response:true }...: avg=92.95ms min=19.79ms med=91.15ms max=322.54ms p(90)=117.04ms p(95)=125.32ms p(99.9)=160.23ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64413
     http_req_receiving.............: avg=77.31µs min=28.1µs  med=71.84µs max=54.56ms  p(90)=103.8µs  p(95)=115.68µs p(99.9)=500.1µs 
     http_req_sending...............: avg=19.02µs min=5.06µs  med=14.21µs max=46.66ms  p(90)=19.81µs  p(95)=21.81µs  p(99.9)=577.24µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.85ms min=19.69ms med=91.06ms max=321.87ms p(90)=116.95ms p(95)=125.23ms p(99.9)=159.85ms
     http_reqs......................: 64413   527.068623/s
     iteration_duration.............: avg=93.31ms min=40.09ms med=91.42ms max=344.04ms p(90)=117.31ms p(95)=125.59ms p(99.9)=161.82ms
     iterations.....................: 64313   526.250359/s
     success_rate...................: 100.00% ✓ 64313      ✗ 0    
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

     checks.........................: 100.00% ✓ 151491     ✗ 0    
     data_received..................: 4.4 GB  36 MB/s
     data_sent......................: 61 MB   497 kB/s
     http_req_blocked...............: avg=5.57µs   min=1.31µs  med=3.35µs   max=4.57ms   p(90)=4.83µs   p(95)=5.43µs   p(99.9)=151.84µs
     http_req_connecting............: avg=1.98µs   min=0s      med=0s       max=4.5ms    p(90)=0s       p(95)=0s       p(99.9)=39.4µs  
     http_req_duration..............: avg=118.39ms min=21.03ms med=116.79ms max=353.67ms p(90)=146.46ms p(95)=156.15ms p(99.9)=199.1ms 
       { expected_response:true }...: avg=118.39ms min=21.03ms med=116.79ms max=353.67ms p(90)=146.46ms p(95)=156.15ms p(99.9)=199.1ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 50597
     http_req_receiving.............: avg=85.15µs  min=29.42µs med=78.62µs  max=119.22ms p(90)=109.85µs p(95)=121.66µs p(99.9)=497.89µs
     http_req_sending...............: avg=32.72µs  min=5.85µs  med=16.42µs  max=128.91ms p(90)=21.75µs  p(95)=23.79µs  p(99.9)=560.1µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=118.28ms min=20.89ms med=116.68ms max=352.92ms p(90)=146.33ms p(95)=156.02ms p(99.9)=198.27ms
     http_reqs......................: 50597   413.584229/s
     iteration_duration.............: avg=118.84ms min=34.98ms med=117.08ms max=363.01ms p(90)=146.74ms p(95)=156.39ms p(99.9)=200.49ms
     iterations.....................: 50497   412.76682/s
     success_rate...................: 100.00% ✓ 50497      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 98616      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   323 kB/s
     http_req_blocked...............: avg=8.85µs   min=1.4µs   med=3.46µs   max=8.04ms   p(90)=4.86µs   p(95)=5.47µs   p(99.9)=1.59ms  
     http_req_connecting............: avg=4.98µs   min=0s      med=0s       max=7.67ms   p(90)=0s       p(95)=0s       p(99.9)=1.45ms  
     http_req_duration..............: avg=181.85ms min=22.85ms med=156.56ms max=410.52ms p(90)=285.08ms p(95)=289.38ms p(99.9)=361.1ms 
       { expected_response:true }...: avg=181.85ms min=22.85ms med=156.56ms max=410.52ms p(90)=285.08ms p(95)=289.38ms p(99.9)=361.1ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 32972
     http_req_receiving.............: avg=87.29µs  min=33.37µs med=83.28µs  max=16.97ms  p(90)=113.62µs p(95)=124.41µs p(99.9)=427.3µs 
     http_req_sending...............: avg=22.26µs  min=6.05µs  med=17.05µs  max=31.14ms  p(90)=21.85µs  p(95)=23.73µs  p(99.9)=487.09µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.74ms min=22.71ms med=156.45ms max=409.59ms p(90)=284.97ms p(95)=289.27ms p(99.9)=361ms   
     http_reqs......................: 32972   268.951446/s
     iteration_duration.............: avg=182.61ms min=76.59ms med=156.86ms max=417.59ms p(90)=285.35ms p(95)=289.64ms p(99.9)=361.46ms
     iterations.....................: 32872   268.13575/s
     success_rate...................: 100.00% ✓ 32872      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 92955      ✗ 0    
     data_received..................: 2.7 GB  22 MB/s
     data_sent......................: 37 MB   306 kB/s
     http_req_blocked...............: avg=5.87µs   min=1.4µs   med=3.44µs   max=2.79ms   p(90)=4.79µs   p(95)=5.36µs   p(99.9)=1.02ms  
     http_req_connecting............: avg=2.13µs   min=0s      med=0s       max=2.64ms   p(90)=0s       p(95)=0s       p(99.9)=978.31µs
     http_req_duration..............: avg=192.94ms min=17.79ms med=178.17ms max=764.42ms p(90)=230.59ms p(95)=253.94ms p(99.9)=689.31ms
       { expected_response:true }...: avg=192.94ms min=17.79ms med=178.17ms max=764.42ms p(90)=230.59ms p(95)=253.94ms p(99.9)=689.31ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31085
     http_req_receiving.............: avg=93.44µs  min=33.63µs med=83.89µs  max=50.51ms  p(90)=113.09µs p(95)=124.12µs p(99.9)=900.54µs
     http_req_sending...............: avg=23.89µs  min=6.17µs  med=16.66µs  max=29.14ms  p(90)=21.38µs  p(95)=23.15µs  p(99.9)=817.62µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=192.82ms min=17.65ms med=178.06ms max=764.33ms p(90)=230.47ms p(95)=253.8ms  p(99.9)=689.2ms 
     http_reqs......................: 31085   254.640428/s
     iteration_duration.............: avg=193.76ms min=75.07ms med=178.59ms max=764.64ms p(90)=230.91ms p(95)=254.71ms p(99.9)=689.61ms
     iterations.....................: 30985   253.821254/s
     success_rate...................: 100.00% ✓ 30985      ✗ 0    
     vus............................: 34      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

