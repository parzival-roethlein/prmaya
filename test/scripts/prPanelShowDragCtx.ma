//Maya ASCII 2018ff08 scene
//Name: prPanelShowDragCtx.ma
//Last modified: Thu, Jan 17, 2019 12:44:25 PM
//Codeset: UTF-8
requires maya "2018ff08";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201804211841-f3d65dda2a";
fileInfo "osv" "Linux 3.10.0-693.21.1.el7.x86_64 #1 SMP Wed Mar 7 19:03:37 UTC 2018 x86_64";
fileInfo "modified-by" "prthlein";
fileInfo "modified-in" "Montreal";
createNode transform -s -n "persp";
	rename -uid "81512900-0001-7A93-5C40-BDF800000250";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 2.0883346645068364 8.0174715950107291 12.377814434089377 ;
	setAttr ".r" -type "double3" -30.338352729603699 17.000000000000593 -8.3146995286575416e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "81512900-0001-7A93-5C40-BDF800000251";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 15.012582793082144;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "81512900-0001-7A93-5C40-BDF800000252";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "81512900-0001-7A93-5C40-BDF800000253";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "81512900-0001-7A93-5C40-BDF800000254";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "81512900-0001-7A93-5C40-BDF800000255";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "81512900-0001-7A93-5C40-BDF800000256";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "81512900-0001-7A93-5C40-BDF800000257";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "group1";
	rename -uid "81512900-0001-7A93-5C40-BE86000002DE";
createNode transform -n "null1" -p "group1";
	rename -uid "81512900-0001-7A93-5C40-BE9A000002DF";
	setAttr ".t" -type "double3" -3 0 0 ;
createNode transform -n "arm_1_control" -p "null1";
	rename -uid "81512900-0001-7A93-5C40-BE4F000002B3";
createNode nurbsCurve -n "arm_1_controlShape" -p "arm_1_control";
	rename -uid "81512900-0001-7A93-5C40-BE4F000002B4";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8
		 9 10
		11
		2.7755575615628914e-17 -0.78361162489122516 -0.78361162489122382
		6.7857323231109146e-17 1.2643170607829329e-16 -1.1081941875543879
		-2.775557561562891e-17 0.78361162489122438 -0.78361162489122427
		-1.1102230246251565e-16 1.1081941875543879 -3.2112695072372299e-16
		-2.775557561562891e-17 0.78361162489122438 0.78361162489122405
		-6.785732323110922e-17 3.3392053635905195e-16 1.1081941875543881
		-5.5511151231257827e-17 -0.78361162489122393 0.78361162489122438
		1.1102230246251565e-16 -1.1081941875543879 5.9521325992805852e-16
		2.7755575615628914e-17 -0.78361162489122516 -0.78361162489122382
		6.7857323231109146e-17 1.2643170607829329e-16 -1.1081941875543879
		-2.775557561562891e-17 0.78361162489122438 -0.78361162489122427
		;
createNode transform -n "null2" -p "arm_1_control";
	rename -uid "81512900-0001-7A93-5C40-BEA2000002E6";
	setAttr ".t" -type "double3" 3 0 0 ;
createNode transform -n "arm_2_control" -p "null2";
	rename -uid "81512900-0001-7A93-5C40-BE28000002AB";
createNode nurbsCurve -n "arm_2_controlShape" -p "arm_2_control";
	rename -uid "81512900-0001-7A93-5C40-BE28000002AA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8
		 9 10
		11
		2.7755575615628914e-17 -0.78361162489122516 -0.78361162489122382
		6.7857323231109146e-17 1.2643170607829329e-16 -1.1081941875543879
		-2.775557561562891e-17 0.78361162489122438 -0.78361162489122427
		-1.1102230246251565e-16 1.1081941875543879 -3.2112695072372299e-16
		-2.775557561562891e-17 0.78361162489122438 0.78361162489122405
		-6.785732323110922e-17 3.3392053635905195e-16 1.1081941875543881
		-5.5511151231257827e-17 -0.78361162489122393 0.78361162489122438
		1.1102230246251565e-16 -1.1081941875543879 5.9521325992805852e-16
		2.7755575615628914e-17 -0.78361162489122516 -0.78361162489122382
		6.7857323231109146e-17 1.2643170607829329e-16 -1.1081941875543879
		-2.775557561562891e-17 0.78361162489122438 -0.78361162489122427
		;
