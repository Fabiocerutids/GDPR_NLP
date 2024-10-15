question_answers = ['C','D','A','A','B','B','A','B','D','C','C','C','A','B','B','B','A','D','C','B','A','C','C','A','C','C','A','C','C','C','C','D','A','C','C','B','A','B','D','B']
question_list = [
"""A shopkeeper wants to register how many visitors enter his shop every day. A system detects the
MAC-address of each visitor's smartphone. It is impossible for the shopkeeper to identify the
owner of the phone from this signal, but telephone providers can link the MAC-address to the
owner of the phone.
According to the GDPR, is the shopkeeper allowed to use this method?
A) Yes, because the shopkeeper cannot identify the owner of the telephone.
B) Yes, because the visitor has automatically consented by connecting to the Wi-Fi.
C) No, because the telephone’s MAC-address must be regarded as personal data.
D) No, because the telephone providers are the owners of the MAC-addresses. 
""",
"""
Personal data as defined in the GDPR can be divided into several types. One of these types is
described:
Data that directly or indirectly reveal someone's racial or ethnic background, political, philosophical,
religious views, union affiliation and data related to health or sex life and sexual orientation.
What type of personal data is this?
A) Direct personal data
B) Indirect personal data
C) Pseudonymized data
D) Special category personal data 
""",
"""
A security breach has occurred in an information system that also holds personal data.
According to the GDPR, what is the very first thing the controller must do?
A) Ascertain whether the breach may have resulted in loss or unlawful processing of personal data
B) Assess the risk of adverse effects to the data subjects using a data protection impact assessment
(DPIA)
C) Assess whether personal data of a sensitive nature has or may have been unlawfully processed
D) Report the breach immediately to all data subjects and the relevant supervisory authority
""",
"""
A natural or legal person, public authority, agency or other body which, alone or jointly with others,
determines the purposes and means of the processing of personal data.
Which role in data protection is defined here?
A) Controller
B) Processor
C) Supervisory authority
D) Third party 
""",
"""
A breach of security that leads to the accidental or unlawful destruction, loss, alteration, unauthorized
disclosure of, or access to, personal data transmitted, stored or otherwise processed.
What is the exact term that is associated with this definition in the GDPR?
A) Confidentiality violation
B) Personal data breach
C) Security breach
D) Security incident
""",
"""
Which data subject right is explicitly defined by the GDPR?
A) A copy of personal data must be provided in the format requested by the data subject.
B) Access to personal data must be provided free of charge for the data subject.
C) Personal data must always be changed at the request of the data subject.
D) Personal data must always be erased if the data subject requests this. 
""",
"""
When personal data are processed, who is ultimately responsible for demonstrating compliance
with the GDPR?
A) Controller
B) Data protection officer (DPO)
C) Processor
D) Supervisory authority
""",
"""
According to the principle of purpose limitation, data should not be processed beyond the
legitimate purpose defined. However, further processing is allowed in a few specific cases,
provided that appropriate safeguards for the rights and freedoms of the data subjects are taken.
For which purpose is further processing not allowed?
A) For archiving purposes in the public interest
B) For direct marketing and commercial purposes
C) For generalized statistical purposes
D) For scientific or historical research purposes
""",
"""
According to the GDPR, in what situation must data subjects always be notified of a personal data
breach?
A) When personal data is processed at a facility of the processor that is not located within the borders of
the EEA
B) When personal data is processed by a party that agreed to the draft processing contract but has not
yet sign it
C) When the system on which the personal data is processed is attacked causing damage to its storage
devices
D) When there is a significant probability that the breach will lead to a high risk for the privacy of the data
subjects 
""",
"""
Some data processing falls outside of the material scope of the GDPR.
What type of processing is not subject to the GDPR?
A) Collecting name and address information for a gymnastics club
B) Creating a back-up of biometric data for data security purposes
C) Editing personal photographs before printing them at home 
""",
"""
The GDPR does not define privacy as a term but uses the concept implicitly throughout the text.
What is a correct definition of privacy as implicitly used throughout the GDPR?
A) The fundamental right to protection of personal data, regardless of how it was obtained
B) The right not to be disturbed by uninvited people, nor being followed, spied on or monitored
C) The right to respect for one's private and family life, home and personal correspondence
D) The right to freedom of opinion and expression and to seeking, receiving and imparting information 
""",
"""
What is the relationship between data protection and privacy?
A) Data protection and privacy are synonyms and have the same meaning.
B) Data protection is the part of privacy that protects a person’s physical integrity.
C) Data protection refers to the measures needed to protect a person’s privacy. 
""",
"""
What is the legal status of the GDPR?
A) The GDPR is functional law in all member states of the EEA. Some Articles allow for member states
law to provide for more specific rules.
B) The GDPR is a recommendation of the European Commission that EEA countries' law authorities
improve their laws on the protection of personal data.
C) The GDPR sets out minimum conditions and requirements. Member states need to pass national laws
to meet these minimum requirements. 
""",
"""
In the GDPR, some types of personal data are regarded as special category personal data.
Which personal data are considered special category personal data?
A) A list of payments made using a credit card
B) An address list of members of a political party
C) A genealogical register of someone’s ancestors 
""",
"""
To plan the amount of parking space needed, a local government monitors and saves the license
plate number of every car that enters and leaves the city center. They have obtained permission to
collect data on the number of cars present in the city center.
By comparing the license plate time of entry and exit the number of cars present every moment of
each day is calculated. Each month a report is created detailing the average number of cars in the
city center at specific moments for every day of the week. At every entrance to the city center, a
billboard clearly states what data is collected by whom, the purpose of the processing and the fact
that the license plate numbers are saved securely for up to two years, because the measurements
will be repeated next year.
Which of the basic principles for legitimate processing of personal data is violated in this scenario?
A) Personal data are collected for specified, explicit and legitimate purposes and not further processed.
B) Personal data are kept in a form permitting identification of data subjects for no longer than is
necessary.
C) Personal data are processed in a manner that ensures appropriate security of the personal data.
D) Personal data are processed in a transparent manner in relation to the data subject.
""",
"""
Personal data shall be adequate, relevant and limited to what is necessary in relation to the purposes
for which they are processed.
Which data processing principle is described here?
A) Accuracy
B) Data minimization
C) Fairness and transparency
D) Purpose limitation 
""",
"""
A person is moving from city A to city B, within an EEA member state. In city A he was a patient of
the local hospital A. In city B, he becomes a patient of hospital B. The patient has opted out of the
national electronic patients file system.
The patient asks hospital A to forward his medical file directly to hospital B.
According to the GDPR, what is allowed?
A) The hospital in A can send the data directly to hospital B, as requested by the patient.
B) The hospital in A can send the file to hospital B, before the patient has requested it.
C) The hospital in A can send the medical file to the data subject, but not to another hospital.
D) The hospital in A cannot send the file, because there is no legitimate ground for processing. 
""",
"""
A company is planning to process personal data. The recently appointed data protection officer
(DPO) executes a data protection impact assessment (DPIA). The DPO finds that all computers
have a setting causing monitors to show a screen saver after five seconds of inaction. However,
the computers are not locked automatically. When employees leave their desk, they usually do not
lock their computers either.
What is this an example of?
A) Data access
B) Personal data breach
C) Security incident
D) Security vulnerability 
""",
"""
The GDPR refers to the principles of proportionality and subsidiarity.
What is the meaning of subsidiarity in this context?
A) Personal data can only be processed in accordance with the purpose specification.
B) Personal data cannot be reused without explicit and informed consent.
C) Personal data may only be processed when there are no other means to achieve the purposes.
D) Personal data must be adequate, relevant and not excessive in relation to the purposes. 
""",
"""
”The controller shall implement appropriate technical and organizational measures for ensuring that
(.) only personal data which are necessary for each specific purpose of the processing are
processed.”
Which term in the GDPR is defined here?
A) Compliance
B) Data protection by design and by default
C) Embedded data protection 
""",
"""
While performing a backup, a data server disk crashed. Both the data and the backup are lost. The
disk contained personal data, but no special category personal data.
The processor states that this is a personal data breach.
Is the statement of the processor true?
A) Yes, because the personal data on the disk were unlawfully processed.
B) Yes, because there were no special category personal data stored on the disk.
C) No, because no personal data on the disk were processed, only destroyed.
D) No, because this is only a security incident and not a data breach. 
""",
"""
Organizations are obliged to keep a number of records to demonstrate compliance with the GDPR.
Which record is not obligatory according to the GDPR?
A) A record of all intended processing together with the processing purpose(s) and legal justifications
B) A record of data breaches with all relevant characteristics, including notifications
C) A record of notifications sent to the supervisory authority regarding processing of personal data
D) A record of processors including personal data provided and the period this data can be retained 
""",
"""
A personal data breach has occurred, and the controller is writing a draft notification for the
supervisory authority. The following information is already in the notification:
- The nature of the personal data breach and its possible consequences.
- Information regarding the parties that can provide additional information about the data breach.
What other information must the controller provide?
A) Information of local and national authorities that were informed about the data breach
B) Name and contact details of the data subjects whose data may have been breached
C) Suggested measures to mitigate the adverse consequences of the data breach
D) The information needed to access the personal data that have been breached 
""",
"""
According to Article 33 of the GDPR the controller shall without undue delay and, where feasible,
not later than 72 hours after having become aware of it, notify a personal data breach to the
supervisory authority.
What is the maximum penalty for non-compliance with this notification obligation?
A) € 10.000.000 or 2% of the annual global turnover, whichever is higher
B) € 20.000.000 or 4% of the annual global turnover, whichever is higher
C) Up to € 500.000 with a minimum of € 120.000
D) Up to € 820.000 with a minimum of € 350.000 
""",
"""
According to the GDPR, what is a task of a supervisory authority?
A) Implement technical and organizational measures to ensure compliance
B) Investigate security breaches of corporate information
C) Monitor and enforce the application of the GDPR 
""",
"""
A Belgian company has their headquarters in France for tax purposes. They enter into a legally
binding contract with a processor in the Netherlands for the processing of personal data of data
subjects with various nationalities.
A personal data breach occurs. The supervisory authorities start an investigation.
Why is the French supervisory authority seen as the lead supervisory authority?
A) Because France is located in the middle of Europe
B) Because France is the largest of the three EEA countries
C) Because the company has their headquarters in France 
""",
"""
On July 10, 2023 the European Commission implemented a ruling regarding the transfer of
personal data between the EEA and the US. The ruling is based on the data protection measures
described in the EU-US Data Privacy Framework.
What kind of a ruling is this?
A) Adequacy decision
B) Derogation
C) Legally binding contract
D) Treaty superseding the GDPR
""",
"""
A controller wants to outsource processing of personal data to a processor.
What must be done before outsourcing?
A) The controller must ask the supervisory authority for permission to outsource the processing of the
data.
B) The controller must ask the supervisory authority if the agreed written contract is compliant with the
regulations.
C) The controller and processor must draft and sign a written contract guaranteeing the confidentiality of
the data.
D) The processor must show the controller that all demands agreed in the service level agreement (SLA)
are met. 
""",
"""
What is the purpose of a data protection audit by the supervisory authority?
A) To advise the controller on the mitigation of privacy risks to protect the controller from liability claims
for non-compliance.
B) To fulfill the obligation in the GDPR to implement appropriate technical and organizational measures
for data protection.
C) To monitor and enforce the application of the GDPR by assessing that processing is performed in
compliance with the GDPR.
""",
"""
In order for personal data processing to be lawful, what is always a requirement?
A) A code of conduct must be in place, describing what the processing exactly entails.
B) The processing must be reported to and allowed by the supervisory authority.
C) There must be a legitimate ground for the processing of personal data. 
""",
"""
Personal data can be transferred outside of the EEA.
According to the GDPR, which transfers outside the EEA are always lawful?
A) Transfers based on the laws of the non-EEA country concerned
B) Transfers falling under World Trade Organization (WTO) rules
C) Transfers governed by approved binding corporate rules (BCR)
D) Transfers within a global corporation or organization
""",
"""
According to the GDPR, what is a description of binding corporate rules (BCR)?
A) A decision on the safety of transferring personal data to a non-EEA country
B) A measure to compensate for the lack of personal data protection in a third country
C) A set of agreements covering personal data transfers between non-EEA countries
D) A set of approved rules on personal data protection used by a group of enterprises 
""",
"""
A written contract between a controller and a processor is called a data processing agreement.
According to the GDPR, what does not have to be covered in the written contract?
A) The contractor code of business ethics and conduct that is used.
B) The information security and personal data breach procedures
C) The technical and organizational measures implemented
D) Which data are covered by the data processing agreement 
""",
"""
One of the objectives of a data protection impact assessment (DPIA) is to strengthen the
confidence of customers or citizens in the way personal data is processed and privacy is
respected.
How can a DPIA strengthen the confidence?
A) The organization minimizes the risk of costly adjustments in processes or the redesign of systems in
a later stage.
B) The organization prevents non-compliance with the GDPR and minimizes the risk of fines.
C) The organization proves that it takes privacy seriously and aims for compliance with the GDPR. 
""",
"""
One of the seven principles of data protection by design is Functionality – Positive-Sum, not ZeroSum.
What is the essence of this principle?
A) Applied security standards must assure the confidentiality, integrity and availability of personal data
throughout their lifecycle.
B) If different types of legitimate objectives are contradictory, the privacy objectives must be given
priority over other security objectives.
C) When embedding privacy into a given technology, process, or system, it should be done in such a way
that full functionality is not impaired.
D) Wherever possible, detailed privacy impact and risk assessments should be carried out and published,
clearly documenting the privacy risks. 
""",
"""
A company wishes to use personal data of their customers. They wish to start sending all female
customers a customized newsletter.
What right do all data subjects have in this scenario?
A) The right to compensation
B) The right to object to profiling
C) The right to rectification 
""",
"""
What is a description of data protection by design and by default?
A) An approach that implements data protection from the start
B) An indication of timeframes if processing relates to erasure
C) Data may only be collected for explicit and legitimate purposes
D) Not holding more data than is strictly required for processing 
""",
"""
According to the GDPR, when is a data protection impact assessment (DPIA) obligatory?
A) When a project includes technologies or processes that use personal data
B) When processing is likely to result in a high risk to the rights of data subjects
C) When similar processing operations with comparable risks are repeated 
""",
"""
The GDPR describes the principle of data minimization.
How can organizations comply with this principle?
A) By applying the concept of least privilege to the personal data collected, stored or otherwise
processed
B) By limiting access rights to staff who need the personal data for the intended processing operations
C) By limiting file sizes, through saving all personal data that is processed in the smallest possible
format
D) By limiting the personal data to what is adequate, relevant and necessary for the processing purposes
""",
"""
What is the main use of a persistent cookie?
A) To ensure that the user’s personal data are stored securely on the server
B) To personalize the user’s experience of the website during a next visit
C) To record every keystroke made by a computer user to find out passwords
D) To save the pages a user has bookmarked in the user’s browser history 
"""
]