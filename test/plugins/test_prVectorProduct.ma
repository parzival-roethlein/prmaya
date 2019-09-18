//Maya ASCII 2018 scene
//Name: test_prVectorProduct.ma
//Last modified: Wed, Sep 18, 2019 01:26:13 AM
//Codeset: 1252
requires maya "2018";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "0C68873B-42E1-044A-9AC2-03AD22B3D66B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1.5833197350095092 2.9952618738532508 3.8447217759220109 ;
	setAttr ".r" -type "double3" -31.538352729604107 15.399999999999844 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "BCA98976-415B-B4E0-3363-7A8DC13AFFC9";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 5.8407819567590753;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "185734B7-4E71-54BE-0AED-54B33B57AF09";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "78AF314D-470D-FE68-C763-F4AD6F9CF944";
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
	rename -uid "9E54F35A-43C4-CA46-C2DD-788533F9E9AD";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "DC9BA180-40FE-E3E3-7412-44B2D01BBD40";
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
	rename -uid "861D92A0-48DE-0615-E46A-3C859E556EE6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "77D5F330-4ED6-96C2-23CE-46A99D981A83";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "input1_locator";
	rename -uid "350F8BD8-4722-940B-C52C-07A63BF65D9E";
	setAttr ".v" no;
createNode locator -n "input1_locatorShape" -p "input1_locator";
	rename -uid "54456CFF-4592-DC32-6D55-3599132A0327";
	setAttr -k off ".v";
createNode transform -n "input2_locator";
	rename -uid "467985BC-4A1F-CA4B-B6E9-6EB38818B029";
	setAttr ".v" no;
createNode locator -n "input2_locatorShape" -p "input2_locator";
	rename -uid "C9612A30-41DE-2BE8-B5B1-3EA7030C44A0";
	setAttr -k off ".v";
createNode transform -n "input1";
	rename -uid "28FBE789-448C-F476-A559-76871E79292C";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 1 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "input1Shape" -p "input1";
	rename -uid "7D8C19ED-4705-89CF-2028-37B507272DA7";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode transform -n "a_annotation" -p "input1";
	rename -uid "9CA2444A-4CBF-61BF-D0AC-86B41CBC42FE";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
createNode annotationShape -n "a_annotationShape" -p "a_annotation";
	rename -uid "BC5451FB-4E6A-6906-78FB-89AF2B2593EF";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "input1";
createNode transform -n "input2";
	rename -uid "140A038C-436B-BFC2-D635-AF840BFDB95D";
	addAttr -ci true -sn "scalar" -ln "scalar" -dv 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1 0 0 ;
	setAttr -k on ".scalar";
createNode locator -n "input2Shape" -p "input2";
	rename -uid "FB8522BD-443A-16C9-F627-4F94E4AE0308";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode transform -n "b_annotation" -p "input2";
	rename -uid "35F0F023-4F54-566D-85AA-4AA3A1B33C1D";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
createNode annotationShape -n "b_annotationShape" -p "b_annotation";
	rename -uid "AFF88E38-4914-412A-DC28-68A10C35C535";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "input2_matrix_scalar";
createNode transform -n "maya_output";
	rename -uid "53EE2F68-45B1-F180-E3AB-AEAFFF1229E9";
createNode mesh -n "maya_outputShape" -p "maya_output";
	rename -uid "AE437293-4800-0F9B-57B8-1F875787A15D";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39099032 0.39099032 -0.39099032 
		-0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 -0.39099032 
		-0.39099032 -0.39099032 0.39099032 -0.39099032 0.39099032 -0.39099032 -0.39099032 
		0.39099032 0.39099032 0.39099032 0.39099032 -0.39099032 0.39099032 0.39099032;
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
createNode transform -n "output";
	rename -uid "414A277B-4DD3-4F2A-1D11-6F82BA5F6B70";
createNode mesh -n "outputShape" -p "output";
	rename -uid "AA33CF02-45BC-EA3E-D820-AE886B5A601D";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.39746848 0.39746848 -0.39746848 
		-0.39746848 0.39746848 -0.39746848 0.39746848 -0.39746848 -0.39746848 -0.39746848 
		-0.39746848 -0.39746848 0.39746848 -0.39746848 0.39746848 -0.39746848 -0.39746848 
		0.39746848 0.39746848 0.39746848 0.39746848 -0.39746848 0.39746848 0.39746848;
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
createNode lightLinker -s -n "lightLinker1";
	rename -uid "950E159D-4647-B657-C89D-ADB53492CF5B";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "53E4ADE0-408B-55D0-8152-398342FC340F";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "3FB7CFC5-4AA0-78C9-E363-B18633443E1A";
createNode displayLayerManager -n "layerManager";
	rename -uid "ABB1CE9A-4E23-3A79-D808-31842A8A3AAC";
createNode displayLayer -n "defaultLayer";
	rename -uid "8F93688F-46E3-F6B2-6739-A181975EFC16";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "1F139352-4C51-6CED-E654-669263BE8A11";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "143B10B8-4219-D6B6-2030-EB8B52461AE1";
	setAttr ".g" yes;
createNode vectorProduct -n "noOperation_vectorProduct";
	rename -uid "D93B6729-4B46-0DF1-E461-DA9B8CF521D4";
	setAttr ".op" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "26C7FD84-4F53-6297-3D65-EB96825D40BE";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "0EA1FA5D-4EA2-37CC-28EE-F0BCBBAC54EF";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -443.84129532314876 -548.09814761406722 ;
	setAttr ".tgi[0].vh" -type "double2" 949.77785733801682 288.45885412168087 ;
	setAttr -s 4 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 236.05557250976563;
	setAttr ".tgi[0].ni[0].y" 155.93301391601563;
	setAttr ".tgi[0].ni[0].nvs" 18306;
	setAttr ".tgi[0].ni[1].x" -174.28457641601563;
	setAttr ".tgi[0].ni[1].y" 173.80892944335938;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" -189.58747863769531;
	setAttr ".tgi[0].ni[2].y" 46.268844604492188;
	setAttr ".tgi[0].ni[2].nvs" 18305;
	setAttr ".tgi[0].ni[3].x" 585.9735107421875;
	setAttr ".tgi[0].ni[3].y" 172.6077880859375;
	setAttr ".tgi[0].ni[3].nvs" 18306;
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
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "input1_locatorShape.wm" "a_annotationShape.dom" -na;
connectAttr "input2_locatorShape.wm" "b_annotationShape.dom" -na;
connectAttr "noOperation_vectorProduct.o" "maya_output.t";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "input2Shape.wp" "noOperation_vectorProduct.i2";
connectAttr "input1Shape.wp" "noOperation_vectorProduct.i1";
connectAttr "input2Shape.wm" "noOperation_vectorProduct.m";
connectAttr "noOperation_vectorProduct.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "input1Shape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "input2Shape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "maya_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "maya_outputShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "outputShape.iog" ":initialShadingGroup.dsm" -na;
// End of test_prVectorProduct.ma
