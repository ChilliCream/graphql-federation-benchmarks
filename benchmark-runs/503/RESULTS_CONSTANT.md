## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.23 | 5,551 | 5,583 | 5,478 | 0.7% | 343 MB | 63.3 KB |  |
| nitro-router-fed | 16.8.0-p.23 | 5,538 | 5,563 | 5,519 | 0.4% | 137 MB | 25.3 KB |  |
| nitro-router | 16.8.0-p.23 | 5,528 | 5,598 | 5,524 | 0.6% | 127 MB | 23.5 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.23 | 5,480 | 5,527 | 5,471 | 0.4% | 119 MB | 22.3 KB |  |
| fusion-fed-net-11 | 16.7.7 | 5,443 | 5,451 | 5,429 | 0.1% | 362 MB | 68.1 KB |  |
| fusion-net-11 | 16.7.7 | 5,433 | 5,489 | 5,398 | 0.8% | 371 MB | 69.9 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.23 | 5,397 | 5,420 | 5,391 | 0.2% | 91 MB | 17.3 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.23 | 5,331 | 5,339 | 5,309 | 0.3% | 353 MB | 67.8 KB |  |
| fusion-aot-11 | 16.7.7 | 5,303 | 5,326 | 5,279 | 0.4% | 111 MB | 21.5 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 5,268 | 5,287 | 5,224 | 0.5% | 120 MB | 23.4 KB |  |
| feddi-gateway | 2026-11-22-1912 | 5,130 | 5,153 | 5,119 | 0.3% | 2,304 MB | 459.9 KB |  |
| hive-router-nightly | v0.3.21-nightly.46ee6fa7 | 4,676 | 4,692 | 4,662 | 0.3% | 94 MB | 20.7 KB |  |
| hive-router | v0.3.17 | 4,570 | 4,587 | 4,549 | 0.3% | 94 MB | 21.1 KB |  |
| grafbase | 0.53.5 | 1,842 | 1,853 | 1,836 | 0.4% | 106 MB | 58.8 KB |  |
| cosmo | 0.373.0 | 1,509 | 1,509 | 1,507 | 0.1% | 169 MB | 114.7 KB |  |
| caliban | 3.2.1 | 1,495 | 1,496 | 1,493 | 0.1% | 6,927 MB | 4,744.5 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 620 | 624 | 619 | 0.3% | 2,609 MB | 4,309.5 KB |  |
| apollo-router | v2.19.1 | 537 | 538 | 536 | 0.2% | 172 MB | 327.3 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.b135f054 | 520 | 520 | 519 | 0.1% | 195 MB | 383.3 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 402 | 402 | 402 | 0.0% | 198 MB | 505.5 KB |  |
| hive-gateway | 2.15.10 | 298 | 302 | 298 | 0.6% | 3,176 MB | 10,912.9 KB |  |
| apollo-gateway | 2.14.4 | 273 | 275 | 273 | 0.4% | 2,167 MB | 8,126.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1999878     ✗ 0     
     data_received..................: 58 GB   486 MB/s
     data_sent......................: 801 MB  6.7 MB/s
     http_req_blocked...............: avg=2.47µs  min=781ns    med=1.91µs  max=6.97ms   p(90)=2.92µs  p(95)=3.48µs   p(99.9)=26.54µs
     http_req_connecting............: avg=133ns   min=0s       med=0s      max=3.47ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.79ms  min=764.75µs med=7.88ms  max=285.91ms p(90)=14.13ms p(95)=17.28ms  p(99.9)=29.67ms
       { expected_response:true }...: avg=8.79ms  min=764.75µs med=7.88ms  max=285.91ms p(90)=14.13ms p(95)=17.28ms  p(99.9)=29.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 666726
     http_req_receiving.............: avg=93.06µs min=25.76µs  med=46.94µs max=154.77ms p(90)=84.35µs p(95)=183.34µs p(99.9)=6.16ms 
     http_req_sending...............: avg=41.36µs min=4.34µs   med=8.1µs   max=199.96ms p(90)=13.32µs p(95)=95.92µs  p(99.9)=4.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.66ms  min=704.31µs med=7.77ms  max=265.02ms p(90)=13.9ms  p(95)=17.01ms  p(99.9)=29.29ms
     http_reqs......................: 666726  5551.146811/s
     iteration_duration.............: avg=8.99ms  min=923.7µs  med=8.06ms  max=294.35ms p(90)=14.33ms p(95)=17.49ms  p(99.9)=29.95ms
     iterations.....................: 666626  5550.314213/s
     success_rate...................: 100.00% ✓ 666626      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: nitro-router-fed (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1995279     ✗ 0     
     data_received..................: 58 GB   485 MB/s
     data_sent......................: 800 MB  6.7 MB/s
     http_req_blocked...............: avg=2.43µs  min=761ns    med=1.89µs  max=6.05ms   p(90)=2.98µs  p(95)=3.59µs   p(99.9)=27.43µs
     http_req_connecting............: avg=149ns   min=0s       med=0s      max=4.07ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.81ms  min=799.26µs med=7.9ms   max=282.01ms p(90)=14.12ms p(95)=17.29ms  p(99.9)=29.61ms
       { expected_response:true }...: avg=8.81ms  min=799.26µs med=7.9ms   max=282.01ms p(90)=14.12ms p(95)=17.29ms  p(99.9)=29.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 665193
     http_req_receiving.............: avg=94.17µs min=24.04µs  med=46.09µs max=222.4ms  p(90)=86.35µs p(95)=185.58µs p(99.9)=6.48ms 
     http_req_sending...............: avg=41.17µs min=4.33µs   med=8.07µs  max=152.75ms p(90)=13.73µs p(95)=96.75µs  p(99.9)=4.77ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.68ms  min=751.96µs med=7.79ms  max=272.34ms p(90)=13.89ms p(95)=17ms     p(99.9)=29.15ms
     http_reqs......................: 665193  5538.300665/s
     iteration_duration.............: avg=9.01ms  min=1.22ms   med=8.08ms  max=297.59ms p(90)=14.33ms p(95)=17.51ms  p(99.9)=29.91ms
     iterations.....................: 665093  5537.468079/s
     success_rate...................: 100.00% ✓ 665093      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: nitro-router (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1991718     ✗ 0     
     data_received..................: 58 GB   484 MB/s
     data_sent......................: 798 MB  6.6 MB/s
     http_req_blocked...............: avg=3.08µs  min=822ns    med=2.38µs  max=17.36ms  p(90)=3.6µs   p(95)=4.25µs   p(99.9)=31.46µs
     http_req_connecting............: avg=315ns   min=0s       med=0s      max=17.11ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.82ms  min=768.79µs med=7.84ms  max=279.65ms p(90)=14.34ms p(95)=17.73ms  p(99.9)=30.8ms 
       { expected_response:true }...: avg=8.82ms  min=768.79µs med=7.84ms  max=279.65ms p(90)=14.34ms p(95)=17.73ms  p(99.9)=30.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 664006
     http_req_receiving.............: avg=99.85µs min=25.94µs  med=47.23µs max=128.37ms p(90)=87.8µs  p(95)=193.58µs p(99.9)=6.69ms 
     http_req_sending...............: avg=45.68µs min=4.11µs   med=8.69µs  max=246.57ms p(90)=14.21µs p(95)=101.71µs p(99.9)=5.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.68ms  min=724.06µs med=7.73ms  max=258.47ms p(90)=14.08ms p(95)=17.43ms  p(99.9)=30.17ms
     http_reqs......................: 664006  5528.695989/s
     iteration_duration.............: avg=9.02ms  min=1.06ms   med=8.03ms  max=314.17ms p(90)=14.55ms p(95)=17.96ms  p(99.9)=31.11ms
     iterations.....................: 663906  5527.863361/s
     success_rate...................: 100.00% ✓ 663906      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1974255     ✗ 0     
     data_received..................: 58 GB   480 MB/s
     data_sent......................: 791 MB  6.6 MB/s
     http_req_blocked...............: avg=6.09µs  min=962ns    med=2.37µs  max=147.47ms p(90)=3.58µs  p(95)=4.2µs    p(99.9)=33.34µs
     http_req_connecting............: avg=3.23µs  min=0s       med=0s      max=134.18ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.9ms   min=777.58µs med=7.92ms  max=188.02ms p(90)=14.49ms p(95)=18ms     p(99.9)=30.98ms
       { expected_response:true }...: avg=8.9ms   min=777.58µs med=7.92ms  max=188.02ms p(90)=14.49ms p(95)=18ms     p(99.9)=30.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 658185
     http_req_receiving.............: avg=98.69µs min=25.09µs  med=47.01µs max=102.54ms p(90)=89.86µs p(95)=198.53µs p(99.9)=6.61ms 
     http_req_sending...............: avg=44.14µs min=4.15µs   med=8.7µs   max=62.24ms  p(90)=14.38µs p(95)=102.51µs p(99.9)=5.17ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.76ms  min=716.87µs med=7.81ms  max=187.36ms p(90)=14.24ms p(95)=17.69ms  p(99.9)=30.47ms
     http_reqs......................: 658185  5480.120203/s
     iteration_duration.............: avg=9.1ms   min=1.1ms    med=8.11ms  max=270.76ms p(90)=14.71ms p(95)=18.22ms  p(99.9)=31.28ms
     iterations.....................: 658085  5479.287592/s
     success_rate...................: 100.00% ✓ 658085      ✗ 0     
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

     checks.........................: 100.00% ✓ 1961250     ✗ 0     
     data_received..................: 57 GB   476 MB/s
     data_sent......................: 786 MB  6.5 MB/s
     http_req_blocked...............: avg=3.13µs  min=892ns    med=2.33µs  max=7.88ms   p(90)=3.56µs  p(95)=4.22µs   p(99.9)=32.5µs 
     http_req_connecting............: avg=340ns   min=0s       med=0s      max=7.86ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.96ms  min=765.71µs med=7.97ms  max=274.36ms p(90)=14.55ms p(95)=17.92ms  p(99.9)=30.82ms
       { expected_response:true }...: avg=8.96ms  min=765.71µs med=7.97ms  max=274.36ms p(90)=14.55ms p(95)=17.92ms  p(99.9)=30.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 653850
     http_req_receiving.............: avg=96.8µs  min=24.19µs  med=46.72µs max=158.64ms p(90)=89.75µs p(95)=192.95µs p(99.9)=6.62ms 
     http_req_sending...............: avg=44.39µs min=4.3µs    med=8.69µs  max=185ms    p(90)=14.76µs p(95)=103.24µs p(99.9)=5.03ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.82ms  min=722.28µs med=7.86ms  max=271.56ms p(90)=14.3ms  p(95)=17.62ms  p(99.9)=30.32ms
     http_reqs......................: 653850  5443.934909/s
     iteration_duration.............: avg=9.16ms  min=1.06ms   med=8.16ms  max=291.49ms p(90)=14.76ms p(95)=18.14ms  p(99.9)=31.12ms
     iterations.....................: 653750  5443.102312/s
     success_rate...................: 100.00% ✓ 653750      ✗ 0     
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

     checks.........................: 100.00% ✓ 1957539     ✗ 0     
     data_received..................: 57 GB   476 MB/s
     data_sent......................: 784 MB  6.5 MB/s
     http_req_blocked...............: avg=2.99µs  min=931ns    med=2.34µs  max=7.2ms    p(90)=3.58µs  p(95)=4.24µs   p(99.9)=33.2µs 
     http_req_connecting............: avg=148ns   min=0s       med=0s      max=4.23ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.98ms  min=729.33µs med=7.98ms  max=278.76ms p(90)=14.6ms  p(95)=18.08ms  p(99.9)=31.25ms
       { expected_response:true }...: avg=8.98ms  min=729.33µs med=7.98ms  max=278.76ms p(90)=14.6ms  p(95)=18.08ms  p(99.9)=31.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 652613
     http_req_receiving.............: avg=99.9µs  min=24.77µs  med=47.01µs max=91.89ms  p(90)=89.87µs p(95)=197.94µs p(99.9)=6.64ms 
     http_req_sending...............: avg=44.76µs min=4.57µs   med=8.61µs  max=229.91ms p(90)=14.54µs p(95)=103.26µs p(99.9)=5.28ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.84ms  min=693.97µs med=7.86ms  max=278.36ms p(90)=14.34ms p(95)=17.77ms  p(99.9)=30.65ms
     http_reqs......................: 652613  5433.717962/s
     iteration_duration.............: avg=9.18ms  min=970.77µs med=8.17ms  max=300.05ms p(90)=14.82ms p(95)=18.3ms   p(99.9)=31.51ms
     iterations.....................: 652513  5432.885353/s
     success_rate...................: 100.00% ✓ 652513      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1944465    ✗ 0     
     data_received..................: 57 GB   472 MB/s
     data_sent......................: 779 MB  6.5 MB/s
     http_req_blocked...............: avg=2.39µs  min=781ns    med=1.87µs  max=7.83ms   p(90)=2.9µs   p(95)=3.46µs   p(99.9)=27.22µs
     http_req_connecting............: avg=153ns   min=0s       med=0s      max=4.3ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.05ms  min=802.57µs med=8.18ms  max=268.79ms p(90)=14.39ms p(95)=17.38ms  p(99.9)=29.4ms 
       { expected_response:true }...: avg=9.05ms  min=802.57µs med=8.18ms  max=268.79ms p(90)=14.39ms p(95)=17.38ms  p(99.9)=29.4ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 648255
     http_req_receiving.............: avg=90.29µs min=25.39µs  med=46.54µs max=33.29ms  p(90)=85.95µs p(95)=185.33µs p(99.9)=5.84ms 
     http_req_sending...............: avg=41µs    min=4.1µs    med=7.9µs   max=124.92ms p(90)=13.31µs p(95)=97.77µs  p(99.9)=4.64ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.92ms  min=756.41µs med=8.07ms  max=268.13ms p(90)=14.17ms p(95)=17.13ms  p(99.9)=29.03ms
     http_reqs......................: 648255  5397.37229/s
     iteration_duration.............: avg=9.24ms  min=1.06ms   med=8.36ms  max=279.3ms  p(90)=14.59ms p(95)=17.6ms   p(99.9)=29.67ms
     iterations.....................: 648155  5396.53969/s
     success_rate...................: 100.00% ✓ 648155     ✗ 0     
     vus............................: 50      min=50       max=50  
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.23)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1920531     ✗ 0     
     data_received..................: 56 GB   467 MB/s
     data_sent......................: 770 MB  6.4 MB/s
     http_req_blocked...............: avg=3.05µs  min=922ns    med=2.45µs  max=6.68ms   p(90)=3.7µs   p(95)=4.37µs   p(99.9)=32.82µs
     http_req_connecting............: avg=184ns   min=0s       med=0s      max=4.8ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.16ms  min=784.01µs med=8.16ms  max=278.65ms p(90)=14.78ms p(95)=18.15ms  p(99.9)=31.35ms
       { expected_response:true }...: avg=9.16ms  min=784.01µs med=8.16ms  max=278.65ms p(90)=14.78ms p(95)=18.15ms  p(99.9)=31.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 640277
     http_req_receiving.............: avg=100.3µs min=25.77µs  med=49.13µs max=176.77ms p(90)=91.21µs p(95)=199.36µs p(99.9)=6.5ms  
     http_req_sending...............: avg=44.39µs min=4.43µs   med=8.78µs  max=80.71ms  p(90)=14.61µs p(95)=104.14µs p(99.9)=5.17ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.01ms  min=731.52µs med=8.05ms  max=261.96ms p(90)=14.54ms p(95)=17.86ms  p(99.9)=30.87ms
     http_reqs......................: 640277  5331.189118/s
     iteration_duration.............: avg=9.36ms  min=1.15ms   med=8.35ms  max=291.67ms p(90)=15ms    p(95)=18.38ms  p(99.9)=31.6ms 
     iterations.....................: 640177  5330.35648/s
     success_rate...................: 100.00% ✓ 640177      ✗ 0     
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

     checks.........................: 100.00% ✓ 1910730     ✗ 0     
     data_received..................: 56 GB   464 MB/s
     data_sent......................: 766 MB  6.4 MB/s
     http_req_blocked...............: avg=2.9µs   min=922ns    med=2.3µs   max=11.38ms  p(90)=3.54µs  p(95)=4.17µs   p(99.9)=31.07µs
     http_req_connecting............: avg=139ns   min=0s       med=0s      max=3.61ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.21ms  min=831.57µs med=8.25ms  max=288.35ms p(90)=14.91ms p(95)=18.23ms  p(99.9)=30.88ms
       { expected_response:true }...: avg=9.21ms  min=831.57µs med=8.25ms  max=288.35ms p(90)=14.91ms p(95)=18.23ms  p(99.9)=30.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 637010
     http_req_receiving.............: avg=94.09µs min=24.6µs   med=45.69µs max=217.43ms p(90)=87.8µs  p(95)=199.37µs p(99.9)=6.13ms 
     http_req_sending...............: avg=42.75µs min=4.37µs   med=8.47µs  max=210.6ms  p(90)=14.42µs p(95)=104.27µs p(99.9)=4.8ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.07ms  min=760.11µs med=8.14ms  max=287.64ms p(90)=14.68ms p(95)=17.95ms  p(99.9)=30.55ms
     http_reqs......................: 637010  5303.694178/s
     iteration_duration.............: avg=9.41ms  min=1.21ms   med=8.44ms  max=314.94ms p(90)=15.12ms p(95)=18.45ms  p(99.9)=31.18ms
     iterations.....................: 636910  5302.861586/s
     success_rate...................: 100.00% ✓ 636910      ✗ 0     
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

     checks.........................: 100.00% ✓ 1898079     ✗ 0     
     data_received..................: 55 GB   461 MB/s
     data_sent......................: 761 MB  6.3 MB/s
     http_req_blocked...............: avg=2.64µs  min=812ns    med=1.99µs  max=7.44ms   p(90)=3.2µs   p(95)=3.84µs   p(99.9)=28.46µs
     http_req_connecting............: avg=146ns   min=0s       med=0s      max=4.04ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.27ms  min=882.44µs med=8.35ms  max=265.36ms p(90)=14.84ms p(95)=18.04ms  p(99.9)=30.49ms
       { expected_response:true }...: avg=9.27ms  min=882.44µs med=8.35ms  max=265.36ms p(90)=14.84ms p(95)=18.04ms  p(99.9)=30.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 632793
     http_req_receiving.............: avg=94.47µs min=24.9µs   med=46.18µs max=112.96ms p(90)=88.83µs p(95)=198.44µs p(99.9)=6.27ms 
     http_req_sending...............: avg=42.92µs min=4.49µs   med=8.36µs  max=94.11ms  p(90)=14.33µs p(95)=103.89µs p(99.9)=4.88ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.14ms  min=821.15µs med=8.24ms  max=265.03ms p(90)=14.61ms p(95)=17.76ms  p(99.9)=30.09ms
     http_reqs......................: 632793  5268.104625/s
     iteration_duration.............: avg=9.47ms  min=1.12ms   med=8.54ms  max=276.75ms p(90)=15.06ms p(95)=18.26ms  p(99.9)=30.77ms
     iterations.....................: 632693  5267.272108/s
     success_rate...................: 100.00% ✓ 632693      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1848378     ✗ 0     
     data_received..................: 54 GB   448 MB/s
     data_sent......................: 741 MB  6.2 MB/s
     http_req_blocked...............: avg=2.64µs   min=811ns    med=2.05µs  max=5.99ms   p(90)=3.32µs  p(95)=4.02µs   p(99.9)=30.78µs
     http_req_connecting............: avg=160ns    min=0s       med=0s      max=3.57ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.52ms   min=821.45µs med=8.54ms  max=286.95ms p(90)=15.29ms p(95)=18.65ms  p(99.9)=32.12ms
       { expected_response:true }...: avg=9.52ms   min=821.45µs med=8.54ms  max=286.95ms p(90)=15.29ms p(95)=18.65ms  p(99.9)=32.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 616226
     http_req_receiving.............: avg=100.86µs min=24.63µs  med=47.49µs max=30.5ms   p(90)=93.63µs p(95)=203.71µs p(99.9)=6.74ms 
     http_req_sending...............: avg=45.43µs  min=4.67µs   med=8.72µs  max=244.35ms p(90)=15.12µs p(95)=106.97µs p(99.9)=5.18ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.37ms   min=750.72µs med=8.42ms  max=286.6ms  p(90)=15.05ms p(95)=18.37ms  p(99.9)=31.69ms
     http_reqs......................: 616226  5130.406251/s
     iteration_duration.............: avg=9.72ms   min=1.27ms   med=8.73ms  max=297.97ms p(90)=15.51ms p(95)=18.88ms  p(99.9)=32.4ms 
     iterations.....................: 616126  5129.573698/s
     success_rate...................: 100.00% ✓ 616126      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.21-nightly.46ee6fa7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1684737    ✗ 0     
     data_received..................: 49 GB   409 MB/s
     data_sent......................: 675 MB  5.6 MB/s
     http_req_blocked...............: avg=3.92µs   min=912ns    med=2.6µs   max=16.83ms  p(90)=4.03µs   p(95)=4.79µs   p(99.9)=37.46µs
     http_req_connecting............: avg=809ns    min=0s       med=0s      max=16.71ms  p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.46ms  min=925.67µs med=9.65ms  max=251.02ms p(90)=15.29ms  p(95)=18.96ms  p(99.9)=30.93ms
       { expected_response:true }...: avg=10.46ms  min=925.67µs med=9.65ms  max=251.02ms p(90)=15.29ms  p(95)=18.96ms  p(99.9)=30.93ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 561679
     http_req_receiving.............: avg=101.92µs min=24.65µs  med=50.92µs max=105.84ms p(90)=101.69µs p(95)=219.16µs p(99.9)=6.5ms  
     http_req_sending...............: avg=46.68µs  min=4.54µs   med=9.47µs  max=56.98ms  p(90)=16.37µs  p(95)=115.36µs p(99.9)=5.12ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.31ms  min=872.93µs med=9.55ms  max=250.52ms p(90)=15ms     p(95)=18.64ms  p(99.9)=30.34ms
     http_reqs......................: 561679  4676.03726/s
     iteration_duration.............: avg=10.67ms  min=1.53ms   med=9.85ms  max=290.7ms  p(90)=15.51ms  p(95)=19.18ms  p(99.9)=31.24ms
     iterations.....................: 561579  4675.20475/s
     success_rate...................: 100.00% ✓ 561579     ✗ 0     
     vus............................: 50      min=50       max=50  
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 1646586     ✗ 0     
     data_received..................: 48 GB   400 MB/s
     data_sent......................: 660 MB  5.5 MB/s
     http_req_blocked...............: avg=3.45µs   min=962ns    med=2.61µs  max=7.93ms   p(90)=3.99µs   p(95)=4.7µs    p(99.9)=36.17µs
     http_req_connecting............: avg=395ns    min=0s       med=0s      max=7.84ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.72ms  min=925.72µs med=10.06ms max=276.61ms p(90)=15.27ms  p(95)=18.77ms  p(99.9)=30.25ms
       { expected_response:true }...: avg=10.72ms  min=925.72µs med=10.06ms max=276.61ms p(90)=15.27ms  p(95)=18.77ms  p(99.9)=30.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 548962
     http_req_receiving.............: avg=101.77µs min=25.23µs  med=50.93µs max=81.74ms  p(90)=100.29µs p(95)=220.61µs p(99.9)=6.65ms 
     http_req_sending...............: avg=44.23µs  min=4.54µs   med=9.46µs  max=80.97ms  p(90)=16.17µs  p(95)=115.2µs  p(99.9)=4.53ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.57ms  min=849.26µs med=9.96ms  max=275.74ms p(90)=15ms     p(95)=18.46ms  p(99.9)=29.76ms
     http_reqs......................: 548962  4570.072392/s
     iteration_duration.............: avg=10.92ms  min=1.53ms   med=10.25ms max=300.83ms p(90)=15.49ms  p(95)=19ms     p(99.9)=30.51ms
     iterations.....................: 548862  4569.239899/s
     success_rate...................: 100.00% ✓ 548862      ✗ 0     
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

     checks.........................: 100.00% ✓ 664431      ✗ 0     
     data_received..................: 19 GB   161 MB/s
     data_sent......................: 266 MB  2.2 MB/s
     http_req_blocked...............: avg=3.22µs  min=852ns   med=2.3µs   max=4.07ms   p(90)=4.46µs   p(95)=5.54µs   p(99.9)=34.12µs
     http_req_connecting............: avg=404ns   min=0s      med=0s      max=4.03ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.85ms min=1.83ms  med=26.25ms max=283.79ms p(90)=34.67ms  p(95)=37.5ms   p(99.9)=51.69ms
       { expected_response:true }...: avg=26.85ms min=1.83ms  med=26.25ms max=283.79ms p(90)=34.67ms  p(95)=37.5ms   p(99.9)=51.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 221577
     http_req_receiving.............: avg=81.47µs min=26.62µs med=57.93µs max=143.68ms p(90)=115.66µs p(95)=162.16µs p(99.9)=1.25ms 
     http_req_sending...............: avg=32.99µs min=4.63µs  med=10.02µs max=171.64ms p(90)=21.43µs  p(95)=76.52µs  p(99.9)=1.26ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.73ms min=1.78ms  med=26.14ms max=283.34ms p(90)=34.55ms  p(95)=37.37ms  p(99.9)=51.56ms
     http_reqs......................: 221577  1842.485176/s
     iteration_duration.............: avg=27.08ms min=8.23ms  med=26.46ms max=308.07ms p(90)=34.88ms  p(95)=37.71ms  p(99.9)=51.91ms
     iterations.....................: 221477  1841.653644/s
     success_rate...................: 100.00% ✓ 221477      ✗ 0     
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

     checks.........................: 100.00% ✓ 544320      ✗ 0     
     data_received..................: 16 GB   132 MB/s
     data_sent......................: 218 MB  1.8 MB/s
     http_req_blocked...............: avg=5.89µs   min=1.02µs  med=2.6µs   max=47.14ms  p(90)=4.15µs   p(95)=4.86µs   p(99.9)=31.22µs 
     http_req_connecting............: avg=2.93µs   min=0s      med=0s      max=47.1ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.83ms  min=1.99ms  med=31.98ms max=299.81ms p(90)=47.26ms  p(95)=52.13ms  p(99.9)=74.03ms 
       { expected_response:true }...: avg=32.83ms  min=1.99ms  med=31.98ms max=299.81ms p(90)=47.26ms  p(95)=52.13ms  p(99.9)=74.03ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 181540
     http_req_receiving.............: avg=107.94µs min=27.69µs med=63.77µs max=230.76ms p(90)=101.04µs p(95)=117.57µs p(99.9)=822.22µs
     http_req_sending...............: avg=26.38µs  min=4.76µs  med=11.29µs max=184.09ms p(90)=17.8µs   p(95)=21.82µs  p(99.9)=819.12µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.7ms   min=1.93ms  med=31.87ms max=98.26ms  p(90)=47.13ms  p(95)=52ms     p(99.9)=72.47ms 
     http_reqs......................: 181540  1509.349376/s
     iteration_duration.............: avg=33.06ms  min=4.11ms  med=32.18ms max=313.75ms p(90)=47.46ms  p(95)=52.33ms  p(99.9)=74.54ms 
     iterations.....................: 181440  1508.517962/s
     success_rate...................: 100.00% ✓ 181440      ✗ 0     
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

     checks.........................: 100.00% ✓ 539118      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 216 MB  1.8 MB/s
     http_req_blocked...............: avg=3.84µs  min=1.02µs  med=3.04µs  max=3.29ms   p(90)=4.68µs  p(95)=5.4µs   p(99.9)=38.84µs 
     http_req_connecting............: avg=505ns   min=0s      med=0s      max=3.25ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=33.14ms min=1.98ms  med=32.19ms max=296.74ms p(90)=47.22ms p(95)=52.21ms p(99.9)=80.53ms 
       { expected_response:true }...: avg=33.14ms min=1.98ms  med=32.19ms max=296.74ms p(90)=47.22ms p(95)=52.21ms p(99.9)=80.53ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 179806
     http_req_receiving.............: avg=74.8µs  min=28.58µs med=62.94µs max=107.07ms p(90)=98.85µs p(95)=114.1µs p(99.9)=861.01µs
     http_req_sending...............: avg=21.92µs min=4.89µs  med=12.08µs max=58.86ms  p(90)=18.49µs p(95)=22.31µs p(99.9)=785µs   
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=33.04ms min=1.88ms  med=32.09ms max=296.6ms  p(90)=47.13ms p(95)=52.11ms p(99.9)=80.37ms 
     http_reqs......................: 179806  1495.130798/s
     iteration_duration.............: avg=33.37ms min=4.88ms  med=32.4ms  max=310.37ms p(90)=47.44ms p(95)=52.44ms p(99.9)=80.99ms 
     iterations.....................: 179706  1494.299274/s
     success_rate...................: 100.00% ✓ 179706      ✗ 0     
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

     checks.........................: 100.00% ✓ 224100     ✗ 0    
     data_received..................: 6.5 GB  54 MB/s
     data_sent......................: 90 MB   746 kB/s
     http_req_blocked...............: avg=3.94µs  min=942ns   med=2.46µs  max=3.81ms   p(90)=3.94µs   p(95)=4.54µs   p(99.9)=41.58µs 
     http_req_connecting............: avg=1.22µs  min=0s      med=0s      max=3.77ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=79.99ms min=3.4ms   med=77.08ms max=309.34ms p(90)=96.55ms  p(95)=106.61ms p(99.9)=204.83ms
       { expected_response:true }...: avg=79.99ms min=3.4ms   med=77.08ms max=309.34ms p(90)=96.55ms  p(95)=106.61ms p(99.9)=204.83ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 74800
     http_req_receiving.............: avg=75.41µs min=27.13µs med=66.51µs max=153.49ms p(90)=100.53µs p(95)=113.08µs p(99.9)=496.28µs
     http_req_sending...............: avg=19.36µs min=4.74µs  med=12.58µs max=101.45ms p(90)=18.61µs  p(95)=20.54µs  p(99.9)=551.11µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=79.89ms min=3.28ms  med=76.99ms max=308.83ms p(90)=96.45ms  p(95)=106.51ms p(99.9)=204.7ms 
     http_reqs......................: 74800   620.961155/s
     iteration_duration.............: avg=80.32ms min=27.66ms med=77.3ms  max=327.07ms p(90)=96.78ms  p(95)=106.89ms p(99.9)=209.18ms
     iterations.....................: 74700   620.130993/s
     success_rate...................: 100.00% ✓ 74700      ✗ 0    
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

     checks.........................: 100.00% ✓ 194256     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   646 kB/s
     http_req_blocked...............: avg=5.03µs  min=1.24µs  med=3.46µs  max=3.49ms   p(90)=5.01µs   p(95)=5.64µs   p(99.9)=49.84µs 
     http_req_connecting............: avg=1.34µs  min=0s      med=0s      max=3.45ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.28ms min=4.43ms  med=90.17ms max=313.72ms p(90)=124.76ms p(95)=134.94ms p(99.9)=175.41ms
       { expected_response:true }...: avg=92.28ms min=4.43ms  med=90.17ms max=313.72ms p(90)=124.76ms p(95)=134.94ms p(99.9)=175.41ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64852
     http_req_receiving.............: avg=83.2µs  min=31.25µs med=75.83µs max=82.18ms  p(90)=107.64µs p(95)=119.76µs p(99.9)=507.15µs
     http_req_sending...............: avg=22.98µs min=5.68µs  med=15.65µs max=81.42ms  p(90)=21.24µs  p(95)=23.34µs  p(99.9)=568.49µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.17ms min=4.29ms  med=90.07ms max=303.69ms p(90)=124.66ms p(95)=134.83ms p(99.9)=175.16ms
     http_reqs......................: 64852   537.868053/s
     iteration_duration.............: avg=92.67ms min=16.66ms med=90.46ms max=328.53ms p(90)=125.03ms p(95)=135.19ms p(99.9)=176.24ms
     iterations.....................: 64752   537.038675/s
     success_rate...................: 100.00% ✓ 64752      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.b135f054)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 187860     ✗ 0    
     data_received..................: 5.5 GB  46 MB/s
     data_sent......................: 75 MB   625 kB/s
     http_req_blocked...............: avg=4.35µs  min=1.06µs  med=2.91µs  max=3.98ms   p(90)=4.37µs   p(95)=4.91µs   p(99.9)=51.19µs 
     http_req_connecting............: avg=1.23µs  min=0s      med=0s      max=3.94ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=95.44ms min=4.54ms  med=93.32ms max=325.71ms p(90)=126.85ms p(95)=137.05ms p(99.9)=179.98ms
       { expected_response:true }...: avg=95.44ms min=4.54ms  med=93.32ms max=325.71ms p(90)=126.85ms p(95)=137.05ms p(99.9)=179.98ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 62720
     http_req_receiving.............: avg=75.17µs min=26.31µs med=71.2µs  max=2.66ms   p(90)=102.09µs p(95)=114.78µs p(99.9)=495.19µs
     http_req_sending...............: avg=25.74µs min=5.03µs  med=15.01µs max=140.98ms p(90)=20.31µs  p(95)=22.26µs  p(99.9)=529.71µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=95.34ms min=4.47ms  med=93.23ms max=325.55ms p(90)=126.74ms p(95)=136.95ms p(99.9)=179.9ms 
     http_reqs......................: 62720   520.016602/s
     iteration_duration.............: avg=95.83ms min=23.03ms med=93.61ms max=337.65ms p(90)=127.12ms p(95)=137.34ms p(99.9)=181.4ms 
     iterations.....................: 62620   519.187494/s
     success_rate...................: 100.00% ✓ 62620      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 145344     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   483 kB/s
     http_req_blocked...............: avg=5.11µs   min=1.04µs  med=2.81µs   max=8.55ms   p(90)=4.12µs   p(95)=4.65µs   p(99.9)=121.89µs
     http_req_connecting............: avg=1.71µs   min=0s      med=0s       max=4.5ms    p(90)=0s       p(95)=0s       p(99.9)=53.57µs 
     http_req_duration..............: avg=123.39ms min=5.44ms  med=120.94ms max=312.22ms p(90)=161.74ms p(95)=174.05ms p(99.9)=229.87ms
       { expected_response:true }...: avg=123.39ms min=5.44ms  med=120.94ms max=312.22ms p(90)=161.74ms p(95)=174.05ms p(99.9)=229.87ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48548
     http_req_receiving.............: avg=76.82µs  min=29.74µs med=73.63µs  max=11.81ms  p(90)=101.84µs p(95)=114.15µs p(99.9)=461.12µs
     http_req_sending...............: avg=28.91µs  min=5.06µs  med=14.83µs  max=130.21ms p(90)=19.5µs   p(95)=21.13µs  p(99.9)=574.63µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.29ms min=5.32ms  med=120.85ms max=310.5ms  p(90)=161.64ms p(95)=173.93ms p(99.9)=229.5ms 
     http_reqs......................: 48548   402.222207/s
     iteration_duration.............: avg=123.88ms min=25.52ms med=121.25ms max=325.58ms p(90)=161.98ms p(95)=174.38ms p(99.9)=231.09ms
     iterations.....................: 48448   401.393703/s
     success_rate...................: 100.00% ✓ 48448      ✗ 0    
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

     checks.........................: 100.00% ✓ 107868     ✗ 0    
     data_received..................: 3.2 GB  26 MB/s
     data_sent......................: 43 MB   358 kB/s
     http_req_blocked...............: avg=5.68µs   min=1.06µs  med=3.04µs   max=4ms      p(90)=4.34µs   p(95)=4.88µs   p(99.9)=1ms     
     http_req_connecting............: avg=2.47µs   min=0s      med=0s       max=3.97ms   p(90)=0s       p(95)=0s       p(99.9)=977.41µs
     http_req_duration..............: avg=166.22ms min=5.29ms  med=148.15ms max=738.33ms p(90)=190.36ms p(95)=215.47ms p(99.9)=676.37ms
       { expected_response:true }...: avg=166.22ms min=5.29ms  med=148.15ms max=738.33ms p(90)=190.36ms p(95)=215.47ms p(99.9)=676.37ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 36056
     http_req_receiving.............: avg=90.8µs   min=31.13µs med=84.89µs  max=87.32ms  p(90)=113.98µs p(95)=125.1µs  p(99.9)=724.41µs
     http_req_sending...............: avg=31.45µs  min=5.28µs  med=16.35µs  max=106.83ms p(90)=20.34µs  p(95)=22.02µs  p(99.9)=520.48µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=166.1ms  min=5.16ms  med=148.03ms max=738.24ms p(90)=190.25ms p(95)=215.35ms p(99.9)=676.26ms
     http_reqs......................: 36056   298.209425/s
     iteration_duration.............: avg=166.93ms min=25.05ms med=148.47ms max=738.57ms p(90)=190.78ms p(95)=216.34ms p(99.9)=676.66ms
     iterations.....................: 35956   297.382352/s
     success_rate...................: 100.00% ✓ 35956      ✗ 0    
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

     checks.........................: 100.00% ✓ 98877      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   328 kB/s
     http_req_blocked...............: avg=5.98µs   min=1.13µs  med=3.11µs   max=3.53ms   p(90)=4.39µs   p(95)=4.94µs   p(99.9)=1.33ms  
     http_req_connecting............: avg=2.67µs   min=0s      med=0s       max=3.49ms   p(90)=0s       p(95)=0s       p(99.9)=1.31ms  
     http_req_duration..............: avg=181.32ms min=7.52ms  med=180.9ms  max=389.37ms p(90)=195.97ms p(95)=201.34ms p(99.9)=260.9ms 
       { expected_response:true }...: avg=181.32ms min=7.52ms  med=180.9ms  max=389.37ms p(90)=195.97ms p(95)=201.34ms p(99.9)=260.9ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 33059
     http_req_receiving.............: avg=87.67µs  min=29.57µs med=82.65µs  max=91.17ms  p(90)=111.19µs p(95)=121.03µs p(99.9)=498.41µs
     http_req_sending...............: avg=30.33µs  min=4.77µs  med=16.07µs  max=139.43ms p(90)=20.32µs  p(95)=22.14µs  p(99.9)=516.37µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=181.2ms  min=7.43ms  med=180.77ms max=388.78ms p(90)=195.87ms p(95)=201.23ms p(99.9)=260.78ms
     http_reqs......................: 33059   273.334539/s
     iteration_duration.............: avg=182.13ms min=24.52ms med=181.59ms max=405.13ms p(90)=196.23ms p(95)=201.63ms p(99.9)=265.34ms
     iterations.....................: 32959   272.507731/s
     success_rate...................: 100.00% ✓ 32959      ✗ 0    
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

