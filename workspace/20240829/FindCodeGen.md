# FindCodeGen

## /clang/include/clang/Basic/CodeGenOptions.h

## /clang/lib/Basic/CodeGenOptions.cpp

## /clang/lib/CodeGen/BackendUtil.cpp

## /clang/lib/CodeGen/CGAtomic.cpp

### 1: CodeGenFunction::EmitAtomicExpr

- 解释：

## /clang/lib/CodeGen/CGBuilder.h

### 2: CGBuilderTy::CreateAtomicCmpXchg

- 解释：

### 3: CGBuilderTy::CreateAtomicRMW

- 解释：

## /clang/lib/CodeGen/CGBuiltin.cpp

### 4: CodeGenFunction::EmitAArch64BuiltinExpr

- 解释：

### 5: CodeGenFunction::EmitAArch64SVEBuiltinExpr

- 解释：

### 6: CodeGenFunction::EmitAMDGPUBuiltinExpr

- 解释：

### 7: CodeGenFunction::EmitBuiltinExpr

- 解释：

### 8: CodeGenFunction::EmitNVPTXBuiltinExpr

- 解释：

### 9: CodeGenFunction::EmitSystemZBuiltinExpr

- 解释：

## /clang/lib/CodeGen/CGCUDANV.cpp

## /clang/lib/CodeGen/CGCUDARuntime.h

## /clang/lib/CodeGen/CGCall.cpp

### 10: CodeGenFunction::EmitCall

- 解释：

## /clang/lib/CodeGen/CGCall.h

### 11: operator&

- 解释：

### 12: operator

- 解释：

## /clang/lib/CodeGen/CGDebugInfo.cpp

### 13: CGDebugInfo::CreateCompileUnit

- 解释：

### 14: CGDebugInfo::CreateRecordStaticField

- 解释：

### 15: CGDebugInfo::EmitGlobalVariable

- 解释：

### 16: CGDebugInfo::finalize

- 解释：

## /clang/lib/CodeGen/CGDebugInfo.h

## /clang/lib/CodeGen/CGExpr.cpp

### 17: CodeGenFunction::EmitLValueForField

- 解释：

## /clang/lib/CodeGen/CGExprComplex.cpp

## /clang/lib/CodeGen/CGExprScalar.cpp

## /clang/lib/CodeGen/CGHLSLRuntime.cpp

### 18: CGHLSLRuntime::addBufferResourceAnnotation

- 解释：

### 19: CGHLSLRuntime::annotateHLSLResource

- 解释：

### 20: CGHLSLRuntime::finishCodeGen

- 解释：

## /clang/lib/CodeGen/CGHLSLRuntime.h

## /clang/lib/CodeGen/CGOpenMPRuntime.cpp

## /clang/lib/CodeGen/CGOpenMPRuntimeGPU.cpp

### 21: CGOpenMPRuntimeGPU::emitOutlinedFunctionCall

- 解释：

### 22: CGOpenMPRuntimeGPU::getParameterAddress

- 解释：

### 23: CGOpenMPRuntimeGPU::processRequiresDirective

- 解释：

## /clang/lib/CodeGen/CGStmtOpenMP.cpp

## /clang/lib/CodeGen/CodeGenModule.cpp

### 24: CodeGenModule::GetAddrOfGlobalTemporary

- 解释：

### 25: CodeGenModule::GetOrCreateMultiVersionResolver

- 解释：

### 26: CodeGenModule::emitMultiVersionFunctions

- 解释：

## /clang/lib/CodeGen/CodeGenTBAA.cpp

### 27: CodeGenTBAA::getBaseTypeInfo

- 解释：

### 28: CodeGenTBAA::getBaseTypeInfoHelper

- 解释：

### 29: CodeGenTBAA::getTypeInfoHelper

- 解释：

## /clang/lib/CodeGen/Targets/AMDGPU.cpp

### 30: AMDGPUTargetCodeGenInfo::getLLVMSyncScopeID

- 解释：

## /clang/lib/Driver/ToolChains/Flang.cpp

### 31: Flang::addCodegenOptions

- 解释：

## /clang/lib/Frontend/CompilerInvocation.cpp

### 32: CompilerInvocation::ParseCodeGenArgs

- 解释：

## /clang/test/CodeGenCXX/RelativeVTablesABI/member-function-pointer.cpp

## /clang/test/CodeGenCXX/attr-target-clones.cpp

