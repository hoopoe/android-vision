import urllib.request
import os


list = [
"https://pp.userapi.com/c621704/v621704504/4ce82/fpS1JSZc-48.jpg",
"https://pp.userapi.com/c621704/v621704504/4ce8c/vzhgqW18wDw.jpg",
"https://pp.userapi.com/c621704/v621704504/4ce96/bX60U6_2_iU.jpg",
"https://pp.userapi.com/c621704/v621704504/4cea0/1Z7DZLNigIk.jpg",
"https://pp.userapi.com/c621704/v621704504/4ceaa/YYP96q2WtDk.jpg",
"https://pp.userapi.com/c621704/v621704504/4cebe/nIw5XJekCDU.jpg",
"https://pp.userapi.com/c621704/v621704504/4cec8/BWRWTyIQPXk.jpg",
"https://pp.userapi.com/c621704/v621704504/4ced2/35E-iVORPGI.jpg",
"https://pp.userapi.com/c621704/v621704504/4cedc/qSmIZiTPjgg.jpg",
"https://pp.userapi.com/c621704/v621704504/4cee6/kzcRqozS-Kk.jpg",
"https://pp.userapi.com/c621704/v621704504/4cef0/aVVA_3y1x5c.jpg",
"https://pp.userapi.com/c621704/v621704504/4cefa/AIHAFDGAjBc.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf04/v4yIJ_yS4qo.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf0e/zOH067bOp7A.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf18/NE9dX3veUMw.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf22/01zESqB3vJk.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf2c/EmSRQ7-UJRE.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf36/_cLJrw-QTTg.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf40/ZJnhHEisKMA.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf4a/cEBoOoodPpQ.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf54/MpJG_E363h0.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf5e/qgiIqHiMrgk.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf68/tzRusEg2cYc.jpg",
"https://pp.userapi.com/c621704/v621704504/4cf9f/YnLebNg_2RY.jpg",
"https://pp.userapi.com/c621704/v621704504/4cfa9/zATPVrw69vQ.jpg",
"https://pp.userapi.com/c621704/v621704504/4cfb3/ohX5XnoIUsk.jpg",
"https://pp.userapi.com/c621704/v621704504/4cfbd/GQ0EZxtKgSw.jpg",
"https://pp.userapi.com/c621704/v621704504/4cfc7/DrrjhYUit1U.jpg",
"https://pp.userapi.com/c621704/v621704504/4cfd1/ouoLCezSZUw.jpg",
"https://pp.userapi.com/c621704/v621704504/4cfe2/_nUyiE-wrNg.jpg",
"https://pp.userapi.com/c621704/v621704504/4cfec/jPAfJBnVfzI.jpg",
"https://pp.userapi.com/c621704/v621704504/4cff6/PBWxpj0PJAk.jpg",
"https://pp.userapi.com/c621704/v621704504/4d000/Aq5uZKfcOwo.jpg",
"https://pp.userapi.com/c621704/v621704504/4d00a/0LmeGQCE6W4.jpg",
"https://pp.userapi.com/c621704/v621704504/4d014/rwuYi_Wjnz4.jpg",
"https://pp.userapi.com/c621704/v621704504/4d01e/cHuUlb5H48M.jpg",
"https://pp.userapi.com/c621704/v621704504/4d028/vdkdIoCtlIg.jpg",
"https://pp.userapi.com/c621704/v621704504/4d032/a-azUbDmd4E.jpg",
"https://pp.userapi.com/c621704/v621704504/4d03c/altBEeogIx0.jpg",
"https://pp.userapi.com/c621704/v621704504/4d046/fqx6x4xS1uY.jpg",
"https://pp.userapi.com/c621704/v621704504/4d050/ejo7M16ttxI.jpg",
"https://pp.userapi.com/c621704/v621704504/4d05a/IeXmpdvmmYE.jpg",
"https://pp.userapi.com/c621704/v621704504/4d064/M9fxdNFmNCs.jpg",
"https://pp.userapi.com/c621704/v621704504/4d06e/0cgpuKL176U.jpg",
"https://pp.userapi.com/c621704/v621704504/4d078/c2EjxMd4qE8.jpg",
"https://pp.userapi.com/c621704/v621704504/4d082/flGAuK3Wx6k.jpg",
"https://pp.userapi.com/c621704/v621704504/4d08c/eznbOB33aQc.jpg",
"https://pp.userapi.com/c621704/v621704504/4d096/FMtmbThENqw.jpg",
"https://pp.userapi.com/c621704/v621704504/4d0a0/I2Ob8Pcja6M.jpg",
"https://pp.userapi.com/c621704/v621704504/4d0ae/wFfDrDiEgzk.jpg",
"https://pp.userapi.com/c621704/v621704504/4d0b8/yuopZtC5TwM.jpg",
"https://pp.userapi.com/c621704/v621704504/4d0c2/fjjvHViVLHI.jpg",
"https://pp.userapi.com/c621704/v621704504/4d0cc/p3G86D0kaPM.jpg",
"https://pp.userapi.com/c621704/v621704504/4d0d6/UUzi8yZZo8o.jpg",
"https://pp.userapi.com/c621704/v621704504/4d0e0/6tA6BrzxxEM.jpg",
"https://pp.userapi.com/c621704/v621704504/4d0ea/TzL--_ylfkg.jpg",
"https://pp.userapi.com/c621704/v621704504/4d0f4/iy5myzbD0jY.jpg",
"https://pp.userapi.com/c621704/v621704504/4d0fe/9-0AzIwpG-M.jpg",
"https://pp.userapi.com/c621704/v621704504/4d108/bNkXECOxFCQ.jpg",
"https://pp.userapi.com/c621704/v621704504/4d112/SU8szYPr01U.jpg",
"https://pp.userapi.com/c621704/v621704504/4d11c/WnGKcBALd4k.jpg",
"https://pp.userapi.com/c621704/v621704504/4d126/2leeVsr_HXw.jpg",
"https://pp.userapi.com/c621704/v621704504/4d130/JhJlZckbBG4.jpg",
"https://pp.userapi.com/c621704/v621704504/4d13a/wI5VuZslIeo.jpg",
"https://pp.userapi.com/c621704/v621704504/4d144/TZo4Bn0ci6M.jpg",
"https://pp.userapi.com/c621704/v621704504/4d14e/uG9P6E4w2aw.jpg",
"https://pp.userapi.com/c621704/v621704504/4d158/9II6lMp8yEQ.jpg",
"https://pp.userapi.com/c621704/v621704504/4d162/1flBTO_duwk.jpg",
"https://pp.userapi.com/c621704/v621704504/4d16c/JwSmnjoYh5I.jpg",
"https://pp.userapi.com/c621704/v621704504/4d176/FWU-3VOAWOI.jpg",
"https://pp.userapi.com/c621704/v621704504/4d18a/LxTSGtOukE8.jpg",
"https://pp.userapi.com/c621704/v621704504/4d194/QiCL2iuJ4D8.jpg",
"https://pp.userapi.com/c621704/v621704504/4d19e/qDb3KlG2PDk.jpg",
"https://pp.userapi.com/c621704/v621704504/4d1a8/VLmEsPIeeKI.jpg",
"https://pp.userapi.com/c621704/v621704504/4d1b2/55tJwhE79yc.jpg",
"https://pp.userapi.com/c621704/v621704504/4d1bc/ic4dAEcjQ94.jpg",
"https://pp.userapi.com/c621704/v621704504/4d1da/RRPhTcZN8KA.jpg",
"https://pp.userapi.com/c621704/v621704504/4d1e4/wdlkBI9NkHk.jpg",
"https://pp.userapi.com/c621704/v621704504/4d1ee/GrPuqtvZohs.jpg",
"https://pp.userapi.com/c621704/v621704504/4d1f8/AFTu4npogc0.jpg",
"https://pp.userapi.com/c621704/v621704504/4d202/2yCeSes34Tw.jpg",
"https://pp.userapi.com/c621704/v621704504/4d20c/qGJqaJAqhmM.jpg",
"https://pp.userapi.com/c621704/v621704504/4d216/JEruzqYZyBc.jpg",
"https://pp.userapi.com/c621704/v621704504/4d220/cF7qxXtOVVM.jpg",
"https://pp.userapi.com/c621704/v621704504/4d22a/gSrKJxnXKWg.jpg",
"https://pp.userapi.com/c621704/v621704504/4d234/AyMwWzMnpXU.jpg",
"https://pp.userapi.com/c621704/v621704504/4d23e/GW93-bNtsw0.jpg",
"https://pp.userapi.com/c621704/v621704504/4d248/SYaqIxdi8gs.jpg",
"https://pp.userapi.com/c621704/v621704504/4d252/RaLD9QlksBk.jpg",
"https://pp.userapi.com/c621704/v621704504/4d25c/YtWNVePWgjg.jpg",
"https://pp.userapi.com/c621704/v621704504/4d266/mocbifadCDw.jpg",
"https://pp.userapi.com/c621704/v621704504/4d270/dX1ZfQHcCzM.jpg",
"https://pp.userapi.com/c621704/v621704504/4d27a/O8pF4E3aJ7g.jpg",
"https://pp.userapi.com/c621704/v621704504/4d284/leZgaXk9v7I.jpg",
"https://pp.userapi.com/c621704/v621704504/4d296/0GN6ivBTrLg.jpg",
"https://pp.userapi.com/c621704/v621704504/4d2a0/CWYYoDJq9YU.jpg",
"https://pp.userapi.com/c621704/v621704504/4d2aa/y1vLrcr4iDA.jpg",
"https://pp.userapi.com/c621704/v621704504/4d2b4/0UWZqU0loZM.jpg",
"https://pp.userapi.com/c621704/v621704504/4d2be/xdHXgfGEcaE.jpg",
"https://pp.userapi.com/c621704/v621704504/4d2c8/BJK22cxxunU.jpg",
"https://pp.userapi.com/c621704/v621704504/4d2d2/fQNE93r-GNU.jpg",
"https://pp.userapi.com/c621704/v621704504/4d2dc/8ORUkTA9qeU.jpg",
"https://pp.userapi.com/c621704/v621704504/4d2e6/0SbySkRsI2A.jpg",
"https://pp.userapi.com/c621704/v621704504/4d2f0/T0rKR-_YEtw.jpg",
"https://pp.userapi.com/c621704/v621704504/4d2fa/OgSfIRtVZiY.jpg",
"https://pp.userapi.com/c621704/v621704504/4d304/stoIpYRslNo.jpg",
"https://pp.userapi.com/c621704/v621704504/4d30e/kyQuiBKje_4.jpg",
"https://pp.userapi.com/c621704/v621704504/4d318/BSfWRPCgj0A.jpg",
"https://pp.userapi.com/c621704/v621704504/4d322/RTImQxFAjjg.jpg",
"https://pp.userapi.com/c621704/v621704504/4d32c/ddhG8K6LX-I.jpg",
"https://pp.userapi.com/c621704/v621704504/4d336/Xq123Ug6dR4.jpg",
"https://pp.userapi.com/c621704/v621704504/4d340/KxZ4bs7jPUg.jpg",
"https://pp.userapi.com/c621704/v621704504/4d34a/PQIW4z2HFpU.jpg",
"https://pp.userapi.com/c621704/v621704504/4d354/lY4PKjbZNYs.jpg",
"https://pp.userapi.com/c621704/v621704504/4d35e/20NNJHLhuSs.jpg",
"https://pp.userapi.com/c621704/v621704504/4d368/rfrnHCBPp_w.jpg",
"https://pp.userapi.com/c621704/v621704504/4d372/xbU_7GHkfws.jpg",
"https://pp.userapi.com/c621704/v621704504/4d37c/HwZArmCyUVM.jpg",
"https://pp.userapi.com/c621704/v621704504/4d386/Tl_fbcAkpPw.jpg",
"https://pp.userapi.com/c621704/v621704504/4d390/yZT8n9uhmGI.jpg",
"https://pp.userapi.com/c621704/v621704504/4d39a/nbz3DL-ERsk.jpg",
"https://pp.userapi.com/c621704/v621704504/4d3a4/Xye8bkpEq84.jpg",
"https://pp.userapi.com/c621704/v621704504/4d3ae/ThrNoLYvTk8.jpg",
"https://pp.userapi.com/c621704/v621704504/4d3b8/NGruer4hQvM.jpg",
"https://pp.userapi.com/c621704/v621704504/4d3c2/7k0kg-MhIV8.jpg",
"https://pp.userapi.com/c621704/v621704504/4d3cc/28LZ7EENwbk.jpg",
"https://pp.userapi.com/c621704/v621704504/4d3d6/kb4OXE6A88Y.jpg",
"https://pp.userapi.com/c621704/v621704504/4d3e0/rMMlovvkAnQ.jpg",
"https://pp.userapi.com/c621704/v621704504/4d3ea/2h8ebgZOcJg.jpg",
"https://pp.userapi.com/c621704/v621704504/4d3f4/xh7jSj1bD80.jpg",
"https://pp.userapi.com/c621704/v621704504/4d3fe/zMv1eptM9Qw.jpg",
"https://pp.userapi.com/c621704/v621704504/4d408/WEiOM_6w4GQ.jpg",
"https://pp.userapi.com/c621704/v621704719/5058c/pUSyE7kONAg.jpg",
"https://pp.userapi.com/c621704/v621704719/50596/p6uxx69o27g.jpg",
"https://pp.userapi.com/c621704/v621704719/505a0/YH4vTlOVvkg.jpg",
"https://pp.userapi.com/c621704/v621704719/505aa/jlEBZtVV28U.jpg",
"https://pp.userapi.com/c621704/v621704719/505b4/TqdNe4Y9UqM.jpg",
"https://pp.userapi.com/c621704/v621704719/505be/GWVQpIXaCZA.jpg",
"https://pp.userapi.com/c621704/v621704719/505c8/fJx7p8EN0Ko.jpg",
"https://pp.userapi.com/c621704/v621704719/505d2/P_AeuTDmUvw.jpg",
"https://pp.userapi.com/c621704/v621704719/505dc/NEKa0d2thO0.jpg",
"https://pp.userapi.com/c621704/v621704719/505e6/rGtZ8o4fLjw.jpg",
"https://pp.userapi.com/c621704/v621704719/505f0/oCherl2CzZA.jpg",
"https://pp.userapi.com/c621704/v621704719/505fa/uBU0zjcLEUY.jpg",
"https://pp.userapi.com/c621704/v621704719/50604/EN7ETxod-mo.jpg",
"https://pp.userapi.com/c621704/v621704719/50618/8I4gWJGViH8.jpg",
"https://pp.userapi.com/c621704/v621704719/50622/KP1s4IPbd5c.jpg",
"https://pp.userapi.com/c621704/v621704719/5062c/0_A0L4_dIr8.jpg",
"https://pp.userapi.com/c621704/v621704719/50636/_WmokgPLCF0.jpg",
"https://pp.userapi.com/c621704/v621704719/50640/fELh4szJhSE.jpg",
"https://pp.userapi.com/c621704/v621704719/5064a/C0qM4gyB9RA.jpg",
"https://pp.userapi.com/c621704/v621704719/50654/FbR9zxO68Hg.jpg",
"https://pp.userapi.com/c621704/v621704719/5065e/mMAOpZIVSvk.jpg",
"https://pp.userapi.com/c621704/v621704719/50668/k9glmMS_kV8.jpg",
"https://pp.userapi.com/c621704/v621704719/50672/dF2PMREHloI.jpg",
"https://pp.userapi.com/c621704/v621704719/5067c/Wc8bR27-G3Q.jpg",
"https://pp.userapi.com/c621704/v621704719/50686/Rpg0eG4YAC8.jpg",
"https://pp.userapi.com/c621704/v621704719/50690/YjeoPzc24_w.jpg",
"https://pp.userapi.com/c621704/v621704719/5069a/yiIQ3BCBrl0.jpg",
"https://pp.userapi.com/c621704/v621704719/506a4/vqncjVfhQhg.jpg",
"https://pp.userapi.com/c621704/v621704719/506ae/NePxdhAk5No.jpg",
"https://pp.userapi.com/c621704/v621704719/506b8/vMqp6PMSjPA.jpg",
"https://pp.userapi.com/c621704/v621704719/506c2/tEPyICCu6g4.jpg",
"https://pp.userapi.com/c621704/v621704719/506cc/NeuLgC9OmFU.jpg",
"https://pp.userapi.com/c621704/v621704719/506d6/AAfGOjfU5Qo.jpg",
"https://pp.userapi.com/c621704/v621704719/506e0/RuvvvPDpMTI.jpg",
"https://pp.userapi.com/c621704/v621704719/506ea/so1Bx3ceGOw.jpg",
"https://pp.userapi.com/c621704/v621704719/506f4/taOF-uG1eN4.jpg",
"https://pp.userapi.com/c621704/v621704719/506fe/ihffGhcluYk.jpg",
"https://pp.userapi.com/c621704/v621704719/50708/4UpHTl3HpWI.jpg",
"https://pp.userapi.com/c621704/v621704719/50712/E_Vhqkp56vs.jpg",
"https://pp.userapi.com/c621704/v621704719/50720/wXOQ9EnPlN0.jpg",
"https://pp.userapi.com/c621704/v621704719/5072a/fBkor7OKhn0.jpg",
"https://pp.userapi.com/c621704/v621704719/50734/M0rJGT6yHwA.jpg",
"https://pp.userapi.com/c621704/v621704719/5073e/3u_FWkRrnbw.jpg",
"https://pp.userapi.com/c621704/v621704719/50748/uS_7cYau8dI.jpg",
"https://pp.userapi.com/c621704/v621704719/50752/puyQDdAU-eE.jpg",
"https://pp.userapi.com/c621704/v621704719/5075c/3lBbT_RLLns.jpg",
"https://pp.userapi.com/c621704/v621704719/50766/0cNdBZgmFEE.jpg",
"https://pp.userapi.com/c621704/v621704719/50770/zB80gaXTAXs.jpg",
"https://pp.userapi.com/c621704/v621704719/5077a/c8MYOsZY6L0.jpg",
"https://pp.userapi.com/c621704/v621704719/50784/jUeFoXYkdV4.jpg",
"https://pp.userapi.com/c621704/v621704719/5078e/7sRUxn8n4UA.jpg",
"https://pp.userapi.com/c621704/v621704719/50798/8A0UCA1N8sI.jpg",
"https://pp.userapi.com/c621704/v621704719/507a2/R4WKvhV4nJk.jpg",
"https://pp.userapi.com/c621704/v621704719/507ac/DM4CtQgNINw.jpg",
"https://pp.userapi.com/c621704/v621704719/507b6/UVFBLBP3jIg.jpg",
"https://pp.userapi.com/c621704/v621704719/507c0/xVymX2-u4lY.jpg",
"https://pp.userapi.com/c621704/v621704719/507ca/cgpBELtCaoM.jpg",
"https://pp.userapi.com/c621704/v621704719/507d4/h0de7izYSQ8.jpg",
"https://pp.userapi.com/c621704/v621704719/507de/88L9B_Lx5wc.jpg",
"https://pp.userapi.com/c621704/v621704719/507e8/99C99EQW3iw.jpg",
"https://pp.userapi.com/c621704/v621704719/507f2/ygk2oMY5-lA.jpg",
"https://pp.userapi.com/c621704/v621704719/507fc/_0KIuQPHBz4.jpg",
"https://pp.userapi.com/c621704/v621704719/50806/GQ2uW0zPDmE.jpg",
"https://pp.userapi.com/c841524/v841524719/4b528/onOzi3HTEiA.jpg",
"https://pp.userapi.com/c841524/v841524719/4b532/8aoxL6ukmYY.jpg",
"https://pp.userapi.com/c841524/v841524719/4b53c/byrAYzljMnk.jpg",
"https://pp.userapi.com/c841524/v841524719/4b546/LfXTv-4T21M.jpg",
"https://pp.userapi.com/c841524/v841524719/4b550/HlNi7BlXefE.jpg",
"https://pp.userapi.com/c841524/v841524719/4b55a/W8G_ykqVlZo.jpg",
"https://pp.userapi.com/c841524/v841524719/4b564/G3fFFShao24.jpg",
"https://pp.userapi.com/c841524/v841524719/4b56e/lvLe0-opK0c.jpg",
"https://pp.userapi.com/c841524/v841524719/4b578/cEA_mC777sM.jpg",
"https://pp.userapi.com/c841524/v841524719/4b582/KqHef--YJTk.jpg",
"https://pp.userapi.com/c841524/v841524719/4b593/dwUbdXipLbE.jpg",
"https://pp.userapi.com/c841524/v841524719/4b59d/VoGoVJHQaww.jpg",
"https://pp.userapi.com/c841524/v841524719/4b5a7/SjWPZIy_awA.jpg",
"https://pp.userapi.com/c841524/v841524719/4b5b1/GA_TR7JOrTE.jpg",
"https://pp.userapi.com/c841524/v841524719/4b5bb/X5NfNoAZUig.jpg",
"https://pp.userapi.com/c841524/v841524719/4b5c5/XHlC6UblhoA.jpg",
"https://pp.userapi.com/c841524/v841524719/4b5cf/jaVG90hVlAo.jpg",
"https://pp.userapi.com/c841524/v841524719/4b5d9/Vu1usiWD-co.jpg",
"https://pp.userapi.com/c841524/v841524719/4b5e3/N81B6lpBiAQ.jpg",
"https://pp.userapi.com/c841524/v841524719/4b5ed/uC7BYhkegUI.jpg",
"https://pp.userapi.com/c841524/v841524719/4b5f7/cRnXqDZL_GU.jpg",
"https://pp.userapi.com/c841524/v841524719/4b601/LN6I1LX9Jqg.jpg",
"https://pp.userapi.com/c841524/v841524719/4b614/xqGxXLyhWwg.jpg",
"https://pp.userapi.com/c841524/v841524719/4b61e/fIOYLtni3Bs.jpg",
"https://pp.userapi.com/c841524/v841524719/4b628/SM_gZ6DKRxo.jpg",
"https://pp.userapi.com/c841524/v841524719/4b646/vSuAMIXUMIU.jpg",
"https://pp.userapi.com/c841524/v841524719/4b650/fUPcXM8nKKo.jpg",
"https://pp.userapi.com/c841524/v841524719/4b65a/tuU--ViRHyM.jpg",
"https://pp.userapi.com/c841524/v841524719/4b664/0w9enMucyhs.jpg",
"https://pp.userapi.com/c841524/v841524719/4b66e/s3k210mKw1E.jpg",
"https://pp.userapi.com/c841524/v841524719/4b678/K1NbBGpmVHA.jpg",
"https://pp.userapi.com/c841524/v841524719/4b682/ShnXOHpctCc.jpg",
"https://pp.userapi.com/c841524/v841524719/4b68c/bH46bat20sc.jpg",
"https://pp.userapi.com/c841524/v841524719/4b696/cDI7GvHTreo.jpg",
"https://pp.userapi.com/c841524/v841524719/4b6a0/fGgvrYqjP14.jpg",
"https://pp.userapi.com/c841524/v841524719/4b6aa/gg8cEoRQ4ec.jpg",
"https://pp.userapi.com/c841524/v841524719/4b6b4/EPR1YokoR5g.jpg",
"https://pp.userapi.com/c841524/v841524719/4b6be/YAzK8JCJG64.jpg",
"https://pp.userapi.com/c841524/v841524719/4b6c8/yfKvvOZ6N4s.jpg",
"https://pp.userapi.com/c841524/v841524719/4b6d2/-2seX9a2kUg.jpg",
"https://pp.userapi.com/c841524/v841524719/4b6dc/wocRbmw8hkE.jpg",
"https://pp.userapi.com/c841524/v841524719/4b6ef/UPfdO8OrTPM.jpg",
"https://pp.userapi.com/c841524/v841524719/4b6f9/Mx2EwC_KeQU.jpg",
"https://pp.userapi.com/c841524/v841524719/4b703/oRGV_smM9vc.jpg",
"https://pp.userapi.com/c841524/v841524719/4b70d/-VfogPmf9mQ.jpg",
"https://pp.userapi.com/c841524/v841524719/4b717/JEKcqqvIljs.jpg"

]

