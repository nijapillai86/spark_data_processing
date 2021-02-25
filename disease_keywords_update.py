# encoding=utf8
# Define disease keywords dictionary
conditions = {
            'ad':{
                 'icd_codes' : ['G30.0','G30.1','G30.8','G30.9','\sG30','331.0'],

                 'main':["Alzheimer's disease with late onset", "alzheimer's disease with early onset","alzheimer's disease",
                        'alzheimer disease','alzh[^\s]+', 
                         
                        ],

                 'drugs' : ['donepezil\s[hcl]?', 'Razadyne', 'Memantine', 'Namenda','Namzaric', 
                            'Aricept[\s]?[hcl]?','rivastigmine',],

                 'incl':[ '^mci\s|\smci\s',"Auditory verbal learning test","AVLT",'short term memory',
                          'Dementia without behavioral disturbance','memory issues','331.83',
                          'Dementia with behavioral disturbance','clock draw \d+','clock \d+','mmse \d{2}','mmse score of \d{2}',
                          'Clock Draw','mild cognitive impairment' ,'slums', "delusions",
                         'MMSA', 'Mini Mental State', 'Mini Mental State Assessment','Mini-cog clock drawing',#'(?=MMSE)(.+)(?=\/30)'
                         'Montreal Cognitive Assessment', '\d+ \d+ moca','anxiety', 'Frontotemporal dementia',
                         'glutamate','senile demnatia','Major Depression','dizziness','forgets', 'dementia',
                         'poor judgement', 'mood swings',  'Behaviour - Agitation','Retrograde Amnesia','g31.84',
                         'cholinesterase', 'acetylcholine', 'Amnesia','Anterograde','F03.90',
                         '24759[0-9]{2,3}', '481d67000', '89051002', '162199006','frontal dementia',
                         'confusion', 'behavioral disturbance','progressive memory loss', 'memory loss','depressed mood',
                         'incoordination','Forgetfulness','[^0-9]331.0',' g318[0-9]','Senile degeneration of brain','Memory problems',
                         'short-term memory','Amyloid PET imaging','MRI','APOE-4','Apolipoprotein - E4', 'Exelon',
                          "frontal dementia", 'vascular dementia', 'Auditory verbal learning test','Prevagen', 
                          'difficulty concentrating','PET scan','R41[.][0-9]{1,3}', 'F02.8[0-1]','presenile onset','galantamine\s', 
                          'Folstein mini mental','disorientation to time and space','bmi \d+[.]\d+','bmi \d+',
                          'cognitive assessment tool',' AVLT ','word finding difficulty', 'altered mental status','R41.82',
                          'mini mental','moca \d{2}','mmse - \d{2}', 'moca','mmse', 'paranoia','delusion','Hallucinations',
                     ]

             },
            'pd':{
                 'icd_codes' : ['\sG20','\sG21','\sG22', ],

                 'main':['parkinson[^\s]+','parkinsonism','Hemiparkinsonism', 'bradykinesia',
                         'resting tremor','Parkinson[^\s] Disease','Tardive dyskinesia','parkinsonian gait',
                         'masklike facies','carbidopa","levodopa', 'Amantadine','Pramipexole', 'Selegiline', 
                          'Rasagiline','Sinemet','carbidopa levodopa',"DaT scan",
                          'Azilect', 'rasagiline', 'Xadago',"safinamide", 'selegiline',"Mirazpex","pramipexole", "Requip","ropinirole", 
                          "Neupro","rotigotine transdermal", "Apokyn" ,"Kynmobi", "apomorphine"
                          
                          ],
                 'drugs' : ['carbidopalevodopa', 'Amantadine','Pramipexole', 'Selegiline', 
                          'Rasagiline','Sinemet','carbidopa levodopa',"Azilect", "rasagiline", 
                          "Xadago", "safinamide", "selegiline","Mirazpex","pramipexole", "Requip","ropinirole", 
                          "Neupro","rotigotine transdermal", "Apokyn" ,"Kynmobi", "apomorphine","Duopa", "Stalevo",
                          "amantadine", "Gocovri", "Osmolex", "Symmetrel"
                        ],

                 'incl': ['idiopathic','stiffness','shaking','hallucinations','senile dementia', 'frontal dementia',
                         'voluntary movements','332[.][0-1]', 'g83.9','rigid muscles', 'impaired posture',
	                 'slurred speech','gait',   'Paralys[^\s]','trembling','balance difficulty', 'restlessness',
                         'coordination','impaired balance',' masked facies', 'trembling of hands', 'loss of balance', 
                         'rigidity','masked face','Tremor',' UPDRS ','Hoehn and Yahr','hypomimia','Shaking palsy',
                         'Inbrija', 'Rytary','Requip','R25.1','Safinamide','postural reflexes','Cogentin','agitans',
                         'Amantadine', 'Symmetrel', 'Trihexyphenidyl', 'Artane', 'benztropine',  
                         'apomorphine','degenerative','F02.8[0-1]','24759[0-9]{2,3}', '481d67000', '89051002', '162199006',
                         'tolcapone', 'entacapone', 'Comtan', 'Tasmar',  'g318[0-9]',
                         'Eldepryl Zelapar',  'retropulsion',' stooped posture',
                         'dopamine', 'ropinirole', 'pramipexole', 'rotigotine', 'Mirapex',
                         'Neupro','masked face','ataxia','ataxic','Apokyn','Pimavanserin',
                         'Lodosyn','sinemet','DAT scan', 'Romberg','pramiapexole', 'postural instability',
                         'hypokinesia','akinesia','Levodopa','levadopa','carbidopa',  'Nuplazid',
                         'rasagiline mesylate','R26[.][0-9]','PET Scan', 'MRA', 'MRI', 
                         'Neuropsychological test',"Parkinsonism", "shuffled gait", "bradykinesia", "hypomimia", 
                         "rigidity", "cogwheeling", "stiffness","falls", "poor postural reflexes","DaT scan",
                         "Deep Brain Stimulator","DBS","other procedure for PD", "Focused Ultrasound"
                         ]
                 },
            'als' :{
                  'icd_codes' : ['335.20', 'G12.21',],

                  'main' : [
                      'amyotrophic lateral sclerosis', 'amyotrophic[^\s]', 'Charcot disease',
                      "Lou Gehrig’s disease",'Amyotrophic Lateral Sclerosis Functional Rating','ALSFRS',  
                      'G12.20', 'G12.9', 'G12.24','^als\s|\sals\s'

                      ],
                      
                  'drugs':['scopolamine\s','riluzole\s', 'Edaravone\s','Robinul\s', 'Hyoscine\s', 'Nuedexta\s' ,'Radicava\s',],


                  'incl'  : ['Tracheotomy', 'gastrostomy',  'neurodegenerative',"Familial motor neuron disease",
                  'motor neuron disease','spasticity', "Babinski's reflex",
                      'denervation', 'tongue atrophy','335.22','335.24', 'G12.2', 'G72.89', 'G71.8', 'G83.9', 'G12.9','M62.5',
                      'up going toe','Elavil', 'slurring', 'gradually worsening speech', 'r47.1',
                       'Scopaderm', 'scopolamine patch', 'trouble walking', 
                      'trouble writing','speech problems','trouble running',
                      'spastic catch', 'tendon reflexes', '4/5 weakness', 
                      'asymmetric weakness', ' peg ', 'Rilutek','FVC','El Escorial Criteria',
                      'pseudobulbar effect', 'feeding tube', '728.2','F48.2','784.51', '787.2','bruising',
                      'glycopyrrolate','atrophy','fasciculation'
                      'Trihexyphenidyl', 'hyperreflexia', 'dysphagia', 'fibrous astrocytes', 
                      'corticospinal tracts','spinal muscle atrophy','bulbar palsy',
                      'trouble walking', 'trouble running', 'trouble swallowing', 'choking',
                      'percutaneous endoscopic gastrostomy', 'edavarone', 
                      'glutamate', 'motor neuron disease', 'denervation', 'tongue atrophy', 
                      'up going toe', 'bruising', 'glycopyrrolate','Pseudobulbar affect',
                       'worsening of speech','slurred speech','slowed speech','Tongue fasciculation','Upgoing toe',
                       'Dysarthria','anartharia','babinski','superoxide dismutase type-1', 'SOD1', 'TARDBP mutation'
                       'Glycopyrronium bromide','Hyoscine','dextromethorphan','quinidine sulfate'
                      ]
            },
            'epy':{
                  'icd_codes' : ['g40.909','\sG40','\sG41','\sg40[.][0-9]{3}','\sG41[.][0-9]{3}'],

                  'main':[ 'epileptic','epilepsy','chronic seizure',
                      'epilep[^\s]+','[^m]g40','[^m]g41',
                      'Complex partial seizure', 'Partial seizure','convulsive disorder','Absence seizure',
                      
                      ],
                  'drugs' : ['Clobazam', 'Carbamazepine', 'Oxcarbazepine\s', 'Sodium valproate','Phenytoin', 
                         'Divalproex sodium', 'Carbamazepine, Sodium valproate','Levetiracetam', 'Keppra','Divalproex sodium',
                         'Lamotrigine','Vimpat','Depakote','tegretol'],

                  'incl':['stares blankly', 'loss of muscle tone','[^0-9]345.90','R56[.][0-9]{1}',
                         '[^0-9]345.10','F44.5','345[^a-z0-9]','seizure[^\s]','Dilantin Kapseals','Trileptal',
                         '780.39','tonic - clonic','drooling',
                         'temporal lobe epilepsy',' TLE ','convulsions',
                         ]
            },
            'lbd':{
                  'icd_codes' : ['G31.83',],

                  'main':[ "Lewy body disease",'lewy bod[^\s]', 'mild parkinsonism','MS-DRG 057', "dementia with Parkinsonism",
                        "Dementia due to parkinson's disease",
                        "Dementia due to parkinsons disease","Diffuse lewy body disease","Lewy body dementia",
                        "lewy body dementia with behavioral disturbance","Dementia related to Parkinson’s Disease",
                        "Lewy body dementia without behavioral disturbance", "Senile dementia of the lewy body type"                      
                      ],
                  'drugs' :["Donepezil","Aricept", "Galantamine" "Razadyne", "Rivastigmine", "Exelon", "Memantine", "Namzaric",
                        "memantine XR", "Namenda", "Namenda XR", "Azilect", "rasagiline", "Xadago", "safinamide", "selegiline",
                        "Mirazpex", "pramipexole", "Requip" ,"ropinirole", "Neupro","rotigotine transdermal", "Apokyn & Kynmobi", "apomorphine",
                        "Sinemet", "carbidopa","levodopa", "Duopa", "Stalevo", "Inbrija", "Rytary",
                        "Comtan" ,"entacapone", "Ongentys", "opicapone", "amantadine", "Gocovri", "Osmolex", "Symmetrel",
                        "Mirazpex","pramipexole", "Requip","ropinirole", 
                          "Neupro","rotigotine transdermal", "Apokyn" ,"Kynmobi", "apomorphine","Duopa", "Stalevo",
                           "Gocovri", "Osmolex", "Symmetrel"
                ],
                  'incl':['ataxia','dementia','parkinsons disease','senile dementia',"DaT scan",'dopaminergic neurons', 
                      'fluctuations','MCC','guadeloupe','retinitis pigmentosa','hallucinations',
                      '331.82','277.87','330.8','loss of cholinergic','F02.81','REM Sleep Behavior Disorder','RBD',
                      'Dementia in other disease classified elsewhere with behavioral disturbance',
                      "mild Cognitive impairment", "inattention", "behavior change","Psychosis", "paranoia", "delusions",
                      "Parkinsonism", "shuffled gait", "bradykinesia", "hypomimia", "rigidity", "cogwheeling", "stiffness", 
                      "falls", "poor postural reflexes","DaT scan", "Deep Brain Stimulator","DBS","other procedure for PD", 
                      "Focused Ultrasound",'degenerative nervous system disorders',

                  ]
            },
            'ms':{
                  'icd_codes' : ['G35','^g35|\sg35\s','[^m]g35'],

                  'main' : [ 'multiple sclerosis', 'multiple scler[^\s]','demyelination','Demyelin[^\s]+', ],

                  'drugs': ['Ocrelizumab', 'Natalizumab','Interferon beta', 'Teriflunomide', 'Dimethyl fumarate',  
                            'Dalfampridine','Ampyra','Glatiramer acetate injection','Copaxone','Interferon Beta - 1b', 
                            'Interferon Beta - 1a','Interferon Beta'  ],

                  'incl' :['exacerbation','G37.9',  'Betaseron','Extavia','myelin','polyneuropathy',
                        'Tysabri','relapsing-remitting','Aubagio','Modafinil','Provigil','spasticity',                
                        'autoimmune disorder','paresthesias','loss of sensation',
                        'dysarthria','[^0-9]340[^a-z0-9]','Expanded disability status','McDonald MS diagnostic criteria',
                        'EDSS','HLA-DRB1 gene','mutation in NR1H3','LXRA',
                        'bladder dysfunction', 'F02.8[0-1]',
                        'recurrent attacks','speech disturbances','cognition','ataxia','cerebellar ataxia',
                        'Visual loss','Extraocular movement disorders','Amantadine','Tecfidera','Imatinib Mesylate', 
                        'Ocrevus','Baclofen','Lioresal','Tizanidine', 'Zanaflex','Gocovri', 'Oxmolex','Methylphenidate',
                        'Ritalin'            
                        ]
            },
            'hhs':{
                  'icd_codes' : ['e1[1-3]{1}[.][0-9]{1,4}','E11','E12','E13','250.90'],
                  
                  'main':["Type 2 diabetes mellitus",'Type 2 diabetes mellitus','Type 2 diabetes',
                          'HbA1c','Metformin\ss]?','Januvia[\s]?','Endocrinology','type ii diabetes','diabetes mellitus',],

                  'drugs':['Insulin lispro', 'Humalog KwikPen','Insulin aspart', 'Novolog FlexPen',
                          'Insulin glargine',  'Lantus', 'Basaglar', 'Toujeo','Insulin detemir', 
                          'Levemir Flex touch','Semaglutide',  'Ozempic pen injector' 'Victoza','Metformin[\s]?[HCL]?', 
                          'Glimepiride', 'Amaryl', 'Glipizide', 'Jardiance',
                          'Glyburide','Glibenclamide', 
                          'Sitagliptin', 'Dapagliflozin', 'Farxiga','Pioglitazone',
                  ],

                  'incl':['glucose intolerance','kidney complications',
                        'macular edema','M14.6', 'diabetes','G62.9','Levemir','Peripheral Neuropathy',
                        'I79.2','hyperglycemia','hypoglycemia','M14.2','Humalog','Toujeo','Novolog',
                        'Ozempic','lispro', 'Humalog KwikPen', 'Basaglar KwikPen', 'Insulin aspart', 
                        'Novolog FlexPen', 'glargine' ,  'detemir', 'Levemir Flex touch', 'Semaglutide',  
                        'Ozempic pen injector','G73.0','G99.0','G63.2', 'G59.0','NKHHC','diabetic retinopathy',
                        'diabetic polyneuropathy','nonketotic hyperglycemic-hyperosmolar coma', 'Diabetes','polyneuropathy'
                        ]

            },
            'mry-pblm' :{
                  'icd_codes':['331.83','R41.3','G31.84','F01.50','F03.90','F02.81','F02.80'],

                  'main':['Dementia in other diseases classified elsewhere with behavioral disturbance',
                        'Dementia in other diseases classified elsewhere without behavioral disturbance' ,
                        'mild cognitive impairment','short[-]?[\s]?term memory','memory loss', 'memory[-]?[\s]?problems', 'dementia', 
                        'donepezil','aricept','rivastigmine', 'memantine', 'namenda','memory issues','memory impairment'],

                  'drugs':['donepezil[\s]?[hcl]?','Aricept[\s]?[hcl]?','rivastigmine[\s]?[hcl]?', 
                          'Memantine[\s]?[hcl]?', 'Namenda[\s]?[hcl]?',],

                  'incl': [
                        'amnesia','dizziness','forgets','namzaric', 'altered mental status','clock draw \d+','clock \d+',
                        'mmse \d{2}','mmse score of \d{2}','mini mental','moca test was \d{2}','clock draw','moca \d{2}','mmse - \d{2}',
                        'moca','R41.82','galantamine','vascular dementia','mmse','[\s]?mci[^a-z]?',
                        'Dementia in other disease classified elsewhere with behavioral disturbance','delusion','Hallucinations',
                        "auditory verbal learning test","avlt","forgetfulness","unspecified dementia without behavioral disturbance"
                ]
            },
            'ftd' :{
                  'icd_codes':['G31.01','G31.09','G31.0','331.19'],

                  'main':['Frontal temporal lobe dementia','Frontotemporal dementia','Pick\'s disease', 'Other frontotemporal dementia',
                  "Fronto-temporal dementia with progranulin mutations","FTD GRN","Behavioral variant FTD", "Expressive language disorder",
                   "Primary progressive aphasia", "FTD with corticobasal syndrome",'Dementia of frontal lobe type with expressive aphasia',
                   'Frontal temporal lobe','Frontal temporal','Fronto-temporal dementia','bvFTD'
                  ],

                  'drugs':['donepezil','Aricept','rivastigmine', 'Memantine', 
                  'Namenda','Olanzapine', 'Zyprexa', 
                  'Quetiapine', 'Seroquel', '^Citalopram', 'Celexa', 
                  'Sertraline' 'Zoloft', 'Trazodone', 'Paroxetine', 'Paxil', 
                  'Namzaric', 'Lexapro', 'Exelon', 'Xanax', 'Nuedexta'],

                  'incl': [#'bmi.*\d{2}[.\d{2}]?','MMSE.*?30','mmse.*?30','moca.*?30',
                  'aphasia', 'loss of memory', 'forgetfulness', 'forget','slurred speech', 'worsening cognition', 
                  'expressive language disorder', 'parkinsonian', 'restlessness', 'agitation', 'problem with executive functions', 
                  'advanced frontotemporal dementia', 'shuffling gait', 'parkinson\'s like symptoms', 'concentration bradykinesia', 
                  'word finding difficulty', 'gait unsteady','mmse \d{2}','mmse score of \d{2}','mini mental','moca test was \d{2}',
                  'MOCA \d{2}','MMSE - \d{2}','moca','SLUMS', 'MINT','PET Scan', 'MRA', 'MRI', 'Neuropsychological test', 'DAT scan',
                  'Blood granulin level', 'HbA1c','F02.80','F80.1','R41.841','F03.90','F03.91','R41. 89','G31.85','Logopenic PPA',
                  'Expressive language disorder','Cognitive communication deficit','Unspecified dementia without behavioral disturbance',
                  'Unspecified dementia with behavioral disturbance','Other symptoms and signs involving cognitive functions and awareness',
                  'Corticobasal degeneration','Dementia with behavioral disturbance, unspecified dementia type','dementia','memory loss',  
                  'mmse','CDR Score'
                ]
            },
            'ldh' :{
                  'icd_codes':['M51.26','M54.16'],

                  'main':['Herniation of lumbar intervertebral disc','Radiculopathy','lumbar region','Extrusion','^LDH|\sLDH\s',
                  'Protrusion','Disc herniation','^L4[-]?L5|\sL4[-]?L5\s','^L5[-]?S1|\sL5[-]?S1\s','^L5[-]?L6|\sL5[-]?L6\s',
                  'lumbar disc herniation','Herniated disc', 'Lumbar','Lumbar radiculopathy', 'Herniated lumbar disc'
                  ],

                  'drugs':['Celecoxib','Celebrex', 'Diclofenac Sodium', 'Baclofen', 
                          'Acetaminophen','Paracetamol','Gabapentin', 'Neurontin', 
                          'Pregabalin', 'Lyrica', 'Ibuprofen', 'Naproxen', 'Aleve','Flanax', 
                          'Methocarbamol', 'Robaxin', 'Carbamazepine', 'Tegretol', 
                          'Oxcarbazepine', 'Trileptal', 'L4[-]?[\s]?5', 'L5[-]?[\s]?S1',
                          'Topiramate','Topamax', 'Tizanidine[\s]?[HCl]?', 'Progesterone','Tramadol'],

                  'incl': ['Lower back pain','Unilateral','lower extremity','Foraminal stenosis', 'Radicular leg pain', 
                  'Foraminal narrowing','lower back spasm','chronic low back pain','Low back pain','Back pain','MRI  Lumbar spine', 
                  'emg/ncs','NCS/EMG','SLR Score','Carpel tunnel','Opiods','EMG','NCS',
                  'M54.5','M51.16','Intervertebral disc disorders with radiculopathy','M54.16',"lumbosacral region",'M48.06',
                  'Spinal stenosis','M48.061','lumbar region without neurogenic claudication','M47.26', 'sciatica',
                  'other spondylosis with radiculopathy','Asthma', '^L1|\sL1\s', '^L2|\sL2\s','^L4|\sL4\s','^L5|\sL5\s', 
                ]
            },

}


