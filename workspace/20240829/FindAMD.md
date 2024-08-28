# FindAMD

## /clang/lib/Basic/Targets/AMDGPU.cpp

## /clang/lib/Basic/Targets/AMDGPU.h

### 1: AMDGPUTargetInfo::getConstantAddressSpace

- 解释：

### 2: AMDGPUTargetInfo::getDWARFAddressSpace

- 解释：

### 3: AMDGPUTargetInfo::getPointerWidthV

- 解释：

### 4: AMDGPUTargetInfo::getVtblPtrAddressSpace

- 解释：

## /clang/lib/CodeGen/CGBuiltin.cpp

### 5: CodeGenFunction::EmitAMDGPUBuiltinExpr

- 解释：

## /clang/lib/CodeGen/Targets/AMDGPU.cpp

### 6: AMDGPUTargetCodeGenInfo::getLLVMSyncScopeID

- 解释：

## /flang/lib/Frontend/FrontendActions.cpp

### 7: getExplicitAndImplicitAMDGPUTargetFeatures

- 解释：

### 8: addAMDGPUSpecificMLIRItems

- 解释：

## /libc/utils/gpu/loader/amdgpu/Loader.cpp

## /llvm/lib/BinaryFormat/AMDGPUMetadataVerifier.cpp

## /llvm/lib/Target/AMDGPU/AMDGPU.h

## /llvm/lib/Target/AMDGPU/AMDGPUArgumentUsageInfo.h

## /llvm/lib/Target/AMDGPU/AMDGPUAsmPrinter.cpp

### 9: AMDGPUAsmPrinter::getSIProgramInfo

- 解释：

## /llvm/lib/Target/AMDGPU/AMDGPUGlobalISelUtils.h

## /llvm/lib/Target/AMDGPU/AMDGPUHSAMetadataStreamer.h

## /llvm/lib/Target/AMDGPU/AMDGPUIGroupLP.cpp

## /llvm/lib/Target/AMDGPU/AMDGPUIGroupLP.h

## /llvm/lib/Target/AMDGPU/AMDGPUISelDAGToDAG.cpp

### 10: AMDGPUDAGToDAGISel::SelectBRCOND

- 解释：

## /llvm/lib/Target/AMDGPU/AMDGPUISelLowering.cpp

### 11: AMDGPUTargetLowering::AMDGPUTargetLowering

- 解释：

### 12: AMDGPUTargetLowering::LowerOperation

- 解释：

### 13: AMDGPUTargetLowering::ReplaceNodeResults

- 解释：

### 14: AMDGPUTargetLowering::lowerFEXP

- 解释：

## /llvm/lib/Target/AMDGPU/AMDGPUISelLowering.h

## /llvm/lib/Target/AMDGPU/AMDGPULegalizerInfo.cpp

### 15: AMDGPULegalizerInfo::AMDGPULegalizerInfo

- 解释：

### 16: AMDGPULegalizerInfo::legalizeCustom

- 解释：

### 17: AMDGPULegalizerInfo::legalizeFExp

- 解释：

## /llvm/lib/Target/AMDGPU/AMDGPULibFunc.cpp

## /llvm/lib/Target/AMDGPU/AMDGPULowerModuleLDSPass.cpp

## /llvm/lib/Target/AMDGPU/AMDGPUMachineFunction.h

## /llvm/lib/Target/AMDGPU/AMDGPURemoveIncompatibleFunctions.cpp

## /llvm/lib/Target/AMDGPU/AMDGPUSubtarget.cpp

## /llvm/lib/Target/AMDGPU/AMDGPUTargetMachine.cpp

## /llvm/lib/Target/AMDGPU/AMDGPUTargetObjectFile.cpp

### 18: AMDGPUTargetObjectFile::getExplicitSectionGlobal

- 解释：

## /llvm/lib/Target/AMDGPU/AMDGPUTargetTransformInfo.cpp

## /llvm/lib/Target/AMDGPU/AsmParser/AMDGPUAsmParser.cpp

### 19: AMDGPUAsmParser::ParseInstruction

- 解释：

### 20: AMDGPUAsmParser::getCPolKind

- 解释：

### 21: AMDGPUAsmParser::getConstantBusLimit

- 解释：

### 22: AMDGPUAsmParser::getNSAMaxSize

- 解释：

### 23: AMDGPUAsmParser::parseCPol

- 解释：

### 24: AMDGPUAsmParser::parseCnt

- 解释：

### 25: AMDGPUAsmParser::parseDimId

- 解释：

### 26: AMDGPUAsmParser::parseInterpAttr

- 解释：

### 27: AMDGPUAsmParser::parseMnemonicSuffix

- 解释：

### 28: AMDGPUAsmParser::validateBLGP

- 解释：

### 29: AMDGPUAsmParser::validateCoherencyBits

- 解释：

### 30: AMDGPUAsmParser::validateMIMGAddrSize

- 解释：

### 31: AMDGPUAsmParser::validateMIMGAtomicDMask

