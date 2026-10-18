## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 2,416 | 2,518 | 2,410 | 1.6% |  |
| fusion-nightly-net11 | 16.7.0-p.28 | 1,951 | 2,000 | 1,940 | 1.1% |  |
| fusion-nightly | 16.7.0-p.28 | 1,928 | 1,976 | 1,910 | 1.1% |  |
| fusion | 16.6.8 | 1,880 | 1,939 | 1,867 | 1.4% |  |
| hive-router | v0.3.5 | 1,864 | 1,935 | 1,850 | 1.5% |  |
| fusion-nightly-fed | 16.7.0-p.28 | 1,837 | 1,890 | 1,829 | 1.1% |  |
| cosmo | 0.359.0 | 1,357 | 1,404 | 1,348 | 1.4% |  |
| grafbase | 0.53.5 | 1,323 | 1,341 | 1,320 | 0.5% |  |
| caliban | 3.2.0 | 1,312 | 1,372 | 1,303 | 1.9% |  |
| hive-gateway-router-runtime | 2.15.2 | 503 | 519 | 501 | 1.2% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 400 | 416 | 398 | 1.6% |  |
| apollo-router | v2.18.0 | 399 | 419 | 396 | 2.2% |  |
| apollo-gateway | 2.14.4 | 257 | 262 | 256 | 0.8% |  |
| hive-gateway | 2.15.2 | 252 | 258 | 249 | 1.3% |  |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 880065      ✗ 0     
     data_received..................: 26 GB   211 MB/s
     data_sent......................: 353 MB  2.9 MB/s
     http_req_blocked...............: avg=4.13µs  min=1.03µs  med=2.69µs  max=8.74ms   p(90)=4.55µs   p(95)=5.53µs   p(99.9)=39.46µs
     http_req_connecting............: avg=931ns   min=0s      med=0s      max=8.62ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=20.21ms min=12.39ms med=19.45ms max=286.53ms p(90)=24.3ms   p(95)=26.6ms   p(99.9)=46.68ms
       { expected_response:true }...: avg=20.21ms min=12.39ms med=19.45ms max=286.53ms p(90)=24.3ms   p(95)=26.6ms   p(99.9)=46.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 293455
     http_req_receiving.............: avg=88.78µs min=22.97µs med=50.41µs max=81.16ms  p(90)=103.41µs p(95)=176.69µs p(99.9)=4.52ms 
     http_req_sending...............: avg=44.76µs min=4.56µs  med=9.78µs  max=173.52ms p(90)=20.51µs  p(95)=100.61µs p(99.9)=3.59ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=20.08ms min=12.32ms med=19.35ms max=283.38ms p(90)=24.15ms  p(95)=26.37ms  p(99.9)=46ms   
     http_reqs......................: 293455  2416.839481/s
     iteration_duration.............: avg=20.44ms min=12.61ms med=19.66ms max=309.53ms p(90)=24.51ms  p(95)=26.83ms  p(99.9)=47.04ms
     iterations.....................: 293355  2416.0159/s
     success_rate...................: 100.00% ✓ 293355      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 713487      ✗ 0     
     data_received..................: 21 GB   171 MB/s
     data_sent......................: 286 MB  2.3 MB/s
     http_req_blocked...............: avg=2.81µs  min=851ns   med=1.95µs  max=9.86ms   p(90)=3.68µs  p(95)=4.49µs  p(99.9)=31.57µs
     http_req_connecting............: avg=258ns   min=0s      med=0s      max=2.54ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25ms    min=16.96ms med=24.44ms max=292.54ms p(90)=28.98ms p(95)=30.72ms p(99.9)=47.8ms 
       { expected_response:true }...: avg=25ms    min=16.96ms med=24.44ms max=292.54ms p(90)=28.98ms p(95)=30.72ms p(99.9)=47.8ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 237929
     http_req_receiving.............: avg=395.4µs min=48.55µs med=88.04µs max=132.29ms p(90)=1.16ms  p(95)=1.9ms   p(99.9)=10.23ms
     http_req_sending...............: avg=33.45µs min=4.4µs   med=8.12µs  max=119.05ms p(90)=18.08µs p(95)=47.21µs p(99.9)=2.08ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.57ms min=16.87ms med=24.04ms max=282.63ms p(90)=28.39ms p(95)=30.06ms p(99.9)=46.12ms
     http_reqs......................: 237929  1951.865509/s
     iteration_duration.............: avg=25.22ms min=17.13ms med=24.64ms max=316.6ms  p(90)=29.18ms p(95)=30.93ms p(99.9)=48.14ms
     iterations.....................: 237829  1951.045153/s
     success_rate...................: 100.00% ✓ 237829      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 705171      ✗ 0     
     data_received..................: 21 GB   169 MB/s
     data_sent......................: 283 MB  2.3 MB/s
     http_req_blocked...............: avg=2.93µs   min=871ns   med=2.01µs  max=9.57ms   p(90)=3.83µs  p(95)=4.64µs  p(99.9)=27.75µs
     http_req_connecting............: avg=433ns    min=0s      med=0s      max=4.3ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.29ms  min=15.77ms med=24.71ms max=279.47ms p(90)=29.58ms p(95)=31.37ms p(99.9)=48.66ms
       { expected_response:true }...: avg=25.29ms  min=15.77ms med=24.71ms max=279.47ms p(90)=29.58ms p(95)=31.37ms p(99.9)=48.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 235157
     http_req_receiving.............: avg=354.96µs min=49.98µs med=91.5µs  max=65.72ms  p(90)=1ms     p(95)=1.66ms  p(99.9)=8.9ms  
     http_req_sending...............: avg=35.25µs  min=4.7µs   med=8.45µs  max=231.99ms p(90)=18.85µs p(95)=41.11µs p(99.9)=1.91ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.9ms   min=15.68ms med=24.34ms max=278.87ms p(90)=29.08ms p(95)=30.84ms p(99.9)=47.25ms
     http_reqs......................: 235157  1928.894982/s
     iteration_duration.............: avg=25.51ms  min=15.97ms med=24.92ms max=312.37ms p(90)=29.79ms p(95)=31.58ms p(99.9)=48.98ms
     iterations.....................: 235057  1928.074724/s
     success_rate...................: 100.00% ✓ 235057      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion (HotChocolate subgraphs) (16.6.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 687699      ✗ 0     
     data_received..................: 20 GB   165 MB/s
     data_sent......................: 276 MB  2.3 MB/s
     http_req_blocked...............: avg=3.1µs    min=852ns   med=2.23µs  max=4.02ms   p(90)=4.04µs   p(95)=4.83µs  p(99.9)=33.56µs
     http_req_connecting............: avg=452ns    min=0s      med=0s      max=3.98ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.94ms  min=16.91ms med=25.34ms max=294.64ms p(90)=30.41ms  p(95)=32.28ms p(99.9)=49.75ms
       { expected_response:true }...: avg=25.94ms  min=16.91ms med=25.34ms max=294.64ms p(90)=30.41ms  p(95)=32.28ms p(99.9)=49.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 229333
     http_req_receiving.............: avg=323.12µs min=49.46µs med=95.38µs max=111.82ms p(90)=832.92µs p(95)=1.34ms  p(99.9)=8.34ms 
     http_req_sending...............: avg=33.96µs  min=4.44µs  med=8.86µs  max=135.97ms p(90)=18.31µs  p(95)=40.58µs p(99.9)=1.76ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.59ms  min=16.8ms  med=25ms    max=290.41ms p(90)=29.98ms  p(95)=31.81ms p(99.9)=48.62ms
     http_reqs......................: 229333  1880.913175/s
     iteration_duration.............: avg=26.16ms  min=17.08ms med=25.55ms max=305ms    p(90)=30.61ms  p(95)=32.49ms p(99.9)=50.18ms
     iterations.....................: 229233  1880.093008/s
     success_rate...................: 100.00% ✓ 229233      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 681807      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 273 MB  2.2 MB/s
     http_req_blocked...............: avg=3.6µs   min=1µs     med=2.73µs  max=8.08ms   p(90)=4.54µs   p(95)=5.35µs   p(99.9)=40.22µs
     http_req_connecting............: avg=415ns   min=0s      med=0s      max=4.15ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.16ms min=17.97ms med=25.69ms max=298.43ms p(90)=29.88ms  p(95)=31.39ms  p(99.9)=48.99ms
       { expected_response:true }...: avg=26.16ms min=17.97ms med=25.69ms max=298.43ms p(90)=29.88ms  p(95)=31.39ms  p(99.9)=48.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 227369
     http_req_receiving.............: avg=82.24µs min=25.79µs med=55.23µs max=27.98ms  p(90)=100.37µs p(95)=128.51µs p(99.9)=2.71ms 
     http_req_sending...............: avg=35.34µs min=4.84µs  med=10.85µs max=154.26ms p(90)=19.77µs  p(95)=28.45µs  p(99.9)=1.65ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.05ms min=17.87ms med=25.59ms max=297.83ms p(90)=29.75ms  p(95)=31.25ms  p(99.9)=48.02ms
     http_reqs......................: 227369  1864.625803/s
     iteration_duration.............: avg=26.39ms min=18.32ms med=25.9ms  max=307.25ms p(90)=30.09ms  p(95)=31.6ms   p(99.9)=49.48ms
     iterations.....................: 227269  1863.805715/s
     success_rate...................: 100.00% ✓ 227269      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 671985      ✗ 0     
     data_received..................: 20 GB   161 MB/s
     data_sent......................: 269 MB  2.2 MB/s
     http_req_blocked...............: avg=2.83µs   min=812ns   med=1.93µs  max=6.9ms    p(90)=3.74µs  p(95)=4.58µs  p(99.9)=32.3µs 
     http_req_connecting............: avg=416ns    min=0s      med=0s      max=3.31ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.56ms  min=17.61ms med=25.99ms max=300.78ms p(90)=31.14ms p(95)=32.99ms p(99.9)=50.49ms
       { expected_response:true }...: avg=26.56ms  min=17.61ms med=25.99ms max=300.78ms p(90)=31.14ms p(95)=32.99ms p(99.9)=50.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 224095
     http_req_receiving.............: avg=396.19µs min=50.13µs med=93.33µs max=262.71ms p(90)=1.03ms  p(95)=1.69ms  p(99.9)=9.93ms 
     http_req_sending...............: avg=31.94µs  min=4.14µs  med=8.15µs  max=44.78ms  p(90)=18.55µs p(95)=38.86µs p(99.9)=1.86ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.13ms  min=17.5ms  med=25.6ms  max=108.29ms p(90)=30.62ms p(95)=32.42ms p(99.9)=47.87ms
     http_reqs......................: 224095  1837.732065/s
     iteration_duration.............: avg=26.77ms  min=17.78ms med=26.2ms  max=330.57ms p(90)=31.34ms p(95)=33.19ms p(99.9)=50.9ms 
     iterations.....................: 223995  1836.911997/s
     success_rate...................: 100.00% ✓ 223995      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.359.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 496548      ✗ 0     
     data_received..................: 15 GB   119 MB/s
     data_sent......................: 199 MB  1.6 MB/s
     http_req_blocked...............: avg=3.28µs  min=901ns   med=2.36µs  max=3.53ms   p(90)=4.14µs  p(95)=4.93µs   p(99.9)=37.15µs
     http_req_connecting............: avg=535ns   min=0s      med=0s      max=3.49ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.01ms min=18.23ms med=35.41ms max=300.36ms p(90)=43.04ms p(95)=45.52ms  p(99.9)=59.17ms
       { expected_response:true }...: avg=36.01ms min=18.23ms med=35.41ms max=300.36ms p(90)=43.04ms p(95)=45.52ms  p(99.9)=59.17ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 165616
     http_req_receiving.............: avg=80.17µs min=26.95µs med=62.78µs max=232.98ms p(90)=106µs   p(95)=126.72µs p(99.9)=1.05ms 
     http_req_sending...............: avg=27.67µs min=4.81µs  med=10.6µs  max=170.42ms p(90)=18.3µs  p(95)=22.99µs  p(99.9)=1.15ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=35.91ms min=18.1ms  med=35.31ms max=296.08ms p(90)=42.93ms p(95)=45.39ms  p(99.9)=58.71ms
     http_reqs......................: 165616  1357.297325/s
     iteration_duration.............: avg=36.24ms min=21.63ms med=35.62ms max=310.86ms p(90)=43.24ms p(95)=45.72ms  p(99.9)=59.54ms
     iterations.....................: 165516  1356.47778/s
     success_rate...................: 100.00% ✓ 165516      ✗ 0     
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

     checks.........................: 100.00% ✓ 484059      ✗ 0     
     data_received..................: 14 GB   116 MB/s
     data_sent......................: 194 MB  1.6 MB/s
     http_req_blocked...............: avg=3.51µs  min=901ns   med=2.27µs  max=4.16ms   p(90)=4.9µs    p(95)=5.94µs   p(99.9)=40.97µs
     http_req_connecting............: avg=610ns   min=0s      med=0s      max=4.12ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.92ms min=18.13ms med=36.6ms  max=305.77ms p(90)=43.38ms  p(95)=45.35ms  p(99.9)=60.21ms
       { expected_response:true }...: avg=36.92ms min=18.13ms med=36.6ms  max=305.77ms p(90)=43.38ms  p(95)=45.35ms  p(99.9)=60.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 161453
     http_req_receiving.............: avg=84.08µs min=27.01µs med=55.03µs max=71.73ms  p(90)=123.11µs p(95)=167.95µs p(99.9)=1.89ms 
     http_req_sending...............: avg=34.51µs min=4.65µs  med=9.21µs  max=118.91ms p(90)=23.24µs  p(95)=47.8µs   p(99.9)=2.02ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=36.8ms  min=17.99ms med=36.49ms max=305.6ms  p(90)=43.25ms  p(95)=45.21ms  p(99.9)=58.98ms
     http_reqs......................: 161453  1323.53107/s
     iteration_duration.............: avg=37.18ms min=19.43ms med=36.83ms max=324.04ms p(90)=43.59ms  p(95)=45.57ms  p(99.9)=60.75ms
     iterations.....................: 161353  1322.711308/s
     success_rate...................: 100.00% ✓ 161353      ✗ 0     
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

     checks.........................: 100.00% ✓ 480189      ✗ 0     
     data_received..................: 14 GB   115 MB/s
     data_sent......................: 192 MB  1.6 MB/s
     http_req_blocked...............: avg=3.36µs  min=982ns   med=2.41µs  max=5.3ms    p(90)=4.17µs  p(95)=4.96µs   p(99.9)=34.76µs
     http_req_connecting............: avg=561ns   min=0s      med=0s      max=3.46ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=37.24ms min=19.65ms med=36.71ms max=312.71ms p(90)=44.17ms p(95)=46.61ms  p(99.9)=59.54ms
       { expected_response:true }...: avg=37.24ms min=19.65ms med=36.71ms max=312.71ms p(90)=44.17ms p(95)=46.61ms  p(99.9)=59.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 160163
     http_req_receiving.............: avg=78.24µs min=27.41µs med=62.47µs max=52.69ms  p(90)=103µs   p(95)=122.97µs p(99.9)=1.31ms 
     http_req_sending...............: avg=26.29µs min=5.03µs  med=11.33µs max=140.24ms p(90)=18.68µs p(95)=22.98µs  p(99.9)=1.1ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.13ms min=19.52ms med=36.62ms max=312ms    p(90)=44.05ms p(95)=46.49ms  p(99.9)=59.3ms 
     http_reqs......................: 160163  1312.375259/s
     iteration_duration.............: avg=37.47ms min=22.51ms med=36.93ms max=322.14ms p(90)=44.38ms p(95)=46.83ms  p(99.9)=59.88ms
     iterations.....................: 160063  1311.555859/s
     success_rate...................: 100.00% ✓ 160063      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 184272     ✗ 0    
     data_received..................: 5.4 GB  44 MB/s
     data_sent......................: 74 MB   604 kB/s
     http_req_blocked...............: avg=4.86µs  min=1.07µs  med=3.14µs  max=3.33ms   p(90)=4.67µs   p(95)=5.32µs   p(99.9)=53.9µs  
     http_req_connecting............: avg=1.49µs  min=0s      med=0s      max=3.31ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=97.31ms min=21.57ms med=95.61ms max=327.57ms p(90)=115.8ms  p(95)=125.62ms p(99.9)=222.29ms
       { expected_response:true }...: avg=97.31ms min=21.57ms med=95.61ms max=327.57ms p(90)=115.8ms  p(95)=125.62ms p(99.9)=222.29ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61524
     http_req_receiving.............: avg=83.84µs min=26.59µs med=77.08µs max=69.48ms  p(90)=110.53µs p(95)=122.94µs p(99.9)=629.24µs
     http_req_sending...............: avg=21.97µs min=5.36µs  med=16.1µs  max=47.12ms  p(90)=21.77µs  p(95)=23.79µs  p(99.9)=548.92µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=97.2ms  min=21.44ms med=95.51ms max=327.02ms p(90)=115.69ms p(95)=125.52ms p(99.9)=222.06ms
     http_reqs......................: 61524   503.095028/s
     iteration_duration.............: avg=97.69ms min=45.02ms med=95.88ms max=344.18ms p(90)=116.06ms p(95)=125.9ms  p(99.9)=223.61ms
     iterations.....................: 61424   502.277306/s
     success_rate...................: 100.00% ✓ 61424      ✗ 0    
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

     checks.........................: 100.00% ✓ 146760     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   481 kB/s
     http_req_blocked...............: avg=6.03µs   min=1.33µs  med=3.7µs    max=3.99ms   p(90)=5.33µs   p(95)=5.98µs   p(99.9)=702.12µs
     http_req_connecting............: avg=2.05µs   min=0s      med=0s       max=3.94ms   p(90)=0s       p(95)=0s       p(99.9)=672.53µs
     http_req_duration..............: avg=122.18ms min=21.7ms  med=120.46ms max=338.14ms p(90)=150.89ms p(95)=161.24ms p(99.9)=205.74ms
       { expected_response:true }...: avg=122.18ms min=21.7ms  med=120.46ms max=338.14ms p(90)=150.89ms p(95)=161.24ms p(99.9)=205.74ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49020
     http_req_receiving.............: avg=95.11µs  min=30.7µs  med=83.72µs  max=128.09ms p(90)=114.22µs p(95)=126.11µs p(99.9)=495.61µs
     http_req_sending...............: avg=24.38µs  min=6.06µs  med=18.14µs  max=96.45ms  p(90)=23.56µs  p(95)=25.67µs  p(99.9)=571.26µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=122.06ms min=21.55ms med=120.35ms max=337.78ms p(90)=150.77ms p(95)=161.11ms p(99.9)=205.28ms
     http_reqs......................: 49020   400.552179/s
     iteration_duration.............: avg=122.68ms min=34.17ms med=120.78ms max=348.7ms  p(90)=151.22ms p(95)=161.62ms p(99.9)=207.9ms 
     iterations.....................: 48920   399.735059/s
     success_rate...................: 100.00% ✓ 48920      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 146493     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   480 kB/s
     http_req_blocked...............: avg=5.37µs   min=1.08µs  med=3.13µs   max=3.57ms   p(90)=4.62µs   p(95)=5.18µs   p(99.9)=521.84µs
     http_req_connecting............: avg=2.03µs   min=0s      med=0s       max=3.52ms   p(90)=0s       p(95)=0s       p(99.9)=492.57µs
     http_req_duration..............: avg=122.42ms min=21.57ms med=120.43ms max=336.45ms p(90)=153.23ms p(95)=163.38ms p(99.9)=208.81ms
       { expected_response:true }...: avg=122.42ms min=21.57ms med=120.43ms max=336.45ms p(90)=153.23ms p(95)=163.38ms p(99.9)=208.81ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48931
     http_req_receiving.............: avg=90.05µs  min=29.36µs med=83.07µs  max=217.05ms p(90)=114.1µs  p(95)=126.47µs p(99.9)=542.85µs
     http_req_sending...............: avg=30.55µs  min=5.09µs  med=15.4µs   max=137.53ms p(90)=20.84µs  p(95)=22.81µs  p(99.9)=517.75µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=122.3ms  min=21.47ms med=120.33ms max=336.1ms  p(90)=153.11ms p(95)=163.24ms p(99.9)=207.88ms
     http_reqs......................: 48931   399.935098/s
     iteration_duration.............: avg=122.91ms min=40.86ms med=120.76ms max=346.82ms p(90)=153.54ms p(95)=163.69ms p(99.9)=211.84ms
     iterations.....................: 48831   399.117753/s
     success_rate...................: 100.00% ✓ 48831      ✗ 0    
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

     checks.........................: 100.00% ✓ 94380      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   309 kB/s
     http_req_blocked...............: avg=7.02µs   min=1.23µs  med=3.52µs   max=4.35ms   p(90)=5.05µs   p(95)=5.66µs   p(99.9)=1.51ms  
     http_req_connecting............: avg=3.22µs   min=0s      med=0s       max=4.31ms   p(90)=0s       p(95)=0s       p(99.9)=1.48ms  
     http_req_duration..............: avg=189.99ms min=23.54ms med=181.87ms max=386.34ms p(90)=261.94ms p(95)=266.3ms  p(99.9)=340.71ms
       { expected_response:true }...: avg=189.99ms min=23.54ms med=181.87ms max=386.34ms p(90)=261.94ms p(95)=266.3ms  p(99.9)=340.71ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31560
     http_req_receiving.............: avg=96.79µs  min=36.6µs  med=90.4µs   max=46.6ms   p(90)=121.27µs p(95)=133.79µs p(99.9)=612.47µs
     http_req_sending...............: avg=28.05µs  min=5.9µs   med=17.92µs  max=106.32ms p(90)=22.72µs  p(95)=24.65µs  p(99.9)=561.68µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=189.86ms min=23.44ms med=181.75ms max=385.71ms p(90)=261.83ms p(95)=266.18ms p(99.9)=340.59ms
     http_reqs......................: 31560   257.189591/s
     iteration_duration.............: avg=190.82ms min=47.5ms  med=182.16ms max=399.4ms  p(90)=262.24ms p(95)=266.59ms p(99.9)=343.45ms
     iterations.....................: 31460   256.374668/s
     success_rate...................: 100.00% ✓ 31460      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 92400      ✗ 0    
     data_received..................: 2.7 GB  22 MB/s
     data_sent......................: 37 MB   304 kB/s
     http_req_blocked...............: avg=8.04µs   min=1.38µs  med=3.73µs   max=4.65ms   p(90)=5.25µs   p(95)=5.91µs   p(99.9)=2.21ms  
     http_req_connecting............: avg=4µs      min=0s      med=0s       max=4.59ms   p(90)=0s       p(95)=0s       p(99.9)=2.15ms  
     http_req_duration..............: avg=194.06ms min=17.98ms med=180.36ms max=802.65ms p(90)=224.48ms p(95)=244.64ms p(99.9)=731.35ms
       { expected_response:true }...: avg=194.06ms min=17.98ms med=180.36ms max=802.65ms p(90)=224.48ms p(95)=244.64ms p(99.9)=731.35ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 30900
     http_req_receiving.............: avg=101.31µs min=35.34µs med=91.92µs  max=65.79ms  p(90)=123.7µs  p(95)=136.39µs p(99.9)=837.8µs 
     http_req_sending...............: avg=28.1µs   min=6.64µs  med=18µs     max=37.67ms  p(90)=22.82µs  p(95)=24.69µs  p(99.9)=591.94µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=193.93ms min=17.87ms med=180.26ms max=802.54ms p(90)=224.34ms p(95)=244.52ms p(99.9)=731.24ms
     http_reqs......................: 30900   252.74369/s
     iteration_duration.............: avg=194.93ms min=42.59ms med=180.76ms max=802.91ms p(90)=224.81ms p(95)=245.04ms p(99.9)=731.68ms
     iterations.....................: 30800   251.925749/s
     success_rate...................: 100.00% ✓ 30800      ✗ 0    
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

