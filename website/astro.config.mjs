// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import remarkGithubAdmonitionsToDirectives from 'remark-github-admonitions-to-directives';

// Lesson callouts are authored in GitHub admonition syntax (`> [!NOTE]`). This
// remark plugin rewrites them into Starlight aside directives before Starlight
// renders them, so the same syntax used in the repo's READMEs and on github.com
// also produces styled callouts on the published site. The mapping targets
// Starlight's aside types (note / tip / caution / danger).
const githubAdmonitionMapping = {
  NOTE: 'note',
  TIP: 'tip',
  IMPORTANT: 'note',
  WARNING: 'caution',
  CAUTION: 'caution',
};

// https://astro.build/config
export default defineConfig({
  site: 'https://github-samples.github.io',
  base: '/copilot-workshops',
  trailingSlash: 'always',
  markdown: {
    remarkPlugins: [
      [remarkGithubAdmonitionsToDirectives, { mapping: githubAdmonitionMapping }],
    ],
  },
  integrations: [
    starlight({
      title: 'Copilot Workshops',
      description:
        'A hands-on workshop exploring GitHub Copilot agents across VS Code, the Copilot CLI, the GitHub Copilot app, and the Copilot cloud agent.',
      locales: {
        root: { label: 'English', lang: 'en' },
        'es-es': { label: 'Español', lang: 'es-ES' },
        'ja-jp': { label: '日本語', lang: 'ja-JP' },
        'ko-kr': { label: '한국어', lang: 'ko-KR' },
        'pl-pl': { label: 'Polski', lang: 'pl-PL' },
        'pt-br': { label: 'Português (Brasil)', lang: 'pt-BR' },
        'zh-cn': { label: '简体中文', lang: 'zh-CN' },
      },
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/github-samples/copilot-workshops',
        },
      ],
      editLink: {
        baseUrl:
          'https://github.com/github-samples/copilot-workshops/edit/main/docs/',
      },
      sidebar: [
        { label: 'Home', link: '/' },
        {
          label: 'First steps',
          translations: {
            'es-ES': 'Primeros pasos',
            'ja-JP': 'はじめの一歩',
            'ko-KR': '첫 단계',
            'pt-BR': 'Primeiros passos',
            'zh-CN': '入门体验',
          },
          items: [
            {
              label: 'Overview',
              link: '/first-steps/',
              translations: {
                'es-ES': 'Descripción general',
                'ja-JP': '概要',
                'ko-KR': '개요',
                'pt-BR': 'Visão geral',
                'zh-CN': '概述',
              },
            },
            {
              label: 'GitHub Copilot app',
              items: [
                {
                  label: 'Overview',
                  link: '/first-steps/copilot-app/',
                  translations: {
                    'es-ES': 'Descripción general',
                    'ja-JP': '概要',
                    'ko-KR': '개요',
                    'pt-BR': 'Visão geral',
                    'zh-CN': '概述',
                  },
                },
                {
                  label: '0. Prerequisites and setup',
                  link: '/first-steps/copilot-app/0-prerequisites/',
                  translations: {
                    'es-ES': '0. Requisitos previos y configuración',
                    'ja-JP': '0. 前提条件とセットアップ',
                    'ko-KR': '0. 사전 준비 및 설정',
                    'pt-BR': '0. Pré-requisitos e configuração',
                    'zh-CN': '0. 先决条件与设置',
                  },
                },
                {
                  label: '1. Create the workspace',
                  link: '/first-steps/copilot-app/1-create-workspace/',
                  translations: {
                    'es-ES': '1. Crea el espacio de trabajo',
                    'ja-JP': '1. ワークスペースを作成する',
                    'ko-KR': '1. 작업 영역 만들기',
                    'pt-BR': '1. Crie o espaço de trabalho',
                    'zh-CN': '1. 创建工作区',
                  },
                },
                {
                  label: '2. Build and polish',
                  link: '/first-steps/copilot-app/2-build-and-polish/',
                  translations: {
                    'es-ES': '2. Crea y mejora',
                    'ja-JP': '2. 作成して仕上げる',
                    'ko-KR': '2. 만들고 다듬기',
                    'pt-BR': '2. Crie e aprimore',
                    'zh-CN': '2. 构建与完善',
                  },
                },
                {
                  label: '3. Inspect and test',
                  link: '/first-steps/copilot-app/3-inspect-and-test/',
                  translations: {
                    'es-ES': '3. Inspecciona y prueba',
                    'ja-JP': '3. 確認してテストする',
                    'ko-KR': '3. 살펴보고 테스트하기',
                    'pt-BR': '3. Inspecione e teste',
                    'zh-CN': '3. 检查与测试',
                  },
                },
                {
                  label: '4. Project instructions',
                  link: '/first-steps/copilot-app/4-project-instructions/',
                  translations: {
                    'es-ES': '4. Instrucciones del proyecto',
                    'ja-JP': '4. プロジェクトの指示',
                    'ko-KR': '4. 프로젝트 지침',
                    'pt-BR': '4. Instruções do projeto',
                    'zh-CN': '4. 项目指令',
                  },
                },
                {
                  label: '5. Publish the project',
                  link: '/first-steps/copilot-app/5-publish/',
                  translations: {
                    'es-ES': '5. Publica el proyecto',
                    'ja-JP': '5. プロジェクトを公開する',
                    'ko-KR': '5. 프로젝트 게시하기',
                    'pt-BR': '5. Publique o projeto',
                    'zh-CN': '5. 发布项目',
                  },
                },
                {
                  label: '6. Issues and sessions',
                  link: '/first-steps/copilot-app/6-issues-and-sessions/',
                  translations: {
                    'es-ES': '6. Incidencias y sesiones',
                    'ja-JP': '6. Issue とセッション',
                    'ko-KR': '6. 이슈와 세션',
                    'pt-BR': '6. Issues e sessões',
                    'zh-CN': '6. 议题与会话',
                  },
                },
                {
                  label: '7. Plan before you edit',
                  link: '/first-steps/copilot-app/7-plan-mode/',
                  translations: {
                    'es-ES': '7. Planifica antes de editar',
                    'ja-JP': '7. 編集前に計画する',
                    'ko-KR': '7. 편집 전에 계획하기',
                    'pt-BR': '7. Planeje antes de editar',
                    'zh-CN': '7. 先规划再编辑',
                  },
                },
                {
                  label: '8. Complete the review loop',
                  link: '/first-steps/copilot-app/8-review-loop/',
                  translations: {
                    'es-ES': '8. Completa el ciclo de revisión',
                    'ja-JP': '8. レビューのサイクルを完了する',
                    'ko-KR': '8. 검토 과정 완료하기',
                    'pt-BR': '8. Conclua o ciclo de revisão',
                    'zh-CN': '8. 完成审查流程',
                  },
                },
                {
                  label: '9. Automate issue triage',
                  link: '/first-steps/copilot-app/9-automations/',
                  translations: {
                    'es-ES': '9. Automatiza la clasificación de incidencias',
                    'ja-JP': '9. Issue のトリアージを自動化する',
                    'ko-KR': '9. 이슈 분류 자동화하기',
                    'pt-BR': '9. Automatize a triagem de issues',
                    'zh-CN': '9. 自动化议题分类',
                  },
                },
                {
                  label: '10. Continue remotely (optional)',
                  link: '/first-steps/copilot-app/10-remote/',
                  translations: {
                    'es-ES': '10. Continúa de forma remota (opcional)',
                    'ja-JP': '10. リモートで続ける (省略可能)',
                    'ko-KR': '10. 원격으로 계속하기 (선택 사항)',
                    'pt-BR': '10. Continue remotamente (opcional)',
                    'zh-CN': '10. 远程继续工作（可选）',
                  },
                },
                {
                  label: '11. Explore a Canvas',
                  link: '/first-steps/copilot-app/11-canvas/',
                  translations: {
                    'es-ES': '11. Explora un Canvas',
                    'ja-JP': '11. Canvas を体験する',
                    'ko-KR': '11. Canvas 살펴보기',
                    'pt-BR': '11. Explore um Canvas',
                    'zh-CN': '11. 探索 Canvas',
                  },
                },
                {
                  label: '12. Review and next steps',
                  link: '/first-steps/copilot-app/12-review/',
                  translations: {
                    'es-ES': '12. Repaso y próximos pasos',
                    'ja-JP': '12. 振り返りと次のステップ',
                    'ko-KR': '12. 복습 및 다음 단계',
                    'pt-BR': '12. Revisão e próximos passos',
                    'zh-CN': '12. 回顾与后续步骤',
                  },
                },
              ],
            },
            {
              label: 'GitHub Copilot CLI',
              items: [
                {
                  label: 'Overview',
                  link: '/first-steps/copilot-cli/',
                  translations: {
                    'es-ES': 'Descripción general',
                    'ja-JP': '概要',
                    'ko-KR': '개요',
                    'pt-BR': 'Visão geral',
                    'zh-CN': '概述',
                  },
                },
                {
                  label: '0. Prerequisites and setup',
                  link: '/first-steps/copilot-cli/0-prerequisites/',
                  translations: {
                    'es-ES': '0. Requisitos previos y configuración',
                    'ja-JP': '0. 前提条件とセットアップ',
                    'ko-KR': '0. 사전 준비 및 설정',
                    'pt-BR': '0. Pré-requisitos e configuração',
                    'zh-CN': '0. 先决条件与设置',
                  },
                },
                {
                  label: '1. Build the quiz',
                  link: '/first-steps/copilot-cli/1-build/',
                  translations: {
                    'es-ES': '1. Crea el cuestionario',
                    'ja-JP': '1. クイズを作成する',
                    'ko-KR': '1. 퀴즈 만들기',
                    'pt-BR': '1. Crie o quiz',
                    'zh-CN': '1. 构建测验',
                  },
                },
                {
                  label: '2. Project instructions',
                  link: '/first-steps/copilot-cli/2-project-instructions/',
                  translations: {
                    'es-ES': '2. Instrucciones del proyecto',
                    'ja-JP': '2. プロジェクトの指示',
                    'ko-KR': '2. 프로젝트 지침',
                    'pt-BR': '2. Instruções do projeto',
                    'zh-CN': '2. 项目指令',
                  },
                },
                {
                  label: '3. Publish the project',
                  link: '/first-steps/copilot-cli/3-publish/',
                  translations: {
                    'es-ES': '3. Publica el proyecto',
                    'ja-JP': '3. プロジェクトを公開する',
                    'ko-KR': '3. 프로젝트 게시하기',
                    'pt-BR': '3. Publique o projeto',
                    'zh-CN': '3. 发布项目',
                  },
                },
                {
                  label: '4. Issues in parallel',
                  link: '/first-steps/copilot-cli/4-issues-and-sessions/',
                  translations: {
                    'es-ES': '4. Incidencias en paralelo',
                    'ja-JP': '4. Issue を並行して処理する',
                    'ko-KR': '4. 이슈 병렬 처리하기',
                    'pt-BR': '4. Issues em paralelo',
                    'zh-CN': '4. 并行处理议题',
                  },
                },
                {
                  label: '5. Plan before you edit',
                  link: '/first-steps/copilot-cli/5-plan-mode/',
                  translations: {
                    'es-ES': '5. Planifica antes de editar',
                    'ja-JP': '5. 編集前に計画する',
                    'ko-KR': '5. 편집 전에 계획하기',
                    'pt-BR': '5. Planeje antes de editar',
                    'zh-CN': '5. 先规划再编辑',
                  },
                },
                {
                  label: '6. Manage context',
                  link: '/first-steps/copilot-cli/6-context/',
                  translations: {
                    'es-ES': '6. Gestiona el contexto',
                    'ja-JP': '6. コンテキストを管理する',
                    'ko-KR': '6. 컨텍스트 관리하기',
                    'pt-BR': '6. Gerencie o contexto',
                    'zh-CN': '6. 管理上下文',
                  },
                },
                {
                  label: '7. Resume and go remote',
                  link: '/first-steps/copilot-cli/7-resume-and-remote/',
                  translations: {
                    'es-ES': '7. Reanuda y continúa de forma remota',
                    'ja-JP': '7. 再開してリモートで続ける',
                    'ko-KR': '7. 재개하고 원격으로 작업하기',
                    'pt-BR': '7. Retome e continue remotamente',
                    'zh-CN': '7. 恢复会话并远程工作',
                  },
                },
                {
                  label: '8. Create and merge a PR',
                  link: '/first-steps/copilot-cli/8-pull-request/',
                  translations: {
                    'es-ES': '8. Crea y combina una solicitud de incorporación de cambios',
                    'ja-JP': '8. プル リクエストを作成してマージする',
                    'ko-KR': '8. 끌어오기 요청 만들기 및 병합하기',
                    'pt-BR': '8. Crie e mescle um pull request',
                    'zh-CN': '8. 创建并合并拉取请求',
                  },
                },
                {
                  label: '9. Delegate work',
                  link: '/first-steps/copilot-cli/9-delegate/',
                  translations: {
                    'es-ES': '9. Delega trabajo',
                    'ja-JP': '9. 作業を委任する',
                    'ko-KR': '9. 작업 위임하기',
                    'pt-BR': '9. Delegue trabalho',
                    'zh-CN': '9. 委派工作',
                  },
                },
                {
                  label: '10. Review and next steps',
                  link: '/first-steps/copilot-cli/10-review/',
                  translations: {
                    'es-ES': '10. Repaso y próximos pasos',
                    'ja-JP': '10. 振り返りと次のステップ',
                    'ko-KR': '10. 복습 및 다음 단계',
                    'pt-BR': '10. Revisão e próximos passos',
                    'zh-CN': '10. 回顾与后续步骤',
                  },
                },
              ],
            },
            {
              label: 'Visual Studio Code',
              items: [
                {
                  label: 'Overview',
                  link: '/first-steps/vscode/',
                  translations: {
                    'es-ES': 'Descripción general',
                    'ja-JP': '概要',
                    'ko-KR': '개요',
                    'pt-BR': 'Visão geral',
                    'zh-CN': '概述',
                  },
                },
                {
                  label: '0. Prerequisites and setup',
                  link: '/first-steps/vscode/0-prerequisites/',
                  translations: {
                    'es-ES': '0. Requisitos previos y configuración',
                    'ja-JP': '0. 前提条件とセットアップ',
                    'ko-KR': '0. 사전 준비 및 설정',
                    'pt-BR': '0. Pré-requisitos e configuração',
                    'zh-CN': '0. 先决条件与设置',
                  },
                },
                {
                  label: '1. Build and polish',
                  link: '/first-steps/vscode/1-build-and-polish/',
                  translations: {
                    'es-ES': '1. Crea y mejora',
                    'ja-JP': '1. 作成して仕上げる',
                    'ko-KR': '1. 만들고 다듬기',
                    'pt-BR': '1. Crie e aprimore',
                    'zh-CN': '1. 构建与完善',
                  },
                },
                {
                  label: '2. Project instructions',
                  link: '/first-steps/vscode/2-project-instructions/',
                  translations: {
                    'es-ES': '2. Instrucciones del proyecto',
                    'ja-JP': '2. プロジェクトの指示',
                    'ko-KR': '2. 프로젝트 지침',
                    'pt-BR': '2. Instruções do projeto',
                    'zh-CN': '2. 项目指令',
                  },
                },
                {
                  label: '3. Inspect context and test',
                  link: '/first-steps/vscode/3-inspect-and-test/',
                  translations: {
                    'es-ES': '3. Inspecciona el contexto y prueba',
                    'ja-JP': '3. コンテキストを確認してテストする',
                    'ko-KR': '3. 컨텍스트 확인 및 테스트하기',
                    'pt-BR': '3. Inspecione o contexto e teste',
                    'zh-CN': '3. 检查上下文并测试',
                  },
                },
                {
                  label: '4. Publish the project',
                  link: '/first-steps/vscode/4-publish/',
                  translations: {
                    'es-ES': '4. Publica el proyecto',
                    'ja-JP': '4. プロジェクトを公開する',
                    'ko-KR': '4. 프로젝트 게시하기',
                    'pt-BR': '4. Publique o projeto',
                    'zh-CN': '4. 发布项目',
                  },
                },
                {
                  label: '5. Plan before you edit',
                  link: '/first-steps/vscode/5-plan-mode/',
                  translations: {
                    'es-ES': '5. Planifica antes de editar',
                    'ja-JP': '5. 編集前に計画する',
                    'ko-KR': '5. 편집 전에 계획하기',
                    'pt-BR': '5. Planeje antes de editar',
                    'zh-CN': '5. 先规划再编辑',
                  },
                },
                {
                  label: '6. GitHub MCP',
                  link: '/first-steps/vscode/6-github-mcp/',
                  translations: {
                    'es-ES': '6. GitHub MCP',
                    'ja-JP': '6. GitHub MCP',
                    'ko-KR': '6. GitHub MCP',
                    'pt-BR': '6. GitHub MCP',
                    'zh-CN': '6. GitHub MCP',
                  },
                },
                {
                  label: '7. Issues and sessions',
                  link: '/first-steps/vscode/7-issues-and-sessions/',
                  translations: {
                    'es-ES': '7. Incidencias y sesiones',
                    'ja-JP': '7. Issue とセッション',
                    'ko-KR': '7. 이슈와 세션',
                    'pt-BR': '7. Issues e sessões',
                    'zh-CN': '7. 议题与会话',
                  },
                },
                {
                  label: '8. Review and merge',
                  link: '/first-steps/vscode/8-review-and-merge/',
                  translations: {
                    'es-ES': '8. Revisa y combina',
                    'ja-JP': '8. レビューしてマージする',
                    'ko-KR': '8. 검토 및 병합하기',
                    'pt-BR': '8. Revise e mescle',
                    'zh-CN': '8. 审查与合并',
                  },
                },
                {
                  label: '9. Cloud session',
                  link: '/first-steps/vscode/9-cloud-session/',
                  translations: {
                    'es-ES': '9. Sesión en la nube',
                    'ja-JP': '9. クラウド セッション',
                    'ko-KR': '9. 클라우드 세션',
                    'pt-BR': '9. Sessão na nuvem',
                    'zh-CN': '9. 云会话',
                  },
                },
                {
                  label: '10. Review and next steps',
                  link: '/first-steps/vscode/10-review/',
                  translations: {
                    'es-ES': '10. Repaso y próximos pasos',
                    'ja-JP': '10. 振り返りと次のステップ',
                    'ko-KR': '10. 복습 및 다음 단계',
                    'pt-BR': '10. Revisão e próximos passos',
                    'zh-CN': '10. 回顾与后续步骤',
                  },
                },
              ],
            },
          ],
        },
        {
          label: 'Real-world development',
          items: [
            { label: 'Overview', link: '/real-world-development/' },
            {
              label: 'GitHub Copilot CLI',
              items: [
                { label: 'Overview', link: '/real-world-development/cli/' },
                { label: '0. Prerequisites', link: '/real-world-development/cli/0-prerequisites/' },
                { label: '1. Installing Copilot CLI', link: '/real-world-development/cli/1-install-copilot-cli/' },
                { label: '2. Add star ratings', link: '/real-world-development/cli/2-add-star-rating/' },
                { label: '3. Agent modes: Plan and Autopilot', link: '/real-world-development/cli/3-agent-modes/' },
                { label: '4. Guiding Copilot with custom instructions', link: '/real-world-development/cli/4-custom-instructions/' },
                { label: '5. Customize and use a quality-checks skill', link: '/real-world-development/cli/5-agent-skills/' },
                { label: '6. Validate functionality with Playwright MCP', link: '/real-world-development/cli/6-mcp-playwright/' },
                { label: '7. Create and use a QA agent', link: '/real-world-development/cli/7-qa-agent/' },
                { label: '8. Create and merge the feature PR', link: '/real-world-development/cli/8-create-pull-request/' },
                { label: '9. Slash commands in Copilot CLI', link: '/real-world-development/cli/9-cli-power-tools/' },
                { label: '10. Wrap-up and next steps', link: '/real-world-development/cli/10-review/' },
                {
                  label: 'Optional: Incorporate Foundry',
                  translations: {
                    'es-ES': 'Opcional: incorpora Foundry',
                    'ja-JP': 'オプション: Foundry を組み込む',
                    'ko-KR': '선택 사항: Foundry 통합하기',
                    'pt-BR': 'Opcional: Incorpore o Foundry',
                    'zh-CN': '可选：集成 Foundry',
                  },
                  collapsed: true,
                  items: [
                    {
                      label: 'Overview',
                      link: '/real-world-development/cli/8-foundry-agent/',
                      translations: {
                        'es-ES': 'Descripción general',
                        'ja-JP': '概要',
                        'ko-KR': '개요',
                        'pt-BR': 'Visão geral',
                        'zh-CN': '概述',
                      },
                    },
                    {
                      label: '1. Prepare the project and model',
                      link: '/real-world-development/cli/8-foundry-agent/1-project-and-model/',
                      translations: {
                        'es-ES': '1. Prepara el proyecto y el modelo',
                        'ja-JP': '1. プロジェクトとモデルを準備する',
                        'ko-KR': '1. 프로젝트와 모델 준비하기',
                        'pt-BR': '1. Prepare o projeto e o modelo',
                        'zh-CN': '1. 准备项目和模型',
                      },
                    },
                    {
                      label: '2. Build and deploy the agent',
                      link: '/real-world-development/cli/8-foundry-agent/2-build-and-deploy/',
                      translations: {
                        'es-ES': '2. Crea y despliega el agente',
                        'ja-JP': '2. エージェントを構築してデプロイする',
                        'ko-KR': '2. 에이전트 빌드 및 배포하기',
                        'pt-BR': '2. Crie e implante o agente',
                        'zh-CN': '2. 构建并部署智能体',
                      },
                    },
                    {
                      label: '3. Connect the agent to the website',
                      link: '/real-world-development/cli/8-foundry-agent/3-connect-to-site/',
                      translations: {
                        'es-ES': '3. Conecta el agente al sitio web',
                        'ja-JP': '3. エージェントを Web サイトに接続する',
                        'ko-KR': '3. 에이전트를 웹사이트에 연결하기',
                        'pt-BR': '3. Conecte o agente ao site',
                        'zh-CN': '3. 将智能体连接到网站',
                      },
                    },
                  ],
                },
              ],
            },
            {
              label: 'GitHub Copilot app',
              items: [
                { label: 'Overview', link: '/real-world-development/app/' },
                { label: '0. Prerequisites', link: '/real-world-development/app/0-prerequisites/' },
                { label: '1. Install the Copilot app', link: '/real-world-development/app/1-install-copilot-app/' },
                { label: '2. Add star ratings', link: '/real-world-development/app/2-add-star-rating/' },
                { label: '3. Agent modes: Plan and Autopilot', link: '/real-world-development/app/3-agent-modes/' },
                { label: '4. Guiding Copilot with custom instructions', link: '/real-world-development/app/4-custom-instructions/' },
                { label: '5. Customize and use a quality-checks skill', link: '/real-world-development/app/5-agent-skills/' },
                { label: '6. Validate with Playwright MCP', link: '/real-world-development/app/6-mcp-playwright/' },
                { label: '7. Create and use a QA agent', link: '/real-world-development/app/7-qa-agent/' },
                { label: '8. Create and merge the feature PR', link: '/real-world-development/app/8-create-pull-request/' },
                { label: '9. Explore and create canvases', link: '/real-world-development/app/9-canvases/' },
                { label: '10. Wrap-up and next steps', link: '/real-world-development/app/10-review/' },
                {
                  label: 'Optional: Incorporate Foundry',
                  translations: {
                    'es-ES': 'Opcional: Incorporar Foundry',
                    'ja-JP': 'オプション: Foundry を組み込む',
                    'ko-KR': '선택 사항: Foundry 통합',
                    'pt-BR': 'Opcional: Incorporar o Foundry',
                    'zh-CN': '可选：集成 Foundry',
                  },
                  items: [
                    {
                      label: 'Overview',
                      link: '/real-world-development/app/8-foundry-canvas/',
                    },
                    {
                      label: '1. Prepare the project and model',
                      link: '/real-world-development/app/8-foundry-canvas/1-project-and-model/',
                      translations: {
                        'es-ES': '1. Preparar el proyecto y el modelo',
                        'ja-JP': '1. プロジェクトとモデルを準備する',
                        'ko-KR': '1. 프로젝트와 모델 준비',
                        'pt-BR': '1. Preparar o projeto e o modelo',
                        'zh-CN': '1. 准备项目和模型',
                      },
                    },
                    {
                      label: '2. Build and deploy the agent',
                      link: '/real-world-development/app/8-foundry-canvas/2-build-and-deploy/',
                      translations: {
                        'es-ES': '2. Crear e implementar el agente',
                        'ja-JP': '2. エージェントを構築してデプロイする',
                        'ko-KR': '2. 에이전트 빌드 및 배포',
                        'pt-BR': '2. Criar e implantar o agente',
                        'zh-CN': '2. 构建并部署代理',
                      },
                    },
                    {
                      label: '3. Connect the agent to the site',
                      link: '/real-world-development/app/8-foundry-canvas/3-connect-to-site/',
                      translations: {
                        'es-ES': '3. Conectar el agente al sitio',
                        'ja-JP': '3. エージェントをサイトに接続する',
                        'ko-KR': '3. 에이전트를 사이트에 연결',
                        'pt-BR': '3. Conectar o agente ao site',
                        'zh-CN': '3. 将代理连接到网站',
                      },
                    },
                  ],
                },
              ],
            },
            {
              label: 'GitHub Copilot cloud agent',
              items: [
                { label: 'Overview', link: '/real-world-development/cloud/' },
                { label: '0. Prerequisites', link: '/real-world-development/cloud/0-prerequisites/' },
                { label: '1. Custom instructions', link: '/real-world-development/cloud/1-custom-instructions/' },
                { label: '2. Cloud agent', link: '/real-world-development/cloud/2-cloud-agent/' },
                { label: '3. Custom agents', link: '/real-world-development/cloud/3-custom-agents/' },
                { label: '4. Managing agents', link: '/real-world-development/cloud/4-managing-agents/' },
                { label: '5. Iterating', link: '/real-world-development/cloud/5-iterating/' },
              ],
            },
            {
              label: 'Visual Studio Code',
              items: [
                { label: 'Overview', link: '/real-world-development/vscode/' },
                { label: '0. Prerequisites', link: '/real-world-development/vscode/0-prerequisites/' },
                { label: '1. Custom instructions', link: '/real-world-development/vscode/1-custom-instructions/' },
                { label: '2. Agent mode', link: '/real-world-development/vscode/2-agent-mode/' },
                { label: '3. Testing with Playwright MCP', link: '/real-world-development/vscode/3-mcp/' },
                { label: '4. Custom agents', link: '/real-world-development/vscode/4-custom-agents/' },
                { label: '5. Managing agents', link: '/real-world-development/vscode/5-managing-agents/' },
                { label: '6. Iterating', link: '/real-world-development/vscode/6-iterating/' },
                {
                  label: 'Optional: Incorporate Foundry',
                  translations: {
                    'es-ES': 'Opcional: Incorporar Foundry',
                    'ja-JP': '省略可能: Foundry を組み込む',
                    'ko-KR': '선택 사항: Foundry 통합',
                    'pt-BR': 'Opcional: Incorporar o Foundry',
                    'zh-CN': '可选：集成 Foundry',
                  },
                  items: [
                    { label: 'Overview', link: '/real-world-development/vscode/7-foundry-toolkit/' },
                    {
                      label: 'Prepare a project and model',
                      link: '/real-world-development/vscode/7-foundry-toolkit/1-project-and-model/',
                      translations: {
                        'es-ES': 'Preparar un proyecto y un modelo',
                        'ja-JP': 'プロジェクトとモデルを準備する',
                        'ko-KR': '프로젝트 및 모델 준비',
                        'pt-BR': 'Preparar um projeto e um modelo',
                        'zh-CN': '准备项目和模型',
                      },
                    },
                    {
                      label: 'Build and deploy an agent',
                      link: '/real-world-development/vscode/7-foundry-toolkit/2-build-and-deploy/',
                      translations: {
                        'es-ES': 'Crear e implementar un agente',
                        'ja-JP': 'エージェントを構築してデプロイする',
                        'ko-KR': '에이전트 빌드 및 배포',
                        'pt-BR': 'Criar e implantar um agente',
                        'zh-CN': '构建并部署代理',
                      },
                    },
                    {
                      label: 'Connect the agent to the site',
                      link: '/real-world-development/vscode/7-foundry-toolkit/3-connect-to-site/',
                      translations: {
                        'es-ES': 'Conectar el agente al sitio',
                        'ja-JP': 'エージェントをサイトに接続する',
                        'ko-KR': '사이트에 에이전트 연결',
                        'pt-BR': 'Conectar o agente ao site',
                        'zh-CN': '将代理连接到网站',
                      },
                    },
                  ],
                },
              ],
            },
          ],
        },
      ],
    }),
  ],
});
