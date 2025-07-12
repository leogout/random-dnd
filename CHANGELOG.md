# Changelog

## [0.5.0](https://github.com/leogout/random-dnd/compare/v0.4.0...v0.5.0) (2025-07-12)


### Features

* added staging and separated prod in another values file ([55bebfe](https://github.com/leogout/random-dnd/commit/55bebfeb83a54503bae02c8a909e92216716c5da))
* deploying a prod and a staging app ([b621c6c](https://github.com/leogout/random-dnd/commit/b621c6c0345b349c4e4bbb7008136daaadd487ee))
* deploying a prod and a staging app ([3ffc620](https://github.com/leogout/random-dnd/commit/3ffc620cb367eb3198914c26f71d3da5fc7ce1cf))


### Bug Fixes

* added user and database to postgres values ([e026f23](https://github.com/leogout/random-dnd/commit/e026f231b4edc1d60e1dcb30e4a8b0e9a18f42b6))
* added user password to postgres config ([87890d2](https://github.com/leogout/random-dnd/commit/87890d237be5e9be29672e614a5d932e8b5473ae))
* deploying secrets on the correct environments ([c01d36f](https://github.com/leogout/random-dnd/commit/c01d36f3f2f7f0ebbac5db3d7547f482bec1b9ff))
* force-ssl-redirect must be a string in values.yml ([3862600](https://github.com/leogout/random-dnd/commit/3862600c0d47694632f15f7f3bd81b0be35599ff))
* putting back postgres-password ([35fb37d](https://github.com/leogout/random-dnd/commit/35fb37d60f12d6449dfac9ade6bd0fa0a3e55b1a))
* regenerated llm-credentials ([8d45f16](https://github.com/leogout/random-dnd/commit/8d45f1606c90502e02d7fd5a6a10f4645005520b))
* removed redundant staging in appName ([053a209](https://github.com/leogout/random-dnd/commit/053a20919fdfc4fb334995b24997823975a2c5fc))
* removed the environment from the helm fullname ([1126ebf](https://github.com/leogout/random-dnd/commit/1126ebf41719c1df9f2f324019e19432c4483082))
* removed the environment repeating in _helpers.tpl ([68de43e](https://github.com/leogout/random-dnd/commit/68de43efa112aa13b8858258d8d48dc71e509315))
* removing configmap ([74c1731](https://github.com/leogout/random-dnd/commit/74c1731b7baf6048d80ac3732deda4d31e2a817d))
* renamed db-credentials to llm-credentials ([111dd8c](https://github.com/leogout/random-dnd/commit/111dd8c319f1baf9979837ebc1064a6bb5abb9cb))
* renamed llm-credentials to llm-credentials-staging ([b1036d7](https://github.com/leogout/random-dnd/commit/b1036d7b5777cb9c0635ed66b390c12f8a38752e))
* repeating environment name in staging configuration ([94b9929](https://github.com/leogout/random-dnd/commit/94b99295d57dc9cf77cd1aa3e675f5ea054dd138))
* setting secrets in the random-jdr namespace ([4426fc8](https://github.com/leogout/random-dnd/commit/4426fc89af3ba1af708f927158bcb0ec6462018e))
* updated postgresql database url ([892e584](https://github.com/leogout/random-dnd/commit/892e584c462ff6a8be3acca9287ddc6cf277b4c4))
* using correct env vars names in pydantic settings ([6987161](https://github.com/leogout/random-dnd/commit/6987161e5aabd3c4f776bbb57466406489be5fdf))
* using staging namespace for llm secret ([15db5a9](https://github.com/leogout/random-dnd/commit/15db5a907180724756bbf84787d60cd28055141b))
* using the correct environment path in secrets ([9b7f7cf](https://github.com/leogout/random-dnd/commit/9b7f7cfcf1c9c9789b5f8b878455a2d9192dddfc))

## [0.4.0](https://github.com/leogout/random-dnd/compare/v0.3.4...v0.4.0) (2025-06-30)


### Features

* **db:** added postgresql database configuration ([6180f53](https://github.com/leogout/random-dnd/commit/6180f5356c83ed89bf77acf7771aae77b0554a6d))
* **db:** added postgresql database configuration ([c56a230](https://github.com/leogout/random-dnd/commit/c56a2306fbfb30977015472df63367a4a73c551b))

## [0.3.4](https://github.com/leogout/random-dnd/compare/v0.3.3...v0.3.4) (2025-06-29)


### Bug Fixes

* **release-please:** added PAT to release-please action ([4c131d4](https://github.com/leogout/random-dnd/commit/4c131d44e650ce4ed11eb53fcad87209ce755bbf))

## [0.3.2](https://github.com/leogout/random-dnd/compare/v0.3.1...v0.3.2) (2025-06-29)


### Bug Fixes

* **cd:** watching for all kind of tags in cd ([d3a4631](https://github.com/leogout/random-dnd/commit/d3a463195439789b459548e6b5465277468e60ee))
* **cd:** watching for all kind of tags in cd ([2112a22](https://github.com/leogout/random-dnd/commit/2112a22a551777acb8e946ea450760d98edce90c))

## [0.3.1](https://github.com/leogout/random-dnd/compare/v0.3.0...v0.3.1) (2025-06-29)


### Bug Fixes

* **cd:** forcing the tags to build new docker images ([5580dc2](https://github.com/leogout/random-dnd/commit/5580dc24a8e43b4ab92a463392636a2f4edd01e6))
* **cd:** forcing the tags to build new docker images ([d01f061](https://github.com/leogout/random-dnd/commit/d01f0619b00b3e7facdd3c96e799cb362d748980))

## [0.3.0](https://github.com/leogout/random-dnd/compare/v0.2.0...v0.3.0) (2025-06-29)


### Features

* **cd:** cd now triggers to build images if a tag is created ([a7cf9a2](https://github.com/leogout/random-dnd/commit/a7cf9a255396acddf7e26ec86d11d646395b19d9))

## [0.2.0](https://github.com/leogout/random-dnd/compare/v0.1.0...v0.2.0) (2025-06-29)


### Features

* **helm:** add postgresql dependency ([aea8201](https://github.com/leogout/random-dnd/commit/aea8201db8adedaec28fa2da3c3cca5f84760a9a))


### Bug Fixes

* **ci:** update values file to include default github default values ([bd10dac](https://github.com/leogout/random-dnd/commit/bd10dac3e6bce8a7122722348208728410bda48f))

## [0.1.0](https://github.com/leogout/random-dnd/compare/v0.0.1...v0.1.0) (2025-06-29)


### Features

* **ci:** add path filtering to CI/CD workflows ([732f2cd](https://github.com/leogout/random-dnd/commit/732f2cd5dbfb49694fa11eff7e5a19ecc6e6f2db))
* **ci:** added release-please ([c922d72](https://github.com/leogout/random-dnd/commit/c922d72e04c2deeffae0f639d2281c70f7e8e227))
* **ci:** added write permissions to the release-please action ([b39e9d9](https://github.com/leogout/random-dnd/commit/b39e9d9f56ca27e8f39903d43920a084785d7dd5))


### Bug Fixes

* **ci:** add permission to create issues with release-please ([e309204](https://github.com/leogout/random-dnd/commit/e3092048cae2aa18181cf7ce03da760041c0e44e))
* **ci:** fixing permissions and updating googleapi action ([9f0d503](https://github.com/leogout/random-dnd/commit/9f0d50382721055f708f089ae2260f81f0390a71))