createNode joint -n "joint1" -p "group1";
	rename -uid "81512900-0001-7A93-5C40-BE31000002AC";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode joint -n "joint2" -p "joint1";
	rename -uid "81512900-0001-7A93-5C40-BE32000002AD";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60344827586206895;
createNode joint -n "joint3" -p "joint2";
	rename -uid "81512900-0001-7A93-5C40-BE33000002AE";
	setAttr ".t" -type "double3" 3 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60344827586206895;
createNode transform -n "pCube2" -p "joint2";
	rename -uid "81512900-0001-7A93-5C40-BE5A000002C0";
	setAttr ".t" -type "double3" 1.627131657670813 0 0 ;
	setAttr ".s" -type "double3" 2.6006412124561908 1 1 ;
	setAttr ".rp" -type "double3" -1.627131657670813 0 0 ;
	setAttr ".sp" -type "double3" -0.58286158277927202 0 0 ;
	setAttr ".spt" -type "double3" -1.044270074891541 0 0 ;
createNode mesh -n "pCubeShape2" -p "pCube2";
	rename -uid "81512900-0001-7A93-5C40-BE5A000002C1";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode parentConstraint -n "joint2_parentConstraint1" -p "joint2";
	rename -uid "81512900-0001-7A93-5C40-BEBD000002F9";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "arm_2_controlW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 3 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "pCube1" -p "joint1";
	rename -uid "81512900-0001-7A93-5C40-BE25000002A8";
	setAttr ".t" -type "double3" 1.5053261870891304 0 0 ;
	setAttr ".s" -type "double3" 2.5826478044945929 1 1 ;
	setAttr ".rp" -type "double3" -1.5053261870891301 0 0 ;
	setAttr ".sp" -type "double3" -0.58286158277927202 0 0 ;
	setAttr ".spt" -type "double3" -0.92246460430985822 0 0 ;
createNode mesh -n "pCubeShape1" -p "pCube1";
	rename -uid "81512900-0001-7A93-5C40-BE25000002A7";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".sdt" 0;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode parentConstraint -n "joint1_parentConstraint1" -p "joint1";
	rename -uid "81512900-0001-7A93-5C40-BEBB000002F8";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "arm_1_controlW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" -3 0 0 ;
	setAttr -k on ".w0";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "81512900-0001-7A93-5C40-BDF800000258";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "81512900-0001-7A93-5C40-BDF90000026D";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "81512900-0001-7A93-5C40-BDF90000026E";
createNode displayLayerManager -n "layerManager";
	rename -uid "81512900-0001-7A93-5C40-BDF90000026F";
createNode displayLayer -n "defaultLayer";
	rename -uid "81512900-0001-7A93-5C40-BDF900000270";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "81512900-0001-7A93-5C40-BDF900000271";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "81512900-0001-7A93-5C40-BDF900000272";
	setAttr ".g" yes;
createNode controller -n "nurbsCircle1_tag";
	rename -uid "81512900-0001-7A93-5C40-BE7D000002DC";
