from flask import Flask ,jsonify,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.debug = True
db = SQLAlchemy(app)

class Personne(db.Model):
    __tablename__ = 'personne'
    id = db.Column(db.Integer, primary_key=True)
    MainBranch=db.Column(db.String(255))
    Hobbyist=db.Column(db.String(255))
    OpenSourcer=db.Column(db.String(255))
    OpenSource=db.Column(db.String(255))
    Employment=db.Column(db.String(255))
    Country=db.Column(db.String(255))
    Student=db.Column(db.String(255))
    EdLevel=db.Column(db.String(255))
    UndergradMajor=db.Column(db.String(255))
    EduOther=db.Column(db.String(255))
    OrgSize=db.Column(db.String(255))
    DevType=db.Column(db.String(255))
    YearsCode=db.Column(db.String(255))
    Age1stCode=db.Column(db.String(255))
    YearsCodePro=db.Column(db.String(255))
    CareerSat=db.Column(db.String(255))
    JobSat=db.Column(db.String(255))
    MgrIdiot=db.Column(db.String(255))
    MgrMoney=db.Column(db.String(255))
    MgrWant=db.Column(db.String(255))
    JobSeek=db.Column(db.String(255))
    LastHireDate=db.Column(db.String(255))
    LastInt=db.Column(db.String(255))
    FizzBuzz=db.Column(db.String(255))
    JobFactors=db.Column(db.String(255))
    ResumeUpdate=db.Column(db.String(255))
    CurrencySymbol=db.Column(db.String(255))
    CurrencyDesc=db.Column(db.String(255))
    CompTotal=db.Column(db.String(255))
    CompFreq=db.Column(db.String(255))
    ConvertedComp=db.Column(db.String(255))
    WorkWeekHrs=db.Column(db.String(255))
    WorkPlan=db.Column(db.String(255))
    WorkChallenge=db.Column(db.String(255))
    WorkRemote=db.Column(db.String(255))
    WorkLoc=db.Column(db.String(255))
    ImpSyn=db.Column(db.String(255))
    CodeRev=db.Column(db.String(255))
    CodeRevHrs=db.Column(db.String(255))
    UnitTests=db.Column(db.String(255))
    PurchaseHow=db.Column(db.String(255))
    PurchaseWhat=db.Column(db.String(255))
    LanguageWorkedWith=db.Column(db.String(255))
    LanguageDesireNextYear=db.Column(db.String(255))
    DatabaseWorkedWith=db.Column(db.String(255))
    DatabaseDesireNextYear=db.Column(db.String(255))
    PlatformWorkedWith=db.Column(db.String(255))
    PlatformDesireNextYear=db.Column(db.String(255))
    WebFrameWorkedWith=db.Column(db.String(255))
    WebFrameDesireNextYear=db.Column(db.String(255))
    MiscTechWorkedWith=db.Column(db.String(255))
    MiscTechDesireNextYear=db.Column(db.String(255))
    DevEnviron=db.Column(db.String(255))
    OpSys=db.Column(db.String(255))
    Containers=db.Column(db.String(255))
    BlockchainOrg=db.Column(db.String(255))
    BlockchainIs=db.Column(db.String(255))
    BetterLife=db.Column(db.String(255))
    ITperson=db.Column(db.String(255))
    OffOn=db.Column(db.String(255))
    SocialMedia=db.Column(db.String(255))
    Extraversion=db.Column(db.String(255))
    ScreenName=db.Column(db.String(255))
    SOVisit1st=db.Column(db.String(255))
    SOVisitFreq=db.Column(db.String(255))
    SOVisitTo=db.Column(db.String(255))
    SOFindAnswer=db.Column(db.String(255))
    SOTimeSaved=db.Column(db.String(255))
    SOHowMuchTime=db.Column(db.String(255))
    SOAccount=db.Column(db.String(255))
    SOPartFreq=db.Column(db.String(255))
    SOJobs=db.Column(db.String(255))
    EntTeams=db.Column(db.String(255))
    SOComm=db.Column(db.String(255))
    WelcomeChange=db.Column(db.String(255))
    SONewContent=db.Column(db.String(255))
    Age=db.Column(db.String(255))
    Gender=db.Column(db.String(255))
    Trans=db.Column(db.String(255))
    Sexuality=db.Column(db.String(255))
    Ethnicity=db.Column(db.String(255))
    Dependents=db.Column(db.String(255))
    SurveyLength=db.Column(db.String(255))
    SurveyEase=db.Column(db.String(255))


    def __init__(self,MainBranch,Hobbyist,OpenSourcer,OpenSource,Employment,Country,Student,EdLevel,UndergradMajor,EduOther,OrgSize,DevType,YearsCode,Age1stCode,YearsCodePro,CareerSat,JobSat,MgrIdiot,MgrMoney,MgrWant,JobSeek,LastHireDate,LastInt,FizzBuzz,JobFactors,ResumeUpdate,CurrencySymbol,CurrencyDesc,CompTotal,CompFreq,ConvertedComp,WorkWeekHrs,WorkPlan,WorkChallenge,WorkRemote,WorkLoc,ImpSyn,CodeRev,CodeRevHrs,UnitTests,PurchaseHow,PurchaseWhat,LanguageWorkedWith,LanguageDesireNextYear,DatabaseWorkedWith,DatabaseDesireNextYear,PlatformWorkedWith,PlatformDesireNextYear,WebFrameWorkedWith,WebFrameDesireNextYear,MiscTechWorkedWith,MiscTechDesireNextYear,DevEnviron,OpSys,Containers,BlockchainOrg,BlockchainIs,BetterLife,ITperson,OffOn,SocialMedia,Extraversion,ScreenName,SOVisit1st,SOVisitFreq,SOVisitTo,SOFindAnswer,SOTimeSaved,SOHowMuchTime,SOAccount,SOPartFreq,SOJobs,EntTeams,SOComm,WelcomeChange,SONewContent,Age,Gender,Trans,Sexuality,Ethnicity,Dependents,SurveyLength,SurveyEase):
        self.MainBranch=MainBranch
        self.Hobbyist=Hobbyist
        self.OpenSourcer=OpenSourcer
        self.OpenSource=OpenSource
        self.Employment=Employment
        self.Country=Country
        self.Student=Student
        self.EdLevel=EdLevel
        self.UndergradMajor=UndergradMajor
        self.EduOther=EduOther
        self.OrgSize=OrgSize
        self.DevType=DevType
        self.YearsCode=YearsCode
        self.Age1stCode=Age1stCode
        self.YearsCodePro=YearsCodePro
        self.CareerSat=CareerSat
        self.JobSat=JobSat
        self.MgrIdiot=MgrIdiot
        self.MgrMoney=MgrMoney
        self.MgrWant=MgrWant
        self.JobSeek=JobSeek
        self.LastHireDate=LastHireDate
        self.LastInt=LastInt
        self.FizzBuzz=FizzBuzz
        self.JobFactors=JobFactors
        self.ResumeUpdate=ResumeUpdate
        self.CurrencySymbol=CurrencySymbol
        self.CurrencyDesc=CurrencyDesc
        self.CompTotal=CompTotal
        self.CompFreq=CompFreq
        self.ConvertedComp=ConvertedComp
        self.WorkWeekHrs=WorkWeekHrs
        self.WorkPlan=WorkPlan
        self.WorkChallenge=WorkChallenge
        self.WorkRemote=WorkRemote
        self.WorkLoc=WorkLoc
        self.ImpSyn=ImpSyn
        self.CodeRev=CodeRev
        self.CodeRevHrs=CodeRevHrs
        self.UnitTests=UnitTests
        self.PurchaseHow=PurchaseHow
        self.PurchaseWhat=PurchaseWhat
        self.LanguageWorkedWith=LanguageWorkedWith
        self.LanguageDesireNextYear=LanguageDesireNextYear
        self.DatabaseWorkedWith=DatabaseWorkedWith
        self.DatabaseDesireNextYear=DatabaseDesireNextYear
        self.PlatformWorkedWith=PlatformWorkedWith
        self.PlatformDesireNextYear=PlatformDesireNextYear
        self.WebFrameWorkedWith=WebFrameWorkedWith
        self.WebFrameDesireNextYear=WebFrameDesireNextYear
        self.MiscTechWorkedWith=MiscTechWorkedWith
        self.MiscTechDesireNextYear=MiscTechDesireNextYear
        self.DevEnviron=DevEnviron
        self.OpSys=OpSys
        self.Containers=Containers
        self.BlockchainOrg=BlockchainOrg
        self.BlockchainIs=BlockchainIs
        self.BetterLife=BetterLife
        self.ITperson=ITperson
        self.OffOn=OffOn
        self.SocialMedia=SocialMedia
        self.Extraversion=Extraversion
        self.ScreenName=ScreenName
        self.SOVisit1st=SOVisit1st
        self.SOVisitFreq=SOVisitFreq
        self.SOVisitTo=SOVisitTo
        self.SOFindAnswer=SOFindAnswer
        self.SOTimeSaved=SOTimeSaved
        self.SOHowMuchTime=SOHowMuchTime
        self.SOAccount=SOAccount
        self.SOPartFreq=SOPartFreq
        self.SOJobs=SOJobs
        self.EntTeams=EntTeams
        self.SOComm=SOComm
        self.WelcomeChange=WelcomeChange
        self.SONewContent=SONewContent
        self.Age=Age
        self.Gender=Gender
        self.Trans=Trans
        self.Sexuality=Sexuality
        self.Ethnicity=Ethnicity
        self.Dependents=Dependents
        self.SurveyLength=SurveyLength
        self.SurveyEase=SurveyEase
@app.route('/personneget', methods=['GET'])
def getpersons():
    all_persons = Personne.query.all()
    result = []
    print(type(all_persons[0]))
    print(all_persons[0])
    for person in all_persons:
        person_data = {}
        person_data['id'] = person.id
        person_data['nom'] = person.nom
        person_data['prenom'] = person.prenom
        person_data['age'] = person.age
        person_data['email'] = person.email
        result.append(person_data)
    return jsonify(result)

@app.route('/personnepost', methods=['POST'])
def addperson():
    data = request.get_json()
    new_person = Personne(data['nom'], data['prenom'], data['age'], data['email'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify(data)

# put method
@app.route('/personneput', methods=['PUT'])
def updateperson():
    data = request.get_json()
    person = Personne.query.get(data['id'])
    person.nom = data['nom']
    person.prenom = data['prenom']
    person.age = data['age']
    person.email = data['email']
    db.session.commit()
    return jsonify(data)
# delete method
@app.route('/personnedelete', methods=['DELETE'])
def deleteperson():
    data = request.get_json()
    person = Personne.query.get(data['id'])
    db.session.delete(person)
    db.session.commit()
    return jsonify(data)
#export to excel

    