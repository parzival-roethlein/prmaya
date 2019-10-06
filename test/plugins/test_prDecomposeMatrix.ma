//Maya ASCII 2018 scene
//Name: test_prDecomposeMatrix.ma
//Last modified: Sat, Oct 05, 2019 02:22:40 AM
//Codeset: 1252
requires maya "2018";
requires -nodeType "decomposeMatrix" "matrixNodes" "1.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "781BF7F8-4A4A-23F1-1705-5C8EBBB4C932";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 3.0019651908525762 2.3387185573802176 5.1123545565209829 ;
	setAttr ".r" -type "double3" -20.138352729603742 34.600000000000669 9.6598656159682859e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "518D0D04-4B2D-7103-421E-788887B0179D";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 6.2884532844691563;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "80A03E00-4603-7838-E478-AABF8520A39E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "28FA8696-4CFC-28D2-5B80-ECA745B1067A";
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
	rename -uid "2F6A65F3-4565-DF7A-8A39-C1B03C44F318";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "3554E4B5-4208-D5B9-A52A-08A628F2B291";
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
	rename -uid "9DB465EE-4913-BBE7-F80A-3D979DF839DC";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "5C094D68-4BB1-7809-9F94-71A4F4DC3ABF";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "cube_group";
	rename -uid "DBEDCD11-4E59-0BC4-1509-F38FAC1BE6D4";
	setAttr ".ro" 4;
createNode transform -n "prnode_output" -p "cube_group";
	rename -uid "13D8EA59-4631-BF0E-B0FC-66A97AB5599D";
createNode mesh -n "prnode_outputShape" -p "prnode_output";
	rename -uid "A380BE01-472D-D47B-C5A5-829374F3EED4";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
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
createNode transform -n "maya_output" -p "cube_group";
	rename -uid "62F65C2C-436C-FF85-13D7-C897A1A133FD";
createNode mesh -n "maya_outputShape" -p "maya_output";
	rename -uid "9F3D0630-4069-A14E-F797-BEBBE8198D38";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  -0.01851755 -0.01851755 0.01851755 
		0.01851755 -0.01851755 0.01851755 -0.01851755 0.01851755 0.01851755 0.01851755 0.01851755 
		0.01851755 -0.01851755 0.01851755 -0.01851755 0.01851755 0.01851755 -0.01851755 -0.01851755 
		-0.01851755 -0.01851755 0.01851755 -0.01851755 -0.01851755;
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
createNode transform -n "matrix_group";
	rename -uid "3B8B0BE1-42C0-A080-6639-4AB3E535FD47";
createNode transform -n "inputMatrix" -p "matrix_group";
	rename -uid "E6482067-49F5-57C7-431E-6695D79FDB5D";
createNode locator -n "inputMatrixShape" -p "inputMatrix";
	rename -uid "2B5BA8B0-472F-DFF9-A349-86ACD32232AC";
	setAttr -k off ".v";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "9799CF20-4FBF-71B6-D397-418B48F5D483";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "D33FB987-4417-D4E0-79D7-72A5A2057F39";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "9D862494-4614-27EB-4394-DE9B8BDF4262";
createNode displayLayerManager -n "layerManager";
	rename -uid "DA80D73C-4429-0E6D-8310-7DBD169F7A79";
createNode displayLayer -n "defaultLayer";
	rename -uid "48AC7BA3-49A7-061B-983C-209E1ED57053";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "7AC3A79C-473C-3185-5A12-35975BBAC48A";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "8B5BF3C3-4EE7-EDE3-FAB2-FD931A64E9C3";
	setAttr ".g" yes;
createNode decomposeMatrix -n "decomposeMatrix1";
	rename -uid "15C5282F-48FF-4F65-B7B9-58921BAB9937";
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "51775098-4AD4-FD8E-6459-4FBA829889D9";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "22AAE918-4B74-5EE8-1DD5-F7AB494DA053";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -519.64284250465801 -367.93255765241719 ;
	setAttr ".tgi[0].vh" -type "double2" 516.49158221406674 417.93255583255547 ;
	setAttr -s 3 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -405.71429443359375;
	setAttr ".tgi[0].ni[0].y" 32.857143402099609;
	setAttr ".tgi[0].ni[0].nvs" 18305;
	setAttr ".tgi[0].ni[1].x" -98.571426391601563;
	setAttr ".tgi[0].ni[1].y" 122.85713958740234;
	setAttr ".tgi[0].ni[1].nvs" 18305;
	setAttr ".tgi[0].ni[2].x" 208.57142639160156;
	setAttr ".tgi[0].ni[2].y" 122.85713958740234;
	setAttr ".tgi[0].ni[2].nvs" 18305;
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
connectAttr "decomposeMatrix1.ot" "maya_output.t";
connectAttr "decomposeMatrix1.os" "maya_output.s";
connectAttr "decomposeMatrix1.osh" "maya_output.sh";
connectAttr "decomposeMatrix1.or" "maya_output.r";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "inputMatrix.m" "decomposeMatrix1.imat";
connectAttr "inputMatrix.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "decomposeMatrix1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "maya_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "prnode_outputShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "maya_outputShape.iog" ":initialShadingGroup.dsm" -na;
// End of test_prDecomposeMatrix.ma