## /clang/test/CodeGenCXX/debug-info-class.cpp

## /clang/test/CodeGenCXX/debug-info-static-member.cpp

## /clang/test/OpenMP/distribute_parallel_for_simd_private_codegen.cpp

## /clang/test/OpenMP/distribute_simd_private_codegen.cpp

## /clang/test/OpenMP/parallel_reduction_codegen.cpp

## /clang/test/OpenMP/target_data_use_device_addr_codegen.cpp

## /clang/test/OpenMP/target_teams_distribute_parallel_for_simd_private_codegen.cpp

## /clang/test/OpenMP/target_teams_distribute_simd_private_codegen.cpp

## /clang/test/OpenMP/teams_distribute_parallel_for_simd_private_codegen.cpp

## /clang/test/OpenMP/teams_distribute_simd_private_codegen.cpp

## /clang/utils/TableGen/RISCVVEmitter.cpp

### 33: emitCodeGenSwitchBody

- 解释：

## /flang/include/flang/Optimizer/CodeGen/Target.h

### 34: CodeGenSpecifics::CodeGenSpecifics

- 解释：

## /flang/include/flang/Optimizer/CodeGen/TypeConverter.h

## /flang/lib/Frontend/CompilerInvocation.cpp

### 35: parseCodeGenArgs

- 解释：

## /flang/lib/Frontend/FrontendActions.cpp

### 36: CodeGenAction::setUpTargetMachine

- 解释：

### 37: CodeGenAction::beginSourceFileAction

- 解释：

### 38: CodeGenAction::executeAction

- 解释：

### 39: CodeGenAction::generateLLVMIR

- 解释：

### 40: CodeGenAction::runOptimizationPipeline

- 解释：

## /flang/lib/Optimizer/CodeGen/CodeGen.cpp

## /flang/lib/Optimizer/CodeGen/Target.cpp

### 41: CodeGenSpecifics::get

- 解释：

## /flang/lib/Optimizer/CodeGen/TargetRewrite.cpp

## /flang/lib/Optimizer/CodeGen/TypeConverter.cpp

## /llvm/include/llvm/CodeGen/AccelTable.h

## /llvm/include/llvm/CodeGen/BasicTTIImpl.h

## /llvm/include/llvm/CodeGen/CallingConvLower.h

## /llvm/include/llvm/CodeGen/CodeGenPassBuilder.h

## /llvm/include/llvm/CodeGen/FunctionLoweringInfo.h

## /llvm/include/llvm/CodeGen/GlobalISel/CombinerHelper.h

## /llvm/include/llvm/CodeGen/GlobalISel/LegacyLegalizerInfo.h

## /llvm/include/llvm/CodeGen/GlobalISel/LegalizerHelper.h

## /llvm/include/llvm/CodeGen/GlobalISel/MachineIRBuilder.h

## /llvm/include/llvm/CodeGen/IndirectThunks.h

## /llvm/include/llvm/CodeGen/MIRYamlMapping.h

## /llvm/include/llvm/CodeGen/MachineBasicBlock.h

## /llvm/include/llvm/CodeGen/MacroFusion.h

## /llvm/include/llvm/CodeGen/Passes.h

## /llvm/include/llvm/CodeGen/PseudoSourceValue.h

## /llvm/include/llvm/CodeGen/SchedulerRegistry.h

## /llvm/include/llvm/CodeGen/SelectionDAGISel.h

## /llvm/include/llvm/CodeGen/TargetInstrInfo.h

## /llvm/include/llvm/CodeGen/TargetLowering.h

## /llvm/include/llvm/CodeGen/TargetSchedule.h

## /llvm/lib/CodeGen/AsmPrinter/AccelTable.cpp

## /llvm/lib/CodeGen/AsmPrinter/AsmPrinter.cpp

## /llvm/lib/CodeGen/AsmPrinter/DwarfDebug.cpp

## /llvm/lib/CodeGen/AssignmentTrackingAnalysis.cpp

## /llvm/lib/CodeGen/BasicBlockSectionsProfileReader.cpp

## /llvm/lib/CodeGen/CodeGenPrepare.cpp

### 42: CodeGenPrepare::optimizeInst

- 解释：

### 43: CodeGenPrepare::optimizeSelectInst

- 解释：

### 44: CodeGenPrepare::splitLargeGEPOffsets

- 解释：

