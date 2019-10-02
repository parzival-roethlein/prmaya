//Maya ASCII 2018 scene
//Name: test_prVectorBlend.ma
//Last modified: Wed, Oct 02, 2019 01:23:44 AM
//Codeset: 1252
requires maya "2018";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "BE80F057-4CF8-69EA-FC3E-A69C5E9BE5F8";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1.0171885838354693 1.5293201303478805 2.9145858301320966 ;
	setAttr ".r" -type "double3" -19.538352729605776 9.4000000000003201 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "94EF5145-4BBA-DFB5-345A-8C95B1101ABF";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 3.1253431358612369;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0.25 0.25 0 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "50A67AB2-4B26-1BBD-3809-97854534E8DA";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "499BC3FD-4E99-B46E-1C34-21B4EE9D74F7";
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
	rename -uid "A0E72EAF-4CBA-2609-C2B4-71B4420ABDD6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "50FDE6F9-4815-BF06-6D5B-E788A2CC446D";
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
	rename -uid "96A15764-4F75-8065-9E67-75995D109124";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "6E24364E-4565-F457-DAB2-049F3A8BFDEA";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "input_group";
	rename -uid "315F2C15-4018-4C49-607E-8CB7E363E363";
createNode transform -n "input1" -p "input_group";
	rename -uid "E35B83E9-435B-B449-BA84-5086400C7F3C";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.5 1 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "input1Shape" -p "input1";
	rename -uid "51A5B44D-4E82-61BC-B64F-4F85DCE35463";
	setAttr -k off ".v";
	setAttr -cb off ".lpx";
	setAttr -cb off ".lpy";
	setAttr -cb off ".lpz";
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
	setAttr -cb off ".lsx";
	setAttr -cb off ".lsy";
	setAttr -cb off ".lsz";
createNode transform -n "input2" -p "input_group";
	rename -uid "E0BBE73A-46FA-F54F-B218-26B91DFD7EEA";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1 0 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "input2Shape" -p "input2";
	rename -uid "B2E22F91-4B12-FDD9-7898-63BAFD653A31";
	setAttr -k off ".v";
	setAttr -cb off ".lpx";
	setAttr -cb off ".lpy";
	setAttr -cb off ".lpz";
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
	setAttr -cb off ".lsx";
	setAttr -cb off ".lsy";
	setAttr -cb off ".lsz";
createNode transform -n "input_annotation_group" -p "input_group";
	rename -uid "886504F2-4F54-CDB8-2C01-16B62A81486D";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
createNode transform -n "input1_arrow_annotation" -p "input_annotation_group";
	rename -uid "D00232EE-4332-6EA4-611D-48B056F4FE21";
createNode annotationShape -n "input1_arrow_annotationShape" -p "input1_arrow_annotation";
	rename -uid "0BE208AC-47EC-1457-082E-FCB0A09F1C5A";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".txt" -type "string" "";
createNode transform -n "input2_arrow_annotation" -p "input_annotation_group";
	rename -uid "F05DADE6-48A7-2FC1-DE5A-A4912642034A";
createNode annotationShape -n "input2_arrow_annotationShape" -p "input2_arrow_annotation";
	rename -uid "F824B046-44D0-EC91-C603-9EBA57DB511A";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".txt" -type "string" "";
createNode transform -n "input1_annotation" -p "input_annotation_group";
	rename -uid "0ED19F2F-4138-4AEE-B285-5B9BAF2F89C9";
	setAttr -l on ".v";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode annotationShape -n "input1_annotationShape" -p "input1_annotation";
	rename -uid "FE61B7EA-4AE5-8B22-55F3-AAB620C0423E";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".txt" -type "string" "input1";
	setAttr ".daro" no;
createNode pointConstraint -n "input1_annotation_pointConstraint1" -p "input1_annotation";
	rename -uid "AC4512C7-437E-CA35-8B1F-49B6146165B1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "input_groupW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "input1W1" -dv 1 -min 0 -at "double";
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
	setAttr -s 2 ".tg";
	setAttr ".rst" -type "double3" 0.5 0 0 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "input2_annotation" -p "input_annotation_group";
	rename -uid "A5889984-41F6-C1FE-0376-4793AE4DF441";
	setAttr -l on ".v";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode annotationShape -n "input2_annotationShape" -p "input2_annotation";
	rename -uid "C7FA8A78-4BCA-A905-C9AA-2D95E155D640";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".txt" -type "string" "input2";
	setAttr ".daro" no;
createNode pointConstraint -n "input2_annotation_pointConstraint1" -p "input2_annotation";
	rename -uid "C76AE11A-4059-D6F7-581C-DD9233400EAF";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "input_groupW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "input2W1" -dv 1 -min 0 -at "double";
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
	setAttr -s 2 ".tg";
	setAttr ".rst" -type "double3" 0 0.5 0 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "output_group";
	rename -uid "DAC4CE01-45BB-0A82-29F9-A881FF9B9595";
