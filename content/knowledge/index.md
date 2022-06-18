---
title: Knowledge
date: 2021-01-01 12:00:00
---
# Contents
- [Guides](#guides)
- [Practices](#practices)
- [MLOps projects](#mlops-projects)
- [勉強会](#study)
- [Conferences](#conferences)
- [書籍](#books)
- [References](#references)

<a id="guides"></a>

# Guides
- MLOpsがどういったものかを理解する上で読んでおくと良い記事や発表資料
### ブログ記事
- [Machine Learning Operations](https://ml-ops.org/)
    - MLOpsを含む機械学習全般に関する活用など網羅的にまとまったサイト
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
    - GoogleによるMLOpsのlevel毎のゴール（取り組み）を示した記事
- [The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction](https://research.google/pubs/pub46555/)
    - MLシステムを定量的に評価する指標としてML Test Scoreを導入し計測した論文
- [Machine Learning operations maturity model](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model)
    - MicrosoftによるMLOpsの成熟度を定性的に示した記事
- [ゆるふわMLOps入門](https://www.nogawanogawa.com/entry/mlops)
    - 日本語で書かれたMLOpsへの取り組み要素を1つ1つ丁寧に紹介した記事

### プレゼンテーション
- [MLOpsの始め方](https://confengine.com/conferences/devopsdays-tokyo-2021/proposal/15205/mlops)
- [機械学習エンジニアのためのMLOps入門](https://speakerdeck.com/chie8842/cookpad-internship-mlops-lecture-1)
- [先駆者に学ぶMLOpsの実際](https://www.slideshare.net/tetsutarowatanabe/mlops-238097926)

<a id="practices"></a>

# Practices
## All in one
### ブログ記事
- [検索アルゴリズム改善における機械学習の活用 ~MLOpsについて~](https://developers.gnavi.co.jp/entry/ml-ops/) - <font color="DodgerBlue">***2022 Gurunavi***</font>
- [バンダイナムコグループの機械学習機能を実現するML基盤について](https://www.wantedly.com/companies/company_9704487/post_articles/371348) - <font color="DodgerBlue">***2022 BANDAI NAMCO***</font>
- [オンライン機械学習サービスとしてGCP Vertex AIのMLOpsを導入した話](https://medium.com/eureka-engineering/vertex-ai-mlops-b74cdff19681) - <font color="DodgerBlue">***2021 Eureka***</font>
- [MLOpsはじめました](https://tech.enigmo.co.jp/entry/2021/12/15/100000) - <font color="DodgerBlue">***2021 enigmo***</font>
- [ヤフーのAIプラットフォーム紹介 ~ AI開発をより手軽に](https://techblog.yahoo.co.jp/entry/2021083130180585/) - <font color="DodgerBlue">***2021 Yahoo! JAPAN***</font>
- [カンムを支える技術 ~機械学習編~](https://tech.kanmu.co.jp/entry/2021/06/11/120953) - <font color="DodgerBlue">***2021 Kanmu***</font>
- [BERTを使ったMLバッチ処理実サービスのアーキテクチャとMLOpsの取り組み](https://tech.stockmark.co.jp/blog/mlops/) - <font color="DodgerBlue">***2020 Stockmark***</font>
- [Kubernetesを利用したコンテナベース機械学習基盤の構築](https://analytics.livesense.co.jp/entry/2018/01/18/090000) - <font color="DodgerBlue">***2018 Livesense***</font>

### プレゼンテーション
- [JX通信社における実践的MLOps](https://speakerdeck.com/fwang/jxtong-xin-she-niokerushi-jian-de-mlops) - <font color="DodgerBlue">***2021 JX Press***</font>
- [少人数PJにおけるMLOps事例](https://speakerdeck.com/s2p/shao-ren-shu-pjniokeru-mlopsshi-li) - <font color="DodgerBlue">***2021 Nikkei***</font>
- [MLflowとONNXで実現するクラウドネイティブなMLOps](https://speakerdeck.com/konabuta/mlflow-to-onnx-deshi-xian-surukuraudoneiteibuna-mlops) - <font color="DodgerBlue">***2021 Microsoft***</font>
- [ニュース配信におけるMLOps・分析基盤の事例紹介](https://speakerdeck.com/sansandsoc/a-case-study-of-mlops-and-analysis-infrastructure-on-news-delivery-system) - <font color="DodgerBlue">***2021 Sansan***</font>
- [GOの機械学習システムを支えるMLOps事例紹介](https://www.slideshare.net/takashisuzuki503/gomlops) - <font color="DodgerBlue">***2021 Mobility Technologies***</font>
    - [同上 - Google Developers ML Summit](https://lp.cloudplatformonline.com/rs/808-GJW-314/images/ML_Summit_D2-Session09.pdf)
- [サイバーエージェントにおけるMLOpsに関する取り組み](https://speakerdeck.com/cyberagentdevelopers/saibaezientoniokerumlopsniguan-suruqu-rizu-mi-ca-base-next) - <font color="DodgerBlue">***2021 CyberAgent***</font>
- [リーガルテックの機械学習基盤を支えるクラウドネイティブ技術の実践](https://speakerdeck.com/rupyjp/cndt2020-rigarutetukufalseji-jie-xue-xi-ji-pan-wozhi-erukuraudoneiteibuji-shu-falseshi-jian) - <font color="DodgerBlue">***2020 LegalForce***</font>
- [MOVの機械学習システムを支えるMLOps実践](https://speakerdeck.com/2kyym/movfalseji-jie-xue-xi-sisutemuwozhi-erumlopsshi-jian) - <font color="DodgerBlue">***2020 Mobility Technologies***</font>
- [クックパッドでの機械学習開発フロー](https://speakerdeck.com/studio_graph/ml-ops-in-cookpad) - <font color="DodgerBlue">***2019 Cookpad***</font>
- [マイクロチームでの機械学習PoC](https://speakerdeck.com/yurfuwa/shibuyasynapse-number-4) - <font color="DodgerBlue">***2018 DeNA***</font>
- [Wantedlyの機械学習プロダクト開発を支える機械学習基盤](https://speakerdeck.com/south37/number-rejectcon2018) - <font color="DodgerBlue">***2018 Wantedly***</font>
- [FreakOutにおけるAWS上での機械学習活用事例](https://speakerdeck.com/shotarok/freakout-aws-summit-tokyo-2018) - <font color="DodgerBlue">***2018 FreakOut***</font>
- [クックパッドの機械学習基盤 2018](https://speakerdeck.com/ayemos/machine-learning-platform-at-cookpad-2018) - <font color="DodgerBlue">***2018 Cookpad***</font>

## Feature Store
### ブログ記事
- [Vertex Feature Storeの機械学習システムへの導入](https://techblog.zozo.com/entry/vertex-feature-store-impl) - <font color="DodgerBlue">***2022 ZOZO***</font>
- [【書き起こし】Vertex PipelinesとFeature Storeを活用した不正防止システム](https://engineering.mercari.com/blog/entry/20210928-mtf2021-day3-1/) - <font color="DodgerBlue">***2021 Merpay***</font>

### プレゼンテーション
- [Vertex PipelinesとFeature Storeを活用した不正防止システム](https://speakerdeck.com/mercari/using-feature-store-and-vertex-pipelines-in-fraud-prevention-system) - <font color="DodgerBlue">***2021 Merpay***</font>

## 実験管理
### ブログ記事
- [SageMaker Experimentsによる実験管理とQuickSightを使ったその可視化](https://moneyforward.com/engineers_blog/2021/08/20/sagemaker-experiments/) - <font color="DodgerBlue">***2021 Money Forward***</font>
- [MLflowで実験管理入門](https://future-architect.github.io/articles/20200626/) - <font color="DodgerBlue">***2020 Future***</font>
- [小さく始めて大きく育てるMLOps2020](https://cyberagent.ai/blog/research/12898/) - <font color="DodgerBlue">***2020 CyberAgent***</font>

### プレゼンテーション
- [Data Version Controlによる実験管理の実務での適用事例](https://speakerdeck.com/sansandsoc/an-experiment-management-example-by-data-version-control) - <font color="DodgerBlue">***2021 Sansan***</font>
- [ABEJA PlatformでのMLOps](https://speakerdeck.com/ysku/abeja-platform-defalse-mlops-linexabeja-mlops-study-at-fukuoka) - <font color="DodgerBlue">***2019 ABEJA***</font>

## パイプライン
### ブログ記事

- [MLOps導入でAmazon SageMaker PipelineによりMLワークフロー構築の話](https://techblog.stanby.co.jp/entry/mlops) - <font color="DodgerBlue">***2022 Stanby***</font>
- [SageMakerとStep Functionsを用いた機械学習パイプラインで構築した検閲システム（後編）](https://tech.connehito.com/entry/2022/03/28/190436) - <font color="DodgerBlue">***2022 Connehito***</font>
- [SageMakerとStep Functionsを用いた機械学習パイプラインで構築した検閲システム（前編）](https://tech.connehito.com/entry/2022/03/24/173719) - <font color="DodgerBlue">***2022 Connehito***</font>
- [AI Platform Pipelines (Kubeflow Pipelines)による機械学習パイプラインの構築と本番導入](https://techblog.zozo.com/entry/aip-pipelines-impl) - <font color="DodgerBlue">***2020 ZOZO***</font>

### プレゼンテーション
- [Google Cloud BuildとAI Platformではじめる軽量MLOps pipelineとAlphaSQL](https://speakerdeck.com/jdsc/google-cloud-build-toai-platformdehazimeruqing-liang-mlops-pipelinetoalphasql) - <font color="DodgerBlue">***2021 JDSC***</font>
- [DVCを活用した機械学習パイプライン開発の高速化](https://speakerdeck.com/unblee/using-dvc-to-accelerate-machine-learning-pipeline-development) - <font color="DodgerBlue">***2021 Wantedly***</font>

## CI/CD (Continuous Integration and Delivery)
### ブログ記事
- [AI Platform Pipelinesの機械学習基盤への導入](https://developers.microad.co.jp/entry/2021/05/17/063000) - <font color="DodgerBlue">***2021 Micro Ad***</font>

### プレゼンテーション
- [KaggleライクなCI環境を構築した話](https://speakerdeck.com/nokoxxx1212/kaggleraikunacihuan-jing-wogou-zhu-sitahua) - <font color="DodgerBlue">***2021 Future***</font>
- [MLOpsを実現するSRE激闘の歴史](https://speakerdeck.com/kenta_sato3/mlopswoshi-xian-surusreji-dou-falseli-shi) - <font color="DodgerBlue">***2020 Stockmark***</font>

## CT (Continuous Training)
### ブログ記事
- [hoge]()

### プレゼンテーション
- [Polyaxon + Kubeflowを利用した効率的な継続的モデルインテグレーション](https://speakerdeck.com/shotarok/continuous-ml-model-integration-with-polyaxon-and-kubefolow-pipelines) - <font color="DodgerBlue">***2021 Mercari***</font>
- [実践Continuous Training](https://speakerdeck.com/htshtsyk/shi-jian-continuous-training-di-6hui-mlopsmian-qiang-hui) - <font color="DodgerBlue">***2021 Alpha***</font>

## モニタリング
### ブログ記事
- [MLOpsを支えるヤフー独自のモデルモニタリングサービス](https://techblog.yahoo.co.jp/entry/2022013130257343/) - <font color="DodgerBlue">***2022 Yahoo! JAPAN***</font>

### プレゼンテーション
- [継続的なモデルモニタリングを実現するKubernetes Operator](https://www.slideshare.net/techblogyahoo/kubernetes-operator-251612755) - <font color="DodgerBlue">***2022 Yahoo! JAPAN***</font>
- [Lupus - A Monitoring System for Accelerating MLOps](https://speakerdeck.com/line_devday2021/lupus-a-monitoring-system-for-accelerating-mlops) - <font color="DodgerBlue">***2021 LINE***</font>
- [Building LINE Pay Monitoring System and Anomaly Log Detection System Using ML](https://speakerdeck.com/line_devday2021/building-line-pay-monitoring-system-and-anomaly-log-detection-system-using-ml) - <font color="DodgerBlue">***2021 LINE***</font>
- [ZOZOのMLOpsチームにおける監視への取り組み](https://speakerdeck.com/inductor/observability-in-10-mins-at-zozo-mlops) - <font color="DodgerBlue">***2020 ZOZO***</font>

## サービング
### ブログ記事
- [How to make GPU inference environment of image category classification production-ready with EKS/Kubernetes](https://medium.com/eureka-engineering/how-to-make-gpu-inference-environment-of-image-category-classification-production-ready-with-88922fb09401) - <font color="DodgerBlue">***2021 Eureka***</font>
- [ヤフーの広告配信で機械学習の改善サイクルを高速化した話 〜 TensorFlow Serving導入](https://techblog.yahoo.co.jp/entry/2020101930034463/) - <font color="DodgerBlue">***2020 Yahoo! JAPAN***</font>

### プレゼンテーション
- [hoge]()

## Others
### ブログ記事
- [モデリング施策を高速・安全に回せる、MLOpsの仕組みづくり](https://techblog.yahoo.co.jp/entry/2021110830236406/) - <font color="DodgerBlue">***2021 Yahoo! JAPAN***</font>
- [AWSを活用した機械翻訳のためのGPU並列処理環境の構築](https://tech.stockmark.co.jp/blog/gpu_translate/) - <font color="DodgerBlue">***2021 Stockmark***</font>
- [KubeflowによるMLOps基盤構築から得られた知見と課題](https://techblog.zozo.com/entry/mlops-platform-kubeflow) - <font color="DodgerBlue">***2021 ZOZO***</font>
- [新卒がMLOpsに挑戦していく話](https://developers.microad.co.jp/entry/2020/03/23/120000) - <font color="DodgerBlue">***2020 Micro Ad***</font>

### プレゼンテーション
- [モバイル向け機械学習モデル管理基盤](https://speakerdeck.com/yujioshima/mlse-mobairuxiang-keji-jie-xue-xi-moderuguan-li-ji-pan) - <font color="DodgerBlue">***2020 Mercari***</font>
- [異音検知プラットフォーム開発におけるMLOpsの実際と考察](https://www.slideshare.net/ShotaSaitoh/mlops-3-mlops) - <font color="DodgerBlue">***2020 Hmcomm***</font>
- [ZOZO MLOpsのチームリーディングとSRE(Engineering)](https://docs.google.com/presentation/d/1zEkR9Dm_epg7fxOCFE-asBsUlHDozwObsBEGAILiqic/edit#slide=id.p1) - <font color="DodgerBlue">***2020 ZOZO***</font>

<a id="mlops-projects"></a>

# MLOps projects & wiki
- [Awesome MLOps](https://github.com/visenger/awesome-mlops)
- [MLOps.toys](https://mlops.toys/)
- [Made With ML](https://madewithml.com/)
- [Feature Stores for ML](https://www.featurestore.org/)
- [MLOps Wiki](https://censius.ai/wiki)

<a id="study"></a>

# 勉強会
- [connpass - MLOps](https://mlops.connpass.com/)
- [connpass - Machine Learning Casual Talks](https://mlct.connpass.com/)

<a id="conferences"></a>

# Conferences
- [MLSys](https://mlsys.org/)
- [OpML](https://www.usenix.org/conferences/byname/1027)
- [TWIMLcon](https://twimlcon.com/)
- [MLOps World](https://mlopsworld.com/)
- [MLOps Summit](https://www.re-work.co/summits/mlops-summit-2022)
- [Data Engineering & MLOps](https://odsc.com/boston/mlops/)

<a id="books"></a>

# 書籍
- [AIエンジニアのための機械学習システムデザインパターン](https://www.shoeisha.co.jp/book/detail/9784798169453)
- [機械学習デザインパターン - データ準備、モデル構築、MLOpsの実践上の問題と解決](https://www.oreilly.co.jp/books/9784873119564/)
- [入門 機械学習パイプライン - TensorFlowで学ぶワークフローの自動化](https://www.oreilly.co.jp/books/9784873119519/)

<a id="references"></a>

# References
- [ApplyingML](https://applyingml.com/)
- [ml-system-design-pattern](https://mercari.github.io/ml-system-design-pattern/README_ja.html)