# list = [
# "https://pp.userapi.com/c638927/v638927925/50885/N0JJNAR7jtA.jpg",
# "https://pp.userapi.com/c638927/v638927925/5088f/3EewXOJorxE.jpg",
# "https://pp.userapi.com/c638927/v638927925/50899/4puLr2imYoY.jpg",
# "https://pp.userapi.com/c638927/v638927925/508a3/puF5bOwKllM.jpg",
# "https://pp.userapi.com/c638927/v638927925/508ad/y-lKC5eqBSQ.jpg",
# "https://pp.userapi.com/c638927/v638927925/508b7/O7DgiFKcOHg.jpg",
# "https://pp.userapi.com/c638927/v638927925/508c1/dGcCTMyU__g.jpg",
# "https://pp.userapi.com/c638927/v638927925/508cb/ZL8LFgbEajk.jpg",
# "https://pp.userapi.com/c638927/v638927925/508d5/2-02Xcmg4Xs.jpg",
# "https://pp.userapi.com/c638927/v638927925/508df/NTUMe-zyxns.jpg",
# "https://pp.userapi.com/c638927/v638927925/508e9/kYCzT3UN4Ck.jpg",
# "https://pp.userapi.com/c638927/v638927925/508f3/8rPboGUNwbk.jpg",
# "https://pp.userapi.com/c638927/v638927925/508fd/PtGGodc2rPE.jpg",
# "https://pp.userapi.com/c638927/v638927925/50907/d40DeV_XPn0.jpg",
# "https://pp.userapi.com/c638927/v638927925/50911/j9X5hTmWt-g.jpg",
# "https://pp.userapi.com/c638927/v638927925/5091b/nprlaPpJhT8.jpg",
# "https://pp.userapi.com/c638927/v638927925/50925/SRS4kDT5ljI.jpg",
# "https://pp.userapi.com/c638927/v638927925/5092f/e1-kfHJo7Nw.jpg",
# "https://pp.userapi.com/c638927/v638927925/50939/0y_FxNqnKWk.jpg",
# "https://pp.userapi.com/c638927/v638927925/50943/ill7fB0voAw.jpg",
# "https://pp.userapi.com/c638927/v638927925/5094d/6xsDmrEL6Y4.jpg",
# "https://pp.userapi.com/c638927/v638927925/50957/y6vKT14LywI.jpg",
# "https://pp.userapi.com/c638927/v638927925/50961/hy5h2RO77g0.jpg",
# "https://pp.userapi.com/c638927/v638927925/5096b/XRngeYleSM0.jpg",
# "https://pp.userapi.com/c638927/v638927925/50975/1EqsQMYA3yk.jpg",
# "https://pp.userapi.com/c638927/v638927925/5097f/1oaF-1jd3J0.jpg",
# "https://pp.userapi.com/c638927/v638927925/50989/IymvqxrKXT4.jpg",
# "https://pp.userapi.com/c638927/v638927925/5099d/IkaIIozYxKQ.jpg",
# "https://pp.userapi.com/c638927/v638927925/509a7/s8RooTEWIiU.jpg",
# "https://pp.userapi.com/c638927/v638927925/509b1/W6HYyZO76LY.jpg",
# "https://pp.userapi.com/c638927/v638927925/509bb/6_uw_yEhmk8.jpg",
# "https://pp.userapi.com/c638927/v638927925/509c5/hpcKi8k-Kj4.jpg",
# "https://pp.userapi.com/c638927/v638927925/509cf/ulCsga5Em3Y.jpg",
# "https://pp.userapi.com/c638927/v638927925/509d9/M_aux4oxCHc.jpg",
# "https://pp.userapi.com/c638927/v638927925/509e3/N7gsB1AXGS0.jpg",
# "https://pp.userapi.com/c638927/v638927925/509ed/CALsF-NqZKw.jpg",
# "https://pp.userapi.com/c638927/v638927925/509f7/Wl2_z0Ec6R4.jpg",
# "https://pp.userapi.com/c638927/v638927925/50a0b/bCkNK7mg4zM.jpg",
# "https://pp.userapi.com/c638927/v638927925/50a6f/3gL6xPxcquY.jpg",
# "https://pp.userapi.com/c638927/v638927925/50a79/gH3L7F5X7JA.jpg",
# "https://pp.userapi.com/c638927/v638927925/50a83/_CjeH0YHVlQ.jpg",
# "https://pp.userapi.com/c638927/v638927925/50a8d/GhgqUuRs7Vo.jpg",
# "https://pp.userapi.com/c638927/v638927925/50a97/QRBVWTMZtM4.jpg",
# "https://pp.userapi.com/c638927/v638927925/50aab/2xCca9xu9lc.jpg",
# "https://pp.userapi.com/c638927/v638927925/50ab5/M9fHgThrrWU.jpg",
# "https://pp.userapi.com/c638927/v638927925/50abf/GZr34Uf4ToI.jpg",
# "https://pp.userapi.com/c638927/v638927925/50ac9/EPo52sFj_38.jpg",
# "https://pp.userapi.com/c638927/v638927925/50ad3/sGMhLbKdjSo.jpg",
# "https://pp.userapi.com/c638927/v638927925/50add/wwl87gBMG7s.jpg",
# "https://pp.userapi.com/c836336/v836336534/57963/YXIAsukWy90.jpg",
# "https://pp.userapi.com/c836336/v836336534/5796d/lVGCm36FZww.jpg",
# "https://pp.userapi.com/c836336/v836336534/57977/oKUFtgQYqmo.jpg",
# "https://pp.userapi.com/c836336/v836336534/57981/7W7udSbyk0A.jpg",
# "https://pp.userapi.com/c836336/v836336534/5798b/uvIuF92uZ9E.jpg",
# "https://pp.userapi.com/c836336/v836336534/57995/HpMXAzHPSkE.jpg",
# "https://pp.userapi.com/c836336/v836336534/5799f/J2m8XGd6anA.jpg",
# "https://pp.userapi.com/c836336/v836336534/579a9/pcA62mFYSdY.jpg",
# "https://pp.userapi.com/c836336/v836336534/579b3/NCwasoIq2qc.jpg",
# "https://pp.userapi.com/c836336/v836336534/579bd/HlZrBb0MoB8.jpg",
# "https://pp.userapi.com/c836336/v836336534/579c7/WyFU-N0xZas.jpg",
# "https://pp.userapi.com/c836336/v836336534/579d1/PrXevIDPTIw.jpg",
# "https://pp.userapi.com/c836336/v836336534/579db/VOn-ch4IQEs.jpg",
# "https://pp.userapi.com/c836336/v836336534/579e5/Eya_G2OvMp0.jpg",
# "https://pp.userapi.com/c836336/v836336534/579ef/isCYRk8E624.jpg",
# "https://pp.userapi.com/c836336/v836336534/579f9/W-cpRxddfUs.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a03/1PpEjotzA3A.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a0d/SmCLslLs_nE.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a17/jhW8WsFtgS0.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a21/yR1V4brKXL0.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a2b/OEtG9ioJAIc.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a35/ZpLfa1z0JXg.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a3f/2lUd-mR06Wg.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a49/A_MRWPzJ1Jw.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a53/9GDB7vU9mbE.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a5d/SG-UQzaXZK0.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a67/1rnssEIchJc.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a71/VPUYZXtCwUE.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a7b/cC8IffnIqZI.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a85/UHJcXaRFIjs.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a8f/dS8gf2Gz1YU.jpg",
# "https://pp.userapi.com/c836336/v836336534/57a99/sb9j-ArkJGo.jpg",
# "https://pp.userapi.com/c836336/v836336534/57aa3/SEUgzH26XR0.jpg",
# "https://pp.userapi.com/c836336/v836336534/57aad/lejMQG5jpSs.jpg",
# "https://pp.userapi.com/c836336/v836336534/57ab7/mM6hhcYAj5k.jpg",
# "https://pp.userapi.com/c836336/v836336534/57ac1/pnsIjUfxXHU.jpg",
# "https://pp.userapi.com/c836336/v836336534/57acb/K5lsKy96TS4.jpg",
# "https://pp.userapi.com/c836336/v836336534/57ad5/-APN9bU__Cg.jpg",
# "https://pp.userapi.com/c836336/v836336534/57adf/k-nTsd6QDHM.jpg",
# "https://pp.userapi.com/c836336/v836336534/57ae9/gHUZ8y2PvZk.jpg",
# "https://pp.userapi.com/c836336/v836336534/57af3/y3xPhW5JNyc.jpg",
# "https://pp.userapi.com/c836336/v836336534/57afd/ATav_YGhhys.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b07/D8-INws9Ops.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b11/CJIMUksqg9I.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b1b/tR2l1mxc9S8.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b25/K42zXX9F8uM.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b2f/bcRXyJ3tP8U.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b39/9pp4pcyWOvg.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b43/wqSXoazUxOA.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b4d/aOfo3y1G5cc.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b57/nZ0ss6DBzr4.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b61/XFx_toay2cY.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b6b/2RrPvLdXIm0.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b75/FRjVhIgLnXs.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b7f/YXG6RAFKc9U.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b89/EiKdJtkzHbI.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b93/TktWHM7deR8.jpg",
# "https://pp.userapi.com/c836336/v836336534/57b9d/6OB5z7bCLgk.jpg",
# "https://pp.userapi.com/c836336/v836336534/57ba7/nykQCEkYUbo.jpg",
# "https://pp.userapi.com/c836336/v836336534/57bb1/1aMed7FnkXE.jpg",
# "https://pp.userapi.com/c836336/v836336534/57bbb/NSSatEmIJRE.jpg",
# "https://pp.userapi.com/c836336/v836336534/57bc5/n7CvjQisGG4.jpg",
# "https://pp.userapi.com/c836336/v836336534/57bcf/zDjKQ4vhKXA.jpg"

