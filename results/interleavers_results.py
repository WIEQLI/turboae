__author__ = 'yihanjiang'

# benchmarks

turbo757_i6_bl100_snr = [-1.5, -1.0, -0.5, 0.0,
                         0.5, 1.0, 1.5, 2.0,
                         2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
turbo757_i6_bl100_ber = [0.056863, 0.02592, 0.010097, 0.002785,
                         0.000747, 0.00022, 6.9e-05, 2.832e-05,
                         1.1175e-05, 4.502e-06, 1.618e-06, 5.53e-07,
                         1.69e-07,5e-08 ]

turbo757_i6_bl100_bler = [0.526, 0.29300000000000004, 0.139, 0.05020000000000002,
                          0.018900000000000028, 0.007299999999999973, 0.0028000000000000247, 0.0010999999999999899,
                          0.0005629, 0.0002336, 8.48e-05, 2.8400000000039505e-05,
                          8.80000000003e-06, 2.59999999996e-06]

turbolte_i6_bl100_snr =  [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
turbolte_i6_bl100_ber = [0.06289789, 0.02797317, 0.00920123, 0.00218761,
                         0.00044006, 9.915e-05, 3.048e-05, 1.3e-05,
                         6.16e-06, 2.64e-06, 1.39e-06, 4.8e-07]
turbolte_i6_bl100_bler = [0.488499, 0.250826, 0.098333, 0.03151300000000001,
                          0.010387000000000035, 0.004279000000000033, 0.0020649999999999835, 0.0010949999999999571,
                          0.0005680000000000129, 0.000264000000000042, 0.00013700000000005375, 4.8000000000048004e-05]

# DeepTurbo as a benchmark

# deepturbo 757, iteration 6
turbofy_dec_757_snr_tf5 = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
turbofy_dec_757_ber_tf5 =  [0.06876672804355621, 0.034134820103645325, 0.013278993777930737, 0.0039285761304199696,
                            0.0009306119754910469, 0.00019915630400646478, 4.617767262971029e-05, 1.2138983947806992e-05,
                            3.7910908758931328e-06, 1.2122184216423193e-06, 3.544449214132328e-07, 1.2888885692063923e-07 ]

turbofy_dec_757_bler_tf5 = [0.6815720000000027, 0.44594700000000115, 0.22712100000000046, 0.08711500000000033,
                            0.02625300000000005, 0.006943999999999906, 0.0018749999999999615, 0.0005277000000000013,
                            0.00017189999999999323, 5.730000000000004e-05, 1.7000000000000013e-05, 6.300000000000004e-06]
# deepturbo LTE, iteration 6
turbofylte_i6_ft5_snr =   [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0,2.5, 3.0, 3.5, 4.0]
turbofylte_i6_ft5_ber =  [0.08252130448818207, 0.04216403886675835, 0.016300421208143234, 0.004570276476442814,
                          0.0009356688242405653, 0.00015390923363156617, 2.5644580091466196e-05, 4.8999922910297755e-06,
                          1.4333338640426518e-06, 3.6666673963736685e-07, 1.7888896763906814e-07, 4.666667763331134e-08]

turbofylte_i6_ft5_bler = [0.7063299999999955, 0.4673839999999981, 0.23551400000000208, 0.08631199999999992,
                          0.023135000000000402, 0.004996000000000043, 0.0010729999999999833, 0.00024299999999999927,
                           7.700000000000006e-05, 2.800000000000001e-05, 1.2500000000000009e-05, 3.7000000000000014e-06]

###########################################################################################################################
# DTA results
###########################################################################################################################
snrs =  [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]

# RNN only results
dta_level2_rnn_enctrain2_dectrainneg15_2_ber = [0.08769059926271439, 0.04307781159877777, 0.016747096553444862, 0.005380249582231045, 0.001673299353569746, 0.0005798998172394931, 0.0002428000298095867, 0.00010475004091858864, 4.6200017095543444e-05, 1.770000199030619e-05, 8.499999239575118e-06, 3.5499992918630596e-06]

# CNN Our results


dta_cont_cnnenc_grudec_enctrain2_dectrainneg15_2_ber = [0.10225459188222885, 0.048412203788757324, 0.018568996340036392, 0.00535960029810667, 0.0013811998069286346, 0.00043360001291148365, 0.00012820000119972974, 4.7399993491126224e-05, 1.4400003237824421e-05, 3.400000196052133e-06, 9.999999974752427e-07, 3.9999997625272954e-07]


dta_q2_cnnenc_grudec_enctrain2_dectrainneg15_2_ber =[0.07956141233444214, 0.03532780334353447, 0.012283999472856522, 0.0038170008920133114,
                                                     0.0012933999532833695, 0.0004459999909158796, 0.00016799998411443084, 6.600000051548705e-05,
                                                     2.5599989385227673e-05, 7.599997843499295e-06, 1.9999999949504854e-06, 7.999999525054591e-07]


dta_q2_cnnenc_cnndec_enctrain2_dectrainneg15_2_ber = [0.17315320670604706, 0.10201200097799301, 0.04709819331765175, 0.01594560034573078,
                                                      0.004049600102007389, 0.0007532000890932977, 0.0001596000511199236, 4.0999995690071955e-05, 1.700000029813964e-05, 5.599999894911889e-06, 2.1999999262334313e-06, 3.9999997625272954e-07]
dta_q2_cnnenc_cnndec_enctrain2_dectrainneg15_2_ber = [0.11324860155582428, 0.056740593165159225, 0.02226019836962223, 0.006556401029229164,
                                                      0.0015670000575482845, 0.0003893998800776899, 0.00012340000830590725, 4.0599985115695745e-05,
                                                      1.359999987471383e-05, 5.199999345175456e-06, 1.1999999287581886e-06, 5.999999643790943e-07]

##############################

# CNN 2 layer encoder, CNN 5 layer decoder, DTA.


dta_cont_cnn2enc_cnn5dec_enctrain2_dectrainneg15_2_ber = [0.10074236243963242, 0.04645926132798195, 0.016037607565522194, 0.004073908552527428,
                                                          0.0008630399242974818, 0.00019923502986785024, 6.059997758711688e-05, 1.9379973309696652e-05,
                                                          6.014996415615315e-06, 1.7300009176324238e-06, 4.1999996369668224e-07, 9.00000216574881e-08]

dta_q2_cnn2enc_cnn5dec_enctrain2_dectrainneg15_2_ber =[0.08949052542448044, 0.04069797322154045, 0.013945434242486954, 0.003680518129840493,
                                                     0.0009017499978654087, 0.000256019935477525, 8.699001045897603e-05, 3.130002733087167e-05,
                                                     1.1149996680615004e-05, 4.020002052129712e-06, 1.3699996088689659e-06, 3.5999994452140527e-07]

dta_cont_cnn2enc_cnn5dec_enctrain0_dectrain0_ber =[0.08134345710277557, 0.03552451357245445, 0.011664831079542637, 0.0030416203662753105,
                                                   0.0007227200549095869, 0.00021446991013363004, 7.218997780000791e-05, 2.530002166167833e-05,
                                                   8.7200114649022e-06, 2.4999987999763107e-06, 7.700000423938036e-07, 2.1000003869175998e-07]

dta_q2_cnn2enc_cnn5dec_enctrain0_dectrain0_ber =[0.08684908598661423, 0.03950152173638344, 0.01391039788722992, 0.0038691104855388403,
                                                  0.0010155497584491968, 0.0003109500976279378, 0.00011194997932761908, 4.18375275330618e-05,
                                                  1.5125009667826816e-05, 5.262500962999184e-06, 1.56249996052793e-06, 6.12499832186586e-07]

dta_cont_cnn2enc_cnn5dec_enctrainneg05_dectrainneg05_ber =  [0.05700160935521126, 0.026030899956822395, 0.010004100389778614, 0.0037539000622928143,
                                                            0.0014785000821575522, 0.000622799969278276, 0.00024505003239028156, 9.615000453777611e-05,
                                                            3.580000702640973e-05, 1.4799999007664155e-05, 5.249999048828613e-06, 2.4999997094710125e-06]



dta_cont_cnn2enc_cnn5dec_enctrainneg15_dectrainneg15_ber  =  [0.047043804079294205, 0.025237491354346275, 0.01260764803737402, 0.006137849763035774,
                                                              0.002895999699831009, 0.0013556497870013118, 0.0006062999600544572, 0.0002708999963942915,
                                                              0.00011360000644344836, 4.029999763588421e-05, 1.7149997802334838e-05, 5.949999831500463e-06]

dta_q2_cnn2enc_cnn5dec_enctrainneg15_dectrainneg15_ber  =  [0.08075735718011856, 0.03741989657282829, 0.013716748915612698, 0.004008599556982517,
                                                            0.0011138498084619641, 0.00034955001319758594, 0.0001240499987034127, 4.6399996790569276e-05,
                                                            1.689999407972209e-05, 6.099999609432416e-06, 2.1999994714860804e-06, 6.999999868639861e-07]



# DTA results:
dta_cont_cnn2enc_cnn5dec_combined_ber = [0.047043804079294205, 0.025237491354346275,  0.010004100389778614, 0.0030416203662753105,
                                        0.0007227200549095869,0.00019923502986785024, 6.059997758711688e-05, 1.9379973309696652e-05,
                                        6.014996415615315e-06, 1.7300009176324238e-06, 4.1999996369668224e-07, 9.00000216574881e-08]

dta_q2_cnn2enc_cnn5dec_combined_ber = [0.08075735718011856, 0.03741989657282829, 0.013716748915612698,  0.003680518129840493,
                                                     0.0009017499978654087, 0.000256019935477525, 8.699001045897603e-05, 3.130002733087167e-05,
                                                     1.1149996680615004e-05, 4.020002052129712e-06, 1.3699996088689659e-06, 3.5999994452140527e-07]

# BLERs

dta_cont_cnn2enc_cnn5dec_enctrain2_dectrainneg15_2_bler =[0.6667735000000005, 0.4258410000000012, 0.21239300000000005, 0.08461900000000021,
                                                          0.03029899999999994, 0.010856499999999944, 0.003988999999999977, 0.0013614999999999838,
                                                          0.00043950000000000033, 0.0001255000000000001, 3.2500000000000024e-05, 8.000000000000003e-06]




dta_q2_cnn2enc_cnn5dec_enctrain2_dectrainneg15_2_bler = [0.6786349999999994, 0.44430499999999956, 0.2330600000000003, 0.10009399999999984,
                                                         0.039813000000000036, 0.015690999999999983, 0.006300999999999979, 0.0024339999999999857,
                                                         0.0008900000000000007, 0.0003210000000000002, 0.00011300000000000009, 3.600000000000003e-05]

dta_q2_cnn2enc_cnn5dec_enctrain2_dectrainneg15_2_bler = [0.6710949999999999, 0.4366969999999998, 0.227437, 0.09784399999999989,
                                                         0.03890200000000008, 0.015698999999999994, 0.0061639999999999785, 0.002382999999999985, 0.0008680000000000006, 0.00033200000000000026, 0.00010500000000000009, 2.900000000000001e-05]

dta_cont_cnn2enc_cnn5dec_enctrain0_dectrain0_bler =  [0.641712999999999, 0.40324099999999996, 0.2007309999999997, 0.08383600000000012,
                                                      0.032335000000000017, 0.012571999999999995, 0.0048169999999999775, 0.0017979999999999888,
                                                      0.0006210000000000005, 0.00018900000000000015, 5.600000000000004e-05, 1.7000000000000007e-05]


dta_q2_cnn2enc_cnn5dec_enctrain0_dectrain0_bler =  [0.6834962500000001, 0.45406999999999975, 0.2449762500000003, 0.11114249999999988,
                                                      0.046681250000000014, 0.019503749999999983, 0.007919999999999988, 0.003123749999999985,
                                                      0.001185000000000001, 0.0004162500000000003, 0.00012500000000000008, 5.125000000000004e-05]



dta_cont_cnn2enc_cnn5dec_enctrainneg15_dectrainneg15_bler  =  [0.755155, 0.5886149999999999, 0.40657999999999994, 0.25509999999999994,
                                                               0.14547499999999994, 0.078055, 0.038000000000000006, 0.018129999999999993,
                                                               0.008054999999999996, 0.0030300000000000023, 0.001360000000000001, 0.0004950000000000003]

dta_q2_cnn2enc_cnn5dec_enctrainneg15_dectrainneg15_bler  =  [0.6655000000000001, 0.44377500000000003, 0.24486999999999995, 0.11482999999999999,
                                                             0.04960000000000002, 0.021174999999999996, 0.008639999999999995, 0.0034450000000000023,
                                                             0.001345000000000001, 0.0005050000000000003, 0.0001800000000000001, 4.5e-05]


# combined result
dta_cont_cnn2enc_cnn5dec_combined_bler =[0.641712999999999, 0.40324099999999996, 0.2007309999999997, 0.08383600000000012,
                                         0.03029899999999994, 0.010856499999999944, 0.003988999999999977, 0.0013614999999999838,
                                        0.00043950000000000033, 0.0001255000000000001, 3.2500000000000024e-05, 8.000000000000003e-06]

dta_q2_cnn2enc_cnn5dec_combined_bler = [0.6655000000000001, 0.44377500000000003, 0.2330600000000003, 0.09784399999999989,
                                        0.03890200000000008, 0.015698999999999994, 0.0061639999999999785, 0.002382999999999985,
                                        0.0008680000000000006, 0.00033200000000000026, 0.00010500000000000009, 2.900000000000001e-05]


dta_cont_no_inter_ber =  [0.15685176849365234, 0.11168290674686432, 0.07274758815765381, 0.04336030036211014, 0.022550400346517563, 0.01062140055000782, 0.004485601559281349, 0.0016831997781991959, 0.0005844999686814845, 0.00018069999350700527, 5.190000229049474e-05, 1.5799994798726402e-05]
dta_cont_no_inter_bler = [0.9673899999999999, 0.9045100000000005, 0.7824700000000006, 0.60095, 0.3937200000000001, 0.22206000000000006, 0.10654, 0.04432999999999999, 0.01674999999999999, 0.005880000000000004, 0.0016900000000000012, 0.0005800000000000003]


cnn_ae_ber =  [0.07059461623430252, 0.04456420615315437, 0.026049993932247162, 0.013904601335525513, 0.006724798120558262, 0.0028732004575431347, 0.001142599736340344, 0.00038819992914795876, 0.00013740001304540783, 4.179999086773023e-05, 1.599999814061448e-05, 3.000000106112566e-06]

import matplotlib.pylab as plt

plt.figure(1)
plt.subplot(121)
plt.yscale('log')
plt.xlabel('SNR')
plt.ylabel('BER')

p1, = plt.plot(turbo757_i6_bl100_snr[:12], turbo757_i6_bl100_ber[:12],'-x', label = 'Turbo-757')
p2, = plt.plot(turbolte_i6_bl100_snr, turbolte_i6_bl100_ber,'-+', label = 'Turbo-LTE')

h4, = plt.plot(snrs, dta_cont_cnn2enc_cnn5dec_combined_ber, '-o', label = 'DTA with interleaving')

i1, = plt.plot(snrs, dta_cont_no_inter_ber, '-o', label = 'DTA without interleaving')


plt.legend(handles =[p1, p2,
                      h4, i1])
plt.grid()

plt.subplot(122)
plt.yscale('log')
plt.xlabel('SNR')
plt.ylabel('BLER')

p1, = plt.plot(turbo757_i6_bl100_snr[:12], turbo757_i6_bl100_bler[:12],'-x', label = 'Turbo-757')
p2, = plt.plot(turbolte_i6_bl100_snr, turbolte_i6_bl100_bler,'-+', label = 'Turbo-LTE')

h4, = plt.plot(snrs, dta_cont_cnn2enc_cnn5dec_combined_bler, '-o', label = 'DTA with interleaving')

i1, = plt.plot(snrs, dta_cont_no_inter_bler, '-o', label = 'DTA without interleaving')


plt.legend(handles =[p1, p2,
                      h4, i1])
plt.grid()


# try different interleaver for all tasks.



enc1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
enc2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
enc3 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]





bl = [20, 50, 100, 200, 1000]


cnn_ae_2dB_ber = [0.0007009999244473875,0.00038431986467912793 ,0.00031172001035884023,0.0002650997485034168,  0.0002462019619997591]

turbo_ae_2dB_ber = [0.0023757496383041143, 8.740001067053527e-05, 1.6999996660160832e-05,  9.349998435936868e-06,  6.24999984211172e-06]


turbo_2dB_ber = [ 0.0007485,  9.4e-05, 3.6e-05, 2.35e-06,  3.9e-07 ]





plt.figure(5)
plt.title('Interleaver Visualization')
plt.xlabel('Code block bit position')
plt.ylabel('Code difference')
p1, = plt.plot(enc1, '-x',label = 'enc1')
p2, = plt.plot(enc2, '-+', label = 'enc2')
p3, = plt.plot(enc3, '-o',label = 'enc3, interleaved')

plt.legend(handles = [p1, p2, p3])

plt.grid(which='major', alpha=100)




plt.figure(2)
plt.subplot(121)
plt.title('Coding Gain of Different block length')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Block Length')
plt.ylabel('BER at 2dB')


p1,  = plt.plot(bl, cnn_ae_2dB_ber,'-x', label = 'CNN-AE')
p2,  = plt.plot(bl, turbo_2dB_ber,'-<', label = 'Turbo')
p3,  = plt.plot(bl, turbo_ae_2dB_ber,'->', label = 'TurboAE')

plt.legend(handles = [p1, p2, p3])

plt.grid()

plt.subplot(122)
plt.title('Neural Architecture Improvement')
plt.yscale('log')
plt.xlabel('SNR')
plt.ylabel('BER')

p1, = plt.plot(snrs, cnn_ae_ber, '-x', label = 'CNN-AE')
p2, = plt.plot(turbo757_i6_bl100_snr[:12], turbo757_i6_bl100_ber[:12],'-<', label = 'Turbo')

p3, = plt.plot(snrs, dta_cont_cnn2enc_cnn5dec_combined_ber, '->', label = 'TurboAE with interleaving')
p4, = plt.plot(snrs, dta_cont_no_inter_ber, '-+', label = 'TurboAE without interleaving')

plt.legend(handles = [p1, p2, p3, p4])
plt.grid()



# random interleaver.
snrs   =   [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
r1_ber_train =  [0.10917463898658752, 0.05341871455311775, 0.01972479745745659, 0.005352799780666828, 0.0010823000920936465, 0.00022910002735443413, 5.505001172423363e-05, 1.8749997252598405e-05, 6.50000038149301e-06, 1.0999999631167157e-06, 6.500000040432496e-07, 4.999999703159119e-08]
r2_ber =   [0.10899858921766281, 0.052930038422346115, 0.01969049498438835, 0.005212900694459677, 0.0011175499530509114, 0.00022390001686289907, 5.97500147705432e-05, 2.079999649140518e-05, 5.399998372013215e-06, 1.5499999790336005e-06, 6.999999868639861e-07, 9.999999406318238e-08]
r3_ber =[0.10886409878730774, 0.05325143784284592, 0.019522948190569878, 0.005302650388330221, 0.0010850998805835843, 0.00023249992227647454, 5.510000846697949e-05, 1.7700000171316788e-05, 6.050000138202449e-06, 9.999999974752427e-07, 2.9999998218954715e-07, 4.999999703159119e-08]
r4_ber =  [0.10891561955213547, 0.05321090668439865, 0.019586646929383278, 0.005185100249946117, 0.00109329994302243, 0.00021130000823177397, 4.975000774720684e-05, 1.934999818331562e-05, 5.649999820889207e-06, 1.8999999156221747e-06, 1.9999998812636477e-07, 1.9999998812636477e-07]

plt.figure(3)
plt.title('TurboAE Random Interleaving Results during Testing Phase')
plt.yscale('log')
plt.xlabel('SNR')
plt.ylabel('BER')

p1, = plt.plot(snrs[:8], dta_cont_no_inter_ber[:8], '-o', label = 'No interleaving')

p2, = plt.plot(snrs[:8], r1_ber_train[:8], '-.', label = 'trained and test on same interleaver')
p3, = plt.plot(snrs[:8], r2_ber[:8], '-<', label = 'Test with random interleaver 1')
p4, = plt.plot(snrs[:8], r3_ber[:8], '->', label = 'Test with random interleaver 2')
p5, = plt.plot(snrs[:8], r4_ber[:8], '-+', label = 'Test with random interleaver 3')

plt.legend(handles =[p1,p2, p3, p4, p5])
plt.grid()


plt.show()