## /llvm/lib/CodeGen/DwarfEHPrepare.cpp

## /llvm/lib/CodeGen/GCMetadata.cpp

## /llvm/lib/CodeGen/GlobalISel/CombinerHelper.cpp

## /llvm/lib/CodeGen/GlobalISel/IRTranslator.cpp

## /llvm/lib/CodeGen/GlobalISel/LegalizerHelper.cpp

## /llvm/lib/CodeGen/GlobalISel/LegalizerInfo.cpp

## /llvm/lib/CodeGen/GlobalISel/MachineIRBuilder.cpp

## /llvm/lib/CodeGen/GlobalMerge.cpp

## /llvm/lib/CodeGen/InlineSpiller.cpp

## /llvm/lib/CodeGen/InterleavedAccessPass.cpp

## /llvm/lib/CodeGen/JMCInstrumenter.cpp

## /llvm/lib/CodeGen/LiveRangeEdit.cpp

## /llvm/lib/CodeGen/MIRParser/MILexer.cpp

## /llvm/lib/CodeGen/MIRParser/MIParser.cpp

## /llvm/lib/CodeGen/MachineCSE.cpp

## /llvm/lib/CodeGen/MachineFunction.cpp

## /llvm/lib/CodeGen/MachineOperand.cpp

## /llvm/lib/CodeGen/MachinePipeliner.cpp

## /llvm/lib/CodeGen/MachineScheduler.cpp

## /llvm/lib/CodeGen/MachineVerifier.cpp

## /llvm/lib/CodeGen/MacroFusion.cpp

## /llvm/lib/CodeGen/PseudoSourceValue.cpp

## /llvm/lib/CodeGen/RegAllocFast.cpp

## /llvm/lib/CodeGen/RegisterCoalescer.cpp

## /llvm/lib/CodeGen/SafeStack.cpp

## /llvm/lib/CodeGen/SanitizerBinaryMetadata.cpp

## /llvm/lib/CodeGen/SelectOptimize.cpp

## /llvm/lib/CodeGen/SelectionDAG/DAGCombiner.cpp

## /llvm/lib/CodeGen/SelectionDAG/FunctionLoweringInfo.cpp

## /llvm/lib/CodeGen/SelectionDAG/LegalizeDAG.cpp

## /llvm/lib/CodeGen/SelectionDAG/LegalizeFloatTypes.cpp

## /llvm/lib/CodeGen/SelectionDAG/LegalizeIntegerTypes.cpp

## /llvm/lib/CodeGen/SelectionDAG/LegalizeTypes.h

## /llvm/lib/CodeGen/SelectionDAG/ScheduleDAGSDNodes.cpp

## /llvm/lib/CodeGen/SelectionDAG/SelectionDAG.cpp

## /llvm/lib/CodeGen/SelectionDAG/SelectionDAGBuilder.cpp

## /llvm/lib/CodeGen/SelectionDAG/SelectionDAGBuilder.h

## /llvm/lib/CodeGen/SelectionDAG/SelectionDAGISel.cpp

## /llvm/lib/CodeGen/SjLjEHPrepare.cpp

## /llvm/lib/CodeGen/StackColoring.cpp

## /llvm/lib/CodeGen/StackSlotColoring.cpp

## /llvm/lib/CodeGen/TargetInstrInfo.cpp

## /llvm/lib/CodeGen/TargetLoweringObjectFileImpl.cpp

## /llvm/lib/CodeGen/TargetPassConfig.cpp

## /llvm/lib/CodeGen/TargetSchedule.cpp

## /llvm/lib/CodeGen/WasmEHPrepare.cpp

## /llvm/lib/CodeGen/WinEHPrepare.cpp

## /mlir/lib/Dialect/SparseTensor/Transforms/CodegenEnv.cpp

### 45: CodegenEnv::clearValidLexInsert

- 解释：

### 46: CodegenEnv::setValidLexInsert

- 解释：

### 47: CodegenEnv::atExpandLevel

- 解释：

### 48: CodegenEnv::getCustomRedId

- 解释：

### 49: CodegenEnv::startReduc

- 解释：

### 50: CodegenEnv::updateReduc

- 解释：

## /mlir/lib/Dialect/SparseTensor/Transforms/CodegenEnv.h

### 51: CodegenEnv::getLoopDepth

- 解释：

## /mlir/lib/Dialect/SparseTensor/Transforms/SparseGPUCodegen.cpp