# REGEX keywords for general inclusion and exclusion

general_inclusion = ['bmi[\s]?[:]?[\s]?\d{2}[.]?[[0-9]{1,2}]?','body mass index[\s]?[:]?[\s]?\d{2}[.]?[[0-9]{1,2}]?',
                    'Moca[:]?[\s]?\d{1,2}',"MMSE[:]?[\s]?\d{1,2}",'mri brain','brain mri','slums \d{1,2}/30'
                    'mmse \d{1,2}','mmse score of \d{2}',"moca was \d{1,2}/30",'mri',"MOCA \d{1,2}/30",
                    'moca test was \d{1,2}','moca \d{1,2}','MMSE - \d{1,2}','\d+/\d+[\s]?mm[\s]?Hg','slums'                     
                    ]


general_exclusion = ['t1491x[a-z]', 'suicide attempt', 'heart disease', 'angiogram',
                     'alcoholism', 'liver disease', 'Dysthmic disorder','Manic depressive disorder',
                     'f1[0-9.]{2,5}', 'suicide attempt','pace maker','shunt','AAA endovascular repair',
                     'kidney disease',  'Respiratory failure', 'carcinoma', 'smoking', 'alcohol abuse','tobacco abuse',
                     'drug abuse','Stroke','sarcoma', 'lymphoma', 'blastoma', 'squamous cell carcinoma of skin',
                     ' c[0-7][0-9.]{1,5}','apixaban', 'dabigatran', 'pradaxa', 'suicidal',
                     'liver disease', 'liver failure', 'human immunodeficiency virus', 
                     'chronic kidney disease', 'chronic hepatitis b?c?3?4?5?', '^hiv|\shiv\s','^ckd|\sckd\s',
                     'Dilantin', 'Carbatrol', 'Lamictil', 'F05(?![a-z])','Delirium',
                     'Cardiac pacemaker','Cardiac stent','Coronary artery bypass','Muscle cramp',
                     'Traumatic Brain Injury', '^TBI|\sTBI ','basal cell', 'cervical cancer', 'prostate cancer', 
                     'malignant brain tumor','skin carcinoma','brain surgery', 'craniotomy',
                     'Meningioma','Bipolar disorder', 'Legally blind','Schizophrenia','Brain tumor', 
                     'Lymphoma',  'Chronic respiratory failure','Liver Failure', 'Human immunodeficiency virus',
                     'Suicide attempt',  'Major depression chronic','Major depression moderate recurrent',
                     'Major depression recurrent','Brain cancer',  'Normal pressure hydrocephalus', 'NPH',  
                     'Open heart surgery','Kidney surgery','Kidney replacement', 'Dialysis', '^esrd|\sesrd\s', 'bladder cancer',
                     "Leukoaraiosis" ,'End Stage Renal Disease','Brain surgery','^tia|\stia\s','cancer', 
                     'normal pressure hydrocephalus','cerebrovascular accident', 'cerebrovascular disease',
                     'psychosis', 'mental retardation', 'Dysthymic disorder','Cardiac ablation',
                     'Coronary artery bypass graft', 'Pacemaker','Ablation','Cardiac Cath','Nerve block','Epidural injection',
                     'Spinal injection','Local anesthesia','Lumbar operation','Lumbar percutaneous nucleotomy',
                     'Chemonucleolysis','intradiscal electrothermal treatment','Spondylolisthesis',
                     'bipolar 1 disorder', 'major depressive disorder','osteophytes',
                     'Copd' ,'chronic obstructive pulmonary disease', 'uncontrolled hypertension', 'type 1DM', 
                     'cardiovascular disease', 'pulmonary infarction', 'coronary heart failure', 
                     'arrhythmia', 'hepatitis C', '^STD|\sSTD\s' , 'Leukemia', 
                     'vitamin k deficiency', 'thrombocytopenia', 'liver cirrhosis', 'aplastic anemia', 'hemophilia', 
                     'coronary artery disease with angina pectoris','coronary artery disease without angina pectoris', 
                     '^MI\s|\sMI\s' ,'Myocardial infarction', 'opioid withdrawal syndrome', 'fibromyalgia', 
                     'Restless Leg syndrome', 'peripheral neuropathy', 'osteoporosis', 'osteoarthritis', 
                     'rheumatoid arthritis', 'gout', 'spondyloarthritis', 
                     'ankylosing spondylitis', 'spinal canal stenosis', 'spondylosis deformans', 'spinal deformity',
                     'Corticosteroid','Tapentadol','Meperidine','Opioid','Marijuana','Cannabis', 'cannabinoids',
                     'Warfarin','Cocaine','Heparin',
                     'Opioid abuse','Cardiac cath','Defibrillator','Bladder stim','Cochlear implant',
                    'Other metallic implants','^AIDS|\sAIDS\s',"drug abuse" ,"alcohol abuse","Aspirin", "clopidogrel","Plavix" ,
                    "Coumadin", "Jantovan", "Dabigatran", "Pradaxa", "Ribaroxaban", "Xarelto"
                     ]

