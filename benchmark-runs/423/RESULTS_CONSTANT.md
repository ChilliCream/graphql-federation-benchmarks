## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-net-11 | 16.7.0 | 3,611 | 3,946 | 3,565 | 3.3% |  |
| fusion-fed-net-11 | 16.7.0 | 3,581 | 3,904 | 3,545 | 3.3% |  |
| fusion-fed-aot-11 | 16.7.0 | 3,515 | 3,811 | 3,482 | 3.2% |  |
| fusion-aot-11 | 16.7.0 | 3,428 | 3,687 | 3,398 | 2.9% |  |
| feddi-gateway | 3c75a7db8876 | 2,895 | 3,146 | 2,824 | 3.7% |  |
| hive-router | v0.3.5 | 2,679 | 2,849 | 2,662 | 2.3% |  |
| grafbase | 0.53.5 | 1,638 | 1,696 | 1,634 | 1.4% |  |
| cosmo | 0.361.0 | 1,430 | 1,490 | 1,423 | 1.6% |  |
| caliban | 3.2.0 | 1,332 | 1,398 | 1,325 | 1.9% |  |
| hive-gateway-router-runtime | 2.15.2 | 506 | 529 | 500 | 1.8% |  |
| apollo-router | v2.18.0 | 444 | 467 | 427 | 3.1% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 406 | 423 | 394 | 2.2% |  |
| apollo-gateway | 2.14.4 | 270 | 273 | 269 | 0.5% |  |
| hive-gateway | 2.15.2 | 261 | 269 | 260 | 1.1% |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1301598     ✗ 0     
     data_received..................: 38 GB   317 MB/s
     data_sent......................: 522 MB  4.3 MB/s
     http_req_blocked...............: avg=2.81µs   min=792ns    med=1.91µs  max=31.8ms   p(90)=3.21µs  p(95)=3.94µs  p(99.9)=28.96µs
     http_req_connecting............: avg=223ns    min=0s       med=0s      max=4.05ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.6ms   min=931.56µs med=12.39ms max=295.64ms p(90)=21.05ms p(95)=25.04ms p(99.9)=49.83ms
       { expected_response:true }...: avg=13.6ms   min=931.56µs med=12.39ms max=295.64ms p(90)=21.05ms p(95)=25.04ms p(99.9)=49.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433966
     http_req_receiving.............: avg=769.93µs min=52.19µs  med=80.89µs max=46.18ms  p(90)=2.18ms  p(95)=4.35ms  p(99.9)=27.85ms
     http_req_sending...............: avg=59.59µs  min=4.43µs   med=8µs     max=183.75ms p(90)=14.92µs p(95)=92.91µs p(99.9)=9.78ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=12.77ms  min=840.44µs med=11.58ms max=295.51ms p(90)=19.9ms  p(95)=23.67ms p(99.9)=47.31ms
     http_reqs......................: 433966  3611.821175/s
     iteration_duration.............: avg=13.82ms  min=1.4ms    med=12.59ms max=327.32ms p(90)=21.27ms p(95)=25.31ms p(99.9)=50.78ms
     iterations.....................: 433866  3610.988893/s
     success_rate...................: 100.00% ✓ 433866      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1290735     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=2.74µs   min=831ns   med=1.95µs  max=17.18ms  p(90)=3.18µs  p(95)=3.84µs  p(99.9)=28.84µs
     http_req_connecting............: avg=227ns    min=0s      med=0s      max=4.06ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.71ms  min=1.22ms  med=12.53ms max=289.86ms p(90)=21.02ms p(95)=25.03ms p(99.9)=49.59ms
       { expected_response:true }...: avg=13.71ms  min=1.22ms  med=12.53ms max=289.86ms p(90)=21.02ms p(95)=25.03ms p(99.9)=49.59ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 430345
     http_req_receiving.............: avg=665.58µs min=51.65µs med=81.38µs max=279.92ms p(90)=1.76ms  p(95)=3.49ms  p(99.9)=26.28ms
     http_req_sending...............: avg=59.58µs  min=4.55µs  med=8.2µs   max=173.28ms p(90)=14.53µs p(95)=93.74µs p(99.9)=9.46ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=12.99ms  min=1.11ms  med=11.79ms max=260.43ms p(90)=20.12ms p(95)=23.92ms p(99.9)=47.62ms
     http_reqs......................: 430345  3581.056766/s
     iteration_duration.............: avg=13.93ms  min=1.75ms  med=12.73ms max=302.66ms p(90)=21.24ms p(95)=25.3ms  p(99.9)=50.26ms
     iterations.....................: 430245  3580.224629/s
     success_rate...................: 100.00% ✓ 430245      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1266828     ✗ 0     
     data_received..................: 37 GB   308 MB/s
     data_sent......................: 508 MB  4.2 MB/s
     http_req_blocked...............: avg=3.51µs   min=811ns   med=2.02µs  max=24.99ms  p(90)=3.33µs  p(95)=4.05µs  p(99.9)=29.46µs
     http_req_connecting............: avg=695ns    min=0s      med=0s      max=9.62ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.97ms  min=1.32ms  med=12.8ms  max=282.01ms p(90)=21.1ms  p(95)=25.23ms p(99.9)=50.49ms
       { expected_response:true }...: avg=13.97ms  min=1.32ms  med=12.8ms  max=282.01ms p(90)=21.1ms  p(95)=25.23ms p(99.9)=50.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 422376
     http_req_receiving.............: avg=757.34µs min=52.42µs med=82.48µs max=172.93ms p(90)=2.11ms  p(95)=3.85ms  p(99.9)=27.78ms
     http_req_sending...............: avg=60.7µs   min=4.52µs  med=8.39µs  max=152.43ms p(90)=15.18µs p(95)=94.21µs p(99.9)=9.82ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.16ms  min=1.24ms  med=11.95ms max=281.8ms  p(90)=20.09ms p(95)=23.93ms p(99.9)=47.95ms
     http_reqs......................: 422376  3515.028228/s
     iteration_duration.............: avg=14.19ms  min=1.78ms  med=13ms    max=298.92ms p(90)=21.33ms p(95)=25.5ms  p(99.9)=51.77ms
     iterations.....................: 422276  3514.196024/s
     success_rate...................: 100.00% ✓ 422276      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1235367     ✗ 0     
     data_received..................: 36 GB   301 MB/s
     data_sent......................: 495 MB  4.1 MB/s
     http_req_blocked...............: avg=2.73µs  min=852ns    med=1.95µs  max=17.25ms  p(90)=3.17µs  p(95)=3.85µs  p(99.9)=25.56µs
     http_req_connecting............: avg=239ns   min=0s       med=0s      max=3.97ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.34ms min=1ms      med=13.22ms max=276.6ms  p(90)=21.45ms p(95)=25.45ms p(99.9)=52.06ms
       { expected_response:true }...: avg=14.34ms min=1ms      med=13.22ms max=276.6ms  p(90)=21.45ms p(95)=25.45ms p(99.9)=52.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 411889
     http_req_receiving.............: avg=1.05ms  min=50.68µs  med=84.48µs max=191.61ms p(90)=3.34ms  p(95)=5.53ms  p(99.9)=30.62ms
     http_req_sending...............: avg=58.24µs min=4.58µs   med=8.09µs  max=231.84ms p(90)=14.6µs  p(95)=89.56µs p(99.9)=9.87ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.22ms min=893.67µs med=12.1ms  max=247.58ms p(90)=19.94ms p(95)=23.67ms p(99.9)=48.88ms
     http_reqs......................: 411889  3428.401098/s
     iteration_duration.............: avg=14.56ms min=1.51ms   med=13.42ms max=288.47ms p(90)=21.67ms p(95)=25.72ms p(99.9)=52.84ms
     iterations.....................: 411789  3427.568737/s
     success_rate...................: 100.00% ✓ 411789      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1043427     ✗ 0     
     data_received..................: 30 GB   253 MB/s
     data_sent......................: 418 MB  3.5 MB/s
     http_req_blocked...............: avg=3.76µs   min=1.06µs   med=2.82µs  max=22.53ms  p(90)=4.4µs   p(95)=5.15µs   p(99.9)=41.3µs 
     http_req_connecting............: avg=270ns    min=0s       med=0s      max=3.93ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.02ms  min=993.8µs  med=16.29ms max=316.49ms p(90)=25.95ms p(95)=29.3ms   p(99.9)=51.05ms
       { expected_response:true }...: avg=17.02ms  min=993.8µs  med=16.29ms max=316.49ms p(90)=25.95ms p(95)=29.3ms   p(99.9)=51.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 347909
     http_req_receiving.............: avg=117.25µs min=25.85µs  med=50.49µs max=260.08ms p(90)=95.12µs p(95)=202.77µs p(99.9)=10.39ms
     http_req_sending...............: avg=54.64µs  min=5.09µs   med=10.59µs max=38.75ms  p(90)=17.92µs p(95)=115.13µs p(99.9)=7.51ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.84ms  min=885.15µs med=16.16ms max=93.88ms  p(90)=25.76ms p(95)=29.01ms  p(99.9)=49.8ms 
     http_reqs......................: 347909  2895.658983/s
     iteration_duration.............: avg=17.23ms  min=1.28ms   med=16.49ms max=326.79ms p(90)=26.16ms p(95)=29.54ms  p(99.9)=51.81ms
     iterations.....................: 347809  2894.826679/s
     success_rate...................: 100.00% ✓ 347809      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 966054      ✗ 0     
     data_received..................: 28 GB   234 MB/s
     data_sent......................: 387 MB  3.2 MB/s
     http_req_blocked...............: avg=3.6µs   min=902ns  med=2.61µs  max=16.26ms  p(90)=4.5µs   p(95)=5.35µs   p(99.9)=38.28µs
     http_req_connecting............: avg=376ns   min=0s     med=0s      max=5.9ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=18.4ms  min=1.63ms med=18.03ms max=271.68ms p(90)=25.32ms p(95)=27.99ms  p(99.9)=47.85ms
       { expected_response:true }...: avg=18.4ms  min=1.63ms med=18.03ms max=271.68ms p(90)=25.32ms p(95)=27.99ms  p(99.9)=47.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 322118
     http_req_receiving.............: avg=99.71µs min=25.9µs med=52.38µs max=31.18ms  p(90)=99.28µs p(95)=186.4µs  p(99.9)=7.75ms 
     http_req_sending...............: avg=50.35µs min=4.53µs med=10.16µs max=223.77ms p(90)=19.38µs p(95)=111.48µs p(99.9)=4.49ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=18.25ms min=1.55ms med=17.9ms  max=271.23ms p(90)=25.15ms p(95)=27.73ms  p(99.9)=46.92ms
     http_reqs......................: 322118  2679.630756/s
     iteration_duration.............: avg=18.62ms min=3.32ms med=18.24ms max=283.61ms p(90)=25.54ms p(95)=28.21ms  p(99.9)=48.39ms
     iterations.....................: 322018  2678.798877/s
     success_rate...................: 100.00% ✓ 322018      ✗ 0     
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

     checks.........................: 100.00% ✓ 590820      ✗ 0     
     data_received..................: 17 GB   144 MB/s
     data_sent......................: 237 MB  2.0 MB/s
     http_req_blocked...............: avg=3.43µs  min=831ns   med=2.23µs  max=11.62ms  p(90)=4.57µs  p(95)=5.71µs   p(99.9)=40.57µs
     http_req_connecting............: avg=465ns   min=0s      med=0s      max=3.99ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=30.21ms min=2.18ms  med=30.19ms max=307.02ms p(90)=39.44ms p(95)=42.42ms  p(99.9)=64.1ms 
       { expected_response:true }...: avg=30.21ms min=2.18ms  med=30.19ms max=307.02ms p(90)=39.44ms p(95)=42.42ms  p(99.9)=64.1ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 197040
     http_req_receiving.............: avg=96.85µs min=26.41µs med=53.72µs max=155.37ms p(90)=125.5µs p(95)=207.71µs p(99.9)=4.45ms 
     http_req_sending...............: avg=41.87µs min=4.49µs  med=9.24µs  max=137.36ms p(90)=23.89µs p(95)=111.53µs p(99.9)=3ms    
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=30.07ms min=2.1ms   med=30.07ms max=306.88ms p(90)=39.29ms p(95)=42.24ms  p(99.9)=63.54ms
     http_reqs......................: 197040  1638.031302/s
     iteration_duration.............: avg=30.45ms min=6.81ms  med=30.41ms max=335.19ms p(90)=39.66ms p(95)=42.64ms  p(99.9)=64.55ms
     iterations.....................: 196940  1637.199983/s
     success_rate...................: 100.00% ✓ 196940      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.361.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 515955      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=4.09µs  min=912ns   med=2.29µs  max=9.16ms   p(90)=3.97µs   p(95)=4.72µs   p(99.9)=35.07µs
     http_req_connecting............: avg=1.39µs  min=0s      med=0s      max=9.01ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.64ms min=2.65ms  med=33.73ms max=282.4ms  p(90)=49.38ms  p(95)=54.31ms  p(99.9)=78.86ms
       { expected_response:true }...: avg=34.64ms min=2.65ms  med=33.73ms max=282.4ms  p(90)=49.38ms  p(95)=54.31ms  p(99.9)=78.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 172085
     http_req_receiving.............: avg=81.56µs min=25.35µs med=63.3µs  max=103.45ms p(90)=105.36µs p(95)=125.52µs p(99.9)=1.31ms 
     http_req_sending...............: avg=27.1µs  min=4.66µs  med=10.46µs max=91.3ms   p(90)=17.93µs  p(95)=22.74µs  p(99.9)=1.23ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.53ms min=2.53ms  med=33.63ms max=277.07ms p(90)=49.27ms  p(95)=54.19ms  p(99.9)=78.53ms
     http_reqs......................: 172085  1430.194341/s
     iteration_duration.............: avg=34.87ms min=4.78ms  med=33.94ms max=297.84ms p(90)=49.59ms  p(95)=54.53ms  p(99.9)=79.33ms
     iterations.....................: 171985  1429.363243/s
     success_rate...................: 100.00% ✓ 171985      ✗ 0     
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

     checks.........................: 100.00% ✓ 480807      ✗ 0     
     data_received..................: 14 GB   117 MB/s
     data_sent......................: 193 MB  1.6 MB/s
     http_req_blocked...............: avg=3.93µs  min=1µs     med=3.06µs  max=4.15ms   p(90)=4.93µs   p(95)=5.7µs    p(99.9)=38.54µs
     http_req_connecting............: avg=564ns   min=0s      med=0s      max=4.11ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=37.17ms min=2.53ms  med=36.12ms max=297.67ms p(90)=52.79ms  p(95)=58.38ms  p(99.9)=88.7ms 
       { expected_response:true }...: avg=37.17ms min=2.53ms  med=36.12ms max=297.67ms p(90)=52.79ms  p(95)=58.38ms  p(99.9)=88.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 160369
     http_req_receiving.............: avg=83.22µs min=26.32µs med=64.22µs max=257.51ms p(90)=104.75µs p(95)=124.71µs p(99.9)=1.47ms 
     http_req_sending...............: avg=28.81µs min=5.05µs  med=13.18µs max=216.47ms p(90)=20.66µs  p(95)=24.88µs  p(99.9)=1.25ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.06ms min=2.47ms  med=36.01ms max=288.79ms p(90)=52.67ms  p(95)=58.26ms  p(99.9)=88.43ms
     http_reqs......................: 160369  1332.854764/s
     iteration_duration.............: avg=37.42ms min=6.34ms  med=36.35ms max=322.04ms p(90)=53.02ms  p(95)=58.61ms  p(99.9)=89.39ms
     iterations.....................: 160269  1332.023647/s
     success_rate...................: 100.00% ✓ 160269      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 182985     ✗ 0    
     data_received..................: 5.3 GB  44 MB/s
     data_sent......................: 73 MB   609 kB/s
     http_req_blocked...............: avg=5.15µs  min=1.22µs  med=3.35µs  max=4.26ms   p(90)=4.78µs   p(95)=5.43µs   p(99.9)=50.67µs 
     http_req_connecting............: avg=1.56µs  min=0s      med=0s      max=4.22ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=97.97ms min=4.49ms  med=95.1ms  max=327.78ms p(90)=118.19ms p(95)=129.15ms p(99.9)=234.61ms
       { expected_response:true }...: avg=97.97ms min=4.49ms  med=95.1ms  max=327.78ms p(90)=118.19ms p(95)=129.15ms p(99.9)=234.61ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61095
     http_req_receiving.............: avg=86.21µs min=30.13µs med=77.59µs max=92.99ms  p(90)=111.61µs p(95)=124.07µs p(99.9)=614.07µs
     http_req_sending...............: avg=24.44µs min=5.53µs  med=15.21µs max=91.5ms   p(90)=21µs     p(95)=22.99µs  p(99.9)=600.39µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=97.86ms min=4.38ms  med=95ms    max=327.09ms p(90)=118.09ms p(95)=129.04ms p(99.9)=233.73ms
     http_reqs......................: 61095   506.70431/s
     iteration_duration.............: avg=98.38ms min=20.45ms med=95.35ms max=345.4ms  p(90)=118.47ms p(95)=129.41ms p(99.9)=237.42ms
     iterations.....................: 60995   505.874938/s
     success_rate...................: 100.00% ✓ 60995      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.18.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 160695     ✗ 0    
     data_received..................: 4.7 GB  39 MB/s
     data_sent......................: 64 MB   534 kB/s
     http_req_blocked...............: avg=5.32µs   min=1.12µs  med=3.33µs   max=4.11ms   p(90)=4.92µs   p(95)=5.49µs   p(99.9)=114.18µs
     http_req_connecting............: avg=1.77µs   min=0s      med=0s       max=4.07ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=111.55ms min=5.47ms  med=109.28ms max=320.89ms p(90)=147.42ms p(95)=158.3ms  p(99.9)=201.72ms
       { expected_response:true }...: avg=111.55ms min=5.47ms  med=109.28ms max=320.89ms p(90)=147.42ms p(95)=158.3ms  p(99.9)=201.72ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 53665
     http_req_receiving.............: avg=87.77µs  min=29.59µs med=85.14µs  max=75.09ms  p(90)=114.19µs p(95)=126.68µs p(99.9)=447.4µs 
     http_req_sending...............: avg=32.15µs  min=5.27µs  med=16.94µs  max=120.11ms p(90)=21.79µs  p(95)=23.59µs  p(99.9)=576.68µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=111.43ms min=5.34ms  med=109.18ms max=320.34ms p(90)=147.31ms p(95)=158.17ms p(99.9)=201.57ms
     http_reqs......................: 53665   444.75504/s
     iteration_duration.............: avg=112.04ms min=20.47ms med=109.61ms max=331.26ms p(90)=147.73ms p(95)=158.6ms  p(99.9)=203.17ms
     iterations.....................: 53565   443.926278/s
     success_rate...................: 100.00% ✓ 53565      ✗ 0    
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

     checks.........................: 100.00% ✓ 147021     ✗ 0    
     data_received..................: 4.3 GB  36 MB/s
     data_sent......................: 59 MB   489 kB/s
     http_req_blocked...............: avg=5.25µs   min=1.09µs  med=3.12µs   max=4.17ms   p(90)=4.54µs   p(95)=5.11µs   p(99.9)=438.54µs
     http_req_connecting............: avg=1.93µs   min=0s      med=0s       max=4.13ms   p(90)=0s       p(95)=0s       p(99.9)=406.85µs
     http_req_duration..............: avg=121.96ms min=5.42ms  med=119.46ms max=338.97ms p(90)=159.73ms p(95)=172.19ms p(99.9)=225.37ms
       { expected_response:true }...: avg=121.96ms min=5.42ms  med=119.46ms max=338.97ms p(90)=159.73ms p(95)=172.19ms p(99.9)=225.37ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49107
     http_req_receiving.............: avg=83.25µs  min=27.53µs med=78.26µs  max=124.36ms p(90)=108.69µs p(95)=120.84µs p(99.9)=513.17µs
     http_req_sending...............: avg=23.24µs  min=5.09µs  med=16.03µs  max=90.88ms  p(90)=21.06µs  p(95)=22.78µs  p(99.9)=510.99µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=121.86ms min=5.34ms  med=119.35ms max=338.46ms p(90)=159.64ms p(95)=172.09ms p(99.9)=224.95ms
     http_reqs......................: 49107   406.815337/s
     iteration_duration.............: avg=122.47ms min=31.68ms med=119.77ms max=346.78ms p(90)=160.06ms p(95)=172.52ms p(99.9)=226.54ms
     iterations.....................: 49007   405.986911/s
     success_rate...................: 100.00% ✓ 49007      ✗ 0    
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

     checks.........................: 100.00% ✓ 97785      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   325 kB/s
     http_req_blocked...............: avg=9.09µs   min=1.1µs   med=3.24µs   max=6.98ms   p(90)=4.6µs    p(95)=5.17µs   p(99.9)=2.63ms  
     http_req_connecting............: avg=5.5µs    min=0s      med=0s       max=6.96ms   p(90)=0s       p(95)=0s       p(99.9)=2.08ms  
     http_req_duration..............: avg=183.36ms min=7.91ms  med=184.97ms max=317.68ms p(90)=193.28ms p(95)=197.46ms p(99.9)=267.53ms
       { expected_response:true }...: avg=183.36ms min=7.91ms  med=184.97ms max=317.68ms p(90)=193.28ms p(95)=197.46ms p(99.9)=267.53ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32695
     http_req_receiving.............: avg=90.84µs  min=30.78µs med=88.76µs  max=3.25ms   p(90)=118.55µs p(95)=130.16µs p(99.9)=567.13µs
     http_req_sending...............: avg=24.42µs  min=5.25µs  med=16.92µs  max=29.26ms  p(90)=21.33µs  p(95)=23.09µs  p(99.9)=880.12µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.25ms min=7.78ms  med=184.85ms max=317.11ms p(90)=193.16ms p(95)=197.35ms p(99.9)=267.43ms
     http_reqs......................: 32695   270.239805/s
     iteration_duration.............: avg=184.19ms min=37.63ms med=185.3ms  max=323.84ms p(90)=193.57ms p(95)=197.73ms p(99.9)=268.76ms
     iterations.....................: 32595   269.413257/s
     success_rate...................: 100.00% ✓ 32595      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 94662      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   314 kB/s
     http_req_blocked...............: avg=7.49µs   min=1.59µs  med=3.94µs   max=4.18ms   p(90)=5.57µs   p(95)=6.23µs   p(99.9)=1.55ms  
     http_req_connecting............: avg=3.22µs   min=0s      med=0s       max=4.14ms   p(90)=0s       p(95)=0s       p(99.9)=1.53ms  
     http_req_duration..............: avg=189.36ms min=5.93ms  med=171.5ms  max=847.14ms p(90)=219.76ms p(95)=258.9ms  p(99.9)=716.62ms
       { expected_response:true }...: avg=189.36ms min=5.93ms  med=171.5ms  max=847.14ms p(90)=219.76ms p(95)=258.9ms  p(99.9)=716.62ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31654
     http_req_receiving.............: avg=103.45µs min=39.39µs med=92.54µs  max=109.53ms p(90)=123.07µs p(95)=135.72µs p(99.9)=1.03ms  
     http_req_sending...............: avg=37.22µs  min=6.83µs  med=18.59µs  max=113.02ms p(90)=23.65µs  p(95)=25.65µs  p(99.9)=709.51µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=189.22ms min=5.84ms  med=171.36ms max=847.03ms p(90)=219.63ms p(95)=258.73ms p(99.9)=716.52ms
     http_reqs......................: 31654   261.659968/s
     iteration_duration.............: avg=190.25ms min=41.03ms med=171.89ms max=847.39ms p(90)=220.24ms p(95)=260.64ms p(99.9)=716.95ms
     iterations.....................: 31554   260.833343/s
     success_rate...................: 100.00% ✓ 31554      ✗ 0    
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