createNode transform -n "output" -p "output_group";
	rename -uid "E3A4C9C1-40C7-9875-4EE4-FB86B4FB359C";
	addAttr -ci true -sn "blender" -ln "blender" -at "double";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0.75 0.5 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".blender" 0.5;
createNode mesh -n "outputShape" -p "output";
	rename -uid "361755DB-4DB5-6BD8-5A5F-BE90E11942F8";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.44482839 0.44482839 -0.44482839 
		-0.44482839 0.44482839 -0.44482839 0.44482839 -0.44482839 -0.44482839 -0.44482839 
		-0.44482839 -0.44482839 0.44482839 -0.44482839 0.44482839 -0.44482839 -0.44482839 
		0.44482839 0.44482839 0.44482839 0.44482839 -0.44482839 0.44482839 0.44482839;
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
createNode transform -n "output_an" -p "output";
	rename -uid "7C0B62B4-438A-6787-80DE-2F95246CBC0B";
	setAttr -k off ".v" no;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "output_anShape" -p "output_an";
	rename -uid "1406F70C-4D1B-AAEE-F302-5691B2D1449B";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode transform -n "output_maya" -p "output_group";
	rename -uid "147BF5BA-4820-DEDF-EF28-FD851BE59618";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
createNode mesh -n "output_mayaShape" -p "output_maya";
	rename -uid "14EB333B-4D22-A99E-6C26-32B66ECD46F4";
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
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.43938744 0.43938744 -0.43938744 
		-0.43938744 0.43938744 -0.43938744 0.43938744 -0.43938744 -0.43938744 -0.43938744 
		-0.43938744 -0.43938744 0.43938744 -0.43938744 0.43938744 -0.43938744 -0.43938744 
		0.43938744 0.43938744 0.43938744 0.43938744 -0.43938744 0.43938744 0.43938744;
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
createNode transform -n "output_annotation_group" -p "output_group";
	rename -uid "C0E90524-4C08-B3C9-87F5-C797F6C2A285";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
createNode transform -n "output_arrow_annotation" -p "output_annotation_group";
	rename -uid "225FAE5B-4453-FC4D-D2C5-3C870632575D";
	setAttr ".t" -type "double3" 0 1.3877787807814457e-15 0 ;
createNode annotationShape -n "output_arrow_annotationShape" -p "output_arrow_annotation";
	rename -uid "8D673B57-453F-39B1-0974-12B5E27F7CDB";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "";
createNode transform -n "output_annotation" -p "output_annotation_group";
	rename -uid "B56A9634-4F6D-0C7F-FB21-DABEA858EE7E";
createNode annotationShape -n "output_annotationShape" -p "output_annotation";
	rename -uid "85AA6C1D-4ECA-B0BE-0D59-67B9DECB231C";
	setAttr -k off ".v";
	setAttr ".txt" -type "string" "output / blender";
	setAttr ".daro" no;
createNode pointConstraint -n "output_annotation_pointConstraint1" -p "output_annotation";
	rename -uid "021E4F54-49CA-6D75-E6A7-909B4F26486F";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "output_groupW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "outputW1" -dv 1 -min 0 -at "double";
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
	setAttr -s 2 ".tg";
	setAttr ".rst" -type "double3" 0.32796799968075524 0.23484830937629678 -0.13506415059729426 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "E8EB9E50-4837-2830-B7B6-B1AF04B57F51";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "4BC8E572-407C-B2E2-0FF5-D7AE4CD1FD46";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "6DBD45D4-433B-7527-5474-1AAD04C4B3A3";
createNode displayLayerManager -n "layerManager";
	rename -uid "D3C12610-4252-06E6-9043-51A283064F8B";
createNode displayLayer -n "defaultLayer";
	rename -uid "3CEB601F-44AB-3B1F-A1FC-419CE307CF60";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "8FE74AB0-4017-9E3A-0D33-5D81DD246A9C";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "9E08ECF3-4E11-2798-6D57-5982D3DBF79A";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "0CCAA7A1-47E5-8793-6DDA-01B09557DB41";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "D7B9B52B-4E46-7CD3-206A-EF9D9B8962E2";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -1133.3332882987147 -553.57140657447724 ;
	setAttr ".tgi[0].vh" -type "double2" 1133.3332882987147 553.57140657447724 ;
