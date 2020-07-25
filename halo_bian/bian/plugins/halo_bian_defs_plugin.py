from halo_bian.bian.bian import FunctionalPatterns



class BianPlugin():

    patterns = None
    assets = None

    def __init__(self):
        self.do_patterns()
        self.do_assets()
        
    def do_patterns(self):
        table = {}
        table["Transaction Engine"] = "Fulfill"
        table["Reward Points Account"] = "Track"
        table["Product Combination"] = "Fulfill"
        table["Position Management"] = "Monitor"
        table["Position Keeping"] = "Track"
        table["Fraud Evaluation"] = "Assess"
        table["Fraud Diagnosis"] = "Analyze"
        table["Customer Position"] = "Analyze"
        table["Counterparty Risk"] = "Monitor"
        table["Accounts Receivable"] = "Process"
        table["Account Reconciliation"] = "Process"
        table["Stock Lending/Repos"] = "Transact"
        table["Corporate Treasury Analysis"] = "Analyze"
        table["Corporate Treasury"] = "Manage"
        table["Bank Portfolio Analysis"] = "Analyze"
        table["Bank Portfolio Administration"] = "Administer"
        table["Asset Securitization"] = "Transact"
        table["Asset & Liability Management"] = "Direct"
        table["Utilities Administration"] = "Administer"
        table["Site Operations"] = "Administer"
        table["Site Administration"] = "Administer"
        table["Property Portfolio"] = "Analyze"
        table["Equipment Maintenance"] = "Maintain"
        table["Equipment Administration"] = "Administer"
        table["Building Maintenance"] = "Maintain"
        table["Segment Direction"] = "Direct"
        table["Product Portfolio"] = "Analyze"
        table["Market Research"] = "Process"
        table["Market Analysis"] = "Analyze"
        table["Customer Portfolio"] = "Analyze"
        table["Contribution Analysis"] = "Analyze"
        table["Competitor Analysis"] = "Analyze"
        table["Channel Portfolio"] = "Analyze"
        table["Branch Portfolio"] = "Analyze"
        table["Organization Direction"] = "Direct"
        table["Business Unit Management"] = "Manage"
        table["Business Unit Financial Operations"] = "Administer"
        table["Business Unit Financial Analysis"] = "Analyze"
        table["Business Unit Direction"] = "Direct"
        table["Business Unit Accounting"] = "Track"
        table["Products & Services Direction"] = "Direct"
        table["Corporate Strategy"] = "Direct"
        table["Corporate Policies"] = "Design"
        table["Continuity Planning"] = "Manage"
        table["Business Architecture"] = "Design"
        table["Merchant Relations"] = "Agree Terms"
        table["Merchant Acquiring Facility"] = "Fulfill"
        table["Credit/Charge Card"] = "Fulfill"
        table["Card Network Participant Facility"] = "Fulfill"
        table["Card Capture"] = "Transact"
        table["Card Billing & Payments"] = "Transact"
        table["Card Authorization"] = "Assess"
        table["Product Inventory Item Management"] = "Allocate"
        table["Product Inventory Distribution"] = "Administer"
        table["E-Branch Operations"] = "Operate"
        table["E-Branch Management"] = "Manage"
        table["Contact Center Operations"] = "Administer"
        table["Contact Center Management"] = "Manage"
        table["Card Terminal Operation"] = "Operate"
        table["Card Terminal Administration"] = "Administer"
        table["Branch Network Management"] = "Manage"
        table["Branch Location Operations"] = "Administer"
        table["Branch Location Management"] = "Manage"
        table["Branch Currency Management"] = "Allocate"
        table["Branch Currency Distribution"] = "Process"
        table["ATM Network Operations"] = "Operate"
        table["ATM Network Management"] = "Manage"
        table["Advanced Voice Services Operations"] = "Operate"
        table["Advanced Voice Services Management"] = "Manage"
        table["Collections"] = "Process"
        table["Collateral Asset Administration"] = "Administer"
        table["Collateral Allocation Management"] = "Allocate"
        table["Trust Services"] = "Fulfill"
        table["Service Product"] = "Fulfill"
        table["Remittances (Old)"] = "Transact"
        table["Customer Tax Handling"] = "Fulfill"
        table["Currency Exchange"] = "Transact"
        table["Corporate Trust Services"] = "Fulfill"
        table["Consumer Investments"] = "Fulfill"
        table["Consumer Advisory Services"] = "Fulfill"
        table["Brokered Product"] = "Manage"
        table["Bank Drafts & Travelers Checks"] = "Transact"
        table["Public Offering"] = "Fulfill"
        table["Private Placement"] = "Fulfill"
        table["M&A Advisory"] = "Fulfill"
        table["Corporate Tax Advisory"] = "Fulfill"
        table["Corporate Finance"] = "Fulfill"
        table["Regulatory & Legal Authority"] = "Manage"
        table["Investor Relations"] = "Enroll"
        table["Corporate Relationship"] = "Manage"
        table["Corporate Communications"] = "Manage"
        table["Corporate Alliance/Stake Holder"] = "Manage"
        table["Transaction Authorization"] = "Assess"
        table["Servicing Event History"] = "Track"
        table["Servicing Activity Analysis"] = "Analyze"
        table["Point of Service"] = "Operate"
        table["Party Authentication"] = "Assess"
        table["Interactive Help"] = "Operate"
        table["Customer Workbench"] = "Operate"
        table["Contact Routing"] = "Allocate"
        table["Contact Handler"] = "Operate"
        table["Contact Dialogue"] = "Process"
        table["Sales Product Agreement"] = "Agree Terms"
        table["Customer Relationship Management"] = "Manage"
        table["Customer Reference Data Management"] = "Catalog"
        table["Customer Proposition"] = "Agree Terms"
        table["Customer Product/Service Eligibility"] = "Assess"
        table["Customer Precedents"] = "Process"
        table["Customer Event History"] = "Track"
        table["Customer Credit Rating"] = "Monitor"
        table["Customer Behavioral Insights"] = "Analyze"
        table["Customer Agreement"] = "Agree Terms"
        table["Customer Access Entitlement"] = "Agree Terms"
        table["Account Recovery"] = "Process"
        table["Document Services"] = "Operate"
        table["Correspondence"] = "Operate"
        table["Archive Services"] = "Operate"
        table["Syndicate Management"] = "Enroll"
        table["Sub Custodian Agreement"] = "Agree Terms"
        table["Product Service Agency"] = "Agree Terms"
        table["Product Broker Agreement"] = "Agree Terms"
        table["Interbank Relationship Management"] = "Manage"
        table["Information Provider Administration"] = "Agree Terms"
        table["Correspondent Bank Relationship Management"] = "Manage"
        table["Correspondent Bank Data Management"] = "Catalog"
        table["Contractor/Supplier Agreement"] = "Agree Terms"
        table["Financial Statements"] = "Analyze"
        table["Financial Control"] = "Assess"
        table["Financial Compliance"] = "Process"
        table["Enterprise Tax Administration"] = "Manage"
        table["Workforce Training"] = "Administer"
        table["Travel & Expenses"] = "Administer"
        table["Recruitment"] = "Process"
        table["Human Resources Direction"] = "Direct"
        table["Employee/Contractor Contract"] = "Agree Terms"
        table["Employee Payroll & Incentives"] = "Process"
        table["Employee Evaluation"] = "Analyze"
        table["Employee Data Management"] = "Catalog"
        table["Employee Certification"] = "Assess"
        table["Employee Benefits"] = "Administer"
        table["Employee Assignment"] = "Allocate"
        table["Employee Access"] = "Assess"
        table["Investment Portfolio Planning"] = "Agree Terms"
        table["Investment Portfolio Management"] = "Fulfill"
        table["Investment Portfolio Analysis"] = "Analyze"
        table["eTrading Workbench"] = "Operate"
        table["Systems Operations"] = "Operate"
        table["Systems Help Desk"] = "Operate"
        table["Systems Assurance"] = "Assess"
        table["Systems Administration"] = "Administer"
        table["System Development"] = "Develop"
        table["System Deployment"] = "Develop"
        table["Production Release"] = "Assess"
        table["Platform Operations"] = "Operate"
        table["IT Systems Direction"] = "Direct"
        table["IT Standards & Guidelines"] = "Design"
        table["Internal Network Operation"] = "Operate"
        table["Development Environment"] = "Administer"
        table["Management Manual"] = "Design"
        table["Knowledge Exchange"] = "Operate"
        table["Intellectual Property Portfolio"] = "Administer"
        table["Savings Account"] = "Fulfill"
        table["Mortgage Loan"] = "Fulfill"
        table["Merchandising Loan"] = "Fulfill"
        table["Loan"] = "Fulfill"
        table["Leasing"] = "Fulfill"
        table["Fiduciary Agreement"] = "Fulfill"
        table["Deposit Account"] = "Fulfill"
        table["Current Account"] = "Fulfill"
        table["Corporate Loan"] = "Fulfill"
        table["Corporate Lease"] = "Fulfill"
        table["Corporate Deposits"] = "Fulfill"
        table["Corporate Current Account"] = "Fulfill"
        table["Consumer Loan"] = "Fulfill"
        table["Quant Model"] = "Design"
        table["Public Reference Data Management"] = "Design"
        table["Market Information Management"] = "Administer"
        table["Market Data Switch Operation"] = "Operate"
        table["Market Data Switch Administration"] = "Administer"
        table["Location Data Management"] = "Catalog"
        table["Information Provider Operation"] = "Operate"
        table["Financial Market Research"] = "Administer"
        table["Financial Market Analysis"] = "Analyze"
        table["Financial Instrument Reference Data Management"] = "Catalog"
        table["Counterparty Administration"] = "Administer"
        table["Unit Trust Administration"] = "Administer"
        table["Trade/Price Reporting"] = "Operate"
        table["Trade Confirmation Matching"] = "Operate"
        table["Settlement Obligation Management"] = "Transact"
        table["Securities Fails Processing"] = "Manage"
        table["Securities Delivery & Receipt Management"] = "Transact"
        table["Order Allocation"] = "Transact"
        table["Mutual Fund Administration"] = "Administer"
        table["Hedge Fund Administration"] = "Administer"
        table["Financial Instrument Valuation"] = "Process"
        table["Custody Administration"] = "Fulfill"
        table["Corporate Events"] = "Process"
        table["Prospect Campaign Management"] = "Analyze"
        table["Prospect Campaign Design"] = "Design"
        table["Promotional Events"] = "Manage"
        table["Customer Surveys"] = "Process"
        table["Customer Campaign Management"] = "Manage"
        table["Customer Campaign Design"] = "Design"
        table["Business Development"] = "Direct"
        table["Brand Management"] = "Manage"
        table["Advertising"] = "Manage"
        table["Production Risk Models"] = "Design"
        table["Operational Risk Models"] = "Design"
        table["Market Risk Models"] = "Design"
        table["Liquidity Risk Models"] = "Design"
        table["Gap Analysis"] = "Analyze"
        table["Fraud Models"] = "Design"
        table["Financial Instrument Valuation Models"] = "Design"
        table["Economic Capital"] = "Analyze"
        table["Customer Behavior Models"] = "Design"
        table["Credit/Margin Management"] = "Direct"
        table["Credit Risk Models"] = "Design"
        table["Contribution Models"] = "Design"
        table["Business Risk Models"] = "Design"
        table["Security Assurance"] = "Assess"
        table["Security Advisory"] = "Process"
        table["Procurement"] = "Administer"
        table["Legal Compliance"] = "Assess"
        table["Internal Audit"] = "Assess"
        table["Fixed Asset Register"] = "Administer"
        table["Company Billing & Payments"] = "Process"
        table["Approved Supplier Directory"] = "Enroll"
        table["Reward Points Awards & Redemption"] = "Transact"
        table["Open Item Management"] = "Process"
        table["Leasing Item Administration"] = "Administer"
        table["Issued Device Tracking"] = "Monitor"
        table["Issued Device Administration"] = "Allocate"
        table["Dunning"] = "Process"
        table["Disbursement"] = "Transact"
        table["Delinquent Account Handling"] = "Process"
        table["Customer Billing"] = "Process"
        table["Channel Activity History"] = "Track"
        table["Channel Activity Analysis"] = "Analyze"
        table["Card Transaction Switch"] = "Operate"
        table["Card Collections"] = "Process"
        table["Party Data Management"] = "Catalog"
        table["Customer Profile"] = "Monitor"
        table["Payment Order"] = "Process"
        table["Payment Execution"] = "Process"
        table["Financial Message Analysis"] = "Analyze"
        table["Financial Gateway"] = "Operate"
        table["Correspondent Bank"] = "Fulfill"
        table["Cheque Processing"] = "Operate"
        table["Central Cash Handling"] = "Allocate"
        table["Card Financial Settlement"] = "Process"
        table["Card eCommerce Gateway"] = "Operate"
        table["Card Clearing"] = "Process"
        table["ACH Fulfillment"] = "Operate"
        table["Special Pricing Conditions"] = "Catalog"
        table["Product Training"] = "Process"
        table["Product Quality Assurance"] = "Assess"
        table["Product Directory"] = "Catalog"
        table["Product Design"] = "Design"
        table["Product Deployment"] = "Develop"
        table["Discount Pricing"] = "Assess"
        table["Regulatory Reporting"] = "Administer"
        table["Regulatory Compliance"] = "Assess"
        table["Guideline Compliance"] = "Assess"
        table["Fraud/AML Resolution"] = "Process"
        table["Financial Accounting"] = "Track"
        table["Compliance Reporting"] = "Administer"
        table["Underwriting"] = "Assess"
        table["Sales Product"] = "Agree Terms"
        table["Sales Planning"] = "Direct"
        table["Prospect Campaign Execution"] = "Process"
        table["Product Sales Support"] = "Administer"
        table["Product Matching"] = "Assess"
        table["Product Expert Sales Support"] = "Administer"
        table["Party Lifecycle Management"] = "Process"
        table["Lead/Opportunity Management"] = "Process"
        table["Customer Offer"] = "Process"
        table["Customer Campaign Execution"] = "Process"
        table["Commissions"] = "Transact"
        table["Commission Agreement"] = "Agree Terms"
        table["Servicing Order"] = "Process"
        table["Servicing Mandate"] = "Agree Terms"
        table["Servicing Issue"] = "Process"
        table["Payment Initiation"] = "Transact"
        table["Customer Case Management"] = "Manage"
        table["Customer Case"] = "Process"
        table["Case Root Cause Analysis"] = "Analyze"
        table["Card Case"] = "Process"
        table["Trade Finance"] = "Fulfill"
        table["Syndicated Loan"] = "Fulfill"
        table["Project Finance"] = "Fulfill"
        table["Limit & Exposure Management"] = "Manage"
        table["Letter of Credit"] = "Transact"
        table["Factoring"] = "Fulfill"
        table["Direct Debit Mandate"] = "Fulfill"
        table["Direct Debit"] = "Fulfill"
        table["Credit Management"] = "Monitor"
        table["Credit Facility"] = "Fulfill"
        table["Cheque Lock Box"] = "Fulfill"
        table["Cash Management & Account Services"] = "Fulfill"
        table["Bank Guarantee"] = "Fulfill"
        table["Trading Models"] = "Design"
        table["Trading Book Oversight"] = "Manage"
        table["Traded Position Management"] = "Transact"
        table["Suitability Checking"] = "Assess"
        table["Quote Management"] = "Process"
        table["Program Trading"] = "Operate"
        table["Market Order Execution"] = "Transact"
        table["Market Order"] = "Transact"
        table["Market Making"] = "Fulfill"
        table["ECM/DCM"] = "Fulfill"
        table["Dealer Workbench"] = "Operate"
        table["Credit Risk Operations"] = "Monitor"
        self.patterns = table
        
    def do_assets(self):
        table = {}
        table["Transaction Engine"] = "TransactionSchedule"
        table["Reward Points Account"] = "RewardPoints"
        table["Product Combination"] = "ProductCombination"
        table["Position Management"] = "FinancialPosition"
        table["Position Keeping"] = "FinancialPosition"
        table["Fraud Evaluation"] = ""
        table["Fraud Diagnosis"] = ""
        table["Customer Position"] = "CustomerPosition"
        table["Counterparty Risk"] = "CounterpartyCreditRisk"
        table["Accounts Receivable"] = "AccountsReceivable"
        table["Account Reconciliation"] = "AccountReconciliation"
        table["Stock Lending/Repos"] = "Repo"
        table["Corporate Treasury Analysis"] = "CorporateTreasury"
        table["Corporate Treasury"] = "CorporateTreasury"
        table["Bank Portfolio Analysis"] = "Asset&LiabilityPortfolio"
        table["Bank Portfolio Administration"] = "Asset&LiabilityPortfolio"
        table["Asset Securitization"] = "AssetSecuritization"
        table["Asset & Liability Management"] = "Asset&LiabilityPortfolio"
        table["Utilities Administration"] = "Utilities"
        table["Site Operations"] = "BuildingServices"
        table["Site Administration"] = "Building"
        table["Property Portfolio"] = "BuildingPortfolio"
        table["Equipment Maintenance"] = "OfficeEquipment"
        table["Equipment Administration"] = "OfficeEquipment"
        table["Building Maintenance"] = "Building"
        table["Segment Direction"] = "Segment"
        table["Product Portfolio"] = "ProductPortfolio"
        table["Market Research"] = "GeneralMarketResearch"
        table["Market Analysis"] = "GeneralMarketResearch"
        table["Customer Portfolio"] = "CustomerSegment"
        table["Contribution Analysis"] = "Contribution"
        table["Competitor Analysis"] = "Competitor"
        table["Channel Portfolio"] = "ChannelPortfolio"
        table["Branch Portfolio"] = "BranchNetwork"
        table["Organization Direction"] = "Organization"
        table["Business Unit Management"] = "BusinessUnit"
        table["Business Unit Financial Operations"] = "BusinesUnitBudegt"
        table["Business Unit Financial Analysis"] = "BusinessUnitFinance"
        table["Business Unit Direction"] = "BusinessUnit"
        table["Business Unit Accounting"] = "BusinessUnitAccounting"
        table["Products & Services Direction"] = "Products&Services"
        table["Corporate Strategy"] = "Enterprise"
        table["Corporate Policies"] = "CorporatePolicy"
        table["Continuity Planning"] = "EnterpriseContinuityAssurance"
        table["Business Architecture"] = "BusinessArchitecture"
        table["Merchant Relations"] = "MerchantRelationship"
        table["Merchant Acquiring Facility"] = "Merchant"
        table["Credit/Charge Card"] = "Credit/ChargeCard"
        table["Card Network Participant Facility"] = "CardNetworkParticipant"
        table["Card Capture"] = "Credit/ChargeCardFinancialCapture"
        table["Card Billing & Payments"] = "Credit/ChargeCardBilling"
        table["Card Authorization"] = "Credit/ChargeCardAuthorization"
        table["Product Inventory Item Management"] = "ProductInventory"
        table["Product Inventory Distribution"] = "ProductInventoryDistribution"
        table["E-Branch Operations"] = "EBranchChannel"
        table["E-Branch Management"] = "EBranchChannel"
        table["Contact Center Operations"] = "ContactCenter"
        table["Contact Center Management"] = "ContactCenter"
        table["Card Terminal Operation"] = "CardPOSTerminal"
        table["Card Terminal Administration"] = "CardPOSNetwork"
        table["Branch Network Management"] = "BranchNetwork"
        table["Branch Location Operations"] = "BranchLocation"
        table["Branch Location Management"] = "BranchLocation"
        table["Branch Currency Management"] = "BranchCash"
        table["Branch Currency Distribution"] = "CashDistribution"
        table["ATM Network Operations"] = "ATMNetwork"
        table["ATM Network Management"] = "ATMNetwork"
        table["Advanced Voice Services Operations"] = "VoiceChannel"
        table["Advanced Voice Services Management"] = "VoiceChannel"
        table["Collections"] = "CollateralAssetLiquidation"
        table["Collateral Asset Administration"] = "CollateralAsset"
        table["Collateral Allocation Management"] = "CollateralAsset"
        table["Trust Services"] = "TrustServices"
        table["Service Product"] = "ServiceProduct"
        table["Remittances (Old)"] = "Remittance"
        table["Customer Tax Handling"] = "CustomerTaxObligation"
        table["Currency Exchange"] = "CurrencyExchange"
        table["Corporate Trust Services"] = "TrustServices"
        table["Consumer Investments"] = "ManagedInvestmentPortfolio"
        table["Consumer Advisory Services"] = "ConsumerAdvice"
        table["Brokered Product"] = "BrokeredProduct"
        table["Bank Drafts & Travelers Checks"] = "BearerDocument"
        table["Public Offering"] = "PublicOffering"
        table["Private Placement"] = "PrivatePlacement"
        table["M&A Advisory"] = "Mergers&Acquisition"
        table["Corporate Tax Advisory"] = "CorporateTaxAdvisoryServices"
        table["Corporate Finance"] = "CorporateFinanceServices"
        table["Regulatory & Legal Authority"] = "Regulatory&LegalAuthorityRelationship"
        table["Investor Relations"] = "Investor"
        table["Corporate Relationship"] = "CorporatePartnerRelationship"
        table["Corporate Communications"] = "EnterpriseCommunication"
        table["Corporate Alliance/Stake Holder"] = "AlliancePartnerRelationship"
        table["Transaction Authorization"] = "InteractiveTransaction"
        table["Servicing Event History"] = "ServicingEvent"
        table["Servicing Activity Analysis"] = "ServicingRootCause"
        table["Point of Service"] = "PointOfService"
        table["Party Authentication"] = "PartyAuthentication"
        table["Interactive Help"] = "InteractiveHelpService"
        table["Customer Workbench"] = "CustomerWorkbench"
        table["Contact Routing"] = "CustomerServicingResource"
        table["Contact Handler"] = "CustomerContact"
        table["Contact Dialogue"] = "CustomerContactSession"
        table["Sales Product Agreement"] = "SalesProduct/Service"
        table["Customer Relationship Management"] = "CustomerRelationship"
        table["Customer Reference Data Management"] = "CustomerReferenceData"
        table["Customer Proposition"] = "CustomerProposition"
        table["Customer Product/Service Eligibility"] = "CustomerEligibility"
        table["Customer Precedents"] = "CustomerPrecedents"
        table["Customer Event History"] = "CustomerEvent"
        table["Customer Credit Rating"] = "CustomerCreditRating"
        table["Customer Behavioral Insights"] = "CustomerBehavior"
        table["Customer Agreement"] = "Customer"
        table["Customer Access Entitlement"] = "CustomerAccessProfile"
        table["Account Recovery"] = "AccountRecovery"
        table["Document Services"] = "DocumentHandling"
        table["Correspondence"] = "Correspondence"
        table["Archive Services"] = "Archive"
        table["Syndicate Management"] = "Syndicate"
        table["Sub Custodian Agreement"] = "SubCustodian"
        table["Product Service Agency"] = "ServiceProvider"
        table["Product Broker Agreement"] = "Broker"
        table["Interbank Relationship Management"] = "BankRelationship"
        table["Information Provider Administration"] = "InformationFeed"
        table["Correspondent Bank Relationship Management"] = "CorrepondentBankRelationship"
        table["Correspondent Bank Data Management"] = "CorrespondentBank"
        table["Contractor/Supplier Agreement"] = "Supplier"
        table["Financial Statements"] = "FinancialStatements"
        table["Financial Control"] = "FinancialControl"
        table["Financial Compliance"] = "FinancialCompliance"
        table["Enterprise Tax Administration"] = "TaxAdministration"
        table["Workforce Training"] = "EmployeeTraining"
        table["Travel & Expenses"] = "EmployeeTravel&Expenses"
        table["Recruitment"] = "Recruitment"
        table["Human Resources Direction"] = "HumanResources"
        table["Employee/Contractor Contract"] = "Employee"
        table["Employee Payroll & Incentives"] = "EmployeePayroll"
        table["Employee Evaluation"] = "Employee"
        table["Employee Data Management"] = "Employee"
        table["Employee Certification"] = "EmployeeCertification"
        table["Employee Benefits"] = "EmployeeBenefits"
        table["Employee Assignment"] = "Employee"
        table["Employee Access"] = "EmployeeAccess"
        table["Investment Portfolio Planning"] = "ManagedInvestmentPortfolio"
        table["Investment Portfolio Management"] = "ManagedInvestmentPortfolio"
        table["Investment Portfolio Analysis"] = "ManagedInvestmentPortfolio"
        table["eTrading Workbench"] = "eTradingWorkbench"
        table["Systems Operations"] = "ITSystem"
        table["Systems Help Desk"] = "HelpDesk"
        table["Systems Assurance"] = "ITSystem"
        table["Systems Administration"] = "ITSystem"
        table["System Development"] = "ITSystemDevelopment"
        table["System Deployment"] = "ITSystemDeployment"
        table["Production Release"] = "ProductionSystem"
        table["Platform Operations"] = "ITSystemsPlatform"
        table["IT Systems Direction"] = "ITSystems"
        table["IT Standards & Guidelines"] = "TechnologyStandards"
        table["Internal Network Operation"] = "InternalNetwork"
        table["Development Environment"] = "DevelopmentEnvironment"
        table["Management Manual"] = "ManagementManual"
        table["Knowledge Exchange"] = "IntellectualPropertyExchange"
        table["Intellectual Property Portfolio"] = "IntellectualProperty"
        table["Savings Account"] = "SavingsAccount"
        table["Mortgage Loan"] = "Loan"
        table["Merchandising Loan"] = "Loan"
        table["Loan"] = "Loan"
        table["Leasing"] = "Leasing"
        table["Fiduciary Agreement"] = "Loan"
        table["Deposit Account"] = "Deposit"
        table["Current Account"] = "CurrentAccount"
        table["Corporate Loan"] = "Loan"
        table["Corporate Lease"] = "Loan"
        table["Corporate Deposits"] = "CorporateDeposit"
        table["Corporate Current Account"] = "CorporateCurrentAccount"
        table["Consumer Loan"] = "Loan"
        table["Quant Model"] = "QuantModel"
        table["Public Reference Data Management"] = "GlobalStandard"
        table["Market Information Management"] = "FinancialMarketInformation"
        table["Market Data Switch Operation"] = "InformationFeedSwitch"
        table["Market Data Switch Administration"] = "InformationFeedSwitch"
        table["Location Data Management"] = "Location"
        table["Information Provider Operation"] = "InformationFeed"
        table["Financial Market Research"] = "FinancialMarketResearch"
        table["Financial Market Analysis"] = "FinancialMarket"
        table["Financial Instrument Reference Data Management"] = "FinancialInstrument"
        table["Counterparty Administration"] = "Counterparty"
        table["Unit Trust Administration"] = "UnitTrust"
        table["Trade/Price Reporting"] = "MarketTradeReporting"
        table["Trade Confirmation Matching"] = "TradeMatching"
        table["Settlement Obligation Management"] = "SecuritiesClearing&Settlement"
        table["Securities Fails Processing"] = "SecurityTradingFails"
        table["Securities Delivery & Receipt Management"] = "SecuritiesClearing&Settlement"
        table["Order Allocation"] = "SecuritiesAllocation"
        table["Mutual Fund Administration"] = "MutualFund"
        table["Hedge Fund Administration"] = "HedgeFund"
        table["Financial Instrument Valuation"] = "MarketAssetValuation"
        table["Custody Administration"] = "Custody"
        table["Corporate Events"] = "CorporateEvents"
        table["Prospect Campaign Management"] = "ProspectCampaignPortfolio"
        table["Prospect Campaign Design"] = "ProspectCampaign"
        table["Promotional Events"] = "PromotionalCampaign"
        table["Customer Surveys"] = "CustomerSurvey"
        table["Customer Campaign Management"] = "CustomerCampaignPortfolio"
        table["Customer Campaign Design"] = "CustomerCampaign"
        table["Business Development"] = "BusinessDevelopment"
        table["Brand Management"] = "Brand"
        table["Advertising"] = "AdvertisingCampaign"
        table["Production Risk Models"] = "ProductionRiskModel"
        table["Operational Risk Models"] = "OpertionalRiskModel"
        table["Market Risk Models"] = "MarketRiskModel"
        table["Liquidity Risk Models"] = "LiquidityRiskModel"
        table["Gap Analysis"] = "interestRateGapRisk"
        table["Fraud Models"] = "FraudModel"
        table["Financial Instrument Valuation Models"] = "MarketAssetValuationModel"
        table["Economic Capital"] = "EconomicCapital"
        table["Customer Behavior Models"] = "CustomerBehaviorModel"
        table["Credit/Margin Management"] = "Credit&Margins"
        table["Credit Risk Models"] = "CreditRiskModel"
        table["Contribution Models"] = "ContributionModel"
        table["Business Risk Models"] = "BusinessOperationRiskModel"
        table["Security Assurance"] = "SecurityCompliance"
        table["Security Advisory"] = "SecurityCompliance"
        table["Procurement"] = "Procurement"
        table["Legal Compliance"] = "LegalCompliance"
        table["Internal Audit"] = "InternalAudit"
        table["Fixed Asset Register"] = "FixedAssetRegister"
        table["Company Billing & Payments"] = "EnterpriseBilling&Payments"
        table["Approved Supplier Directory"] = "Supplier"
        table["Reward Points Awards & Redemption"] = "RewardPoints"
        table["Open Item Management"] = "OpenItem"
        table["Leasing Item Administration"] = "LeasingItem"
        table["Issued Device Tracking"] = "IssuedDevice"
        table["Issued Device Administration"] = "IssuedDevice"
        table["Dunning"] = "Dunning"
        table["Disbursement"] = "Disbursement"
        table["Delinquent Account Handling"] = "CardDelinquentAccountHandling"
        table["Customer Billing"] = "CustomerBilling"
        table["Channel Activity History"] = "ChannelActivity"
        table["Channel Activity Analysis"] = "ChannelActivity"
        table["Card Transaction Switch"] = "CardTransactionSwitch"
        table["Card Collections"] = "CardCollections"
        table["Party Data Management"] = "Party"
        table["Customer Profile"] = "Party"
        table["Payment Order"] = "PaymentOrder"
        table["Payment Execution"] = "PaymentExecution"
        table["Financial Message Analysis"] = "FinancialNetworkGateway"
        table["Financial Gateway"] = "FinancialGateway"
        table["Correspondent Bank"] = "CorrespondentBank"
        table["Cheque Processing"] = "ChequeProcessing"
        table["Central Cash Handling"] = "CentralCash"
        table["Card Financial Settlement"] = "CardFinancialSettlement"
        table["Card eCommerce Gateway"] = "ECommerceGateway"
        table["Card Clearing"] = "CardClearing"
        table["ACH Fulfillment"] = "ACHFulfillment"
        table["Special Pricing Conditions"] = "SpecialPricingConditions"
        table["Product Training"] = "ProductTraining"
        table["Product Quality Assurance"] = "Product/Service"
        table["Product Directory"] = "Product"
        table["Product Design"] = "Product/Service"
        table["Product Deployment"] = "Product/ServiceDeployment"
        table["Discount Pricing"] = "Product/ServiceDiscount"
        table["Regulatory Reporting"] = "RegulatoryCompliance"
        table["Regulatory Compliance"] = "RegulatoryCompliance"
        table["Guideline Compliance"] = "GuidelineCompliance"
        table["Fraud/AML Resolution"] = "Fraud/AMLResolution"
        table["Financial Accounting"] = "FinancialBooking"
        table["Compliance Reporting"] = "ComplianceReporting"
        table["Underwriting"] = "Underwriting"
        table["Sales Product"] = "Product/Service"
        table["Sales Planning"] = "Marketing&Sales"
        table["Prospect Campaign Execution"] = "ProspectCampaign"
        table["Product Sales Support"] = "ProductSalesSupport"
        table["Product Matching"] = "Product/CustomerCombination"
        table["Product Expert Sales Support"] = "SalesSpecialistSupport"
        table["Party Lifecycle Management"] = "PartyRelationship"
        table["Lead/Opportunity Management"] = "Lead/Opportunity"
        table["Customer Offer"] = "CustomerOffer"
        table["Customer Campaign Execution"] = "Customer Campaign"
        table["Commissions"] = "Commission"
        table["Commission Agreement"] = "EmployeeCommission"
        table["Servicing Order"] = "ServicingOrder"
        table["Servicing Mandate"] = "ServicingMandate"
        table["Servicing Issue"] = "ServicingIssue"
        table["Payment Initiation"] = "PaymentInitiation"
        table["Customer Case Management"] = "CustomerCase"
        table["Customer Case"] = "CustomerCase"
        table["Case Root Cause Analysis"] = "CustomerCaseRootCause"
        table["Card Case"] = "CardCase"
        table["Trade Finance"] = "TradeFinance"
        table["Syndicated Loan"] = "SyndicatedLoan"
        table["Project Finance"] = "ProjectFinance"
        table["Limit & Exposure Management"] = "Limit&Exposure"
        table["Letter of Credit"] = "LetterOfCredit"
        table["Factoring"] = "Factoring"
        table["Direct Debit Mandate"] = "DirectDebitMandate"
        table["Direct Debit"] = "DirectDebit"
        table["Credit Management"] = "CreditPosition"
        table["Credit Facility"] = "CreditFacility"
        table["Cheque Lock Box"] = "LockBox"
        table["Cash Management & Account Services"] = "CashManagement"
        table["Bank Guarantee"] = "BankGuarantee"
        table["Trading Models"] = "TradingModel"
        table["Trading Book Oversight"] = "TradingPosition"
        table["Traded Position Management"] = "TradedPosition"
        table["Suitability Checking"] = "Suitability"
        table["Quote Management"] = "Quotation"
        table["Program Trading"] = "ProgramTrading"
        table["Market Order Execution"] = "MarketOrder"
        table["Market Order"] = "MarketOrder"
        table["Market Making"] = "MarketMaking"
        table["ECM/DCM"] = "ECM/DCM"
        table["Dealer Workbench"] = "TradingDesk"
        table["Credit Risk Operations"] = "TradingCreditPosition"
        self.assets = table

    def ready(self):
        if self.assets and self.patterns:
            return True
        return False

    def run(self,core,*params):
        record = core.record
        if not record:
            raise Exception("no record")
        if "name" in record:
            name = record["name"]
        else:
            raise Exception("no name")
        fp = self.patterns[name]
        at = self.assets[name]
        array = FunctionalPatterns.patterns[fp]
        ga = array[0]
        bqt = array[1]
        bq = "bq"
        sq = "sq"
        cr = at+ga
        defs = 'from halo_bian.bian.bian import FunctionalPatterns\n'+\
        'ASSET_TYPE = "'+at+'"\n'+\
        'FUNCTIONAL_PATTERN = FunctionalPatterns.'+fp.upper()+'\n'+\
        'GENERIC_ARTIFACT = "'+ga+'"\n'+\
        'BEHAVIOR_QUALIFIER_TYPE = "'+bqt+'"\n'+\
        'BEHAVIOR_QUALIFIER = {'+bq+'}\n'+\
        'SUB_QUALIFIER = {'+sq+'}\n'+\
        'CONTROL_RECORD = "'+cr+'"\n'+\
        'SERVICE_DOMAINS = None\n'+\
        'file_dir = os.path.dirname(__file__)\n'+\
        "file_path = os.path.join(file_dir, '..', '..', 'env', 'config', 'bian_sds.json')\n"+\
        "with open(file_path, 'r') as fb:\n"+\
        '    SERVICE_DOMAINS = json.load(fb)\n'+\
        "BIAN_VER = '8'\n"+\
        "BIAN_API_VER = '2.0'\n"+\
        "SERVICE_DOMAIN = '" + name + "'\n"+\
        "HALO_CONTEXT_LIST = []\n"+\
        "HALO_CONTEXT_CLASS = 'halo_bian.bian.bian.BianContext'\n"+\
        "REQUEST_FILTER_CLASS = 'halo_bian.bian.bian.BianRequestFilter'\n"\
        "REQUEST_FILTER_CLEAR_CLASS = None\n"+\
        "INIT_CLASS_NAME = 'halo_bian.bian.abs_bian_srv.BianGlobalService'\n"

        return {"defs":defs}