#Full-form of condition keys

key_names         = {
                     "Memory related problems" : "mry-pblm",
                     "Alzheimer\'s Disease" : 'ad',  
                     "Parkinson\'s Disease" : 'pd',
                     "Amyotrophic Lateral Sclerosis" : 'als',
                     "Epilepsy" : 'epy',
                     "Lewy Body Disease" : 'lbd',
                     "Multiple Sclerosis" : 'ms',
                     "Diabetes Mellitus" :'hhs',
                     "Fronto-Temporal Dementia": 'ftd',
                     "Lumbar Disc Herniation": 'ldh',
                    }

condition_priority = {
                     "mry-pblm"  : 1,
                     "ad"  : 1, 
                     "pd"  : 1,
                     "als" : 1,
                     "epy" : 0,
                     "lbd" : 1,
                     "ms"  : 1,
                     "hhs" : 0,
                     "ftd" : 1,
                     "ldh" : 1,
                    }
icd_codes          = {
                      'mry-pblm': ['R41.3','G31.84','F01.50'],

                      'ad' : ['G30.0','G30.1','G30.8','G30.9','G30',],

                      'pd' : ['G20','G21','G22', ],                        
     
                      'als': ['335.20', 'G12.21'], 

                      'lbd': ['G31.83'],      

                      'ms' : ['G35'],   

                      'epy' : ['G40','G41',],

                      'hhs' : ['E11','E12','E13',] , 

                      'ftd' : ['G31.0','G31.01','G31.09'] , 
                    }