# ]

# list= ["https://pp.userapi.com/c841326/v841326345/4efe7/9sSLSnrltR0.jpg",
# "https://pp.userapi.com/c841326/v841326345/4eff1/w_-89CoorWo.jpg",
# "https://pp.userapi.com/c841326/v841326345/4effb/ZXVR5zJAmCE.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f005/Ij960R2AreA.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f00f/rKQKrRAkrxE.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f019/D-PvM2UtmCc.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f02d/4lNdPpSNuTw.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f037/Ddx6Z5s_u00.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f041/VliNT9Jzg0M.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f04b/rTKEyd2IizA.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f055/WVC9FjP8uqI.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f05f/wdi2qCTOf6s.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f069/Ojw9TlsAzq0.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f073/4t2pPDekztc.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f07d/rIaf_8d6oMI.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f087/6EKQFYo6BLQ.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f091/EvFBD1TkarY.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f09b/kC5hO88KZLE.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f0a5/uGd4ZaWome4.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f0af/s5iqooRjr34.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f0b9/FYThf34FLK8.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f0c3/r5wsY_csTj4.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f0cd/5xXFu71_HIY.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f0d7/17RDxBZyDcY.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f0e1/qoaGV3DrUSI.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f0eb/MPWsnIqFO00.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f0f5/HW0BksL-EVA.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f0ff/XW6dtA9Xyoo.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f109/RX4K_3_OjIg.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f113/tyUkUpsjr74.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f11d/3LIpZlu6OdE.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f127/LEm0EvpKs1Q.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f131/Y1wXE1qIRvs.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f13b/0mAIes1Whgo.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f145/8e3_fHi7QEU.jpg",
# "https://pp.userapi.com/c841326/v841326345/4f14f/B-oJ1Z10ufE.jpg",
# ]


for i in list:
  urllib.request.urlretrieve(i, "images/"+os.path.basename(i))