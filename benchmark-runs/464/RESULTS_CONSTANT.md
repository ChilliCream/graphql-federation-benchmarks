## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 5,048 | 5,088 | 4,981 | 0.8% | 368 MB | 74.6 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,984 | 4,996 | 4,953 | 0.3% | 383 MB | 78.7 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,841 | 4,866 | 4,836 | 0.3% | 396 MB | 83.7 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,816 | 4,828 | 4,795 | 0.2% | 368 MB | 78.1 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,676 | 4,687 | 4,670 | 0.2% | 123 MB | 27.0 KB |  |
| fusion-aot-11 | 16.7.3 | 4,665 | 4,672 | 4,645 | 0.2% | 126 MB | 27.7 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,590 | 4,621 | 4,570 | 0.4% | 133 MB | 29.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,465 | 4,480 | 4,440 | 0.4% | 127 MB | 29.2 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,270 | 4,382 | 4,119 | 2.4% | 2,307 MB | 553.2 KB |  |
| hive-router | v0.3.6 | 3,009 | 3,046 | 3,000 | 0.6% | 92 MB | 31.2 KB |  |
| grafbase | 0.53.5 | 1,892 | 1,895 | 1,887 | 0.2% | 109 MB | 59.2 KB |  |
| cosmo | 0.363.0 | 1,500 | 1,502 | 1,499 | 0.1% | 164 MB | 112.0 KB |  |
| caliban | 3.2.0 | 1,387 | 1,387 | 1,382 | 0.2% | 4,093 MB | 3,021.8 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 530 | 530 | 527 | 0.3% | 2,737 MB | 5,287.5 KB |  |
| apollo-router | v2.19.0 | 528 | 529 | 528 | 0.1% | 177 MB | 342.7 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 432 | 432 | 432 | 0.0% | 203 MB | 480.4 KB |  |
| hive-gateway | 2.15.3 | 275 | 276 | 274 | 0.3% | 3,692 MB | 13,747.8 KB |  |
| apollo-gateway | 2.14.4 | 270 | 271 | 269 | 0.3% | 2,137 MB | 8,106.0 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1818858     ✗ 0     
     data_received..................: 53 GB   442 MB/s
     data_sent......................: 729 MB  6.1 MB/s
     http_req_blocked...............: avg=3.05µs  min=781ns    med=1.87µs  max=171.44ms p(90)=3µs     p(95)=3.63µs   p(99.9)=27.54µs
     http_req_connecting............: avg=733ns   min=0s       med=0s      max=171.29ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.69ms  min=822.45µs med=8.89ms  max=258.79ms p(90)=14.83ms p(95)=17.55ms  p(99.9)=29.51ms
       { expected_response:true }...: avg=9.69ms  min=822.45µs med=8.89ms  max=258.79ms p(90)=14.83ms p(95)=17.55ms  p(99.9)=29.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 606386
     http_req_receiving.............: avg=92.13µs min=23.75µs  med=45.15µs max=25.05ms  p(90)=89.69µs p(95)=194.1µs  p(99.9)=6.06ms 
     http_req_sending...............: avg=41.04µs min=4.3µs    med=8µs     max=185.86ms p(90)=14.63µs p(95)=100.49µs p(99.9)=4.38ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.56ms  min=746.97µs med=8.78ms  max=255.23ms p(90)=14.63ms p(95)=17.29ms  p(99.9)=29.09ms
     http_reqs......................: 606386  5048.719287/s
     iteration_duration.............: avg=9.88ms  min=1.16ms   med=9.07ms  max=284.8ms  p(90)=15.03ms p(95)=17.76ms  p(99.9)=29.79ms
     iterations.....................: 606286  5047.886695/s
     success_rate...................: 100.00% ✓ 606286      ✗ 0     
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

     checks.........................: 100.00% ✓ 1795779     ✗ 0     
     data_received..................: 52 GB   436 MB/s
     data_sent......................: 720 MB  6.0 MB/s
     http_req_blocked...............: avg=2.38µs  min=781ns    med=1.94µs  max=4.45ms   p(90)=3.04µs  p(95)=3.63µs   p(99.9)=24.75µs
     http_req_connecting............: avg=94ns    min=0s       med=0s      max=3.28ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.81ms  min=827.94µs med=9.03ms  max=280.35ms p(90)=14.98ms p(95)=17.66ms  p(99.9)=29.55ms
       { expected_response:true }...: avg=9.81ms  min=827.94µs med=9.03ms  max=280.35ms p(90)=14.98ms p(95)=17.66ms  p(99.9)=29.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 598693
     http_req_receiving.............: avg=91.65µs min=25.67µs  med=46.47µs max=152.73ms p(90)=88.74µs p(95)=191.83µs p(99.9)=5.67ms 
     http_req_sending...............: avg=40.93µs min=4.57µs   med=8.14µs  max=165.58ms p(90)=14.3µs  p(95)=100.59µs p(99.9)=4.3ms  
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.68ms  min=758.53µs med=8.92ms  max=280.25ms p(90)=14.77ms p(95)=17.41ms  p(99.9)=29.14ms
     http_reqs......................: 598693  4984.347184/s
     iteration_duration.............: avg=10.01ms min=1.34ms   med=9.22ms  max=293.64ms p(90)=15.18ms p(95)=17.87ms  p(99.9)=29.79ms
     iterations.....................: 598593  4983.514646/s
     success_rate...................: 100.00% ✓ 598593      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1744716     ✗ 0     
     data_received..................: 51 GB   424 MB/s
     data_sent......................: 699 MB  5.8 MB/s
     http_req_blocked...............: avg=2.54µs  min=792ns    med=1.93µs  max=10.6ms   p(90)=3.11µs  p(95)=3.81µs   p(99.9)=26.8µs 
     http_req_connecting............: avg=154ns   min=0s       med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.1ms  min=1ms      med=9.36ms  max=265.87ms p(90)=15.27ms p(95)=17.85ms  p(99.9)=30.51ms
       { expected_response:true }...: avg=10.1ms  min=1ms      med=9.36ms  max=265.87ms p(90)=15.27ms p(95)=17.85ms  p(99.9)=30.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 581672
     http_req_receiving.............: avg=97.05µs min=24.56µs  med=46.65µs max=45.91ms  p(90)=92.29µs p(95)=191.91µs p(99.9)=6.78ms 
     http_req_sending...............: avg=41.77µs min=4.33µs   med=8.08µs  max=191.05ms p(90)=14.91µs p(95)=98.79µs  p(99.9)=4.46ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.97ms  min=921.69µs med=9.25ms  max=265.21ms p(90)=15.07ms p(95)=17.59ms  p(99.9)=29.78ms
     http_reqs......................: 581672  4841.946257/s
     iteration_duration.............: avg=10.3ms  min=1.16ms   med=9.55ms  max=299.05ms p(90)=15.48ms p(95)=18.07ms  p(99.9)=30.79ms
     iterations.....................: 581572  4841.113838/s
     success_rate...................: 100.00% ✓ 581572      ✗ 0     
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

     checks.........................: 100.00% ✓ 1735458     ✗ 0     
     data_received..................: 51 GB   421 MB/s
     data_sent......................: 695 MB  5.8 MB/s
     http_req_blocked...............: avg=3.44µs   min=962ns    med=2.52µs  max=9.02ms   p(90)=3.91µs   p(95)=4.72µs   p(99.9)=35.04µs
     http_req_connecting............: avg=420ns    min=0s       med=0s      max=8.89ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.14ms  min=971.26µs med=9.23ms  max=269.32ms p(90)=15.71ms  p(95)=18.71ms  p(99.9)=31.67ms
       { expected_response:true }...: avg=10.14ms  min=971.26µs med=9.23ms  max=269.32ms p(90)=15.71ms  p(95)=18.71ms  p(99.9)=31.67ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 578586
     http_req_receiving.............: avg=107.13µs min=25.75µs  med=49.54µs max=154.17ms p(90)=100.12µs p(95)=208.02µs p(99.9)=7.5ms  
     http_req_sending...............: avg=47.24µs  min=4.61µs   med=9.28µs  max=187.87ms p(90)=16.97µs  p(95)=107.06µs p(99.9)=5.37ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.99ms   min=922.59µs med=9.11ms  max=268.29ms p(90)=15.47ms  p(95)=18.42ms  p(99.9)=31.03ms
     http_reqs......................: 578586  4816.465295/s
     iteration_duration.............: avg=10.35ms  min=1.36ms   med=9.44ms  max=304.86ms p(90)=15.92ms  p(95)=18.94ms  p(99.9)=31.97ms
     iterations.....................: 578486  4815.63284/s
     success_rate...................: 100.00% ✓ 578486      ✗ 0     
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

     checks.........................: 100.00% ✓ 1685010     ✗ 0     
     data_received..................: 49 GB   409 MB/s
     data_sent......................: 675 MB  5.6 MB/s
     http_req_blocked...............: avg=3.01µs  min=882ns    med=2.31µs  max=6.82ms   p(90)=3.57µs  p(95)=4.2µs    p(99.9)=29.85µs
     http_req_connecting............: avg=250ns   min=0s       med=0s      max=4.9ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.47ms min=916.02µs med=9.75ms  max=271.39ms p(90)=15.67ms p(95)=18.4ms   p(99.9)=30.35ms
       { expected_response:true }...: avg=10.47ms min=916.02µs med=9.75ms  max=271.39ms p(90)=15.67ms p(95)=18.4ms   p(99.9)=30.35ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 561770
     http_req_receiving.............: avg=96.3µs  min=24.48µs  med=47.58µs max=146.02ms p(90)=94.23µs p(95)=216.55µs p(99.9)=5.59ms 
     http_req_sending...............: avg=41.79µs min=4.49µs   med=8.65µs  max=164.51ms p(90)=15.19µs p(95)=109.43µs p(99.9)=4.18ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.33ms min=863.63µs med=9.63ms  max=263.66ms p(90)=15.45ms p(95)=18.15ms  p(99.9)=29.91ms
     http_reqs......................: 561770  4676.876288/s
     iteration_duration.............: avg=10.67ms min=1.2ms    med=9.93ms  max=284.75ms p(90)=15.87ms p(95)=18.62ms  p(99.9)=30.61ms
     iterations.....................: 561670  4676.043763/s
     success_rate...................: 100.00% ✓ 561670      ✗ 0     
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

     checks.........................: 100.00% ✓ 1681095     ✗ 0     
     data_received..................: 49 GB   408 MB/s
     data_sent......................: 674 MB  5.6 MB/s
     http_req_blocked...............: avg=2.98µs   min=1µs      med=2.42µs  max=5.04ms   p(90)=3.74µs  p(95)=4.42µs   p(99.9)=32.37µs
     http_req_connecting............: avg=161ns    min=0s       med=0s      max=4.04ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.49ms  min=926.32µs med=9.73ms  max=280.5ms  p(90)=15.8ms  p(95)=18.67ms  p(99.9)=30.52ms
       { expected_response:true }...: avg=10.49ms  min=926.32µs med=9.73ms  max=280.5ms  p(90)=15.8ms  p(95)=18.67ms  p(99.9)=30.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 560465
     http_req_receiving.............: avg=100.18µs min=24.59µs  med=47.74µs max=114.03ms p(90)=96.78µs p(95)=219.68µs p(99.9)=6.56ms 
     http_req_sending...............: avg=42.75µs  min=4.73µs   med=8.91µs  max=102.41ms p(90)=15.75µs p(95)=111.6µs  p(99.9)=4.4ms  
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.35ms  min=866.46µs med=9.62ms  max=280.22ms p(90)=15.58ms p(95)=18.39ms  p(99.9)=30.06ms
     http_reqs......................: 560465  4665.832671/s
     iteration_duration.............: avg=10.69ms  min=1.32ms   med=9.92ms  max=289.59ms p(90)=16ms    p(95)=18.9ms   p(99.9)=30.8ms 
     iterations.....................: 560365  4665.000178/s
     success_rate...................: 100.00% ✓ 560365      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1654188     ✗ 0     
     data_received..................: 48 GB   402 MB/s
     data_sent......................: 663 MB  5.5 MB/s
     http_req_blocked...............: avg=3.41µs  min=1µs      med=2.49µs  max=9.45ms   p(90)=3.91µs  p(95)=4.68µs   p(99.9)=33.35µs
     http_req_connecting............: avg=418ns   min=0s       med=0s      max=8.84ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.66ms min=1.06ms   med=9.91ms  max=270.62ms p(90)=15.97ms p(95)=18.87ms  p(99.9)=31.49ms
       { expected_response:true }...: avg=10.66ms min=1.06ms   med=9.91ms  max=270.62ms p(90)=15.97ms p(95)=18.87ms  p(99.9)=31.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 551496
     http_req_receiving.............: avg=105.6µs min=26µs     med=49.03µs max=40.05ms  p(90)=102.3µs p(95)=217.25µs p(99.9)=6.89ms 
     http_req_sending...............: avg=46.46µs min=4.67µs   med=9.08µs  max=171.44ms p(90)=16.87µs p(95)=110.83µs p(99.9)=5ms    
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.51ms min=986.62µs med=9.79ms  max=268.92ms p(90)=15.73ms p(95)=18.57ms  p(99.9)=30.99ms
     http_reqs......................: 551496  4590.332547/s
     iteration_duration.............: avg=10.87ms min=1.61ms   med=10.11ms max=293.34ms p(90)=16.18ms p(95)=19.09ms  p(99.9)=31.83ms
     iterations.....................: 551396  4589.500205/s
     success_rate...................: 100.00% ✓ 551396      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1609080     ✗ 0     
     data_received..................: 47 GB   391 MB/s
     data_sent......................: 645 MB  5.4 MB/s
     http_req_blocked...............: avg=2.56µs  min=832ns   med=1.97µs  max=5.44ms   p(90)=3.12µs  p(95)=3.77µs   p(99.9)=26.51µs
     http_req_connecting............: avg=161ns   min=0s      med=0s      max=3.48ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.97ms min=1.06ms  med=10.41ms max=295.22ms p(90)=15.84ms p(95)=18.25ms  p(99.9)=30.33ms
       { expected_response:true }...: avg=10.97ms min=1.06ms  med=10.41ms max=295.22ms p(90)=15.84ms p(95)=18.25ms  p(99.9)=30.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 536460
     http_req_receiving.............: avg=97.02µs min=26.34µs med=48.13µs max=122.43ms p(90)=96.77µs p(95)=207.67µs p(99.9)=5.94ms 
     http_req_sending...............: avg=40.53µs min=4.43µs  med=8.28µs  max=110.78ms p(90)=15.25µs p(95)=103.51µs p(99.9)=4.01ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.84ms min=1.01ms  med=10.3ms  max=294.71ms p(90)=15.64ms p(95)=18ms     p(99.9)=29.94ms
     http_reqs......................: 536460  4465.153074/s
     iteration_duration.............: avg=11.17ms min=1.55ms  med=10.6ms  max=305.92ms p(90)=16.04ms p(95)=18.46ms  p(99.9)=30.58ms
     iterations.....................: 536360  4464.320738/s
     success_rate...................: 100.00% ✓ 536360      ✗ 0     
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

     checks.........................: 100.00% ✓ 1538589     ✗ 0     
     data_received..................: 45 GB   373 MB/s
     data_sent......................: 617 MB  5.1 MB/s
     http_req_blocked...............: avg=2.56µs  min=832ns    med=2µs     max=4.14ms   p(90)=3.19µs  p(95)=3.8µs    p(99.9)=30.66µs
     http_req_connecting............: avg=173ns   min=0s       med=0s      max=3.81ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.49ms min=751.97µs med=11.22ms max=291.43ms p(90)=16.96ms p(95)=19.06ms  p(99.9)=29.43ms
       { expected_response:true }...: avg=11.49ms min=751.97µs med=11.22ms max=291.43ms p(90)=16.96ms p(95)=19.06ms  p(99.9)=29.43ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 512963
     http_req_receiving.............: avg=83.6µs  min=24.72µs  med=46.59µs max=82.88ms  p(90)=92.76µs p(95)=206.66µs p(99.9)=4.22ms 
     http_req_sending...............: avg=38.77µs min=4.29µs   med=8.53µs  max=151.72ms p(90)=15.1µs  p(95)=111.4µs  p(99.9)=3.19ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.37ms min=701.14µs med=11.11ms max=289.68ms p(90)=16.8ms  p(95)=18.88ms  p(99.9)=29.07ms
     http_reqs......................: 512963  4270.807019/s
     iteration_duration.............: avg=11.68ms min=1.24ms   med=11.4ms  max=327.43ms p(90)=17.15ms p(95)=19.27ms  p(99.9)=29.64ms
     iterations.....................: 512863  4269.974443/s
     success_rate...................: 100.00% ✓ 512863      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1084662     ✗ 0     
     data_received..................: 32 GB   263 MB/s
     data_sent......................: 435 MB  3.6 MB/s
     http_req_blocked...............: avg=3.42µs  min=852ns   med=2.31µs  max=8ms      p(90)=3.83µs  p(95)=4.61µs   p(99.9)=32.95µs
     http_req_connecting............: avg=715ns   min=0s      med=0s      max=7.94ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.38ms min=1.36ms  med=16.38ms max=266.78ms p(90)=21.91ms p(95)=23.42ms  p(99.9)=30.79ms
       { expected_response:true }...: avg=16.38ms min=1.36ms  med=16.38ms max=266.78ms p(90)=21.91ms p(95)=23.42ms  p(99.9)=30.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 361654
     http_req_receiving.............: avg=75.68µs min=23.79µs med=51.61µs max=189.93ms p(90)=95.99µs p(95)=183.93µs p(99.9)=1.31ms 
     http_req_sending...............: avg=35.72µs min=4.63µs  med=10.04µs max=158.03ms p(90)=18.68µs p(95)=111.64µs p(99.9)=1.37ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.27ms min=1.3ms   med=16.27ms max=244.25ms p(90)=21.8ms  p(95)=23.3ms   p(99.9)=30.61ms
     http_reqs......................: 361654  3009.275538/s
     iteration_duration.............: avg=16.58ms min=3.39ms  med=16.58ms max=281.88ms p(90)=22.11ms p(95)=23.62ms  p(99.9)=31.05ms
     iterations.....................: 361554  3008.443451/s
     success_rate...................: 100.00% ✓ 361554      ✗ 0     
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

     checks.........................: 100.00% ✓ 682449      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 274 MB  2.3 MB/s
     http_req_blocked...............: avg=3.12µs  min=841ns   med=2.35µs  max=2.5ms    p(90)=4.53µs   p(95)=5.58µs   p(99.9)=40.57µs
     http_req_connecting............: avg=246ns   min=0s      med=0s      max=2.47ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.13ms min=1.87ms  med=25.58ms max=297.13ms p(90)=33.88ms  p(95)=36.62ms  p(99.9)=50.29ms
       { expected_response:true }...: avg=26.13ms min=1.87ms  med=25.58ms max=297.13ms p(90)=33.88ms  p(95)=36.62ms  p(99.9)=50.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 227583
     http_req_receiving.............: avg=84.7µs  min=27.81µs med=57.08µs max=255.85ms p(90)=119.03µs p(95)=181.98µs p(99.9)=1.45ms 
     http_req_sending...............: avg=33.15µs min=4.73µs  med=10.04µs max=176.54ms p(90)=22.54µs  p(95)=100µs    p(99.9)=1.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.01ms min=1.82ms  med=25.47ms max=296.48ms p(90)=33.75ms  p(95)=36.49ms  p(99.9)=49.97ms
     http_reqs......................: 227583  1892.424868/s
     iteration_duration.............: avg=26.36ms min=3.79ms  med=25.79ms max=309.55ms p(90)=34.1ms   p(95)=36.83ms  p(99.9)=50.54ms
     iterations.....................: 227483  1891.593336/s
     success_rate...................: 100.00% ✓ 227483      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 541131      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 217 MB  1.8 MB/s
     http_req_blocked...............: avg=2.92µs  min=911ns   med=2.13µs  max=3.65ms   p(90)=3.58µs  p(95)=4.25µs   p(99.9)=29.6µs  
     http_req_connecting............: avg=481ns   min=0s      med=0s      max=3.61ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.03ms min=2.01ms  med=32.16ms max=300.03ms p(90)=47.5ms  p(95)=52.35ms  p(99.9)=75.92ms 
       { expected_response:true }...: avg=33.03ms min=2.01ms  med=32.16ms max=300.03ms p(90)=47.5ms  p(95)=52.35ms  p(99.9)=75.92ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 180477
     http_req_receiving.............: avg=69.17µs min=27.11µs med=58.86µs max=10.66ms  p(90)=95.43µs p(95)=110.82µs p(99.9)=693.1µs 
     http_req_sending...............: avg=20.72µs min=4.55µs  med=9.96µs  max=103.65ms p(90)=16.48µs p(95)=20.27µs  p(99.9)=764.75µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.94ms min=1.95ms  med=32.08ms max=299.58ms p(90)=47.41ms p(95)=52.26ms  p(99.9)=75.82ms 
     http_reqs......................: 180477  1500.609808/s
     iteration_duration.............: avg=33.25ms min=4.03ms  med=32.36ms max=309.13ms p(90)=47.7ms  p(95)=52.54ms  p(99.9)=76.67ms 
     iterations.....................: 180377  1499.778339/s
     success_rate...................: 100.00% ✓ 180377      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 500442      ✗ 0     
     data_received..................: 15 GB   121 MB/s
     data_sent......................: 201 MB  1.7 MB/s
     http_req_blocked...............: avg=2.93µs  min=861ns   med=2.09µs  max=4.21ms   p(90)=3.47µs  p(95)=4.08µs   p(99.9)=28.46µs 
     http_req_connecting............: avg=547ns   min=0s      med=0s      max=4.16ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.74ms min=2.02ms  med=34.7ms  max=317.95ms p(90)=51.06ms p(95)=56.39ms  p(99.9)=85.3ms  
       { expected_response:true }...: avg=35.74ms min=2.02ms  med=34.7ms  max=317.95ms p(90)=51.06ms p(95)=56.39ms  p(99.9)=85.3ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 166914
     http_req_receiving.............: avg=71.99µs min=27.66µs med=56.06µs max=201.56ms p(90)=86.98µs p(95)=100.89µs p(99.9)=711.32µs
     http_req_sending...............: avg=22.05µs min=4.56µs  med=9.84µs  max=267ms    p(90)=14.98µs p(95)=18.09µs  p(99.9)=669.43µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.65ms min=1.95ms  med=34.62ms max=287.14ms p(90)=50.97ms p(95)=56.3ms   p(99.9)=84.78ms 
     http_reqs......................: 166914  1387.851103/s
     iteration_duration.............: avg=35.96ms min=5.53ms  med=34.9ms  max=318.23ms p(90)=51.26ms p(95)=56.59ms  p(99.9)=86.04ms 
     iterations.....................: 166814  1387.019626/s
     success_rate...................: 100.00% ✓ 166814      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 191664     ✗ 0    
     data_received..................: 5.6 GB  47 MB/s
     data_sent......................: 77 MB   637 kB/s
     http_req_blocked...............: avg=4.74µs  min=1.15µs  med=2.98µs  max=3.7ms    p(90)=4.4µs    p(95)=5.02µs   p(99.9)=48.26µs 
     http_req_connecting............: avg=1.48µs  min=0s      med=0s      max=3.66ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.56ms min=3.94ms  med=90.93ms max=318.5ms  p(90)=112.93ms p(95)=123.78ms p(99.9)=219.62ms
       { expected_response:true }...: avg=93.56ms min=3.94ms  med=90.93ms max=318.5ms  p(90)=112.93ms p(95)=123.78ms p(99.9)=219.62ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63988
     http_req_receiving.............: avg=76.92µs min=27.86µs med=69.46µs max=24.19ms  p(90)=101.5µs  p(95)=113.91µs p(99.9)=592.68µs
     http_req_sending...............: avg=21.25µs min=5.34µs  med=13.7µs  max=68.94ms  p(90)=19.44µs  p(95)=21.51µs  p(99.9)=526.86µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.46ms min=3.82ms  med=90.84ms max=318.15ms p(90)=112.83ms p(95)=123.67ms p(99.9)=219.55ms
     http_reqs......................: 63988   530.695809/s
     iteration_duration.............: avg=93.93ms min=23.39ms med=91.16ms max=334.62ms p(90)=113.18ms p(95)=124.02ms p(99.9)=221.01ms
     iterations.....................: 63888   529.866441/s
     success_rate...................: 100.00% ✓ 63888      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 190950     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   635 kB/s
     http_req_blocked...............: avg=4.63µs  min=1.02µs  med=2.9µs   max=4.07ms   p(90)=4.39µs   p(95)=4.94µs   p(99.9)=48.82µs 
     http_req_connecting............: avg=1.52µs  min=0s      med=0s      max=4.03ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.9ms  min=4.44ms  med=92.03ms max=326.46ms p(90)=126.79ms p(95)=136.79ms p(99.9)=180.15ms
       { expected_response:true }...: avg=93.9ms  min=4.44ms  med=92.03ms max=326.46ms p(90)=126.79ms p(95)=136.79ms p(99.9)=180.15ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63750
     http_req_receiving.............: avg=79.39µs min=27.15µs med=70.81µs max=112.98ms p(90)=101.89µs p(95)=114.41µs p(99.9)=510.21µs
     http_req_sending...............: avg=23.21µs min=4.91µs  med=13.78µs max=101.27ms p(90)=19.28µs  p(95)=21.11µs  p(99.9)=511.54µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.79ms min=4.36ms  med=91.94ms max=313.04ms p(90)=126.7ms  p(95)=136.69ms p(99.9)=179.28ms
     http_reqs......................: 63750   528.733852/s
     iteration_duration.............: avg=94.28ms min=23.92ms med=92.33ms max=339.51ms p(90)=127.06ms p(95)=137.06ms p(99.9)=181.33ms
     iterations.....................: 63650   527.904466/s
     success_rate...................: 100.00% ✓ 63650      ✗ 0    
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

     checks.........................: 100.00% ✓ 156276     ✗ 0    
     data_received..................: 4.6 GB  38 MB/s
     data_sent......................: 63 MB   519 kB/s
     http_req_blocked...............: avg=4.9µs    min=1.08µs  med=3.04µs   max=4ms      p(90)=4.44µs   p(95)=4.98µs   p(99.9)=84.24µs 
     http_req_connecting............: avg=1.72µs   min=0s      med=0s       max=3.96ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=114.76ms min=5.24ms  med=112.48ms max=329.88ms p(90)=149.85ms p(95)=161.93ms p(99.9)=208.91ms
       { expected_response:true }...: avg=114.76ms min=5.24ms  med=112.48ms max=329.88ms p(90)=149.85ms p(95)=161.93ms p(99.9)=208.91ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 52192
     http_req_receiving.............: avg=79.03µs  min=25.98µs med=74.03µs  max=114.19ms p(90)=103.85µs p(95)=115.42µs p(99.9)=410.74µs
     http_req_sending...............: avg=21.43µs  min=5.07µs  med=15.06µs  max=67.55ms  p(90)=20µs     p(95)=21.81µs  p(99.9)=524.03µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=114.65ms min=5.13ms  med=112.38ms max=329.26ms p(90)=149.75ms p(95)=161.84ms p(99.9)=208.32ms
     http_reqs......................: 52192   432.491808/s
     iteration_duration.............: avg=115.21ms min=25.73ms med=112.8ms  max=350.46ms p(90)=150.12ms p(95)=162.25ms p(99.9)=211.19ms
     iterations.....................: 52092   431.663153/s
     success_rate...................: 100.00% ✓ 52092      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 99858      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   331 kB/s
     http_req_blocked...............: avg=5.8µs    min=1.12µs  med=2.92µs   max=3.89ms   p(90)=4.2µs    p(95)=4.74µs   p(99.9)=1.2ms   
     http_req_connecting............: avg=2.65µs   min=0s      med=0s       max=3.85ms   p(90)=0s       p(95)=0s       p(99.9)=1.17ms  
     http_req_duration..............: avg=179.63ms min=5.69ms  med=162.01ms max=802.03ms p(90)=204.88ms p(95)=232.81ms p(99.9)=701.4ms 
       { expected_response:true }...: avg=179.63ms min=5.69ms  med=162.01ms max=802.03ms p(90)=204.88ms p(95)=232.81ms p(99.9)=701.4ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 33386
     http_req_receiving.............: avg=91.32µs  min=32.25µs med=88.17µs  max=21.04ms  p(90)=117.37µs p(95)=128.17µs p(99.9)=662.3µs 
     http_req_sending...............: avg=37.97µs  min=5.5µs   med=16.47µs  max=122.63ms p(90)=20.53µs  p(95)=22.17µs  p(99.9)=545.9µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=179.5ms  min=5.58ms  med=161.89ms max=801.92ms p(90)=204.78ms p(95)=232.61ms p(99.9)=701.3ms 
     http_reqs......................: 33386   275.607581/s
     iteration_duration.............: avg=180.42ms min=37.34ms med=162.35ms max=802.28ms p(90)=205.22ms p(95)=233.45ms p(99.9)=701.67ms
     iterations.....................: 33286   274.782062/s
     success_rate...................: 100.00% ✓ 33286      ✗ 0    
     vus............................: 19      min=19       max=50 
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

     checks.........................: 100.00% ✓ 97956      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   325 kB/s
     http_req_blocked...............: avg=5.74µs   min=1.07µs  med=2.88µs   max=3.56ms   p(90)=4.12µs   p(95)=4.63µs   p(99.9)=1.24ms  
     http_req_connecting............: avg=2.71µs   min=0s      med=0s       max=3.52ms   p(90)=0s       p(95)=0s       p(99.9)=1.21ms  
     http_req_duration..............: avg=183.07ms min=7.45ms  med=189.97ms max=372.87ms p(90)=205.36ms p(95)=210.06ms p(99.9)=278.2ms 
       { expected_response:true }...: avg=183.07ms min=7.45ms  med=189.97ms max=372.87ms p(90)=205.36ms p(95)=210.06ms p(99.9)=278.2ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 32752
     http_req_receiving.............: avg=85.83µs  min=30.47µs med=80.06µs  max=123.88ms p(90)=108.19µs p(95)=118.68µs p(99.9)=519.54µs
     http_req_sending...............: avg=25.94µs  min=5.23µs  med=15.23µs  max=74.09ms  p(90)=19.02µs  p(95)=20.63µs  p(99.9)=537.74µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.95ms min=7.38ms  med=189.87ms max=372.39ms p(90)=205.26ms p(95)=209.95ms p(99.9)=277.57ms
     http_reqs......................: 32752   270.784791/s
     iteration_duration.............: avg=183.86ms min=38.53ms med=190.23ms max=381.21ms p(90)=205.62ms p(95)=210.31ms p(99.9)=279.75ms
     iterations.....................: 32652   269.958017/s
     success_rate...................: 100.00% ✓ 32652      ✗ 0    
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

