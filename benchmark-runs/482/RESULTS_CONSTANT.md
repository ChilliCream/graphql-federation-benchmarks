## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.6 | 5,514 | 5,527 | 5,512 | 0.1% | 380 MB | 70.5 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.15 | 5,441 | 5,477 | 5,420 | 0.4% | 374 MB | 70.5 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.15 | 5,373 | 5,376 | 5,361 | 0.1% | 386 MB | 73.5 KB |  |
| fusion-fed-net-11 | 16.7.6 | 5,345 | 5,372 | 5,329 | 0.3% | 376 MB | 72.1 KB |  |
| fusion-aot-11 | 16.7.6 | 5,307 | 5,332 | 5,275 | 0.4% | 116 MB | 22.3 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.15 | 5,213 | 5,238 | 5,210 | 0.2% | 134 MB | 26.4 KB |  |
| fusion-fed-aot-11 | 16.7.6 | 5,205 | 5,237 | 5,173 | 0.5% | 144 MB | 28.3 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.15 | 5,121 | 5,138 | 5,115 | 0.2% | 126 MB | 25.3 KB |  |
| feddi-gateway | 2026-11-03-0517 | 5,092 | 5,108 | 5,080 | 0.2% | 2,297 MB | 461.9 KB |  |
| hive-router | v0.3.13 | 2,790 | 2,817 | 2,767 | 0.7% | 90 MB | 32.9 KB |  |
| grafbase | 0.53.5 | 1,750 | 1,754 | 1,743 | 0.3% | 106 MB | 61.8 KB |  |
| cosmo | 0.372.0 | 1,475 | 1,476 | 1,464 | 0.4% | 168 MB | 116.4 KB |  |
| caliban | 3.2.1 | 1,429 | 1,446 | 1,420 | 0.8% | 4,517 MB | 3,237.0 KB |  |
| hive-gateway-router-runtime | 2.15.8 | 593 | 595 | 591 | 0.2% | 2,620 MB | 4,524.1 KB |  |
| apollo-router | v2.19.1 | 531 | 532 | 531 | 0.1% | 174 MB | 336.1 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 400 | 401 | 399 | 0.2% | 197 MB | 504.9 KB |  |
| hive-gateway | 2.15.8 | 301 | 302 | 300 | 0.2% | 3,190 MB | 10,851.6 KB |  |
| apollo-gateway | 2.14.4 | 271 | 272 | 268 | 0.7% | 2,166 MB | 8,184.9 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1986708     ✗ 0     
     data_received..................: 58 GB   483 MB/s
     data_sent......................: 796 MB  6.6 MB/s
     http_req_blocked...............: avg=2.48µs   min=711ns    med=1.97µs  max=6.11ms   p(90)=3.08µs  p(95)=3.68µs   p(99.9)=27.78µs
     http_req_connecting............: avg=136ns    min=0s       med=0s      max=3.96ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.85ms   min=768.28µs med=7.91ms  max=283.07ms p(90)=14.27ms p(95)=17.53ms  p(99.9)=30.19ms
       { expected_response:true }...: avg=8.85ms   min=768.28µs med=7.91ms  max=283.07ms p(90)=14.27ms p(95)=17.53ms  p(99.9)=30.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 662336
     http_req_receiving.............: avg=102.17µs min=23.88µs  med=45.41µs max=257.21ms p(90)=86.75µs p(95)=188.61µs p(99.9)=6.52ms 
     http_req_sending...............: avg=41.62µs  min=4.27µs   med=8.13µs  max=63.2ms   p(90)=13.58µs p(95)=99.49µs  p(99.9)=4.83ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.71ms   min=714.23µs med=7.8ms   max=124.65ms p(90)=14.03ms p(95)=17.24ms  p(99.9)=29.62ms
     http_reqs......................: 662336  5514.662705/s
     iteration_duration.............: avg=9.05ms   min=973.11µs med=8.09ms  max=294.78ms p(90)=14.48ms p(95)=17.75ms  p(99.9)=30.47ms
     iterations.....................: 662236  5513.830097/s
     success_rate...................: 100.00% ✓ 662236      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1960122     ✗ 0     
     data_received..................: 57 GB   476 MB/s
     data_sent......................: 786 MB  6.5 MB/s
     http_req_blocked...............: avg=4.58µs  min=831ns    med=2.36µs  max=77.9ms   p(90)=3.57µs  p(95)=4.24µs   p(99.9)=31.78µs
     http_req_connecting............: avg=1.69µs  min=0s       med=0s      max=50.92ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.97ms  min=757.87µs med=7.98ms  max=275.48ms p(90)=14.6ms  p(95)=17.99ms  p(99.9)=30.99ms
       { expected_response:true }...: avg=8.97ms  min=757.87µs med=7.98ms  max=275.48ms p(90)=14.6ms  p(95)=17.99ms  p(99.9)=30.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 653474
     http_req_receiving.............: avg=99.11µs min=25.53µs  med=47.69µs max=140.72ms p(90)=88.08µs p(95)=196.92µs p(99.9)=6.75ms 
     http_req_sending...............: avg=46.86µs min=4.48µs   med=8.67µs  max=76.73ms  p(90)=14.29µs p(95)=102.25µs p(99.9)=5.41ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.82ms  min=711.08µs med=7.87ms  max=220ms    p(90)=14.34ms p(95)=17.7ms   p(99.9)=30.26ms
     http_reqs......................: 653474  5441.030169/s
     iteration_duration.............: avg=9.17ms  min=1.17ms   med=8.17ms  max=315.04ms p(90)=14.81ms p(95)=18.22ms  p(99.9)=31.3ms 
     iterations.....................: 653374  5440.197537/s
     success_rate...................: 100.00% ✓ 653374      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1935726     ✗ 0     
     data_received..................: 57 GB   470 MB/s
     data_sent......................: 776 MB  6.5 MB/s
     http_req_blocked...............: avg=2.53µs  min=822ns    med=1.96µs  max=5.15ms   p(90)=3.08µs  p(95)=3.68µs   p(99.9)=27.6µs 
     http_req_connecting............: avg=152ns   min=0s       med=0s      max=3.81ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.09ms  min=803.85µs med=8.16ms  max=260.36ms p(90)=14.59ms p(95)=17.75ms  p(99.9)=30.54ms
       { expected_response:true }...: avg=9.09ms  min=803.85µs med=8.16ms  max=260.36ms p(90)=14.59ms p(95)=17.75ms  p(99.9)=30.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 645342
     http_req_receiving.............: avg=94.17µs min=24.75µs  med=46.59µs max=22.77ms  p(90)=87.25µs p(95)=189.87µs p(99.9)=6.29ms 
     http_req_sending...............: avg=41.64µs min=4.49µs   med=8.25µs  max=79.6ms   p(90)=13.88µs p(95)=99.68µs  p(99.9)=4.62ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.95ms  min=753.05µs med=8.06ms  max=260.06ms p(90)=14.37ms p(95)=17.46ms  p(99.9)=30.1ms 
     http_reqs......................: 645342  5373.008473/s
     iteration_duration.............: avg=9.28ms  min=1.02ms   med=8.35ms  max=280.92ms p(90)=14.8ms  p(95)=17.97ms  p(99.9)=30.82ms
     iterations.....................: 645242  5372.17589/s
     success_rate...................: 100.00% ✓ 645242      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1925817     ✗ 0     
     data_received..................: 56 GB   468 MB/s
     data_sent......................: 772 MB  6.4 MB/s
     http_req_blocked...............: avg=3.19µs  min=932ns    med=2.39µs  max=8.36ms   p(90)=3.57µs  p(95)=4.18µs   p(99.9)=30.99µs
     http_req_connecting............: avg=343ns   min=0s       med=0s      max=7.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.13ms  min=799.21µs med=8.15ms  max=276.71ms p(90)=14.79ms p(95)=18.13ms  p(99.9)=31ms   
       { expected_response:true }...: avg=9.13ms  min=799.21µs med=8.15ms  max=276.71ms p(90)=14.79ms p(95)=18.13ms  p(99.9)=31ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 642039
     http_req_receiving.............: avg=97.08µs min=26.38µs  med=48.41µs max=91.97ms  p(90)=87.71µs p(95)=195.38µs p(99.9)=6.18ms 
     http_req_sending...............: avg=44.38µs min=4.69µs   med=8.6µs   max=229.32ms p(90)=14.18µs p(95)=102.31µs p(99.9)=4.98ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.99ms  min=751.54µs med=8.04ms  max=273.26ms p(90)=14.55ms p(95)=17.85ms  p(99.9)=30.61ms
     http_reqs......................: 642039  5345.631738/s
     iteration_duration.............: avg=9.33ms  min=1.11ms   med=8.34ms  max=291.51ms p(90)=15ms    p(95)=18.36ms  p(99.9)=31.31ms
     iterations.....................: 641939  5344.799136/s
     success_rate...................: 100.00% ✓ 641939      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1912251     ✗ 0     
     data_received..................: 56 GB   464 MB/s
     data_sent......................: 766 MB  6.4 MB/s
     http_req_blocked...............: avg=2.59µs  min=781ns    med=2.04µs  max=6.37ms   p(90)=3.22µs  p(95)=3.82µs   p(99.9)=29.9µs 
     http_req_connecting............: avg=154ns   min=0s       med=0s      max=3.81ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.2ms   min=851.54µs med=8.28ms  max=284.21ms p(90)=14.78ms p(95)=17.97ms  p(99.9)=30.75ms
       { expected_response:true }...: avg=9.2ms   min=851.54µs med=8.28ms  max=284.21ms p(90)=14.78ms p(95)=17.97ms  p(99.9)=30.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 637517
     http_req_receiving.............: avg=91.08µs min=24.74µs  med=44.92µs max=70.02ms  p(90)=86.65µs p(95)=193.4µs  p(99.9)=5.79ms 
     http_req_sending...............: avg=41.64µs min=4.41µs   med=8.22µs  max=85.04ms  p(90)=14.13µs p(95)=103.78µs p(99.9)=4.68ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.07ms  min=802.5µs  med=8.17ms  max=274.38ms p(90)=14.56ms p(95)=17.71ms  p(99.9)=30.32ms
     http_reqs......................: 637517  5307.630215/s
     iteration_duration.............: avg=9.4ms   min=1.32ms   med=8.46ms  max=299.79ms p(90)=14.99ms p(95)=18.19ms  p(99.9)=31.05ms
     iterations.....................: 637417  5306.797668/s
     success_rate...................: 100.00% ✓ 637417      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1878201     ✗ 0     
     data_received..................: 55 GB   456 MB/s
     data_sent......................: 753 MB  6.3 MB/s
     http_req_blocked...............: avg=2.37µs  min=792ns    med=1.87µs  max=5.13ms   p(90)=2.95µs  p(95)=3.5µs    p(99.9)=26.89µs
     http_req_connecting............: avg=134ns   min=0s       med=0s      max=3.31ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.38ms  min=851.27µs med=8.51ms  max=269.85ms p(90)=14.88ms p(95)=17.85ms  p(99.9)=30.33ms
       { expected_response:true }...: avg=9.38ms  min=851.27µs med=8.51ms  max=269.85ms p(90)=14.88ms p(95)=17.85ms  p(99.9)=30.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 626167
     http_req_receiving.............: avg=90.71µs min=24.15µs  med=45.45µs max=226.11ms p(90)=86.83µs p(95)=193.39µs p(99.9)=5.58ms 
     http_req_sending...............: avg=40.78µs min=4.34µs   med=8.07µs  max=210.01ms p(90)=13.6µs  p(95)=99.99µs  p(99.9)=4.48ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.25ms  min=779.67µs med=8.4ms   max=260.06ms p(90)=14.66ms p(95)=17.61ms  p(99.9)=29.88ms
     http_reqs......................: 626167  5213.142405/s
     iteration_duration.............: avg=9.57ms  min=1.28ms   med=8.69ms  max=285.84ms p(90)=15.08ms p(95)=18.07ms  p(99.9)=30.59ms
     iterations.....................: 626067  5212.309856/s
     success_rate...................: 100.00% ✓ 626067      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1875483     ✗ 0     
     data_received..................: 55 GB   456 MB/s
     data_sent......................: 752 MB  6.3 MB/s
     http_req_blocked...............: avg=3.85µs  min=801ns    med=2.01µs  max=118.21ms p(90)=3.16µs  p(95)=3.76µs   p(99.9)=26.99µs
     http_req_connecting............: avg=1.43µs  min=0s       med=0s      max=118.16ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.39ms  min=859.51µs med=8.48ms  max=237.35ms p(90)=14.89ms p(95)=18.03ms  p(99.9)=30.71ms
       { expected_response:true }...: avg=9.39ms  min=859.51µs med=8.48ms  max=237.35ms p(90)=14.89ms p(95)=18.03ms  p(99.9)=30.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 625261
     http_req_receiving.............: avg=94.05µs min=25.81µs  med=46.87µs max=66.1ms   p(90)=88.57µs p(95)=197.03µs p(99.9)=6.14ms 
     http_req_sending...............: avg=43.84µs min=4.52µs   med=8.6µs   max=68.97ms  p(90)=14.47µs p(95)=103.14µs p(99.9)=5.03ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.25ms  min=811.33µs med=8.37ms  max=206.23ms p(90)=14.67ms p(95)=17.75ms  p(99.9)=30.22ms
     http_reqs......................: 625261  5205.665134/s
     iteration_duration.............: avg=9.58ms  min=1.35ms   med=8.67ms  max=287.54ms p(90)=15.1ms  p(95)=18.25ms  p(99.9)=31ms   
     iterations.....................: 625161  5204.832575/s
     success_rate...................: 100.00% ✓ 625161      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1845288     ✗ 0     
     data_received..................: 54 GB   448 MB/s
     data_sent......................: 739 MB  6.2 MB/s
     http_req_blocked...............: avg=2.97µs  min=962ns    med=2.36µs  max=7.75ms   p(90)=3.61µs  p(95)=4.22µs   p(99.9)=32.24µs
     http_req_connecting............: avg=138ns   min=0s       med=0s      max=3.36ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.54ms  min=869.21µs med=8.58ms  max=277.32ms p(90)=15.38ms p(95)=18.73ms  p(99.9)=31.54ms
       { expected_response:true }...: avg=9.54ms  min=869.21µs med=8.58ms  max=277.32ms p(90)=15.38ms p(95)=18.73ms  p(99.9)=31.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 615196
     http_req_receiving.............: avg=97.51µs min=25.17µs  med=47.58µs max=23.09ms  p(90)=90.76µs p(95)=208.86µs p(99.9)=6.22ms 
     http_req_sending...............: avg=43.06µs min=4.46µs   med=8.61µs  max=144.64ms p(90)=14.73µs p(95)=108.05µs p(99.9)=4.72ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.4ms   min=807.7µs  med=8.47ms  max=276.74ms p(90)=15.14ms p(95)=18.44ms  p(99.9)=31.16ms
     http_reqs......................: 615196  5121.6483/s
     iteration_duration.............: avg=9.74ms  min=1.34ms   med=8.77ms  max=287.33ms p(90)=15.59ms p(95)=18.95ms  p(99.9)=31.82ms
     iterations.....................: 615096  5120.815777/s
     success_rate...................: 100.00% ✓ 615096      ✗ 0     
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

     checks.........................: 100.00% ✓ 1834488     ✗ 0     
     data_received..................: 54 GB   445 MB/s
     data_sent......................: 735 MB  6.1 MB/s
     http_req_blocked...............: avg=2.73µs  min=792ns    med=1.97µs  max=10.38ms  p(90)=3.27µs  p(95)=3.95µs   p(99.9)=27.76µs
     http_req_connecting............: avg=277ns   min=0s       med=0s      max=10.32ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.6ms   min=712.22µs med=8.79ms  max=273.12ms p(90)=14.71ms p(95)=18.02ms  p(99.9)=29.38ms
       { expected_response:true }...: avg=9.6ms   min=712.22µs med=8.79ms  max=273.12ms p(90)=14.71ms p(95)=18.02ms  p(99.9)=29.38ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 611596
     http_req_receiving.............: avg=90.06µs min=24.07µs  med=45.29µs max=265.42ms p(90)=89.04µs p(95)=193.25µs p(99.9)=5.82ms 
     http_req_sending...............: avg=43.24µs min=4.37µs   med=8.34µs  max=177.18ms p(90)=14.96µs p(95)=105.42µs p(99.9)=4.78ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.47ms  min=648.46µs med=8.7ms   max=269.89ms p(90)=14.45ms p(95)=17.78ms  p(99.9)=28.9ms 
     http_reqs......................: 611596  5092.347433/s
     iteration_duration.............: avg=9.8ms   min=1.18ms   med=8.97ms  max=309.83ms p(90)=14.93ms p(95)=18.23ms  p(99.9)=29.64ms
     iterations.....................: 611496  5091.5148/s
     success_rate...................: 100.00% ✓ 611496      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 1005741     ✗ 0     
     data_received..................: 29 GB   244 MB/s
     data_sent......................: 403 MB  3.4 MB/s
     http_req_blocked...............: avg=2.57µs  min=842ns   med=2.12µs  max=2.62ms   p(90)=3.36µs  p(95)=3.98µs   p(99.9)=27.52µs
     http_req_connecting............: avg=165ns   min=0s      med=0s      max=2.59ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.69ms min=1.16ms  med=17.51ms max=281.85ms p(90)=25.11ms p(95)=27.14ms  p(99.9)=35.36ms
       { expected_response:true }...: avg=17.69ms min=1.16ms  med=17.51ms max=281.85ms p(90)=25.11ms p(95)=27.14ms  p(99.9)=35.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 335347
     http_req_receiving.............: avg=64.72µs min=25.14µs med=48.99µs max=125.79ms p(90)=83.01µs p(95)=110.11µs p(99.9)=1ms    
     http_req_sending...............: avg=27.57µs min=4.4µs   med=9.32µs  max=43.36ms  p(90)=15.06µs p(95)=71.98µs  p(99.9)=1.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.6ms  min=1.12ms  med=17.42ms max=281.44ms p(90)=25.01ms p(95)=27.05ms  p(99.9)=35.25ms
     http_reqs......................: 335347  2790.241465/s
     iteration_duration.............: avg=17.88ms min=2.25ms  med=17.69ms max=290.66ms p(90)=25.29ms p(95)=27.32ms  p(99.9)=35.59ms
     iterations.....................: 335247  2789.409419/s
     success_rate...................: 100.00% ✓ 335247      ✗ 0     
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

     checks.........................: 100.00% ✓ 631074      ✗ 0     
     data_received..................: 18 GB   153 MB/s
     data_sent......................: 253 MB  2.1 MB/s
     http_req_blocked...............: avg=3.97µs  min=1.05µs  med=3.09µs  max=3.71ms   p(90)=5.15µs   p(95)=6.19µs   p(99.9)=43.95µs
     http_req_connecting............: avg=433ns   min=0s      med=0s      max=3.67ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=28.26ms min=1.9ms   med=27.62ms max=298.66ms p(90)=36.52ms  p(95)=39.46ms  p(99.9)=54.17ms
       { expected_response:true }...: avg=28.26ms min=1.9ms   med=27.62ms max=298.66ms p(90)=36.52ms  p(95)=39.46ms  p(99.9)=54.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 210458
     http_req_receiving.............: avg=92.76µs min=30.23µs med=65.84µs max=182.35ms p(90)=124.65µs p(95)=191.22µs p(99.9)=1.45ms 
     http_req_sending...............: avg=35.31µs min=5.23µs  med=12.11µs max=165.84ms p(90)=23.46µs  p(95)=106.04µs p(99.9)=1.31ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=28.13ms min=1.79ms  med=27.5ms  max=271.3ms  p(90)=36.38ms  p(95)=39.32ms  p(99.9)=53.88ms
     http_reqs......................: 210458  1750.132561/s
     iteration_duration.............: avg=28.51ms min=7.66ms  med=27.85ms max=310.23ms p(90)=36.75ms  p(95)=39.69ms  p(99.9)=54.64ms
     iterations.....................: 210358  1749.300978/s
     success_rate...................: 100.00% ✓ 210358      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 532218      ✗ 0     
     data_received..................: 16 GB   129 MB/s
     data_sent......................: 213 MB  1.8 MB/s
     http_req_blocked...............: avg=3.43µs  min=1.08µs  med=2.6µs   max=4.29ms   p(90)=4.12µs  p(95)=4.78µs   p(99.9)=31.96µs 
     http_req_connecting............: avg=530ns   min=0s      med=0s      max=4.24ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.59ms min=2.04ms  med=32.69ms max=318.72ms p(90)=48.59ms p(95)=53.6ms   p(99.9)=76.32ms 
       { expected_response:true }...: avg=33.59ms min=2.04ms  med=32.69ms max=318.72ms p(90)=48.59ms p(95)=53.6ms   p(99.9)=76.32ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 177506
     http_req_receiving.............: avg=70.1µs  min=25.95µs med=59.38µs max=29.52ms  p(90)=94.45µs p(95)=109.99µs p(99.9)=754.53µs
     http_req_sending...............: avg=24.04µs min=4.8µs   med=11.18µs max=162.1ms  p(90)=17.18µs p(95)=21.13µs  p(99.9)=785.76µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.5ms  min=1.98ms  med=32.6ms  max=318.56ms p(90)=48.5ms  p(95)=53.51ms  p(99.9)=76.15ms 
     http_reqs......................: 177506  1475.892549/s
     iteration_duration.............: avg=33.81ms min=4.43ms  med=32.89ms max=327.13ms p(90)=48.79ms p(95)=53.8ms   p(99.9)=76.68ms 
     iterations.....................: 177406  1475.061088/s
     success_rate...................: 100.00% ✓ 177406      ✗ 0     
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

     checks.........................: 100.00% ✓ 515649      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.96µs  min=892ns   med=2.15µs  max=8.55ms   p(90)=3.62µs  p(95)=4.28µs   p(99.9)=28.34µs 
     http_req_connecting............: avg=1.46µs  min=0s      med=0s      max=8.52ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.68ms min=2.26ms  med=33.61ms max=276.25ms p(90)=49.56ms p(95)=54.91ms  p(99.9)=84.67ms 
       { expected_response:true }...: avg=34.68ms min=2.26ms  med=33.61ms max=276.25ms p(90)=49.56ms p(95)=54.91ms  p(99.9)=84.67ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 171983
     http_req_receiving.............: avg=66.02µs min=26.28µs med=55.44µs max=92.42ms  p(90)=88.18µs p(95)=102.79µs p(99.9)=758.04µs
     http_req_sending...............: avg=18.95µs min=4.68µs  med=10.34µs max=64.97ms  p(90)=16.07µs p(95)=19.42µs  p(99.9)=711.69µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.59ms min=2.2ms   med=33.53ms max=274.86ms p(90)=49.47ms p(95)=54.83ms  p(99.9)=84.45ms 
     http_reqs......................: 171983  1429.612807/s
     iteration_duration.............: avg=34.9ms  min=4.91ms  med=33.81ms max=306.87ms p(90)=49.75ms p(95)=55.12ms  p(99.9)=85.1ms  
     iterations.....................: 171883  1428.781555/s
     success_rate...................: 100.00% ✓ 171883      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 214287     ✗ 0    
     data_received..................: 6.3 GB  52 MB/s
     data_sent......................: 86 MB   713 kB/s
     http_req_blocked...............: avg=4.44µs  min=1.16µs  med=2.93µs  max=3.33ms   p(90)=4.34µs   p(95)=4.96µs   p(99.9)=41.57µs 
     http_req_connecting............: avg=1.25µs  min=0s      med=0s      max=3.31ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=83.67ms min=3.53ms  med=80.89ms max=315.85ms p(90)=102.89ms p(95)=114.52ms p(99.9)=212.22ms
       { expected_response:true }...: avg=83.67ms min=3.53ms  med=80.89ms max=315.85ms p(90)=102.89ms p(95)=114.52ms p(99.9)=212.22ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 71529
     http_req_receiving.............: avg=78.31µs min=28.8µs  med=67.87µs max=79.11ms  p(90)=100.42µs p(95)=112.62µs p(99.9)=580.69µs
     http_req_sending...............: avg=22.91µs min=5µs     med=13.37µs max=72.79ms  p(90)=18.96µs  p(95)=20.9µs   p(99.9)=578.22µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=83.57ms min=3.47ms  med=80.79ms max=315.41ms p(90)=102.78ms p(95)=114.41ms p(99.9)=212.01ms
     http_reqs......................: 71529   593.601893/s
     iteration_duration.............: avg=84.01ms min=25.73ms med=81.13ms max=324.3ms  p(90)=103.14ms p(95)=114.81ms p(99.9)=213.11ms
     iterations.....................: 71429   592.772017/s
     success_rate...................: 100.00% ✓ 71429      ✗ 0    
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

     checks.........................: 100.00% ✓ 192051     ✗ 0    
     data_received..................: 5.6 GB  47 MB/s
     data_sent......................: 77 MB   639 kB/s
     http_req_blocked...............: avg=4.47µs  min=1.08µs  med=2.83µs  max=3.36ms   p(90)=4.26µs   p(95)=4.82µs   p(99.9)=51.71µs 
     http_req_connecting............: avg=1.39µs  min=0s      med=0s      max=3.33ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.35ms min=4.38ms  med=91.32ms max=323.25ms p(90)=126.04ms p(95)=135.99ms p(99.9)=176.59ms
       { expected_response:true }...: avg=93.35ms min=4.38ms  med=91.32ms max=323.25ms p(90)=126.04ms p(95)=135.99ms p(99.9)=176.59ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64117
     http_req_receiving.............: avg=76.16µs min=26.76µs med=71.39µs max=61.44ms  p(90)=101.94µs p(95)=114.19µs p(99.9)=492.13µs
     http_req_sending...............: avg=22.65µs min=4.69µs  med=14.08µs max=87.19ms  p(90)=19.38µs  p(95)=21.19µs  p(99.9)=489.48µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.25ms min=4.3ms   med=91.23ms max=322.71ms p(90)=125.93ms p(95)=135.88ms p(99.9)=176.51ms
     http_reqs......................: 64117   531.762141/s
     iteration_duration.............: avg=93.74ms min=20.36ms med=91.6ms  max=334.12ms p(90)=126.29ms p(95)=136.23ms p(99.9)=177.73ms
     iterations.....................: 64017   530.932779/s
     success_rate...................: 100.00% ✓ 64017      ✗ 0    
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

     checks.........................: 100.00% ✓ 144843     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   481 kB/s
     http_req_blocked...............: avg=5.09µs  min=1.08µs  med=2.9µs    max=4.7ms    p(90)=4.21µs   p(95)=4.72µs   p(99.9)=161.82µs
     http_req_connecting............: avg=1.93µs  min=0s      med=0s       max=4.57ms   p(90)=0s       p(95)=0s       p(99.9)=74.29µs 
     http_req_duration..............: avg=123.8ms min=5.32ms  med=121.39ms max=317.18ms p(90)=162.33ms p(95)=175.04ms p(99.9)=223.82ms
       { expected_response:true }...: avg=123.8ms min=5.32ms  med=121.39ms max=317.18ms p(90)=162.33ms p(95)=175.04ms p(99.9)=223.82ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48381
     http_req_receiving.............: avg=80.14µs min=30.04µs med=74.73µs  max=103.62ms p(90)=103.74µs p(95)=115.85µs p(99.9)=510.63µs
     http_req_sending...............: avg=19.24µs min=5.2µs   med=14.59µs  max=57.56ms  p(90)=19.41µs  p(95)=21.04µs  p(99.9)=577.74µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123.7ms min=5.24ms  med=121.29ms max=316.21ms p(90)=162.22ms p(95)=174.95ms p(99.9)=223.54ms
     http_reqs......................: 48381   400.91338/s
     iteration_duration.............: avg=124.3ms min=29.87ms med=121.69ms max=328.67ms p(90)=162.61ms p(95)=175.31ms p(99.9)=226.14ms
     iterations.....................: 48281   400.084721/s
     success_rate...................: 100.00% ✓ 48281      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 109026     ✗ 0    
     data_received..................: 3.2 GB  26 MB/s
     data_sent......................: 44 MB   362 kB/s
     http_req_blocked...............: avg=6.59µs   min=1.3µs   med=3.64µs   max=3.88ms   p(90)=5.14µs   p(95)=5.76µs   p(99.9)=1ms     
     http_req_connecting............: avg=2.68µs   min=0s      med=0s       max=3.84ms   p(90)=0s       p(95)=0s       p(99.9)=979.81µs
     http_req_duration..............: avg=164.48ms min=5.4ms   med=146.91ms max=749.39ms p(90)=187.01ms p(95)=209.16ms p(99.9)=687.57ms
       { expected_response:true }...: avg=164.48ms min=5.4ms   med=146.91ms max=749.39ms p(90)=187.01ms p(95)=209.16ms p(99.9)=687.57ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 36442
     http_req_receiving.............: avg=93.3µs   min=35.91µs med=88.84µs  max=15.7ms   p(90)=118.02µs p(95)=129.19µs p(99.9)=721.03µs
     http_req_sending...............: avg=21.49µs  min=6.27µs  med=17.8µs   max=12.62ms  p(90)=22.34µs  p(95)=24.2µs   p(99.9)=583.35µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=164.37ms min=5.3ms   med=146.79ms max=749.28ms p(90)=186.9ms  p(95)=209.06ms p(99.9)=687.46ms
     http_reqs......................: 36442   301.359555/s
     iteration_duration.............: avg=165.18ms min=83.01ms med=147.22ms max=749.66ms p(90)=187.34ms p(95)=209.7ms  p(99.9)=688.08ms
     iterations.....................: 36342   300.532598/s
     success_rate...................: 100.00% ✓ 36342      ✗ 0    
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

     checks.........................: 100.00% ✓ 98334      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   326 kB/s
     http_req_blocked...............: avg=6.12µs   min=1.06µs  med=2.95µs   max=3.69ms   p(90)=4.2µs    p(95)=4.72µs   p(99.9)=1.74ms  
     http_req_connecting............: avg=3.01µs   min=0s      med=0s       max=3.64ms   p(90)=0s       p(95)=0s       p(99.9)=1.72ms  
     http_req_duration..............: avg=182.33ms min=7.59ms  med=187.46ms max=385.82ms p(90)=196.87ms p(95)=201.33ms p(99.9)=266.54ms
       { expected_response:true }...: avg=182.33ms min=7.59ms  med=187.46ms max=385.82ms p(90)=196.87ms p(95)=201.33ms p(99.9)=266.54ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32878
     http_req_receiving.............: avg=84.85µs  min=30.54µs med=81.26µs  max=51.76ms  p(90)=110.2µs  p(95)=121.03µs p(99.9)=466.3µs 
     http_req_sending...............: avg=33.5µs   min=5.09µs  med=15.74µs  max=100.78ms p(90)=19.76µs  p(95)=21.5µs   p(99.9)=419.13µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.21ms min=7.51ms  med=187.36ms max=385.52ms p(90)=196.76ms p(95)=201.22ms p(99.9)=266.4ms 
     http_reqs......................: 32878   271.772162/s
     iteration_duration.............: avg=183.15ms min=42.5ms  med=187.72ms max=394.82ms p(90)=197.13ms p(95)=201.63ms p(99.9)=273.84ms
     iterations.....................: 32778   270.945554/s
     success_rate...................: 100.00% ✓ 32778      ✗ 0    
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