- 解释：

### 32: AMDGPUAsmParser::validateMIMGD16

- 解释：

### 33: AMDGPUAsmParser::validateMIMGDataSize

- 解释：

### 34: AMDGPUAsmParser::validateMIMGMSAA

- 解释：

### 35: AMDGPUAsmParser::validateSMEMOffset

- 解释：

### 36: AMDGPUAsmParser::validateVOPDRegBankConstraints

- 解释：

## /llvm/lib/Target/AMDGPU/Disassembler/AMDGPUDisassembler.cpp

### 37: AMDGPUDisassembler::convertEXPInst

- 解释：

### 38: AMDGPUDisassembler::convertMIMGInst

- 解释：

### 39: AMDGPUDisassembler::convertVINTERPInst

- 解释：

### 40: AMDGPUDisassembler::getInstruction

- 解释：

### 41: AMDGPUDisassembler::onSymbolStart

- 解释：

## /llvm/lib/Target/AMDGPU/Disassembler/AMDGPUDisassembler.h

## /llvm/lib/Target/AMDGPU/GCNCreateVOPD.cpp

## /llvm/lib/Target/AMDGPU/GCNHazardRecognizer.cpp

## /llvm/lib/Target/AMDGPU/GCNHazardRecognizer.h

## /llvm/lib/Target/AMDGPU/GCNRegPressure.cpp

## /llvm/lib/Target/AMDGPU/GCNRegPressure.h

## /llvm/lib/Target/AMDGPU/GCNSchedStrategy.cpp

## /llvm/lib/Target/AMDGPU/GCNSubtarget.h

## /llvm/lib/Target/AMDGPU/GCNVOPDUtils.cpp

## /llvm/lib/Target/AMDGPU/MCTargetDesc/AMDGPUAsmBackend.cpp

### 42: AMDGPUAsmBackend::shouldForceRelocation

- 解释：

## /llvm/lib/Target/AMDGPU/MCTargetDesc/AMDGPUInstPrinter.cpp

### 43: AMDGPUInstPrinter::printCPol

- 解释：

### 44: AMDGPUInstPrinter::printRegularOperand

- 解释：

### 45: AMDGPUInstPrinter::printVOPDst

- 解释：

## /llvm/lib/Target/AMDGPU/MCTargetDesc/AMDGPUInstPrinter.h

## /llvm/lib/Target/AMDGPU/R600OpenCLImageTypeLoweringPass.cpp

## /llvm/lib/Target/AMDGPU/SIAnnotateControlFlow.cpp

## /llvm/lib/Target/AMDGPU/SIDefines.h

## /llvm/lib/Target/AMDGPU/SIISelLowering.cpp

## /llvm/lib/Target/AMDGPU/SIISelLowering.h

## /llvm/lib/Target/AMDGPU/SIInsertHardClauses.cpp

## /llvm/lib/Target/AMDGPU/SIInstrInfo.cpp

## /llvm/lib/Target/AMDGPU/SIInstrInfo.h

## /llvm/lib/Target/AMDGPU/SIMachineFunctionInfo.cpp

## /llvm/lib/Target/AMDGPU/SIRegisterInfo.cpp

## /llvm/lib/Target/AMDGPU/Utils/AMDGPUAsmUtils.cpp

## /llvm/lib/Target/AMDGPU/Utils/AMDGPUBaseInfo.cpp

### 46: getTgtId

- 解释：

### 47: AMDGPUTargetID::setTargetIDFromTargetIDStream

- 解释：

### 48: getTargetIDSettingFromFeatureString

- 解释：

### 49: InstInfo::getInvalidCompOperandIndex

- 解释：

### 50: getNSAMaxSize

- 解释：

### 51: getSMRDEncodedOffset

- 解释：

### 52: getVOPDFull

- 解释：

### 53: isLegalSMRDEncodedSignedOffset

- 解释：

### 54: isLegalSMRDEncodedUnsignedOffset

- 解释：

### 55: isMAC

- 解释：

### 56: isPermlane16

- 解释：

## /llvm/lib/Target/AMDGPU/Utils/AMDGPUBaseInfo.h

### 57: InstInfo::hasInvalidOperand

- 解释：

## /llvm/lib/Target/AMDGPU/Utils/AMDGPUMemoryUtils.h

## /llvm/lib/Transforms/IPO/WholeProgramDevirt.cpp

## /mlir/lib/CAPI/Dialect/AMDGPU.cpp

### 58: mlirAMDGPUDialectGetNamespace

- 解释：

### 59: mlirContextLoadAMDGPUDialect

- 解释：

### 60: mlirDialectRegistryInsertAMDGPUDialect

- 解释：

## /openmp/libomptarget/plugins-nextgen/amdgpu/dynamic_hsa/hsa_ext_amd.h

## /openmp/libomptarget/plugins-nextgen/amdgpu/src/rtl.cpp

### 61: AMDGPUDeviceTy::callGlobalCtorDtorCommon

- 解释：