createNode blendColors -n "output_blendColors";
	rename -uid "A76B262D-41F7-4689-1F1A-558CCBEB609B";
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
connectAttr "input1Shape.wm" "input1_arrow_annotationShape.dom" -na;
connectAttr "input2Shape.wm" "input2_arrow_annotationShape.dom" -na;
connectAttr "input1_annotation_pointConstraint1.ctx" "input1_annotation.tx";
connectAttr "input1_annotation_pointConstraint1.cty" "input1_annotation.ty";
connectAttr "input1_annotation_pointConstraint1.ctz" "input1_annotation.tz";
connectAttr "input1_annotation.pim" "input1_annotation_pointConstraint1.cpim";
connectAttr "input1_annotation.rp" "input1_annotation_pointConstraint1.crp";
connectAttr "input1_annotation.rpt" "input1_annotation_pointConstraint1.crt";
connectAttr "input_group.t" "input1_annotation_pointConstraint1.tg[0].tt";
connectAttr "input_group.rp" "input1_annotation_pointConstraint1.tg[0].trp";
connectAttr "input_group.rpt" "input1_annotation_pointConstraint1.tg[0].trt";
connectAttr "input_group.pm" "input1_annotation_pointConstraint1.tg[0].tpm";
connectAttr "input1_annotation_pointConstraint1.w0" "input1_annotation_pointConstraint1.tg[0].tw"
		;
connectAttr "input1.t" "input1_annotation_pointConstraint1.tg[1].tt";
connectAttr "input1.rp" "input1_annotation_pointConstraint1.tg[1].trp";
connectAttr "input1.rpt" "input1_annotation_pointConstraint1.tg[1].trt";
connectAttr "input1.pm" "input1_annotation_pointConstraint1.tg[1].tpm";
connectAttr "input1_annotation_pointConstraint1.w1" "input1_annotation_pointConstraint1.tg[1].tw"
		;
connectAttr "input2_annotation_pointConstraint1.ctx" "input2_annotation.tx";
connectAttr "input2_annotation_pointConstraint1.cty" "input2_annotation.ty";
connectAttr "input2_annotation_pointConstraint1.ctz" "input2_annotation.tz";
connectAttr "input2_annotation.pim" "input2_annotation_pointConstraint1.cpim";
connectAttr "input2_annotation.rp" "input2_annotation_pointConstraint1.crp";
connectAttr "input2_annotation.rpt" "input2_annotation_pointConstraint1.crt";
connectAttr "input_group.t" "input2_annotation_pointConstraint1.tg[0].tt";
connectAttr "input_group.rp" "input2_annotation_pointConstraint1.tg[0].trp";
connectAttr "input_group.rpt" "input2_annotation_pointConstraint1.tg[0].trt";
connectAttr "input_group.pm" "input2_annotation_pointConstraint1.tg[0].tpm";
connectAttr "input2_annotation_pointConstraint1.w0" "input2_annotation_pointConstraint1.tg[0].tw"
		;
connectAttr "input2.t" "input2_annotation_pointConstraint1.tg[1].tt";
connectAttr "input2.rp" "input2_annotation_pointConstraint1.tg[1].trp";
connectAttr "input2.rpt" "input2_annotation_pointConstraint1.tg[1].trt";
connectAttr "input2.pm" "input2_annotation_pointConstraint1.tg[1].tpm";
connectAttr "input2_annotation_pointConstraint1.w1" "input2_annotation_pointConstraint1.tg[1].tw"
		;
connectAttr "output_blendColors.op" "output_maya.t";
connectAttr "output_anShape.wm" "output_arrow_annotationShape.dom" -na;
connectAttr "output_annotation_pointConstraint1.ctx" "output_annotation.tx";
connectAttr "output_annotation_pointConstraint1.cty" "output_annotation.ty";
connectAttr "output_annotation_pointConstraint1.ctz" "output_annotation.tz";
connectAttr "output_annotation.pim" "output_annotation_pointConstraint1.cpim";
connectAttr "output_annotation.rp" "output_annotation_pointConstraint1.crp";
connectAttr "output_annotation.rpt" "output_annotation_pointConstraint1.crt";
connectAttr "output_group.t" "output_annotation_pointConstraint1.tg[0].tt";
connectAttr "output_group.rp" "output_annotation_pointConstraint1.tg[0].trp";
connectAttr "output_group.rpt" "output_annotation_pointConstraint1.tg[0].trt";
connectAttr "output_group.pm" "output_annotation_pointConstraint1.tg[0].tpm";
connectAttr "output_annotation_pointConstraint1.w0" "output_annotation_pointConstraint1.tg[0].tw"
		;
connectAttr "output_an.t" "output_annotation_pointConstraint1.tg[1].tt";
connectAttr "output_an.rp" "output_annotation_pointConstraint1.tg[1].trp";
connectAttr "output_an.rpt" "output_annotation_pointConstraint1.tg[1].trt";
connectAttr "output_an.pm" "output_annotation_pointConstraint1.tg[1].tpm";
connectAttr "output_annotation_pointConstraint1.w1" "output_annotation_pointConstraint1.tg[1].tw"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "input1.t" "output_blendColors.c1";
connectAttr "input2.t" "output_blendColors.c2";
connectAttr "output.blender" "output_blendColors.b";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "outputShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "output_mayaShape.iog" ":initialShadingGroup.dsm" -na;
// End of test_prVectorBlend.ma