createNode controller -n "nurbsCircle2_tag";
	rename -uid "81512900-0001-7A93-5C40-BE7D000002DD";
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "81512900-0001-7A93-5C40-BEF900000300";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 60 -ast 1 -aet 60 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "/work/21762_TRAIN/config/ocio/config.ocio";
	setAttr ".vtn" -type "string" "Medium High Contrast (Monitor)";
	setAttr ".wsn" -type "string" "linear";
	setAttr ".pote" no;
	setAttr ".otn" -type "string" "Medium High Contrast (Monitor)";
	setAttr ".potn" -type "string" "Medium High Contrast (Monitor)";
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "joint1_parentConstraint1.ctx" "joint1.tx";
connectAttr "joint1_parentConstraint1.cty" "joint1.ty";
connectAttr "joint1_parentConstraint1.ctz" "joint1.tz";
connectAttr "joint1_parentConstraint1.crx" "joint1.rx";
connectAttr "joint1_parentConstraint1.cry" "joint1.ry";
connectAttr "joint1_parentConstraint1.crz" "joint1.rz";
connectAttr "joint1.s" "joint2.is";
connectAttr "joint2_parentConstraint1.ctx" "joint2.tx";
connectAttr "joint2_parentConstraint1.cty" "joint2.ty";
connectAttr "joint2_parentConstraint1.ctz" "joint2.tz";
connectAttr "joint2_parentConstraint1.crx" "joint2.rx";
connectAttr "joint2_parentConstraint1.cry" "joint2.ry";
connectAttr "joint2_parentConstraint1.crz" "joint2.rz";
connectAttr "joint2.s" "joint3.is";
connectAttr "joint2.ro" "joint2_parentConstraint1.cro";
connectAttr "joint2.pim" "joint2_parentConstraint1.cpim";
connectAttr "joint2.rp" "joint2_parentConstraint1.crp";
connectAttr "joint2.rpt" "joint2_parentConstraint1.crt";
connectAttr "joint2.jo" "joint2_parentConstraint1.cjo";
connectAttr "arm_2_control.t" "joint2_parentConstraint1.tg[0].tt";
connectAttr "arm_2_control.rp" "joint2_parentConstraint1.tg[0].trp";
connectAttr "arm_2_control.rpt" "joint2_parentConstraint1.tg[0].trt";
connectAttr "arm_2_control.r" "joint2_parentConstraint1.tg[0].tr";
connectAttr "arm_2_control.ro" "joint2_parentConstraint1.tg[0].tro";
connectAttr "arm_2_control.s" "joint2_parentConstraint1.tg[0].ts";
connectAttr "arm_2_control.pm" "joint2_parentConstraint1.tg[0].tpm";
connectAttr "joint2_parentConstraint1.w0" "joint2_parentConstraint1.tg[0].tw";
connectAttr "joint1.ro" "joint1_parentConstraint1.cro";
connectAttr "joint1.pim" "joint1_parentConstraint1.cpim";
connectAttr "joint1.rp" "joint1_parentConstraint1.crp";
connectAttr "joint1.rpt" "joint1_parentConstraint1.crt";
connectAttr "joint1.jo" "joint1_parentConstraint1.cjo";
connectAttr "arm_1_control.t" "joint1_parentConstraint1.tg[0].tt";
connectAttr "arm_1_control.rp" "joint1_parentConstraint1.tg[0].trp";
connectAttr "arm_1_control.rpt" "joint1_parentConstraint1.tg[0].trt";
connectAttr "arm_1_control.r" "joint1_parentConstraint1.tg[0].tr";
connectAttr "arm_1_control.ro" "joint1_parentConstraint1.tg[0].tro";
connectAttr "arm_1_control.s" "joint1_parentConstraint1.tg[0].ts";
connectAttr "arm_1_control.pm" "joint1_parentConstraint1.tg[0].tpm";
connectAttr "joint1_parentConstraint1.w0" "joint1_parentConstraint1.tg[0].tw";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "arm_2_control.msg" "nurbsCircle1_tag.act";
connectAttr "arm_1_control.msg" "nurbsCircle2_tag.act";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "pCubeShape1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "pCubeShape2.iog" ":initialShadingGroup.dsm" -na;
// End of prPanelShowDragCtx.ma
